# PeekableInputStream run registry

Follow the [preservation methodology](../../docs/run-methodology.md) and the
[repository agent instructions](../../AGENTS.md). Use
`uv run --frozen python tools/experiment_runs.py list` from the study repository
to verify registered attempts and supplements. Add a row here when a new attempt is reserved;
the authoritative identity is that attempt's `run.json`.

| Attempt | Source condition | Origin | Evidence |
| --- | --- | --- | --- |
| [json-001](runs/json/001/run.json) | WIT-UP JSON only | Historical import | [Markdown report](runs/json/001/evidence/peekable-input-stream-report.md), [integrity seal](runs/json/001/seal.json) |
| [java-source-001](runs/java-source/001/run.json) | Java production source only | Prospective; generation complete and sealed | [Generation report](runs/java-source/001/report.md), [integrity seal](runs/java-source/001/seal.json) |

The historical import preserves the original prompt attachment and all retained
evidence. Its manifest records unknown generation metadata and maps historical
absolute paths to the present layout. Treat it separately from prospective runs
using revised process prompts. Its original absolute command paths must not be
reused for another attempt.

Prospective records use schema version 2. Measurements and amendments live in
`supplements/<condition>/<generation-sequence>/<supplement-sequence>/`, refer to
the generation's exact seal hash, and contribute zero new independent samples.
The prospective Java-source generation contains 20 passed tests, with no failures,
errors, or skips. Its additional style-check findings remain in the generation
report. The frozen test and generation seal are immutable.

| Linked evaluation | Configuration | State | Evidence |
| --- | --- | --- | --- |
| [001](supplements/java-source/001/001/run.json) | Original full-suite plan | Sealed incomplete: preparation parsing failure | [Diagnostic report](supplements/java-source/001/001/report.md) |
| [002](supplements/java-source/001/002/run.json) | Revision 1, auxiliary Maven POM | Sealed incomplete: PIT discovery skipped | [Diagnostic report](supplements/java-source/001/002/report.md) |
| [003](supplements/java-source/001/003/run.json) | Revision 2, actual source roots | Sealed incomplete: relative-fixture baseline failures | [Diagnostic report](supplements/java-source/001/003/report.md) |
| [004](supplements/java-source/001/004/run.json) | Revision 3, Java-directory override | Sealed incomplete: native-directory mismatch remained | [Diagnostic report](supplements/java-source/001/004/report.md) |
| [005](supplements/java-source/001/005/run.json) | Revision 4, PIT CLI from native checkout root | Evaluation complete and sealed | [Before/after Markdown report](supplements/java-source/001/005/report.md), [integrity seal](supplements/java-source/001/005/seal.json) |

Every evaluation contributes zero independent generations. Earlier pipeline
diagnostics remain separate from the generated-test outcome and final metrics.
The valid pair measured target JaCoCo line coverage from 0/16 to 11/16, branch
coverage from 0/8 to 8/8, and PIT mutation score from 0/14 to 7/14. The report
retains all counters and the complete frozen Java source.
Register supplements through the manager; after adding any, create a new
`bundle-study` collection so that recovery retains both the original and its
linked evidence. Do not rewrite the historical seal to upgrade its schema.

The local bundle and checksum are stored outside the repository under
`D:/Projects/experiment-backups/peekable-input-stream/`. Shared raw JSON input
snapshots are stored under `D:/Projects/experiment-backups/shared-inputs/` using
their SHA-256 hashes as filenames. These are local preservation copies, not an
off-machine disaster-recovery backup. Input snapshot locations are recorded in
the [backup inventory](../../docs/input-backups.json).

The sealed evaluation backup is
`D:/Projects/experiment-backups/peekable-input-stream/java-source/001/evaluations/005/evaluation.zip`.
The verified complete collection, including both generations and all five linked
evaluations, is
`D:/Projects/experiment-backups/peekable-input-stream/collections/001/study-collection.zip`.
Both have independent SHA-256 sidecars. They preserve required evidence and
diagnostics without copying regenerable dependency caches or presentation assets.

Run IDs appear only in provenance directories and metadata. Each generator receives
its own rendered prompt and permitted inputs, without this registry or other runs.
