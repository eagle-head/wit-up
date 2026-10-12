# PeekableInputStream run registry

Follow the [preservation methodology](../../docs/run-methodology.md) and the
[repository agent instructions](../../AGENTS.md). Use
`uv run --frozen python tools/experiment_runs.py list` from the study repository
to verify registered attempts and supplements. Add a row here when a new attempt is reserved;
the authoritative identity is that attempt's `run.json`.

| Attempt | Source condition | Origin | Evidence |
| --- | --- | --- | --- |
| [json-001](runs/json/001/run.json) | WIT-UP JSON only | Historical import | [Markdown report](runs/json/001/evidence/peekable-input-stream-report.md), [integrity seal](runs/json/001/seal.json) |

The historical import preserves the original prompt attachment and all retained
evidence. Its manifest records unknown generation metadata and maps historical
absolute paths to the present layout. Treat it separately from prospective runs
using revised process prompts. Its original absolute command paths must not be
reused for another attempt.

Prospective records use schema version 2. Measurements and amendments live in
`supplements/<condition>/<generation-sequence>/<supplement-sequence>/`, refer to
the generation's exact seal hash, and contribute zero new independent samples.
There are currently no prospective generations or supplements in this registry.
Register supplements through the manager; after adding any, create a new
`bundle-study` collection so that recovery retains both the original and its
linked evidence. Do not rewrite the historical seal to upgrade its schema.

The local bundle and checksum are stored outside the repository under
`D:/Projects/experiment-backups/peekable-input-stream/`. Shared raw JSON input
snapshots are stored under `D:/Projects/experiment-backups/shared-inputs/` using
their SHA-256 hashes as filenames. These are local preservation copies, not an
off-machine disaster-recovery backup. Input snapshot locations are recorded in
the [backup inventory](../../docs/input-backups.json).

Run IDs appear only in provenance directories and metadata. Each generator receives
its own rendered prompt and permitted inputs, without this registry or other runs.
