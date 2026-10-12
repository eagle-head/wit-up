# Experimental run preservation methodology

## Scope and identities

This protocol preserves independent exception-test generations for
`org.apache.commons.io.input.buffer.PeekableInputStream` at Commons IO commit
`11f0abe7a3fb6954b2985ca4ab0697b2fb489e84`. Prospective records use schema version 2.
It does not authorize a generation, measurement, external upload, or push.

One independent generation has one source condition (`json` or `java-source`),
fresh chat, checkout, and reserved directory. A retry executes the same frozen
source and never increases the number of independent generations. An evaluation
or annotation is a supplement with `sampleContribution: 0`, linked to the original
generation's seal hash. Run identifiers belong only in provenance and folder names.

Never pool different model/settings, input, prompt, protocol, environment, or
measurement configurations as interchangeable repetitions. Preserve unknown
settings as unknown with a reason. The historical imported attempt remains schema
1, immutable, and separate from prospective repetitions. No timestamps or settings
are retroactively invented. Original historical paths remain historical locators.

## Storage and information boundaries

```text
commons-io-validation/peekable-input-stream/
  README.md
  runs/<condition>/<sequence>/
    run.json
    inputs/
      prompt.txt
      template.txt
      environment.json
      process/AGENTS.md
      process/docs/...
      preservation-manager.py
      production-source.zip       # Java-source condition only
    evidence/test-source/PeekableInputStreamTest.java
    executions/<sequence>/
      request.json                # Written before the command
      environment.json
      output.log
      surefire-reports.zip        # If native XML exists
      artifacts/...               # Declared measurement files
      result.json                 # Written once after the command
    report.md
    seal.json
  supplements/<condition>/<generation-sequence>/<supplement-sequence>/
    run.json                      # Parent path and exact seal hash
    inputs/...
    evidence/...
    executions/...
    report.md
    seal.json
```

Keep checkouts on D: outside the evidence tree, for example
`D:/Projects/experiment-workspaces/peekable-input-stream/json-002`.
The manager reserves an exclusive sibling `.working/<record-id>` for temporary
files and tool output. Never reuse a checkout across generations or evaluations.
A prepared detached checkout is sufficient; do not create branches named for runs.

The preparer handles reservation and metadata without exposing earlier results.
The generator uses only its rendered prompt, assigned metadata, snapshotted process
instructions, and designated scenario inputs. The evaluator acts after freezing
and separate authorization. The analyst compares closed records.

Open a fresh chat on the assigned Java checkout. Do not fork a chat containing
earlier tests, candidate inventories, alternative prompts, source-condition
feedback, or measurements. Do not supply the study repository's result index as
generator context. Copy only the rendered prompt and allowed inputs.
The copied process documents contain no target-specific test oracles or outcomes.
Do not follow their links into earlier evidence. Isolation is procedural, not an
access-control sandbox. Disclose prohibited exposure, stop generation, and close
the attempt as `contaminated`; do not claim independence by ignoring exposure.

## Prepare and preserve inputs

Prepare a distinct checkout at the fixed commit. Inspect only metadata during
preflight: HEAD, tracked equality, and existence of the target test. Reject a
preexisting target test and other untracked changes. Never reset another checkout
or print behavioral source diffs to the generator.

Use process-only Temurin runtime `1.8.0_504-b01`, javac `1.8.0_504`, Maven `3.9.16`,
and the baseline's JUnit Jupiter `5.5.2` and Surefire `2.22.2`. Record actual command
output, builds, executable locations, OS, environment variables, and generator
settings before generation and before each execution. An environment JSON must
contain `java`, `javac`, `maven`, `os`, and `processEnvironment`; version strings
must come from observations, not copied defaults. Include `generator` with model,
settings, and application build when observable, otherwise nulls with a reason.

For JSON generations, also provide exactly two `sourceInputs` entries with these
fields (replace every example value with observed data):

```json
{
  "role": "results",
  "path": "D:/original/raw-results.json",
  "backup": "D:/preserved-inputs/observed-sha256.json",
  "sha256": "observed-sha256"
}
```

