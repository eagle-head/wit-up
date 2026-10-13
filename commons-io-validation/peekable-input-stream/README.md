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
evidence. Its manifest retains the metadata originally captured and maps historical
absolute paths to the present layout. Linked annotations recover the generation
model, reasoning effort, runtime version, and chat provenance from the original
sessions. The historical schema and original absolute command paths remain
unchanged; those paths must not be reused for another attempt.

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

The JSON-source aligned evaluation is registered separately:

| Linked evaluation | Configuration | State | Evidence |
| --- | --- | --- | --- |
| [json-001/evaluation-001](supplements/json/001/001/run.json) | Revision 4, identical recipes and runtime artifacts to the completed Java-source evaluation | Evaluation complete and sealed | [Before/after Markdown report](supplements/json/001/001/report.md), [integrity seal](supplements/json/001/001/seal.json) |

Every evaluation contributes zero independent generations. Earlier pipeline
diagnostics remain separate from the generated-test outcome and final metrics.
The Java-source pair measured target JaCoCo line coverage from 0/16 to 11/16, branch
coverage from 0/8 to 8/8, and PIT mutation score from 0/14 to 7/14. The report
retains all counters and the complete frozen Java source.
The aligned JSON pair measured line coverage from 0/16 to 11/16, branch coverage
from 0/8 to 7/8, and mutation score from 0/14 to 1/14. Its 10 generated cases
passed unchanged in the full suite. Both selected evaluations use identical
production class bytes, the same 14 mutant identities, and the same runtime JARs.

The [consolidated pilot report](reports/exception-test-generation-comparison.md)
contains the aligned results, exact tools and commands, complete frozen Java for
both conditions, original prompts, and corrected generation provenance. A
[Brazilian Portuguese report](reports/exception-test-generation-comparison.pt-BR.md)
is also available. The reports assess whether JSON supplies enough information
for exception-test generation without generator access to production source.
They distinguish demonstrated feasibility from the observed effectiveness gap,
prioritize missing dependency-failure scenarios and public-fixture/oracle gaps
in a table linking each JSON improvement to evidence and effect measurements,
and propose controlled comparisons of unchanged and enriched JSON inputs.
The proposed comparisons have not been executed. Both generations
used GPT-6.1 Sol (`gpt-6.1-sol`) with Extra High
reasoning effort (`xhigh`) in separate fresh chats without prior conversation
history. Suite size and composition are observed outcomes to explain. This remains
a descriptive pilot with one generation per condition; additional generations
are deferred pending feedback from Professor Rodrigo and Doctoral Student Adriano.

| Linked annotation | Correction | Evidence |
| --- | --- | --- |
| [json-001/annotation-002](supplements/json/001/002/run.json) | Recovered generation configuration and chat provenance | [Annotation](supplements/json/001/002/report.md) |
| [java-source-001/annotation-006](supplements/java-source/001/006/run.json) | Recovered generation configuration and chat provenance | [Annotation](supplements/java-source/001/006/report.md) |

The annotations preserve exact session locators and the operator's attestation,
bind to the original generation seals, and contribute zero independent samples.

Register supplements through the manager; after adding any, create a new
`bundle-study` collection so that recovery retains both the original and its
linked evidence. Do not rewrite the historical seal to upgrade its schema.

The local bundle and checksum are stored outside the repository under
`D:/Projects/experiment-backups/peekable-input-stream/`. Shared raw JSON input
snapshots are stored under `D:/Projects/experiment-backups/shared-inputs/` using
their SHA-256 hashes as filenames. These are local preservation copies, not an
off-machine disaster-recovery backup. Input snapshot locations are recorded in
the [backup inventory](../../docs/input-backups.json).

The selected evaluation backups are
`D:/Projects/experiment-backups/peekable-input-stream/java-source/001/evaluations/005/evaluation.zip`
and `D:/Projects/experiment-backups/peekable-input-stream/json/001/evaluations/001/evaluation.zip`.
The latest verified complete collection, including both generations, all six
linked evaluations, and both provenance annotations, is
`D:/Projects/experiment-backups/peekable-input-stream/collections/003/study-collection.zip`.
The latest consolidated Markdown reports are backed up under
`D:/Projects/experiment-backups/peekable-input-stream/reports/005/`.
The report filenames are `exception-test-generation-comparison.md` and
`exception-test-generation-comparison.pt-BR.md`. The archive and report backups
have independent SHA-256 sidecars. The latest backup also preserves the JSON-input
review and report-preservation verification. Earlier report snapshots and their
reviews remain in `reports/001/` (execution counters), `reports/002/` (mutation
insights), `reports/003/` (explicit conclusions), `reports/004/` (JSON sufficiency),
`collections/002/`, and
`collections/003/`; preceding collections remain preserved.
No dependency caches or presentation assets enter the evidence.

Run IDs appear only in provenance directories and metadata. Each generator receives
its own rendered prompt and permitted inputs, without this registry or other runs.
