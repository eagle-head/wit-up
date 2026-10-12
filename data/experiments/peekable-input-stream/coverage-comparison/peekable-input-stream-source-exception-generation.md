# PeekableInputStream exception-only Java-source generation assessment

[Documentation index](../README.md) | [Study log](../study-log.md) |
[Prepared source prompt](../prompts/exception-test-generation-source.txt)

Assessed on October 11, 2026, and supplemented that day with a post-generation
JaCoCo comparison at the user's request. The initial assessment used existing
execution evidence only; its complete text is preserved in the
[assessment before coverage](../../data/experiments/peekable-input-stream/source-exceptions/coverage/assessment-before-coverage.md).
The supplement executes the existing suite before and after adding the exact
generated file in an isolated checkout. The entire generated file remains in
one Java block below. No tests, assertions, production, dependencies, build
configuration, or generation prompts were corrected. No mutation analysis or
additional standalone Checkstyle assessment was performed.

## Outcome

The generated suite contains **17 test methods and 17 executed cases: all passed,
with no failures, errors, or skips**. It stays within the requested exception-only
scope. Expectations are consistent with the inspected production source and the
observed execution. No unsuccessful test or newly confirmed production defect
is reported by this run.

The broader repository run also returned exit code 0. Its 137 Surefire XML
reports contain **1,558 reported cases: 1,552 passed and 6 skipped, with no
failures or errors**. The generated class passed again in that run.

The subsequent JaCoCo measurement increased target line coverage from **0/16
(0.00%) to 13/16 (81.25%)** and target branch coverage from **0/8 (0.00%) to
8/8 (100.00%)**. All 17 generated cases passed with instrumentation enabled.
Both coverage builds returned exit code 0, but inherited project-wide coverage
requirements were not fully met; their warnings are reported separately below.

This demonstrates a bounded ability to derive runnable exception tests from
Java source under the revised protocol. It does not establish complete exception
coverage, sensitivity to production mutations, exact internal path execution, or
equivalence to the full reference suite. The generated file's Checkstyle
compliance remains unverified because the Maven check excluded test source.

## Trial identity and input preservation

| Item | Recorded value |
| --- | --- |
| Model and reasoning | User-reported **GPT-6.1 Sol Extra High**; the retrieved chat does not independently expose these settings. |
| Generation chat | `Add PeekableInputStream exceptionals`, ID `01a12da4-040e-7c71-9e75-e5d70e44a952`. |
| Branch | `test/peekable-input-stream-exceptions`. |
| Starting and current HEAD | `d7a3c884d07ff5f1829b09087f34dcb8043f0f64`. |
| Designated scenario source | Java production source under "D:/Projects/wit-up/commons-io/src/main/java". |
| Submitted input | The prompt was supplied as a pasted-text attachment in a new chat. |
| Observed generation | One completed turn and one target-file creation; no subsequent test-file repair in the retrieved record. |
| Local turn time | October 11, 2026, 21:04:47–21:15:46 in America/New_York, UTC−04:00. |
| UTC turn time | `2026-10-12T01:04:47Z` to `2026-10-12T01:15:46Z`. |
| Recorded duration | `659405 ms`, approximately 10 minutes 59 seconds, including inspection and repository verification. |
| Generated file | "D:/Projects/wit-up/commons-io/src/test/java/org/apache/commons/io/input/buffer/PeekableInputStreamTest.java". |
| Generated source SHA-256 | `653D136D35FDAC4E556D76C1AD0965E82E05706ADDB91DD549E991FCE06B5221`. |
| Prepared prompt SHA-256 | `61DEBBF6647167F5CDDEBBCD5E06C1EC71C09782541DD8537E93114212F01063`. |
| Submitted attachment SHA-256 | `E66872D5E0EE4C729BD405A7BF45118D31A1CFD32359AA11489F73494D53E284`. |
| Tokens and cost | Unavailable in the retrieved record. |

The attachment matches the prepared prompt after normalizing CRLF to LF and
trimming trailing whitespace. Their byte hashes differ; no byte-identity claim
is made for those two files. Neither prompt was changed after observing the run.

The preparation record printed the expected HEAD, `tracked_diff_exit=0`, and
`target_test_exists=False`. The inspection batch nevertheless had exit code 1;
the generation agent attributed this to an optional read of a missing root
"AGENTS.md". The available output contains the successful preparation predicates,
but no detailed missing-file diagnostic. This batch status is retained separately
from the two successful Maven commands.