The other role is `summaries`. The backup must be a distinct, byte-identical copy
of the original raw export. Preserve shared copies by content hash outside the
repository; do not duplicate large inputs per attempt. The manager verifies both
original and backup at preparation and freezing, and renders backup paths into
the prompt. Thus the generator reads the preserved original bytes. Never replace
them with derived datasets. Missing analyzed-JAR or producer provenance remains
unverified; an artifact label is not binary equivalence.

For Java-source generations, the manager preserves the permitted production tree
with `git archive` and checks the live baseline. Retain the source repository or a
verified Git bundle containing the exact baseline outside the experiment checkout
for full build recovery; the production-only ZIP does not include the build's
other inputs. Record this backup alongside shared inputs before claiming recovery.

The manager snapshots the selected template, rendered prompt, process documents,
and its own source. It records hashes and original locations. List any additional
human instruction files under `additionalInstructions` in the environment JSON
before preparation; their bytes are copied into `inputs/additional/`. Give the
generator those exact copies. New instructions after preparation change the
intervention: preserve them in the report, close that attempt as incomplete, and
prepare a separately identified generation rather than silently changing inputs.

From the study repository:

```powershell
uv run --frozen python tools/experiment_runs.py init `
  --condition json `
  --checkout D:/Projects/experiment-workspaces/peekable-input-stream/json-002 `
  --prompt-template docs/prompts/exception-test-generation-json.txt `
  --environment D:/Projects/experiment-workspaces/peekable-input-stream/environment.json
```

The manager writes a minimal manifest immediately after reserving the directory.
Preflight errors become `preparation-failed` with their diagnostic. Close these
with a Markdown report and `seal --outcome preflight-failed --reason ...`.
Directories and identifiers are never recycled. If a process was interrupted
between directory reservation and manifest creation, inspect its partial evidence
and use `recover --run PATH --reason 'Observed interruption and retained evidence'`.
Recovery preserves existing bytes and never invents prompt or toolchain values.
The recovery command is only for manifestless generation reservations.

One local agent owns each active record. Exclusive locks serialize preparation and
record writes. A lock conflict is a reported error. Before removing a stale lock,
confirm the recorded process has ended and inspect partial files. Interrupted
freeze/record transactions remain visible: preserve their diagnostics and close
incomplete after an explicit reviewed recovery; never overwrite partial evidence
to manufacture a completed result.

## Freeze once

Generate the entire initial suite from permitted inputs. Do not target a fixed
number of tests or a coverage score. Freeze before the first compilation:

```powershell
uv run --frozen python tools/experiment_runs.py freeze `
  --run commons-io-validation/peekable-input-stream/runs/json/002 `
  --fresh-chat-attested
```

The attestation must be true. The manager checks input hashes and baseline, copies
the Java bytes, and refuses another freeze. No repairs, changed fixtures, renamed
tests, or new cases may follow execution feedback. Do not commit in the experiment
checkout before evaluation; HEAD is part of the baseline contract.

Use `verify --run PATH --live` immediately before execution to check the live
checkout and external inputs. Plain `verify` checks portable preserved evidence
and does not require the original machine's checkout. The two checks serve
different purposes and must not be substituted.

## Reserve, execute, and finish each invocation

Every invocation needs `begin` before the command and `record` afterward. The
manager does not execute Maven. `begin` fixes the command, scope, environment,
timestamp, native-report destination, and declared artifacts in `request.json`.
It returns a sequence and exclusive `output.log` path. Finish one invocation before
beginning another. A generation has exactly one `generated-tests` invocation;
authorized retries use `supplemental-tests`.

Set process-only `JAVA_HOME`, PATH, D: TEMP/TMP, and `MAVEN_OPTS=-DargLine=` for the
plain Maven test command. Preserve actual versions and both output streams.
Reserve the native Surefire directory while it is absent or empty:

