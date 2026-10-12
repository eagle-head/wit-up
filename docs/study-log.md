# Study log

[Documentation index](README.md)

Dates below distinguish the initial work on October 8, 2026, from Java validation
and experiment preparation on October 9, 2026. Generated artifacts also record
timestamps. Entries describe applied work, not an earlier preregistration.
Append new entries for material changes rather than rewriting old choices as if
they were planned from the outset.

This log consolidates the supplied preparation handoff, the subsequent work in
this conversation, and retained local records. The scope and case-assessment
documents describe the initial JSON-inspection phase; the later Java work and
experimental decisions are recorded below.

## 2026-10-08: workspace and input preparation

- Organized the study in "D:/Projects/wit-up", with the WIT-UP checkout in
  "core" and Apache Commons IO in "commons-io". Set Commons IO to
  `11f0abe7a3fb6954b2985ca4ab0697b2fb489e84`.
- Copied "witup-results-commons-io-11f0abe7a.json" and
  "witup-summaries-commons-io-11f0abe7a.json" into
  "commons-io-analysis-results" and verified equality with the supplied files.
  This check establishes copy identity, not the identity of the analyzed JAR.

## 2026-10-08: complete JSON inventory

- Initialized the packaged Python application with uv and used an existing
  Python 3.13.15 interpreter. Added ijson and DuckDB through uv; kept JupyterLab
  in a separate optional dependency group and Ruff in the development group.
- Read all 88,303 result rows and 72,419 summary rows, representing 1,127 method
  signatures and 134 declaring classes. Inspected the WIT-UP export boundary to
  interpret field meanings and grouped summaries, without reviewing the Java
  projects for correctness.
- Initial validation assumed a named exception in every summary. The actual
  data contained 161 null values. Corrected that assumption, preserved those rows
  as unknown exceptions and documented the data gap; no exception was invented.
- The first row-by-row derived-table insertion was interrupted because it was
  slow. Changed insertion to batches and completed a fresh full run. No partial
  run was reported as a completed analysis.
- Confirmed unique join keys, complete summary/result correspondence and no
  matched verdict or metadata disagreement. Derived datasets and recognized
  counts were checked, and formatting/lint/lock checks passed. Produced a DuckDB
  database, Parquet datasets, and statistics.
- Created eight candidate tiers, including the 65 simple-signature and 156
  null-argument hypotheses. These are data-shape labels, not execution outcomes.

## 2026-10-08: selection policy and case inspection

- The requested follow-up fixed 20 cases, balanced 10 + 10 between the two simpler
  strata. Chose deterministic purposive diversity selection, one path per full
  method signature, with class novelty as the first preference.
- Defined the ordered selection rule after population exploration; inspected its
  preview before saving the durable inventory. No preregistration is claimed.
- The preview contained `IOUtils.toByteArray(java.io.Reader)` with a null
  condition on `stack_7`. Retained it and flagged argument-binding ambiguity;
  did not replace it with an easier-looking case or alter the original pool.
- Recorded parsed originals, array record numbers, input byte identities,
  selection reasons and rule-derived assessments. Per-case observations use the
  exported records; no Java source was consulted in this phase.
- Split the original long report into an overview, four focused findings pages
  and an illustrative-example appendix. Added separate scope, selection and
  assessment methodology documents, with one document per selected case.
- Qualitative observations include negative integer predicates with false truth
  flags, serialized empty strings paired with null flags, unconstrained argument
  choices, and a temporary-like symbol. These findings are descriptive and do not
  establish generation feasibility.
- The selected records cover 20 methods and 20 classes. None was declared ready
  for execution: argument binding, object setup, accessibility, and the effective
  exception location still required investigation.
- Reviewed 35 documentation files and checked 123 local links without finding
  broken links. Replaced authorship-focused wording with descriptions of the
  procedures and limitations. These counts belong to the original documentation
  review, not to later additions.

## Validation record for the case-inspection phase

The completed validation record is maintained in
[case validation](findings/case-validation.md). It distinguishes software/data
checks from semantic interpretation and from the future generation experiment.

## Limitations at the end of 2026-10-08

The actual WIT-UP producer revision, analyzed JAR bytes and analysis-failures
export are unavailable. Sampling is purposive and biased toward simpler record
shapes. Assessment combines limited expression rules with a qualitative
inspection; no independent assessment was performed. At that checkpoint, no
test-generation experiment, Java execution, or population effectiveness estimate
had occurred.

## 2026-10-09: narrower target and Java tooling

- Shifted preparation toward a small unit with understandable behavior and
  demonstrable test gaps. Proposed a validated reference suite with explicit
  scenarios, meaningful assertions, coverage, and mutation analysis before
  assessing independent generation.
- Discussed source-only and JSON-only generation conditions, with comparable
  execution conditions and measurements of input/output tokens, attempts, cost,
  elapsed time, and results. These were design proposals; neither the comparison
  nor measurement automation was implemented.
- Verified Temurin JDK `8.0.504+1` and Maven `3.9.16`, pinned them in
  "commons-io/mise.toml", and confirmed that Maven runs with Java 8. Retained
  JUnit Jupiter `5.5.2` and Surefire `2.22.2`.