Current Git inspection again finds no tracked differences from the baseline.
Only the generated test is untracked. Existing XML properties identify Temurin
Java `1.8.0_504`, JUnit Jupiter `5.5.2`, and Surefire `2.22.2`; the recorded
Maven executable path identifies version `3.9.16`.

## Recorded validation

Both commands ran from "D:/Projects/wit-up/commons-io".

| Command | Recorded exit | Reported cases | Failures | Errors | Skips |
| --- | ---: | ---: | ---: | ---: | ---: |
| `mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" "-Dtest=org.apache.commons.io.input.buffer.PeekableInputStreamTest" clean test` | 0 | 17 | 0 | 0 | 0 |
| `mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura"` | 0 | 1,558 | 0 | 0 | 6 |

The second command used the checkout's configured default goals:
`clean verify apache-rat:check clirr:check checkstyle:check javadoc:javadoc`.
The generation agent reported completing license, compatibility, Checkstyle,
and Javadoc checks. The retrieved broader-build output is truncated, so it does
not independently expose every goal's complete diagnostics. The exit status,
target XML, full-suite aggregation, and Checkstyle XML remain available.

The archived target Surefire XML and text report come from the second clean run.
The first run is preserved through its retrieved command output, which records
17 passing cases and a successful build. These are two executions of the same
17 cases, not 34 distinct generated cases.

Independent aggregation confirms 137 suite reports and the stated totals.
The reported total equals the original 1,541-case baseline plus 17 generated
cases. The six skips belong to existing suites:
`FileUtilsCleanDirectoryTestCase` (2), `FileUtilsTestCase` (1),
`BOMInputStreamTest` (1), and `CharSequenceInputStreamTest` (2).

The agent retained existing unchecked-operation and deprecated-API diagnostics
and reported a Javadoc warning about unknown parameter `docEncoding`. Two
command outputs are marked truncated in the retrieved chat: a convention/build
configuration read and the broader Maven output. The capture does not reproduce
every diagnostic.

Coverage profiles were disabled in both original generation commands. Neither
produced JaCoCo or PIT measurements. JaCoCo was subsequently run for the
separate assessment below; PIT remains unmeasured for this generated suite.

## Post-generation JaCoCo comparison

### Design and execution controls

This is a **reconstructed before/after measurement**, performed after generation
was complete. It does not recover a generation-time coverage report. Coverage
results were not supplied to the generator, and the used prompt remains unchanged.

The before state was a detached checkout of
`d7a3c884d07ff5f1829b09087f34dcb8043f0f64`, with the existing repository tests
and without the target test. The after state added only the preserved
"PeekableInputStreamTest.java", with the SHA-256 recorded above. Both runs used
the same temporary directory,
"D:/Projects/wit-up/.worktrees/commons-io-coverage", without changing the active
branch or the original checkout. No test exclusions or coverage filters were added.

Both runs used Temurin `1.8.0_504`, Maven `3.9.16`, JUnit Jupiter `5.5.2`,
Surefire `2.22.2`, and JaCoCo `0.8.14` on Windows. The identical command was:

```powershell
mvn -B -Pjacoco "-Djacoco.skip=false" clean verify jacoco:report
```

Each clean build started with an empty coverage data file. The agent accumulated
execution data across Surefire's forked processes. Before starting the second
clean build, the first run's execution data, HTML/XML/CSV coverage reports,
Surefire reports, logs, and compiled production outputs were archived outside
the checkout. The same artifacts were archived after the second run.

The [machine-readable comparison](../../data/experiments/peekable-input-stream/source-exceptions/coverage/comparison.json)
records the controls and all counters. All 398 common files under "src" and
all 172 files under "target/classes" were byte-identical between states. The
only additional source was the generated target test. Comparing test identities
and outcomes found exactly 17 added passing target cases, no removed or changed
existing cases, and the same six skipped cases. The report's original evidence,
prompts, generated source, and original checkout's build artifacts also remained
unchanged across 1,108 recorded file hashes.