```powershell
uv run --frozen python tools/experiment_runs.py begin `
  --run commons-io-validation/peekable-input-stream/runs/json/002 `
  --phase generated-tests `
  --command 'mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" "-Dtest=org.apache.commons.io.input.buffer.PeekableInputStreamTest" clean test' `
  --scope 'Frozen PeekableInputStreamTest only' `
  --environment D:/Projects/experiment-workspaces/peekable-input-stream/environment.json `
  --reports D:/Projects/experiment-workspaces/peekable-input-stream/json-002/target/surefire-reports
```

From the assigned checkout, run the original command once and capture its exit
status immediately. `$executionLog` is the path returned by `begin`:

```powershell
mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" "-Dtest=org.apache.commons.io.input.buffer.PeekableInputStreamTest" clean test *> $executionLog
$executionExit = $LASTEXITCODE
```

Then, from the study repository:

```powershell
uv run --frozen python tools/experiment_runs.py record `
  --run commons-io-validation/peekable-input-stream/runs/json/002 `
  --execution 001 --exit-code $executionExit
```

Use `--tests-not-started --reason 'Specific diagnostic from the captured log'` only
when the log establishes no test execution. Missing reports alone do not establish
zero. Without native reports or that observation, counts remain unknown.
`record` preserves malformed, conflicting, or predating reports but marks their
attribution invalid and leaves suite counts unknown. Raw native counts, actual
exit status, and protocol problems remain separate. A post-test pipeline failure
can coexist with genuinely passed test assertions; its process exit stays failed.

Before a retry, finish the previous record and archive any old native-report
directory within the assigned working area. Verify absolute source/destination
paths and use `Move-Item -LiteralPath` with an unused destination. Never copy an old
XML into a new invocation. A fresh destination, timestamp checks, and immutable
receipts reduce accidental mixing; they do not prove a manually reported command
was executed. Preserve command/session provenance honestly.

Checkout drift must remain reportable. `record` archives the log even when the
checkout no longer matches, lists the discrepancy, and refuses valid attribution.
An `infrastructure` invocation may begin to capture an already observed discrepancy.
It does not authorize repairs. Sealing checks every finished request, environment,
log, ZIP, artifact, and receipt against hashes recorded at capture, including before
the final seal. Changed or missing evidence blocks verification and completion.

## Evaluation and amendments

Close the generation first. Separately authorized JaCoCo/PIT work belongs in an
evaluation supplement, using the exact frozen source and a distinct checkout.
Use the [paired measurement protocol](measurement-protocol.md) and its canonical
[configuration](measurement-plan.json) and [PIT POM](pit-analysis-pom.xml).
The four phases use the same existing full suite, adding only the frozen test
after. Measure the baseline; never infer zero. Do not narrow scope or suppress an
unmutated-test failure to get a successful pair.

Save the user's measurement authorization verbatim with context in a Markdown
note, then reserve the evaluation:

```powershell
uv run --frozen python tools/experiment_runs.py supplement `
  --run commons-io-validation/peekable-input-stream/runs/json/002 `
  --kind evaluation --note D:/Projects/experiment-workspaces/measurement-authorization.md `
  --checkout D:/Projects/experiment-workspaces/peekable-input-stream/evaluation `
  --environment D:/Projects/experiment-workspaces/peekable-input-stream/environment.json `
  --plan docs/measurement-plan.json
