import { invoke } from "@tauri-apps/api/core";
import { useState } from "react";

type BridgeStatus = "OK" | "ERROR" | "TIMEOUT" | "BLOCKED";

type BridgeError = {
  code: string;
  message: string;
  stderr_excerpt: string | null;
  repair_hint: string | null;
};

type BridgeSmokeResponse = {
  request_id: string;
  bridge_version: string;
  command_id: "engine.cli_help_smoke";
  status: BridgeStatus;
  duration_ms: number;
  exit_code: number | null;
  stdout_excerpt: string;
  stderr_excerpt: string;
  engine: {
    name: string;
    version: string | null;
    mode: string;
  };
  artifacts: string[];
  warnings: string[];
  errors: BridgeError[];
};

const boundaries = [
  "Only one temporary DA-T004 bridge command is implemented: engine.cli_help_smoke.",
  "The command uses fixed app-owned arguments for python -m research_core.cli --help inside .venv-qa-t005.",
  "No sidecar, workspace behavior, or structured engine operation exists.",
  "Artifact metadata is display-only from the bridge response; no artifact files are created, scanned, read, or mutated.",
  "No dataset import, broker/live, AI/model, signing, updater, telemetry, cloud, network, public release, or financial advice behavior is implemented."
];

export function App() {
  const [result, setResult] = useState<BridgeSmokeResponse | null>(null);
  const [invokeError, setInvokeError] = useState<string | null>(null);
  const [isRunning, setIsRunning] = useState(false);

  async function runBridgeSmoke() {
    setIsRunning(true);
    setInvokeError(null);

    try {
      setResult(await invoke<BridgeSmokeResponse>("run_engine_cli_help_smoke"));
    } catch (error) {
      setInvokeError(error instanceof Error ? error.message : String(error));
    } finally {
      setIsRunning(false);
    }
  }

  return (
    <main className="shell">
      <section className="masthead" aria-labelledby="nullforge-title">
        <p className="ticket">WB-T001</p>
        <h1 id="nullforge-title">NullForge bridge smoke</h1>
        <p className="summary">
          Local Tauri shell with one bounded ResearchCore Engine help-smoke and read-only artifact metadata.
        </p>
      </section>

      <section className="status-band" aria-label="Implementation status">
        <div>
          <span className="label">Scope</span>
          <strong>Bridge smoke only</strong>
        </div>
        <div>
          <span className="label">Bridge</span>
          <strong>engine.cli_help_smoke</strong>
        </div>
        <div>
          <span className="label">Artifacts</span>
          <strong>Read-only response field</strong>
        </div>
      </section>

      <section className="bridge-smoke" aria-labelledby="bridge-smoke-title">
        <div className="bridge-smoke-header">
          <div>
            <span className="label">Command</span>
            <h2 id="bridge-smoke-title">engine.cli_help_smoke</h2>
          </div>
          <button type="button" onClick={runBridgeSmoke} disabled={isRunning}>
            {isRunning ? "Running" : "Run smoke"}
          </button>
        </div>

        {invokeError ? <p className="invoke-error">{invokeError}</p> : null}

        {result ? (
          <div className="bridge-result" aria-live="polite">
            <dl>
              <div>
                <dt>Status</dt>
                <dd className={`status-pill status-pill--${result.status.toLowerCase()}`}>
                  {result.status}
                </dd>
              </div>
              <div>
                <dt>Duration</dt>
                <dd>{result.duration_ms} ms</dd>
              </div>
              <div>
                <dt>Exit code</dt>
                <dd>{result.exit_code ?? "n/a"}</dd>
              </div>
              <div>
                <dt>Bridge</dt>
                <dd>{result.bridge_version}</dd>
              </div>
            </dl>

            <section className="artifact-metadata" aria-labelledby="artifact-metadata-title">
              <div>
                <span className="label">Artifacts</span>
                <h3 id="artifact-metadata-title">Read-only metadata</h3>
              </div>
              <span className="artifact-count">{result.artifacts.length}</span>
              {result.artifacts.length > 0 ? (
                <ul>
                  {result.artifacts.map((artifact, index) => (
                    <li key={`${artifact}-${index}`}>{artifact}</li>
                  ))}
                </ul>
              ) : (
                <p>No artifacts were returned by this bridge smoke.</p>
              )}
            </section>

            <div className="output-grid">
              <section aria-label="Bounded stdout excerpt">
                <h3>stdout</h3>
                <pre>{result.stdout_excerpt || "No stdout captured."}</pre>
              </section>
              <section aria-label="Bounded stderr excerpt">
                <h3>stderr</h3>
                <pre>{result.stderr_excerpt || "No stderr captured."}</pre>
              </section>
            </div>

            {result.warnings.length > 0 ? (
              <ul className="note-list">
                {result.warnings.map((warning) => (
                  <li key={warning}>{warning}</li>
                ))}
              </ul>
            ) : null}

            {result.errors.length > 0 ? (
              <ul className="error-list">
                {result.errors.map((error) => (
                  <li key={error.code}>
                    <strong>{error.code}</strong>
                    <span>{error.message}</span>
                  </li>
                ))}
              </ul>
            ) : null}
          </div>
        ) : null}
      </section>

      <section className="boundary" aria-labelledby="boundary-title">
        <h2 id="boundary-title">Boundaries</h2>
        <ul>
          {boundaries.map((boundary) => (
            <li key={boundary}>{boundary}</li>
          ))}
        </ul>
      </section>
    </main>
  );
}
