use serde::Serialize;
use std::{
    path::PathBuf,
    process::{Command, Stdio},
    thread,
    time::{Duration, Instant},
};

const BRIDGE_VERSION: &str = "0.1";
const COMMAND_ID: &str = "engine.cli_help_smoke";
const REQUEST_ID: &str = "da-t004-engine-cli-help-smoke";
const TIMEOUT_MS: u64 = 5_000;
const EXCERPT_LIMIT_CHARS: usize = 2_000;

#[derive(Serialize)]
struct BridgeResponse {
    request_id: String,
    bridge_version: String,
    command_id: String,
    status: String,
    duration_ms: u64,
    exit_code: Option<i32>,
    stdout_excerpt: String,
    stderr_excerpt: String,
    engine: EngineInfo,
    artifacts: Vec<String>,
    warnings: Vec<String>,
    errors: Vec<BridgeError>,
}

#[derive(Serialize)]
struct EngineInfo {
    name: String,
    version: Option<String>,
    mode: String,
}

#[derive(Serialize)]
struct BridgeError {
    code: String,
    message: String,
    stderr_excerpt: Option<String>,
    repair_hint: Option<String>,
}

#[tauri::command]
fn run_engine_cli_help_smoke() -> BridgeResponse {
    let started = Instant::now();
    let Some(repo_root) = repo_root() else {
        return blocked_response(
            started,
            "ENGINE_ENVIRONMENT_UNRESOLVED",
            "The repo-local development root could not be resolved.",
            "Run DA-T004 from the repo-local desktop scaffold context.",
        );
    };
    let python_path = repo_root.join(".venv-qa-t005").join("Scripts").join("python.exe");

    if !python_path.is_file() {
        return blocked_response(
            started,
            "ENGINE_VENV_UNAVAILABLE",
            ".venv-qa-t005\\Scripts\\python.exe is unavailable.",
            "Do not repair automatically; use a separately scoped environment-readiness ticket.",
        );
    }

    let mut child = match Command::new(&python_path)
        .args(["-m", "research_core.cli", "--help"])
        .current_dir(&repo_root)
        .stdin(Stdio::null())
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .spawn()
    {
        Ok(child) => child,
        Err(error) => {
            return blocked_response(
                started,
                "ENGINE_PROCESS_UNAVAILABLE",
                &format!("The fixed ResearchCore Engine smoke process could not start: {error}"),
                "Do not repair automatically; verify .venv-qa-t005 in a separately scoped ticket.",
            )
        }
    };

    loop {
        match child.try_wait() {
            Ok(Some(_status)) => {
                return match child.wait_with_output() {
                    Ok(output) => {
                        response_from_output(started, output.status.code(), output.stdout, output.stderr)
                    }
                    Err(error) => error_response(
                        started,
                        None,
                        "",
                        "",
                        "ENGINE_OUTPUT_UNAVAILABLE",
                        &format!("The fixed ResearchCore Engine smoke output could not be read: {error}"),
                    ),
                };
            }
            Ok(None) if started.elapsed() >= Duration::from_millis(TIMEOUT_MS) => {
                let _ = child.kill();
                return match child.wait_with_output() {
                    Ok(output) => timeout_response(started, output.status.code(), output.stdout, output.stderr),
                    Err(error) => error_response(
                        started,
                        None,
                        "",
                        "",
                        "ENGINE_TIMEOUT_OUTPUT_UNAVAILABLE",
                        &format!(
                            "The fixed ResearchCore Engine smoke timed out and output could not be read: {error}"
                        ),
                    ),
                };
            }
            Ok(None) => thread::sleep(Duration::from_millis(50)),
            Err(error) => {
                return error_response(
                    started,
                    None,
                    "",
                    "",
                    "ENGINE_WAIT_FAILED",
                    &format!("The fixed ResearchCore Engine smoke wait failed: {error}"),
                )
            }
        }
    }
}

fn repo_root() -> Option<PathBuf> {
    let manifest_dir = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    manifest_dir.parent()?.parent()?.parent().map(PathBuf::from)
}