| State | Local execution time, October 11 (UTC−04:00) | Suite XML files | Reported cases | Passed | Failures / errors | Skipped | Maven exit |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Before: existing suite | 21:45:40–21:48:59 | 136 | 1,541 | 1,535 | 0 / 0 | 6 | 0 |
| After: existing suite plus generated file | 21:49:48–21:53:08 | 137 | 1,558 | 1,552 | 0 / 0 | 6 | 0 |

UTC timestamps, executable paths, arguments, and exit codes are retained in each
run's metadata. These are fresh assessment executions, separate from the two
original generation executions described above.

### Target coverage

Percentages equal covered units divided by total units, rounded to two decimal
places. Deltas are percentage points (pp), calculated before rounding.

| JaCoCo counter for `PeekableInputStream` | Before | After | Added covered units | Change |
| --- | ---: | ---: | ---: | ---: |
| Lines | 0/16 (0.00%) | 13/16 (81.25%) | 13 | +81.25 pp |
| Branches | 0/8 (0.00%) | 8/8 (100.00%) | 8 | +100.00 pp |
| Instructions | 0/98 (0.00%) | 87/98 (88.78%) | 87 | +88.78 pp |
| Methods, including constructors | 0/4 (0.00%) | 3/4 (75.00%) | 3 | +75.00 pp |