- Updated JaCoCo to `0.8.14` and configured PIT `1.15.8` with
  `pitest-junit5-plugin` `1.2.2` in "commons-io/pom.xml". Adjusted JVM argument
  handling for the tools and added the Apache license header to
  "commons-io/mise.toml". Compilation covered 153 production files and 155 test
  files. A focused integration check collected coverage and detected a mutation.
- Initialized CodeGraph only in "commons-io", indexing 342 files. Created
  `test/reference-suite` from the original Commons IO base while preserving local
  changes.
- The preparation handoff reported that the parent workspace was not yet a Git
  repository and that "core", "commons-io", and "commons-io-analysis-results"
  were already listed in its ".gitignore". At consolidation, the parent does
  contain ".git" and its project files remain untracked. The initialization
  timing is not established by this record; the earlier observation is not the
  current state.

## 2026-10-09: baseline coverage and target selection

Executed the existing suite with fresh JaCoCo data. Production and test source
still matched the original baseline; build configuration already included the
tooling changes. The selected target, `PeekableInputStream`, had **0/16 covered
lines (0.00%) and 0/8 covered branches (0.00%)**, without a dedicated test file.

Selected this small, entirely uncovered class after reviewing implemented
behavior. Its 31 SAT summary paths in the supplied WIT-UP data do not establish
executable fixtures. The [baseline report](findings/unit-test-coverage-baseline.md)
retains the target's measurement, commands, and artifact-availability limits.
The earlier selection inventory is preserved in the archived report.

## 2026-10-09: reference suite and contract correction

- Built tests incrementally for uncovered behavior, then used focused mutation
  analysis and a test-adequacy review to add the necessary cases. This was an
  interactive, assisted reference-building process using the custom testing
  guidance requested at that stage. It is not an independent generation trial.