```

The manager links the parent seal hash, copies the frozen source into the clean
evaluation checkout, and preserves the plan, POM, protocol, and environment. Use
`begin`/`record` with the returned supplement directory for every phase. Declare
native artifacts using `begin --artifacts PATH`, where PATH contains a JSON object
mapping the protocol's artifact roles to this evaluation's output paths. The
evaluator must preserve rendered scripts and exact substitutions before execution.
No generated behavior is revised from measurements. Repeated or failed pairs
remain linked evaluations with no added independent sample.

For a later correction, create a US English Markdown note describing the original
claim, correction, supporting evidence, and limits. Register it using
`supplement --run PARENT --kind annotation --note NOTE`. The manager snapshots and
seals the annotation, binds it to the parent's exact seal, and includes it in
`list`. The original remains byte-identical. Extra measurements always use a new
evaluation supplement; an annotation cannot replace native measurements.

## Closing and acceptance

Use an explicit outcome:

| Outcome | Required evidence |
| --- | --- |
| `generation-complete` | Frozen source, complete Java in Markdown, exactly one initial invocation with known outcome, every invocation finished, no unresolved protocol discrepancy. Genuine executed-test failure or documented startup failure remains a valid negative generation outcome. |
| `evaluation-complete` | Frozen source in Markdown, all four successful measurement phases, required native artifacts, equal production class hashes and mutant identities, valid protocol observations. |
| `incomplete` | Markdown report and explicit reason; preserve pending invocations and all partial output. No claim that missing phases passed. |
| `preflight-failed` | Preparation diagnostic, report, and reason. No invented input/version values. |
| `contaminated` | Disclosure, report, and reason; no independent-generation claim. |
| `no-supported-tests` | Source-grounded report and reason; no empty or disabled suite. |
| `annotation` | Linked correction note; sealed automatically by the supplement command. |

A generation seal does not imply measurement completion or test quality. JaCoCo/PIT
artifacts are required only for an evaluation-complete seal. Sealing incomplete
records preserves failure; it does not remove their study membership. Keep all
executed-test failures, missing measurements, and infrastructure diagnostics visible.

```powershell
uv run --frozen python tools/experiment_runs.py seal --run PATH --report report.md --outcome generation-complete
uv run --frozen python tools/experiment_runs.py verify --run PATH
uv run --frozen python tools/experiment_runs.py bundle --run PATH --destination D:/Projects/experiment-backups/generation.zip
```

Retain exact inputs, full Java, Markdown report, commands, configurations, logs,
raw diagnostics, native XML, and JaCoCo execution data. Compress full-suite XML
losslessly. Before moving regenerable HTML, downloaded tools, or caches to external
D: storage, verify all required evidence was retained. Never clean unsealed
evidence or discard failures. Manager operations serialize writes and refuse sealed
records. Direct filesystem access can still change bytes; independent checksums,
verified bundles, and Git history anchor the preserved inventory.

## Git, backup, and recovery

Inspect the semantic branch name before commits. Use atomic Conventional Commits
in US English, separating preservation tooling from experiment evidence. Do not
name branches or commits for run IDs, chats, or creators. Preserve unrelated work.
Stage intended evidence explicitly; do not include ignored raw exports, checkouts,
caches, or presentation assets. `.gitattributes` disables text normalization for
both `runs/**` and `supplements/**`. Verify sealed records before and after the
actual Git commit/clone round trip, not just the working tree.

`bundle` preserves one record. After any annotation or evaluation, also create a
new complete collection bundle containing every sealed generation and supplement:

```powershell
uv run --frozen python tools/experiment_runs.py bundle-study --destination D:/Projects/experiment-backups/study-collection.zip
```

Both bundle operations reject existing destinations, compare archived bytes, and
write an independent SHA-256 sidecar. The collection retains canonical `runs/`
and `supplements/` paths, so linked records restore together. No supplement is
silently omitted. Close active records explicitly before creating the collection.
Use a new destination for each backup version.

Shared raw exports and external source repositories are separate backup items;
verify their bytes and record their locations, as in [input-backups.json](input-backups.json).
For recovery, verify the ZIP against its sidecar, extract into a new empty D:
study directory, and run `--study-root RESTORED list`. Restore all parents of
supplements before verification. Do not overwrite existing evidence or rewrite
historical absolute paths. Live replay requires newly assigned evaluation paths.

D: local copies protect against repository cleanup, not disk loss. Independently
managed off-machine backup is required for disaster recovery; no upload is implied.

## Local verification

```powershell
uv run --frozen python -m unittest discover -s tests
uv run --frozen ruff check src tools tests
uv run --frozen ruff format --check src tools tests
uv run --frozen pyright src tools tests
uv run --frozen python tools/experiment_runs.py list
git diff --check
```

Preservation tests use synthetic inputs and isolated Git fixtures on D:. They test
observable lifecycle, integrity, failure attribution, and backup recovery. They
do not generate, repair, execute, or establish behavior of Commons IO tests.