The remaining uncovered source lines are **49, 50, and 92**. Lines 49–50 belong
to the default-capacity constructor, whose only generated invocation fails in
the superclass constructor. Line 92 delegates the slice comparison; the generated
slice invocations that reach it throw from the delegated method. These are
instrumentation results, not evidence that the corresponding statements were
never entered. JaCoCo explains that an exception can interrupt execution before
a subsequent probe records the preceding instructions. See the
[JaCoCo exception coverage explanation](https://www.jacoco.org/jacoco/trunk/doc/faq.html).

The whole-array overload has 6/6 covered lines and 4/4 branches; the slice
overload has 5/6 covered lines and 4/4 branches. The sized constructor has 2/2
covered lines, and the default-capacity constructor has 0/2. The successful
whole-array peek used to prepare the array-bounds fixture contributes coverage
even though its return value is not asserted.

**100% target branch coverage does not mean complete exception coverage or
reference-suite equivalence.** JaCoCo's branch counter counts conditional
alternatives and does not count exception handling as branches. Several
exception checks are also implemented in delegated classes, outside this
target-class denominator. Coverage measures execution, not oracle strength.
See the [JaCoCo counter definitions](https://www.jacoco.org/jacoco/trunk/doc/counters.html).

### Delegated classes and project context

| Scope | Lines before | Lines after | Branches before | Branches after |
| --- | ---: | ---: | ---: | ---: |
| `CircularBufferInputStream` | 34/47 (72.34%) | 35/47 (74.47%) | 15/22 (68.18%) | 16/22 (72.73%) |
| `CircularByteBuffer` | 25/74 (33.78%) | 37/74 (50.00%) | 12/58 (20.69%) | 26/58 (44.83%) |
| Entire project, 161 measured classes | 5,429/6,087 (89.19%) | 5,458/6,087 (89.67%) | 2,507/2,910 (86.15%) | 2,534/2,910 (87.08%) |

The project-level observed changes are **+29 covered lines (+0.48 pp)** and
**+27 covered branches (+0.93 pp)**. They cannot all be attributed to the
generated tests. Outside the target, its two buffer dependencies, and the
`BrokenInputStream` fixture, coverage also changed in `FileEntry` (+3 branches)
and `FileAlterationMonitor` (+1 line, +1 branch). These classes are outside the
generated scenarios; their changes were not causally isolated. The complete
class-level differences are preserved in the comparison JSON.

This single pair provides concrete counters with preserved inputs and outputs.
It does not establish repeated-run stability of every project counter. The
target result is the primary measure; whole-project coverage supplies context.
The reconstructed baseline uses the corrected production commit and is separate
from the October 9 measurement on the earlier production revision.

### Coverage checks and retained diagnostics

Both Maven commands reported `BUILD SUCCESS`, but **the inherited JaCoCo
coverage requirements were not fully met**. Commons Parent 50 configures
`commons.jacoco.haltOnFailure=false`, so coverage violations are warnings.
That setting and all thresholds were retained unchanged.

| Project-wide requirement | Minimum | Before | After |
| --- | ---: | ---: | ---: |
| Classes | 100% | 98.76% — not met | 99.38% — not met |
| Instructions | 90% | 89.36% — not met | 90.05% — met |
| Methods | 95% | 88.93% — not met | 89.26% — not met |
| Branches | 85% | 86.15% — met | 87.08% — met |
| Lines | 90% | 89.19% — not met | 89.67% — not met |
| Complexity | 85% | 83.34% — not met | 84.01% — not met |

There were five coverage-rule warnings before and four after. Complete logs also
retain the six skipped tests, the Git branch-information warning from the
detached checkout, and existing compiler diagnostics. No warning was suppressed
or threshold relaxed. This assessment does not correct those coverage deficits.

### Reproduction and preservation

Recreate a disposable checkout at the recorded commit with the target test
absent. Run the command above using the recorded Java and Maven versions, then
preserve the entire measurement before another clean build. Restore the exact
Java appendix as the target test, verify its SHA-256, and repeat the same command.
Compare the test identities, production bytes, and JaCoCo XML counters before
interpreting the delta. The temporary measurement checkout is disposable; the
retained artifacts below are outside it.

- [Before JaCoCo HTML](../../data/experiments/peekable-input-stream/source-exceptions/coverage/before/jacoco/index.html), [XML](../../data/experiments/peekable-input-stream/source-exceptions/coverage/before/jacoco/jacoco.xml), and [CSV](../../data/experiments/peekable-input-stream/source-exceptions/coverage/before/jacoco/jacoco.csv).
- [After JaCoCo HTML](../../data/experiments/peekable-input-stream/source-exceptions/coverage/after/jacoco/index.html), [XML](../../data/experiments/peekable-input-stream/source-exceptions/coverage/after/jacoco/jacoco.xml), and [CSV](../../data/experiments/peekable-input-stream/source-exceptions/coverage/after/jacoco/jacoco.csv).
- Complete Maven logs: [before](../../data/experiments/peekable-input-stream/source-exceptions/coverage/before/maven.log) and [after](../../data/experiments/peekable-input-stream/source-exceptions/coverage/after/maven.log).
- Execution metadata: [before](../../data/experiments/peekable-input-stream/source-exceptions/coverage/before/run.json) and [after](../../data/experiments/peekable-input-stream/source-exceptions/coverage/after/run.json).
- Test identities and outcomes: [before](../../data/experiments/peekable-input-stream/source-exceptions/coverage/before/suite-summary.json) and [after](../../data/experiments/peekable-input-stream/source-exceptions/coverage/after/suite-summary.json).
- [Counter comparison and controls](../../data/experiments/peekable-input-stream/source-exceptions/coverage/comparison.json) and [original-file preservation hashes](../../data/experiments/peekable-input-stream/source-exceptions/coverage/preservation-manifest.json).
- [Coverage artifact inventory and hashes](../../data/experiments/peekable-input-stream/source-exceptions/coverage/artifact-manifest.json).
- [Artifact, appendix, and link verification](../../data/experiments/peekable-input-stream/source-exceptions/coverage/verification.json), including the previously unavailable historical study-log artifacts.

Each run directory additionally retains "jacoco.exec", every Surefire report,
environment output, source and compiled-output hash manifests, and a ZIP of the
compiled production outputs. The initial report copy preserves the premeasurement
text, including its original statement that coverage was unavailable. Its relative
links retain the original report location as their reference context.
After verifying the retained artifacts, the temporary checkout was removed.
The original branch and generated source remain in place.

## Generated scenarios and source associations

The suite contains 17 `assertThrows` calls and 14 `assertEquals` calls checking
exception messages: **31 assertion call sites**. All 17 cases completed without
failure; the source count is not a coverage or mutation metric.

| Asserted exception | Cases |
| --- | ---: |
| `NullPointerException` | 4 |
| `IllegalArgumentException` | 8 |
| `IOException` | 2 |
| `EOFException` | 2 |
| `ArrayIndexOutOfBoundsException` | 1 |
| **Total** | **17** |

The following keys identify current production files. Line locators below refer
to this unchanged checkout, not to the generated report's appendix.

| Key | Source file |
| --- | --- |
| P | "D:/Projects/wit-up/commons-io/src/main/java/org/apache/commons/io/input/buffer/PeekableInputStream.java" |
| C | "D:/Projects/wit-up/commons-io/src/main/java/org/apache/commons/io/input/buffer/CircularBufferInputStream.java" |
| B | "D:/Projects/wit-up/commons-io/src/main/java/org/apache/commons/io/input/buffer/CircularByteBuffer.java" |
| R | "D:/Projects/wit-up/commons-io/src/main/java/org/apache/commons/io/input/BrokenInputStream.java" |
| N | "D:/Projects/wit-up/commons-io/src/main/java/org/apache/commons/io/input/NullInputStream.java" |

P declares `PeekableInputStream(InputStream)` at lines 48–49,
`PeekableInputStream(InputStream, int)` at 38–39, `peek(byte[])` at 61–70,
and `peek(byte[], int, int)` at 83–92. C supplies the constructors and
`fillBuffer()`; B supplies delegated `peek(byte[], int, int)` validation
and comparison. All peek fixtures use explicit capacity 2. Unless stated
otherwise, they use a fresh `NullInputStream(0)` and zeroed comparison arrays.

| Generated test | Expected exception | Concrete fixture and source support |
| --- | --- | --- |
| `testConstructorRejectsNullInputStream` | `NullPointerException` | Null input through P's default constructor, lines 48–49; C default constructor 60–61 delegates to null validation at 43–44. Checks message `InputStream`. |
| `testSizedConstructorRejectsNullInputStream` | `NullPointerException` | Null input and capacity 2; P sized constructor 38–39 → C 43–44. Checks message `InputStream`. |
| `testSizedConstructorRejectsZeroBufferSize` | `IllegalArgumentException` | Nonnull input and capacity 0; P sized constructor 38–39 → C capacity guard 45–46. Checks `Invalid buffer size: 0`. |
| `testPeekRejectsNullBuffer` | `NullPointerException` | Null comparison array; P whole-array overload 61–62. Checks `Buffer`. |
| `testPeekSliceRejectsNullBuffer` | `NullPointerException` | Null array, offset 0, length 1; P slice overload 83–84. Checks `Buffer`. |
| `testPeekRejectsBufferLargerThanCapacity` | `IllegalArgumentException` | Array size 3 exceeds capacity 2; P whole-array guard 63–65. Checks the size/capacity message. |
| `testPeekSliceRejectsBufferLargerThanCapacity` | `IllegalArgumentException` | Array size 3, offset 0, length 1; P slice guard 85–87 checks the whole array size. Checks the size/capacity message. |
| `testPeekRejectsEmptyBuffer` | `IllegalArgumentException` | Array size 0; P 67–70 delegates offset 0 to B 148–149. Checks `Invalid offset: 0`. |
| `testPeekPropagatesReadFailure` | `IOException` | Fresh `BrokenInputStream()`, array size 1; P 67–68 → C refill 69–76 → R `read()` 61–62. R constructor 50–51 supplies message `Broken input stream`. |
| `testPeekSlicePropagatesReadFailure` | `IOException` | Same failure input, array size 1, offset 0, length 1; P 89–90 → C refill → R read. Checks the same message. |
| `testPeekPropagatesEndOfFileException` | `EOFException` | `NullInputStream(0, true, true)`, array size 1; P 67–68 → C 76 → N bulk read 242–243 and `doEndOfFile()` 342–345. |
| `testPeekSlicePropagatesEndOfFileException` | `EOFException` | Same EOF input, array size 1, offset 0, length 1; P 89–90 → C 76 → N read and EOF handling. |
| `testPeekSliceRejectsNegativeOffset` | `IllegalArgumentException` | Array size 2, offset −1, length 1; P slice delegation 89–92 → B 148–149. Checks `Invalid offset: -1`. |
| `testPeekSliceRejectsOffsetAtBufferLength` | `IllegalArgumentException` | Array size 2, offset 2, length 1; P 89–92 → B 148–149. Checks `Invalid offset: 2`. |
| `testPeekSliceRejectsNegativeLength` | `IllegalArgumentException` | Array size 2, offset 0, length −1; P 89–92 → B 151–152. Checks `Invalid length: -1`. |
| `testPeekSliceRejectsLengthLargerThanCapacity` | `IllegalArgumentException` | Array size 2, offset 0, length 3; P 89–92 → B 151–152. Checks `Invalid length: 3`. |
| `testPeekSliceThrowsWhenMatchingSliceExceedsArray` | `ArrayIndexOutOfBoundsException` | `NullInputStream(2)`, array size 2; a whole-array peek fills the buffer outside the assertion. The target slice uses offset 1 and length 2; P 89–92 → B 148–159. |

N's one-argument constructor at 91–92 selects nonthrowing EOF behavior;
its three-argument constructor at 106–109 supports the explicit EOF fixtures.
Its bulk read at 238–252 leaves the fresh zeroed refill array unchanged through
`processBytes()` at 330–331. These production implementations supply fixture
behavior within the designated source location. R's inherited bulk-read
delegation is not separately instrumented by the tests.

## Oracle strength and fixture interpretation

Setup is outside each exception assertion. Constructor assertions invoke the
target constructor directly; peek assertions invoke exactly one target overload.
A setup exception therefore cannot satisfy the intended target assertion.

The 14 message comparisons distinguish selected validation and propagation
outcomes more precisely than exception type alone. However, `assertThrows`
accepts the requested class or a subclass. The tests do not assert exact runtime
classes, exception-object identity, or complete internal execution traces.
Implementation messages are supported by the selected source, without being
independently established as a stable public contract.

The array-bounds fixture has a meaningful setup sequence: the initial whole-array
peek fills both internal slots with zero bytes. In the asserted slice invocation,
the requested length 2 equals the buffered count 2 and the first compared byte
matches. The next comparison accesses index 2 of a two-element array. This
source trace explains why ordinary public setup reaches the observed exception;
the test does not inspect or write private state. It records current behavior
for this invalid slice and does not independently confirm a production defect.

The chosen capacities, array lengths, offsets, and stream sizes are concrete
fixture values satisfying source predicates, not exported solver assignments.
Capacity 2 differs from the documented default 8192; the explicit EOF fixtures
change `throwEofException` from the one-argument constructor's default false
to true. These choices are disclosed in the generation response.

The EOF cases exercise propagation of an input stream's `EOFException`.
They do not test the earlier normal-return false matches involving zero or
stale buffered bytes. Normal-result cases were deliberately excluded by this
prompt. No original-versus-corrected production comparison was performed.

## Unrepresented candidates and completeness limits

The generation agent identified the following omissions:

| Candidate family | Reported reason |
| --- | --- |
| Negative capacities, offsets beyond the array end, empty slice arrays, and combined invalid arguments | Classified as redundant with represented validation guards. |
| A read from an already exhausted `NullInputStream` | Another delegated `IOException` route; read-error propagation was already represented. |
| `NegativeArraySizeException` in B's constructor | C rejects nonpositive capacities before creating the internal buffer. |
| Exceptions from B's bulk `add` | No supported target fixture through the inspected refill implementations with valid read counts. |
| Delegated length validation in the whole-array overload | It delegates a nonnegative array length after the target capacity guard. |

These are the agent's identified candidates, not a measured exhaustive inventory
of all exceptional behavior. Guard overlap does not prove equivalence for every
argument combination, validation order, or input-stream implementation.
No omitted candidate was represented as a skipped JUnit case. Exceptions in
inherited methods outside the constructors and declared peek overloads were
outside the requested scope.

## Repository conventions and context boundaries

The archived Checkstyle XML reports **156 files and zero errors**, with **zero
test-source files**. The generated file was explicitly absent from that scope.
The passing Maven gate therefore does not validate its style.

Source inspection finds no method Javadocs on the 17 public test methods, while
the configured `JavadocMethod` rule requires documentation when that source is
checked. This is a convention gap identified from source and configuration.
No direct test-source Checkstyle invocation was recorded or performed here;
an exact count of failing diagnostics is not claimed. The file uses imported
simple type names, has no tabs, and its longest line has 134 characters.

The visible generation record contains scoped CodeGraph queries for P, C, B,
R, and N, a direct read of B after the tool withheld its stale indexed slice,
and an unrelated `ByteOrderParserTest` read for conventions. The recorded
CodeGraph responses expose only the requested production files; no prior target
test, JSON source, or study finding appears in those responses. The index warning
for B does not establish a generation-time production change: Git and the current
source still match the baseline.

No custom skill loading, earlier target-test retrieval, alternative-source
consultation, or post-validation assertion rewrite is visible in the command
record. Broader build verification and generated Javadocs occurred after the
single test-file creation. These observations support the documented source-use
boundary, but do not independently isolate every injected instruction, memory,
or other hidden context input.

## Relationship to the earlier trials and reference suite

This is the first reviewed Java-source result under the new exception-only
paired prompts. Its 17/17 outcome differs from the earlier broad source trial's
21 passed, 4 failures, and 1 error, but the scope and instructions also changed.
The improvement in the observed pass fraction cannot be attributed solely to
model behavior or prompting quality.

The earlier JSON trial's 12 passing cases used the previous JSON prompt.
It is not the matching comparator for this new protocol. No result from the
new paired JSON prompt is part of the evidence reviewed here.

The full reference suite's historical 34 passing target cases, 16/16 covered
lines, 8/8 covered branches, and 14/14 killed default target mutations remain
measurements of another suite. They do not transfer to this generated output.
The reference includes normal behavior and EOF regression cases outside the
new exception-only scope. The new measurement gives this output 13/16 lines and
8/8 branches, compared with the reference's historical 16/16 and 8/8. Equal branch
coverage does not establish equal behavior or assertion strength. The reference
was not rerun in this assessment, and its original raw coverage reports remain
unavailable. Exception-path completeness and mutation sensitivity of this
generated output remain unmeasured.

## Preserved evidence

Existing reports were copied outside "D:/Projects/wit-up/commons-io/target"
and checked byte-for-byte against their originals. The full-suite summary was
derived from existing XML files. Retrieved command output was archived with
normalized line endings; the broader output remains truncated. The selected
chat record preserves statuses and provenance and is not a full context capture.

- [Target Surefire XML](../../data/experiments/peekable-input-stream/source-exceptions/surefire.xml)
- [Target Surefire text report](../../data/experiments/peekable-input-stream/source-exceptions/surefire.txt)
- [Checkstyle XML](../../data/experiments/peekable-input-stream/source-exceptions/checkstyle.xml)
- [Existing full-suite summary](../../data/experiments/peekable-input-stream/source-exceptions/suite-summary.json)
- [Retrieved target-run output](../../data/experiments/peekable-input-stream/source-exceptions/target-test-run.log)
- [Retrieved broader-build output, truncated](../../data/experiments/peekable-input-stream/source-exceptions/repository-verification.log)
- [Selected generation-chat records](../../data/experiments/peekable-input-stream/source-exceptions/generation-record.json)

The original generated file remains unchanged in the checkout. The appendix
preserves its license header, imports, 17 methods, fixture comment, and all
31 assertion calls. It contains no corrected alternative.

## Appendix: complete generated Java source

```java
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.apache.commons.io.input.buffer;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import java.io.EOFException;
import java.io.IOException;

import org.apache.commons.io.input.BrokenInputStream;
import org.apache.commons.io.input.NullInputStream;
import org.junit.jupiter.api.Test;

public class PeekableInputStreamTest {

    @Test
    public void testConstructorRejectsNullInputStream() {
        final NullPointerException exception = assertThrows(NullPointerException.class,
                () -> new PeekableInputStream(null));
        assertEquals("InputStream", exception.getMessage());
    }

    @Test
    public void testSizedConstructorRejectsNullInputStream() {
        final NullPointerException exception = assertThrows(NullPointerException.class,
                () -> new PeekableInputStream(null, 2));
        assertEquals("InputStream", exception.getMessage());
    }

    @Test
    public void testSizedConstructorRejectsZeroBufferSize() {
        final NullInputStream input = new NullInputStream(0);

        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class,
                () -> new PeekableInputStream(input, 0));
        assertEquals("Invalid buffer size: 0", exception.getMessage());
    }

    @Test
    public void testPeekRejectsNullBuffer() {
        final PeekableInputStream stream = new PeekableInputStream(new NullInputStream(0), 2);

        final NullPointerException exception = assertThrows(NullPointerException.class, () -> stream.peek(null));
        assertEquals("Buffer", exception.getMessage());
    }

    @Test
    public void testPeekSliceRejectsNullBuffer() {
        final PeekableInputStream stream = new PeekableInputStream(new NullInputStream(0), 2);

        final NullPointerException exception = assertThrows(NullPointerException.class, () -> stream.peek(null, 0, 1));
        assertEquals("Buffer", exception.getMessage());
    }

    @Test
    public void testPeekRejectsBufferLargerThanCapacity() {
        final PeekableInputStream stream = new PeekableInputStream(new NullInputStream(0), 2);
        final byte[] comparison = new byte[3];

        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class, () -> stream.peek(comparison));
        assertEquals("Peek request size of 3 bytes exceeds buffer size of 2 bytes", exception.getMessage());
    }

    @Test
    public void testPeekSliceRejectsBufferLargerThanCapacity() {
        final PeekableInputStream stream = new PeekableInputStream(new NullInputStream(0), 2);
        final byte[] comparison = new byte[3];

        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class, () -> stream.peek(comparison, 0, 1));
        assertEquals("Peek request size of 3 bytes exceeds buffer size of 2 bytes", exception.getMessage());
    }

    @Test
    public void testPeekRejectsEmptyBuffer() {
        final PeekableInputStream stream = new PeekableInputStream(new NullInputStream(0), 2);
        final byte[] comparison = new byte[0];

        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class, () -> stream.peek(comparison));
        assertEquals("Invalid offset: 0", exception.getMessage());
    }

    @Test
    public void testPeekPropagatesReadFailure() {
        final PeekableInputStream stream = new PeekableInputStream(new BrokenInputStream(), 2);
        final byte[] comparison = new byte[1];

        final IOException exception = assertThrows(IOException.class, () -> stream.peek(comparison));
        assertEquals("Broken input stream", exception.getMessage());
    }

    @Test
    public void testPeekSlicePropagatesReadFailure() {
        final PeekableInputStream stream = new PeekableInputStream(new BrokenInputStream(), 2);
        final byte[] comparison = new byte[1];

        final IOException exception = assertThrows(IOException.class, () -> stream.peek(comparison, 0, 1));
        assertEquals("Broken input stream", exception.getMessage());
    }

    @Test
    public void testPeekPropagatesEndOfFileException() {
        final NullInputStream input = new NullInputStream(0, true, true);
        final PeekableInputStream stream = new PeekableInputStream(input, 2);
        final byte[] comparison = new byte[1];

        assertThrows(EOFException.class, () -> stream.peek(comparison));
    }

    @Test
    public void testPeekSlicePropagatesEndOfFileException() {
        final NullInputStream input = new NullInputStream(0, true, true);
        final PeekableInputStream stream = new PeekableInputStream(input, 2);
        final byte[] comparison = new byte[1];

        assertThrows(EOFException.class, () -> stream.peek(comparison, 0, 1));
    }

    @Test
    public void testPeekSliceRejectsNegativeOffset() {
        final PeekableInputStream stream = new PeekableInputStream(new NullInputStream(0), 2);
        final byte[] comparison = new byte[2];

        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class, () -> stream.peek(comparison, -1, 1));
        assertEquals("Invalid offset: -1", exception.getMessage());
    }

    @Test
    public void testPeekSliceRejectsOffsetAtBufferLength() {
        final PeekableInputStream stream = new PeekableInputStream(new NullInputStream(0), 2);
        final byte[] comparison = new byte[2];

        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class, () -> stream.peek(comparison, 2, 1));
        assertEquals("Invalid offset: 2", exception.getMessage());
    }

    @Test
    public void testPeekSliceRejectsNegativeLength() {
        final PeekableInputStream stream = new PeekableInputStream(new NullInputStream(0), 2);
        final byte[] comparison = new byte[2];

        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class, () -> stream.peek(comparison, 0, -1));
        assertEquals("Invalid length: -1", exception.getMessage());
    }

    @Test
    public void testPeekSliceRejectsLengthLargerThanCapacity() {
        final PeekableInputStream stream = new PeekableInputStream(new NullInputStream(0), 2);
        final byte[] comparison = new byte[2];

        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class, () -> stream.peek(comparison, 0, 3));
        assertEquals("Invalid length: 3", exception.getMessage());
    }

    @Test
    public void testPeekSliceThrowsWhenMatchingSliceExceedsArray() throws IOException {
        final PeekableInputStream stream = new PeekableInputStream(new NullInputStream(2), 2);
        final byte[] comparison = new byte[2];
        // Fill both slots so the length equality guard permits comparison.
        stream.peek(comparison);

        assertThrows(ArrayIndexOutOfBoundsException.class, () -> stream.peek(comparison, 1, 2));
    }
}
```