fn response_from_output(
    started: Instant,
    exit_code: Option<i32>,
    stdout: Vec<u8>,
    stderr: Vec<u8>,
) -> BridgeResponse {
    let stdout_excerpt = bounded_excerpt(&stdout);
    let stderr_excerpt = bounded_excerpt(&stderr);

    if exit_code == Some(0) {
        return base_response(
            "OK",
            started,
            exit_code,
            stdout_excerpt,
            stderr_excerpt,
            vec!["Temporary dev-only bridge proof; CLI help is not structured engine output."],
            vec![],
        );
    }

    if stderr_excerpt.contains("No module named research_core.cli")
        || stderr_excerpt.contains("No module named research_core")
    {
        return base_response(
            "BLOCKED",
            started,
            exit_code,
            stdout_excerpt,
            stderr_excerpt.clone(),
            vec!["No install or repair was attempted."],
            vec![BridgeError {
                code: "ENGINE_CLI_UNAVAILABLE".to_string(),
                message: "research_core.cli is unavailable inside .venv-qa-t005.".to_string(),
                stderr_excerpt: Some(stderr_excerpt),
                repair_hint: Some(
                    "Use a separately scoped environment-readiness ticket; DA-T004 must not repair the venv."
                        .to_string(),
                ),
            }],
        );
    }

    error_response(
        started,
        exit_code,
        &stdout_excerpt,
        &stderr_excerpt,
        "ENGINE_COMMAND_FAILED",
        "The fixed ResearchCore Engine help-smoke command failed.",
    )
}

fn timeout_response(
    started: Instant,
    exit_code: Option<i32>,
    stdout: Vec<u8>,
    stderr: Vec<u8>,
) -> BridgeResponse {
    base_response(
        "TIMEOUT",
        started,
        exit_code,
        bounded_excerpt(&stdout),
        bounded_excerpt(&stderr),
        vec!["The fixed help-smoke process exceeded the DA-T004 timeout and was stopped."],
        vec![BridgeError {
            code: "ENGINE_TIMEOUT".to_string(),
            message: "The fixed ResearchCore Engine help-smoke command timed out.".to_string(),
            stderr_excerpt: None,
            repair_hint: Some("Retry only after a separately scoped investigation.".to_string()),
        }],
    )
}

fn blocked_response(
    started: Instant,
    code: &str,
    message: &str,
    repair_hint: &str,
) -> BridgeResponse {
    base_response(
        "BLOCKED",
        started,
        None,
        String::new(),
        String::new(),
        vec!["No install or repair was attempted."],
        vec![BridgeError {
            code: code.to_string(),
            message: message.to_string(),
            stderr_excerpt: None,
            repair_hint: Some(repair_hint.to_string()),
        }],
    )
}

fn error_response(
    started: Instant,
    exit_code: Option<i32>,
    stdout_excerpt: &str,
    stderr_excerpt: &str,
    code: &str,
    message: &str,
) -> BridgeResponse {
    base_response(
        "ERROR",
        started,
        exit_code,
        stdout_excerpt.to_string(),
        stderr_excerpt.to_string(),
        vec![],
        vec![BridgeError {
            code: code.to_string(),
            message: message.to_string(),
            stderr_excerpt: if stderr_excerpt.is_empty() {
                None
            } else {
                Some(stderr_excerpt.to_string())
            },
            repair_hint: Some(
                "Investigate in a separately scoped ticket before expanding DA-T004.".to_string(),
            ),
        }],
    )
}

fn base_response(
    status: &str,
    started: Instant,
    exit_code: Option<i32>,
    stdout_excerpt: String,
    stderr_excerpt: String,
    warnings: Vec<&str>,
    errors: Vec<BridgeError>,
) -> BridgeResponse {
    BridgeResponse {
        request_id: REQUEST_ID.to_string(),
        bridge_version: BRIDGE_VERSION.to_string(),
        command_id: COMMAND_ID.to_string(),
        status: status.to_string(),
        duration_ms: duration_ms(started),
        exit_code,
        stdout_excerpt,
        stderr_excerpt,
        engine: EngineInfo {
            name: "ResearchCore Engine".to_string(),
            version: None,
            mode: "dev-venv".to_string(),
        },
        artifacts: vec![],
        warnings: warnings.into_iter().map(str::to_string).collect(),
        errors,
    }
}

fn duration_ms(started: Instant) -> u64 {
    let elapsed = started.elapsed().as_millis();
    if elapsed > u64::MAX as u128 {
        u64::MAX
    } else {
        elapsed as u64
    }
}

fn bounded_excerpt(bytes: &[u8]) -> String {
    let text = String::from_utf8_lossy(bytes).replace("\r\n", "\n");
    let mut excerpt = String::new();
    let mut truncated = false;

    for (index, character) in text.chars().enumerate() {
        if index >= EXCERPT_LIMIT_CHARS {
            truncated = true;
            break;
        }
        excerpt.push(character);
    }

    if truncated {
        excerpt.push_str("\n...[truncated]");
    }

    excerpt
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![run_engine_cli_help_smoke])
        .run(tauri::generate_context!())
        .expect("error while running NullForge launch-only shell");
}