- Investigated both prefix comparisons and EOF behavior. The initial
  interpretation treated a shorter matching prefix as valid and led to an
  intermediate `>` length guard. Deeper contract review corrected that
  interpretation: `peek` compares against the complete currently buffered
  content, so a shorter matching prefix returning `false` is not a defect.
  The review consulted the project's
  [contract clarification](https://github.com/apache/commons-io/pull/856) and
  [IO-855](https://issues.apache.org/jira/browse/IO-855).
- Confirmed a length-handling defect when the requested comparison exceeds the
  valid buffered bytes, including empty, truncated, or exhausted streams. The
  original `<` guard could allow unused or stale buffer bytes to participate in
  a comparison. The final production change is confined to
  "src/main/java/org/apache/commons/io/input/buffer/CircularByteBuffer.java":
  `pLength < currentNumberOfBytes` became `pLength != currentNumberOfBytes`.
  "PeekableInputStream.java" itself was unchanged.
- Examined the empty-array case separately. An empty comparison array retains
  the existing `IllegalArgumentException` behavior; a zero-length slice of a
  nonempty array returns `false` when buffered content is present. Did not add
  empty-prefix semantics to production code.
- Corrected the test expectations to the established contract. Against the
  intermediate prefix implementation, the corrected suite reported three
  failures: the two shorter-prefix cases and the zero-length-slice case. All
  passed after the final guard correction. These failures concern the
  intermediate implementation, not three newly discovered original defects.
- The resulting target suite contains 27 test methods, 34 executed cases, and
  53 assertion call sites. It exercises matching and mismatching comparisons,
  slices, retained buffered content, short reads and refill, EOF states, input
  validation, propagated I/O exceptions, and nonconsumption where applicable.

Retained validation results for the corrected contract and production code:

| Check | Result | Retained record |
| --- | --- | --- |
| Target test class | 34 target cases; no failures, errors, or skips | Focused test log (historical file unavailable: "../commons-io/target/coverage/peekable-input-stream-exact-match-tests.log") |
| JaCoCo for `PeekableInputStream` | 16/16 lines, 8/8 branches, 4/4 methods, 98/98 instructions | Focused coverage XML (historical file unavailable: "../commons-io/target/coverage/peekable-input-stream-exact-match-jacoco/jacoco.xml") |
| PIT, default mutators, target class only | 14 generated mutations, all 14 killed | Mutation report (historical file unavailable: "../commons-io/target/pit-reports/peekable-input-stream-exact-match/mutations.xml") |

Kept the intermediate failing run (historical file unavailable: "../commons-io/target/coverage/peekable-input-stream-exact-match-red-tests.log")
alongside the passing evidence. Coverage and the bounded PIT result support the
reference suite within the measured scope; they do not prove the absence of all
defects or establish mutation adequacy for every dependency.

## 2026-10-09: repository conventions and local reference commits

- Reviewed the project's contribution guidance while considering an upstream
  PR. The review also found an existing
  [upstream PR with the same guard correction](https://github.com/apache/commons-io/pull/876).
  The user subsequently fixed the purpose as local WIT-UP work. No fork, push,
  or PR was created.
- Adapted "PeekableInputStreamTest.java" to the repository's conventions while
  preserving scenarios and assertions: package-private declarations, `test...`
  method names, no arrange/act/assert section comments, and inline assertion
  lambdas. Production code was unchanged in this style-only step.
- Removing method Javadocs initially produced 27 Checkstyle errors. Restored
  the required documentation and retained the failing audit. The configured
  Maven Checkstyle invocation does not cover test source, so the target test
  source was checked directly with Checkstyle `8.19`; the
  final test-source audit (historical file unavailable: "../commons-io/target/coverage/peekable-input-stream-test-style-validation.log")
  passed without suppressions or relaxed rules.
- Verified that the style changes preserved the test operations, fixtures,
  annotations, and assertions. The
  post-style focused run (historical file unavailable: "../commons-io/target/coverage/peekable-input-stream-test-style-tests.log")
  again passed all 34 target cases. The historical PIT result precedes this
  style-only change and was not rerun afterward.
- Accepted the suite as the local reference for the defined scope. Committed
  from inside "D:/Projects/wit-up/commons-io" in three semantic commits:

| Commit | Purpose |
| --- | --- |
| `deab48f6d7999f50c4ff13fde99890a2d133c397` | Correct the buffer length guard and add the reference tests and package documentation. |
| `3172ba0a70285b27febb43a1cf506482bdc5a2fd` | Preserve coverage, mutation, and toolchain configuration. |
| `256fa0d0e19247ce41a084125a57fbd487029704` | Ignore generated CodeGraph files. |

`test/reference-suite` points to `256fa0d0e19247ce41a084125a57fbd487029704`.
The user explicitly excluded "commons-io/docs/unit-test-coverage-baseline.md"
from the commits; at that point, it remained a local, untracked study record.
All other pending Commons IO changes from this preparation were committed.

## 2026-10-09: generation branch and preserved prompt

- Created `test/peekable-input-stream-generation` from `test/reference-suite`,
  retaining the corrected production code and tooling configuration. Removed
  only "src/test/java/org/apache/commons/io/input/buffer/PeekableInputStreamTest.java"
  and committed that removal as
  `d7a3c884d07ff5f1829b09087f34dcb8043f0f64`. Verified that this deletion is the
  only difference from the reference branch. The package documentation remains.
- Preserved the English [generation prompt draft](prompts/unit-test-generation.txt).
  It defines the first source-only condition, permits repository-owned rules
  and other tests in the current checkout, and explicitly prohibits all skills
  except Codex built-in skills. Custom, repository-defined, user-installed, and
  plugin-provided skills are prohibited even if repository guidance invokes
  them. This restriction applies to the future independent generation stage;
  it does not retroactively describe reference-suite construction.
- Clarified that other existing tests may be consulted for conventions and API
  use. The removed target reference test and its copies may not be recovered
  from branches, history, backups, generated artifacts, or prior conversations.
  The prompt also excludes WIT-UP exports, coverage and mutation reports,
  compiled tests, and external test examples from this first condition.
- Limited generation changes to the target test file. The prompt requires a
  focused test run with commands, counts, and failures reported, without changing
  production or weakening assertions just to obtain a passing result. It does
  not prescribe scenarios, test counts, coverage targets, or known-defect hints.
- Standardized prompt paths to forward slashes and double quotes. The draft has
  not been executed or frozen as a completed experimental input. Prompt-type
  comparisons remain a possible later extension.
- Recommended a fresh chat without inherited reference-building history and
  preservation of the exact prompt, follow-ups, supplied context, model settings,
  starting revision, commands, and results. No fresh experimental chat was
  created, and no operational skill-isolation configuration was applied.

## Status before the first independent generation trial

The reference suite and corrected production code are committed locally; the
generation branch contains the same production and configuration with only the
target test source removed. The preparation handoff's final statements that the
reference suite was not yet built and all Commons IO changes were uncommitted
describe its earlier cutoff and are superseded by the entries above.

No independent LLM generation trial, source-versus-JSON comparison, or generation
cost/token measurement has run. Preparing the reference interactively does not
establish feasibility of generating tests from WIT-UP outputs.

Before that experiment, remaining controls include preserving the reference
evidence outside the generation agent's accessible context and cleaning stale
build output. Compiled target tests and a reference-source backup still exist
under "commons-io/target"; deleting the Java source alone does not remove those
inputs or prevent stale classes from affecting a run. No cleanup was performed
as part of this documentation consolidation.

The prompt's skill prohibition has been written, but effective skill discovery,
inherited instructions, memory, and chat context have not been independently
isolated for a trial. No absence-of-bias claim is made. The final condition design
and any JSON-based input protocol still need to be fixed before measurement.

The WIT-UP producer revision and analyzed JAR bytes remain unavailable. In
addition, the generation baseline contains a production correction after
`11f0abe7a`; equivalence between the old export's analyzed program and the corrected
checkout has not been established. This difference must be addressed explicitly
before interpreting a WIT-UP-based generation result. The original purposive
sample and its execution gaps remain unchanged.

## 2026-10-09: source-only generation result

- The user ran the preserved source-only prompt in a separate chat and reported
  the model setting as GPT-6.1 Sol Extra High. The generation produced 26 test
  cases: 21 passed, 4 failed, 1 errored, and none were skipped. The result and
  its interpretation are recorded in the
  [generation assessment](findings/peekable-input-stream-generation.md).
- Reviewed the existing results without correcting the generated tests or
  production. Added the complete generated Java source to the assessment's
  appendix, retaining the original assertions and fixtures.
- The generation's clean build removed the earlier reference validation
  artifacts under "commons-io/target". Historical metrics remain in the study
  record; their original report files were not recreated.

## 2026-10-09: JSON generation preparation

- Confirmed that the assessment appendix exactly matched the source-only test
  file before removing it from the checkout. Used that appendix as the preserved
  code copy, without creating another Java backup.
- Copied the source-only Surefire XML, Surefire text report, and Checkstyle XML
  into "data/experiments/peekable-input-stream/source-only". Verified each copy
  against its original and updated the assessment links to these retained files.
- Created and selected `test/peekable-input-stream-json-generation` directly at
  `d7a3c884d07ff5f1829b09087f34dcb8043f0f64`, from inside
  "D:/Projects/wit-up/commons-io". Removed the untracked generated
  "PeekableInputStreamTest.java" and its four compiled class files. Retained
  production, configuration, other test sources, and the local baseline document.
- Saved the proposed English [JSON generation prompt](prompts/unit-test-generation-json.txt)
  in a separate file, with the new branch named explicitly. Preserved the
  original source-only prompt byte-for-byte. Both prompts use forward slashes
  and double quotes for filesystem paths.
- The new condition uses the two original JSON exports as the sole source of
  target-specific scenarios, constraints, and expected outcomes. It retains the
  built-in-skills-only restriction, repository conventions, and prohibition on
  retrieving earlier target tests or using coverage and mutation reports.
  Production source and behavioral API documentation are excluded from test
  design in this condition. The final response must associate tests with their
  exported records and disclose assumptions and unrepresented SAT records.

The JSON generation has not been executed. No new generation chat, test run,
coverage measurement, mutation run, commit, or push was performed during this
preparation. The new branch remains exactly at the requested base commit. The
export-to-production version difference and context-isolation limitations remain
as described in the assessment; branch preparation does not resolve them.

## 2026-10-09: coverage baseline document relocation

- Moved the local coverage baseline from
  "commons-io/docs/unit-test-coverage-baseline.md" to
  "docs/findings/unit-test-coverage-baseline.md", placing the study observation
  outside the external Commons IO checkout.
- Updated navigation and source links for the new location. Retained the
  original measurement and documented that its generated artifact files were
  removed by the previously recorded clean build. No measurements were repeated.

## 2026-10-09: JSON-based generation result

- The user ran the JSON prompt in a separate chat and reported GPT-6.1 Sol Extra
  High. All 12 generated cases passed. The same target cases passed again
  during repository verification, with no failures, errors, or skips.
- Reviewed the results without modifying tests or production. The
  [JSON generation assessment](findings/peekable-input-stream-json-generation.md)
  contains the complete generated Java source, the test-to-record associations,
  assignment variants, unrepresented SAT records, and context-exposure limits.
- Preserved the existing target execution reports and original build evidence under
  "data/experiments/peekable-input-stream/json-only". No additional Java validation,
  coverage analysis, mutation run, or test-source correction was performed.
- The 12 tests associate with 11 of 31 SAT records; eight use explicitly changed
  model assignments. They assert invalid-argument exceptions only. A passing
  result does not establish complete path reproduction or equivalence to the
  broader reference suite. Accidental unrelated production-source exposure through
  CodeGraph is disclosed in the assessment.

## 2026-10-11: exception-focused prompt pair

- Prepared two new English prompts: the
  [Java-source condition](prompts/exception-test-generation-source.txt) and the
  [JSON-source condition](prompts/exception-test-generation-json.txt). Preserved
  both earlier prompt files byte-for-byte.
- Restricted both conditions to exceptional behavior in the target constructors
  and declared peek overloads. The common text includes identical source-use
  boundaries, fixture rules, built-in-skills-only restrictions, repository
  conventions, traceability requirements, and a fixed target test command.
  Only the marked scenario-source block differs. Instructions for interpreting
  each source format appear in both files, without importing earlier findings
  or specifying target exception scenarios or a desired test count.
- Required an already prepared checkout at
  `d7a3c884d07ff5f1829b09087f34dcb8043f0f64`, with the earlier target test absent.
  The prompts stop if preparation is incomplete or prohibited behavioral
  material enters the context. The current generated test remains in place;
  no new branch or checkout was prepared for these prompts.
- Future paired runs need separate fresh chats and the same model and reasoning
  settings. Equal prompt rules do not establish equivalence between the older
  JSON artifact and the corrected production baseline; that input limitation
  remains as previously recorded.

This step created prompts only. No test generation, Java execution, coverage or
mutation analysis, commit, or push was performed.

## 2026-10-11: exception-only Java-source generation result

- Before the user ran the new source prompt, created and selected
  `test/peekable-input-stream-exceptions` from
  `d7a3c884d07ff5f1829b09087f34dcb8043f0f64`, with commands executed inside
  "D:/Projects/wit-up/commons-io". Confirmed that the previous JSON attempt's
  source was preserved byte-for-byte in its assessment and that its archived
  execution reports matched the current evidence, then removed only its target
  test source and compiled class. The tracked baseline remained unchanged.
- The user ran the exception-only source prompt in a new chat and reported
  GPT-6.1 Sol Extra High. The generation produced 17 test methods and 17 cases,
  all passing. A subsequent repository verification again passed all 17
  target cases with no failures, errors, or skips.
- Reviewed the current file, production associations, original prompt attachment,
  generation chat, and existing reports. The
  [exception-only source assessment](findings/peekable-input-stream-source-exception-generation.md)
  contains the entire generated Java file in one block, all 17 source associations,
  fixture assumptions, omitted candidates, and validation limitations.
- Preserved the target Surefire XML and text report, Checkstyle XML,
  retrieved Maven outputs, and selected chat
  records under "data/experiments/peekable-input-stream/source-exceptions".
  The broader retrieved Maven output remains truncated; the preparation batch's
  recorded exit code 1 is retained separately from successful Maven executions.
- Maven Checkstyle excluded the target test source. The generated
  test has no method Javadocs, so test-source style compliance remains unverified.
  No coverage or mutation measurement exists for this generated suite. The
  previous JSON trial used a different prompt and is not its matching comparator.

No tests, assertions, production, dependencies, or configuration were corrected
during this assessment. No additional Java validation, generation attempt,
coverage or mutation run, branch change, commit, or push was performed.

## 2026-10-11: post-generation coverage comparison for the exception-only source suite

- At the user's request, supplemented the
  [exception-only source assessment](findings/peekable-input-stream-source-exception-generation.md)
  with a reconstructed before/after JaCoCo measurement. Preserved its complete
  premeasurement text under
  "data/experiments/peekable-input-stream/source-exceptions/coverage/assessment-before-coverage.md".
  This is a later assessment, not a generation-time measurement or a change to
  the generation protocol. The used prompts and complete Java appendix remain
  unchanged.
- Created a detached measurement checkout on D: at
  `d7a3c884d07ff5f1829b09087f34dcb8043f0f64`. Ran the complete existing suite
  without the target test, then added the exact preserved generated file and ran
  the same command again: `mvn -B -Pjacoco "-Djacoco.skip=false" clean verify jacoco:report`.
  Both runs used Temurin 8.0.504+1, Maven 3.9.16, and JaCoCo 0.8.14. No test
  exclusions, coverage filters, threshold changes, or source repairs were made.
- The before state had no target test cases. The after state had 17 passing
  target cases with no failures, errors, or skips. Comparing case identities
  and outcomes found only those added cases. All common source files and
  compiled production outputs were byte-identical.
- Target coverage increased from 0/16 to **13/16 lines (81.25%)**, from 0/8 to
  **8/8 branches (100.00%)**, from 0/98 to **87/98 instructions (88.78%)**, and
  from 0/4 to **3/4 methods (75.00%)**. The remaining missed lines are 49, 50,
  and 92. Exception-aborted probe sequences limit interpretation of those
  missed lines; full target branch coverage does not establish complete
  exception coverage or reference-suite equivalence.
- Both Maven commands returned exit code 0. Inherited coverage checks emitted
  warnings, retained in the complete logs; configuration and thresholds were
  unchanged. Build success does not establish that every coverage check passed.
- Preserved both runs' complete Maven logs, metadata, JaCoCo execution data,
  HTML/XML/CSV reports, Surefire reports, source and class hashes, and compiled
  production ZIPs outside the checkout. Added a
  [machine-readable comparison](../data/experiments/peekable-input-stream/target-coverage/comparison.json).
  Verified that 1,108 original evidence, prompt, source, and build-artifact files
  remained unchanged. The active branch and original target test were retained.
  Removed the detached measurement checkout after verifying the preserved data.
- A cross-document link check found eight unavailable historical artifact links
  in earlier study-log entries, all under the original checkout's "target"
  directory. Their loss in an earlier clean build was already recorded above.
  Links in the updated assessment and this new entry resolve. The unavailable
  historical artifacts remain a limitation for the later report review; their
  paths and historical measurements were preserved.

No additional tests were designed, and no tests or production were corrected.
No mutation run, generation attempt, commit, or push was performed. Coverage
backfills for the earlier source and JSON reports, and any reconstruction of the
reference-suite measurement, remain separate later work; their historical
results were not overwritten.

## 2026-10-11: coverage comparisons for the earlier suites and reference

- Saved the existing 17-case generated file locally in Commons IO commit
  `84e58db4515f0df154e288aa402018c91cf9649e`, subject
  `test: cover exceptional peek input conditions`, on
  `test/peekable-input-stream-exceptions`. Git commands ran inside
  "D:/Projects/wit-up/commons-io". This recorded the already existing file;
  its working bytes, committed blob, and report appendix were identical. No
  assertion, fixture, production file, or configuration was edited. No push
  was performed. The coverage baseline remains the earlier `d7a3c884d` commit.
- Preserved the three earlier documents and the existing study log, index,
  and latest assessment before updating them. Restored the first source and
  JSON suites directly from their complete Java report blocks and verified
  their original SHA-256 hashes. Restored the reference suite from its exact
  committed blob at `256fa0d0e19247ce41a084125a57fbd487029704`. No new tests
  were designed and no existing tests were changed.
- Executed three separate before/after pairs in a detached checkout on D:,
  with identical production and configuration at
  `d7a3c884d07ff5f1829b09087f34dcb8043f0f64`. Each before state omitted the
  target file, and each after state added only its corresponding preserved
  file. Every full-suite command was
  `mvn -B -Pjacoco "-Djacoco.skip=false" clean verify jacoco:report`.
  Versions were Temurin 1.8.0_504, Maven 3.9.16, JUnit Jupiter 5.5.2,
  Surefire 2.22.2, and JaCoCo 0.8.14.
- All three new before runs had no target test. After adding the corresponding
  file, source had 21 passing cases, four failures, and one error; JSON had
  12 passing cases; reference had 34 passing cases. No target case was skipped.
  Source and JSON identities and outcomes exactly matched their original
  archived Surefire reports.
- The source after build returned exit code 1. A separate `jacoco:report`
  invocation read the captured data and returned 0; no failure-ignore option
  was used, and the failed build result was retained. The measurement runner
  captured all six runs and returned aggregate exit code 1 to preserve that
  failure. The other five full builds returned 0. Coverage-rule warnings were
  retained, with no threshold or suppression changes. The source after build
  stopped before the verify-phase coverage check, so that check is unexecuted.

The following table consolidates the **target-class** results. Every before
state had 0/16 covered lines, 0/8 branches, 0/98 instructions, and 0/4 methods.
The latest exception-only source pair is retained from the preceding entry;
it was not rerun during this extension.

| Suite | Target outcomes | Lines after | Branches after | Instructions after | Methods after |
| --- | --- | ---: | ---: | ---: | ---: |
| [Earlier source-only](findings/peekable-input-stream-generation.md#post-generation-jacoco-comparison) | 21 passed, 4 failures, 1 error | 16/16 (100.00%) | 8/8 (100.00%) | 98/98 (100.00%) | 4/4 (100.00%) |
| [Earlier JSON](findings/peekable-input-stream-json-generation.md#post-generation-jacoco-comparison) | 12 passed | 11/16 (68.75%) | 7/8 (87.50%) | 77/98 (78.57%) | 3/4 (75.00%) |
| [Exception-only source](findings/peekable-input-stream-source-exception-generation.md#post-generation-jacoco-comparison) | 17 passed | 13/16 (81.25%) | 8/8 (100.00%) | 87/98 (88.78%) | 3/4 (75.00%) |
| [Reference](findings/unit-test-coverage-baseline.md#reconstructed-reference-suite-coverage-comparison) | 34 passed | 16/16 (100.00%) | 8/8 (100.00%) | 98/98 (100.00%) | 4/4 (100.00%) |

- Cross-pair checks confirmed identical baseline source bytes, compiled
  production outputs, and baseline case identities/outcomes across all four
  pairs. Reported counters refer exclusively to `PeekableInputStream`.
- Full target coverage in the first source suite coexists with its five
  unsuccessful cases. Coverage alone therefore does not establish correct
  expectations or reference-suite equivalence. The prompts differ in scope
  and other rules, and the reference was built interactively. These data do
  not establish an isolated causal effect of switching the scenario source.
- Preserved complete Maven logs, command metadata, JaCoCo execution data and
  HTML/XML/CSV reports, all Surefire reports, source/class hashes, and compiled
  production ZIPs outside the checkout. Per-suite comparison JSON files and
  artifact manifests accompany the updated reports. The
  [combined comparison](../data/experiments/peekable-input-stream/target-coverage/comparison.json)
  records the four pairs and the failed source build explicitly. Its current
  view contains only target counters and test outcomes, plus build provenance.
- Verified that 2,790 original source, prompt, execution-evidence, and original
  build-artifact files remained unchanged. All three generated Java appendices
  retain their original bytes. The earlier unavailable reference artifacts were
  labeled as historical unavailable paths, preserving all eight locations and
  original measurements. New reference coverage does not restore the deleted
  original logs, coverage data, Checkstyle records, or PIT report; mutation
  analysis was not rerun.

The three earlier coverage supplements are complete. The primary Commons IO
checkout retains the saved 17-case file and its branch. No generation prompt,
test behavior, assertion, fixture, production source, or build configuration was
changed. The disposable measurement checkout was removed after artifact and
source verification. The original October 9 baseline remains a separate
historical record. The [verification record](../data/experiments/peekable-input-stream/coverage-comparison/verification.json)
and [preservation inventory](../data/experiments/peekable-input-stream/coverage-comparison/artifact-manifest.json)
record the final controls and retained evidence.

## 2026-10-11: reporting scope limited to the target class

At the user's request, revised all four coverage assessments, this study log,
and the documentation index to report only `PeekableInputStream` coverage and
its dedicated test outcomes. Removed project totals, other-class coverage,
and candidate-ranking metrics from the active reports. JaCoCo HTML links now
open the target class directly. The reporting rule also applies to future
generation and reference-suite assessments.

The target's before coverage remains zero in every pair. All existing target
counters, failed test outcomes, and generated Java appendices are unchanged.
Build diagnostics remain in the original complete logs; no quality gate was
changed or represented as passing because of this reporting change.

Preserved the six documents as they stood before this edit under
"data/experiments/peekable-input-stream/target-coverage/report-snapshots".
Added a [target-only comparison](../data/experiments/peekable-input-stream/target-coverage/comparison.json)
derived from the archived class counters and target Surefire XML. Complete raw
measurement artifacts and prior report versions remain historical evidence,
outside the scope of the current comparison. No tests were rerun, and no test,
production file, build configuration, prompt, branch, or commit was changed.

## 2026-10-11: preparation for JSON-based exception generation

- Preserved the completed 17-case source exception suite on
  `test/peekable-input-stream-exceptions` at
  `84e58db4515f0df154e288aa402018c91cf9649e`. Verified byte identity among the
  working file, committed Git blob, and complete Java assessment appendix.
  Added an exact [standalone source copy](../data/experiments/peekable-input-stream/source-exceptions/PeekableInputStreamTest.java)
  outside the generation checkout. Existing reports and execution evidence remain
  unchanged.
- Created and selected `test/peekable-input-stream-exception-conditions` directly
  from `d7a3c884d07ff5f1829b09087f34dcb8043f0f64` inside
  "D:/Projects/wit-up/commons-io". The target test source is absent, HEAD is the
  required baseline, and the working tree is clean. Production and build
  configuration match that commit.
- Kept the [exception-only JSON prompt](prompts/exception-test-generation-json.txt)
  unchanged. Its SHA-256 is
  `945BEA425089EE30FFE3230EF1B104E74D7F8CC58B53354F94D23DB4B5C5246F`.
  Both designated JSON input files exist. The prompt retains the same rules as
  its paired source prompt outside the scenario-source block, including the
  restriction to Codex built-in skills.
- Recorded the preservation and checkout preconditions in the
  [preparation record](../data/experiments/peekable-input-stream/json-exceptions/preparation.json).

No generation, test execution, coverage measurement, mutation analysis, new
commit, or push was performed. The JSON condition is prepared for a fresh chat;
no result is claimed.

## 2026-10-11: exception-only JSON generation and target coverage assessment

- The user ran the paired JSON prompt in a fresh chat and reported GPT-6.1 Sol
  Extra High. The recorded generation lasted 742116 ms, from 23:10:12 to 23:22:34
  locally (UTC−04:00). It created one file with 11 tests and 11 exception assertions.
  Source SHA-256:
  `C8FCE4484A2B0A8620DB781029F9BDC698FB69ED5AD15F015F2BED1ED98A5536`.
- The original target command failed at Apache RAT because
  ".ruff_cache/CACHEDIR.TAG" had an unapproved license. Compilation and Surefire
  were not reached: zero cases executed, with failures, errors, and skips
  unmeasured. Additional repository verification failed at the same gate;
  a separate Checkstyle command also failed with class-resolution diagnostics.
  These failures and the exact generated source were preserved without repairs.
- Programmatic extraction verified 100 target records in each designated JSON
  file, joined uniquely by `artifact` and `pathId`: 31 SAT and 69 UNSAT.
  The 11 tests associate with 11 distinct SAT records; seven use changes to
  concrete model values. Association is not measured path reproduction.
  The source and JSON prompts remain identical outside the scenario-source block.
- At the user's request, measured before and after in a fresh detached checkout
  of `d7a3c884d07ff5f1829b09087f34dcb8043f0f64`. Before omitted the target test;
  after added the exact archived source. The unrelated local cache was absent
  from both measurement states. RAT remained enabled and passed; no exclusion,
  gate change, test edit, or production edit was introduced.
- Both measurement commands were
  `mvn -B -Pjacoco "-Djacoco.skip=false" clean verify jacoco:report`.
  They ran locally from 23:25:51 to 23:29:13 and from 23:29:14 to 23:32:35.
  Both returned exit 0, retaining inherited coverage warnings. All 11 target
  cases passed in this later execution, with no failures, errors, or skips.
  This does not replace the original blocked generation-time outcome.
- Common source and compiled production bytes matched between the two states
  and the paired source condition's baseline. Existing test identities and
  outcomes were unchanged. The primary checkout, generated source, prompt files,
  local cache, and original RAT artifact were preserved.
- Created the [complete JSON exception assessment](findings/peekable-input-stream-json-exception-generation.md)
  with all generated Java code in one block. Updated the documentation index
  and [target-only comparison](../data/experiments/peekable-input-stream/target-coverage/comparison.json)
  to include this fifth condition. Earlier comparison data and the updated
  documents' previous versions were archived before extending them.

| Target counter | Before | After |
| --- | ---: | ---: |
| Lines | 0/16 (0.00%) | 12/16 (75.00%) |
| Branches | 0/8 (0.00%) | 7/8 (87.50%) |
| Instructions | 0/98 (0.00%) | 85/98 (86.73%) |
| Methods, including constructors | 0/4 (0.00%) | 3/4 (75.00%) |

The missed lines are 49, 50, 90, and 92. The default constructor is untested,
the slice refill branch is not taken, and exceptional delegation leaves line 92
without a completed coverage probe. The paired source suite had 13/16 lines and
8/8 branches. These are target execution differences, not proof of equivalent
exception behavior or mutation adequacy.

The [verification record](../data/experiments/peekable-input-stream/json-exceptions/verification.json)
and [artifact inventory](../data/experiments/peekable-input-stream/json-exceptions/artifact-manifest.json)
retain the preservation and measurement checks. No test or production correction,
new generation, mutation analysis, commit, or push was performed. The disposable
measurement checkout was removed after preservation and verification.

## 2026-10-12: root repository storage review

Reviewed the root repository separately from the Commons IO checkout. Git listed
6,496 untracked files; 6,439 belonged to the experiment evidence archive. None of
the root project files was already tracked.

Updated the root ".gitignore" with scoped exclusions for rendered JaCoCo views,
non-target Surefire output and process dumps, binary execution data, compiled
production ZIPs, and temporary worktrees. Kept JaCoCo XML/CSV, dedicated target
reports, Maven and generation logs, source snapshots, metadata, comparisons,
measurement scripts, and preservation manifests available for commit. The
original evidence remains on disk; the ignore rules do not change measurements
or suppress diagnostics.

The candidate list decreased from 6,496 to 237 files, including the new
[repository storage policy](methodology/repository-storage.md). The selected
content is approximately 16.35 MB. The documentation explains which local-only
artifact links require restoration after cloning and why full manifests still
refer to excluded originals.

Verified that the experiment archive's 6,439 files retained their byte identities
and that the dedicated target results and both JaCoCo counter formats remain
versionable for all five conditions. No staging, commit, push, deletion, test
execution, or change inside Commons IO was performed.

## 2026-10-12: RAT environment correction and original-command validation

The blocker came from the unrelated Ruff cache inside the Commons IO checkout,
not from a missing license header in the generated test. Preserved all three
cache files byte-for-byte under the JSON condition's "environment/.ruff_cache"
archive and relocated that directory out of the Java checkout. Preserved the
original RAT report before running the build again. The
[cache relocation record](../data/experiments/peekable-input-stream/json-exceptions/environment/cache-relocation.json)
maps the former file locations to the archived bytes. Historical manifests retain
their original paths and are not rewritten to conceal this later relocation.

Reran the exact original target command inside "D:/Projects/wit-up/commons-io":

```powershell
mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" "-Dtest=org.apache.commons.io.input.buffer.PeekableInputStreamTest" clean test
```

The run completed locally on October 12 from 10:42:03 to 10:42:11 (UTC−04:00),
with RAT enabled and Maven exit 0. All 11 existing target cases passed, with
zero failures, errors, or skips. The generated source's SHA-256, production,
tracked configuration, baseline HEAD, and both paired prompts were unchanged.
No generation, coverage measurement, mutation analysis, exclusion, or gate
relaxation occurred. The original October 11 failed execution and its later
isolated coverage results remain separate historical observations.

Preserved the new [run metadata](../data/experiments/peekable-input-stream/json-exceptions/environment/run.json),
[Maven log](../data/experiments/peekable-input-stream/json-exceptions/environment/target-test-run.log),
[target Surefire XML](../data/experiments/peekable-input-stream/json-exceptions/environment/TEST-org.apache.commons.io.input.buffer.PeekableInputStreamTest.xml),
and [verification](../data/experiments/peekable-input-stream/json-exceptions/environment/verification.json).
Added the [checkout preparation procedure](methodology/generation-checkout-preparation.md):
keep Python tool state outside Commons IO and run RAT before opening a future
independent generation chat. This is an environment-preparation procedure;
the preserved experimental prompts remain fixed.

## 2026-10-12: root commits and text line-ending policy

Created two semantic commits in the root repository: "ca317f3" for the Python
analysis pipeline and "bd38cc7" for the documentation and selected study evidence.
The root contained 247 tracked files, and the external Commons IO checkout was
unchanged. Ruff, formatting, all five Python tests, and the dependency-lock check
passed. The initial documentation diff check reported CRLF as trailing whitespace;
inspection found no additional trailing spaces or tabs.

Configured root-local Git conversion and versioned editor/attribute rules for
CRLF working files and LF Git text. Normalized only root-owned versioned text;
no scenarios, assertions, measured counters, or diagnostic messages were changed.
Original evidence bytes remain recoverable from root commit
"bd38cc700eaad2654736df7d02cab951d0a0cd10". The
[normalization record](../data/experiments/peekable-input-stream/line-ending-normalization.json)
records the representation changes; historical hash manifests remain unchanged
in meaning and still identify their original captures. The
[storage policy](methodology/repository-storage.md#text-line-endings) explains
verification and reproduction implications. Global Git settings, external Java
checkouts, ignored raw exports, and binary evidence were not modified.

After normalization, Ruff, formatting, all five Python tests, and the lockfile
check passed. The authored-text diff check passed. The complete diff check
exited 2 for 308 preexisting trailing-whitespace findings in captured
Maven/RAT output. Those lines were preserved beyond the requested line-ending
conversion. The uv package rebuild emitted its existing cross-drive hardlink
warning and successfully used file copies. No whitespace-rule suppression or
diagnostic filtering was configured.
