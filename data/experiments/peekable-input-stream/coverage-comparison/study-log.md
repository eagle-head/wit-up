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

Executed the existing Commons IO suite with a fresh JaCoCo execution file:
**1,541 reported tests, 0 failures, 0 errors, and 6 existing skips**. Production
and test source still matched the original base at this measurement; the build
configuration already included the tooling changes. The inventory covered 148
source files with executable lines.

Ranked files by line coverage and reviewed implemented behavior to exclude
facades, empty callbacks, and simple exception shells. The retained shortlist was:

| Source file | Covered lines | Line coverage | Branch coverage |
| --- | --- | --- | --- |
| "PeekableInputStream.java" | 0 / 16 | 0.00% | 0.00% |
| "IOConsumer.java" | 0 / 5 | 0.00% | Not applicable |
| "AbstractCharacterFilterReader.java" | 5 / 16 | 31.25% | 20.00% |
| "CircularByteBuffer.java" | 25 / 74 | 33.78% | 20.69% |
| "AccumulatorPathVisitor.java" | 11 / 24 | 45.83% | 8.33% |

Retained `IOConsumer` because `andThen` implements concrete behavior. Recommended,
then selected, `PeekableInputStream` as the first reference-suite target: it was
small, completely uncovered, and had 31 SAT summary paths in the supplied WIT-UP
data. Those SAT labels do not establish executable fixtures.

The [baseline report](findings/unit-test-coverage-baseline.md) owns the
ranking criteria, exclusions, commands, and artifact inventory. Preserved the
execution log, fresh coverage data, XML copy, and source-file inventory. Later
focused measurements were kept separately, and the original baseline HTML report
was restored rather than replaced by a focused result.

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
| Target plus existing circular-stream test | 35 tests: 34 target cases and 1 existing case; no failures, errors, or skips | [Focused test log](../commons-io/target/coverage/peekable-input-stream-exact-match-tests.log) |
| Full Commons IO suite | 1,575 reported tests; 0 failures, 0 errors, 6 existing skips | [Full-suite log](../commons-io/target/coverage/peekable-input-stream-exact-match-suite.log) |
| JaCoCo for `PeekableInputStream` | 16/16 lines, 8/8 branches, 4/4 methods, 98/98 instructions | [Focused coverage XML](../commons-io/target/coverage/peekable-input-stream-exact-match-jacoco/jacoco.xml) |
| PIT, default mutators, target class only | 14 generated mutations, all 14 killed | [Mutation report](../commons-io/target/pit-reports/peekable-input-stream-exact-match/mutations.xml) |
| Maven production Checkstyle | Passed | [Checkstyle log](../commons-io/target/coverage/peekable-input-stream-contract-checkstyle.log) |

Kept [the intermediate failing run](../commons-io/target/coverage/peekable-input-stream-exact-match-red-tests.log)
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
  [final test-source audit](../commons-io/target/coverage/peekable-input-stream-test-style-validation.log)
  passed without suppressions or relaxed rules.
- Verified that the style changes preserved the test operations, fixtures,
  annotations, and assertions. The
  [post-style focused run](../commons-io/target/coverage/peekable-input-stream-test-style-tests.log)
  again passed all 35 cases. The full-suite and PIT results above precede this
  style-only change; neither was rerun afterward.
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
  High. All 12 generated cases passed. The generation agent's broader verification
  also passed, with 1,553 tests, no failures or errors, and six existing skips.
- Reviewed the results without modifying tests or production. The
  [JSON generation assessment](findings/peekable-input-stream-json-generation.md)
  contains the complete generated Java source, the test-to-record associations,
  assignment variants, unrepresented SAT records, and context-exposure limits.
- Preserved the existing target execution reports and a summary of the 137
  existing suite XML reports under
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
  all passing. A subsequent repository verification reported 1,558 cases:
  1,552 passed, six skipped in existing suites, and no failures or errors.
- Reviewed the current file, production associations, original prompt attachment,
  generation chat, and existing reports. The
  [exception-only source assessment](findings/peekable-input-stream-source-exception-generation.md)
  contains the entire generated Java file in one block, all 17 source associations,
  fixture assumptions, omitted candidates, and validation limitations.
- Preserved the target Surefire XML and text report, Checkstyle XML, an aggregate
  of 137 existing suite XML reports, retrieved Maven outputs, and selected chat
  records under "data/experiments/peekable-input-stream/source-exceptions".
  The broader retrieved Maven output remains truncated; the preparation batch's
  recorded exit code 1 is retained separately from successful Maven executions.
- Maven Checkstyle checked 156 files and excluded test source. The generated
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
- The before state reported 1,541 cases: 1,535 passed and six skipped. The after
  state reported 1,558: 1,552 passed and the same six skipped. Neither run had
  failures or errors. Comparing case identities and outcomes found exactly the
  17 added passing target cases and no changes to existing cases. All common
  source files and compiled production outputs were byte-identical.
- Target coverage increased from 0/16 to **13/16 lines (81.25%)**, from 0/8 to
  **8/8 branches (100.00%)**, from 0/98 to **87/98 instructions (88.78%)**, and
  from 0/4 to **3/4 methods (75.00%)**. The remaining missed lines are 49, 50,
  and 92. Exception-aborted probe sequences limit interpretation of those
  missed lines; full target branch coverage does not establish complete
  exception coverage or reference-suite equivalence.
- Project line coverage increased from 5,429/6,087 to 5,458/6,087; branches
  increased from 2,507/2,910 to 2,534/2,910. Coverage also changed in two monitor
  classes outside the generated fixtures. The report therefore retains global
  counts as context and does not attribute their entire delta to the new tests
  or claim repeated-run stability from one measurement pair.
- Both Maven commands returned exit code 0, but inherited project-wide JaCoCo
  requirements were not fully met: five rule warnings before and four after.
  Commons Parent 50 already sets `commons.jacoco.haltOnFailure=false`; that
  setting was preserved. Coverage-check warnings are recorded separately from
  successful test execution and Maven exit status.
- Preserved both runs' complete Maven logs, metadata, JaCoCo execution data,
  HTML/XML/CSV reports, Surefire reports, source and class hashes, and compiled
  production ZIPs outside the checkout. Added a
  [machine-readable comparison](../data/experiments/peekable-input-stream/source-exceptions/coverage/comparison.json).
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
