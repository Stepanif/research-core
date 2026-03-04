# Run CI Locally

Use these scripts for docs tasks (no Makefile is present in this repository):

```text
python tools/docs/gen_cli_ref.py
python tools/docs/gen_schema_ref.py
python tools/docs/verify_generated_docs_clean.py
mkdocs build
mkdocs serve
```
