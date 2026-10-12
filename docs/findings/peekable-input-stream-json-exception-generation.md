# PeekableInputStream exception-only JSON generation assessment

[Documentation index](../README.md) | [Study log](../study-log.md) |
[Prepared JSON prompt](../prompts/exception-test-generation-json.txt) |
[Paired source assessment](peekable-input-stream-source-exception-generation.md)

Assessed on October 11, 2026. This report preserves the original generation
outcome and adds a separately executed JaCoCo comparison requested afterward.
All reported coverage and test-result comparisons concern only
`org.apache.commons.io.input.buffer.PeekableInputStream` and its dedicated test.
The complete generated source appears in one Java block at the end.
No generated test, assertion, fixture, production file, dependency, configuration,
or prompt was corrected. No mutation analysis was performed.

## Outcome

The generator created **11 test methods with 11 exception assertions**.
The original required Maven command failed at Apache RAT before compilation:
the local cache file ".ruff_cache/CACHEDIR.TAG" had an unapproved license.
**No tests executed during generation.** Target assertion failures, errors,
and skips were unmeasured, rather than zero. This original failure remains part
of the result and is not replaced by the later assessment.

In the later isolated coverage run, **all 11 cases compiled and passed**, with
zero failures, errors, or skips. Target coverage increased from **0/16 to
12/16 lines (75.00%)** and **0/8 to 7/8 branches (87.50%)**. This establishes
runnable exception fixtures under the recorded measurement conditions; the
original generation-time build remains blocked in its preserved record.

The tests address eight `IllegalArgumentException` scenarios, two
`NullPointerException` scenarios, and one `ArrayIndexOutOfBoundsException`
scenario. Their source associations refer to 11 distinct SAT records out of
31 candidates. These associations are not measurements of internal path
reproduction. The expectations check exception types only.

## Trial identity and preserved input

| Item | Recorded value |
| --- | --- |
| Model and reasoning | User-reported **GPT-6.1 Sol Extra High**; the retrieved chat does not independently expose these settings. |
| Generation chat | `Add PeekableInputStream exception`, ID `01a12e16-d71c-7790-be72-d9f9af70f175`. |
| Branch | `test/peekable-input-stream-exception-conditions`. |
| Generation and measurement baseline | `d7a3c884d07ff5f1829b09087f34dcb8043f0f64`. |
| Local generation time | October 11, 2026, 23:10:12–23:22:34, America/New_York, UTC−04:00. |
| UTC generation time | `2026-10-12T03:10:12Z` to `2026-10-12T03:22:34Z`. |
| Recorded duration | `742116 ms`, approximately 12 minutes 22 seconds, including inspection and failed validation commands. |
| Observed creation | One completed generation turn and one target-file creation; no subsequent test rewrite in the retrieved record. |
| Source file | "D:/Projects/wit-up/commons-io/src/test/java/org/apache/commons/io/input/buffer/PeekableInputStreamTest.java". |
| Source SHA-256 | `C8FCE4484A2B0A8620DB781029F9BDC698FB69ED5AD15F015F2BED1ED98A5536`. |
| Prepared JSON prompt SHA-256 | `945BEA425089EE30FFE3230EF1B104E74D7F8CC58B53354F94D23DB4B5C5246F`. |
| Submitted attachment SHA-256 | `68EE4242856375F87A8FEA4CD5093D30AC9C758698E307F709D2451764209D7E`. |
| Tokens and cost | Unavailable; no estimate is substituted. |

The attachment matches the prepared prompt after newline normalization and
trimming trailing whitespace; byte identity is not claimed for those two files.
The generated source is byte-identical to the file creation captured in the
generation chat, the preserved standalone copy, and the appendix.

The generation preflight confirmed the required HEAD, a clean tracked baseline,
and the absence of the target test. The completed attempt left only the new
target source untracked. Its tracked production and configuration still match
the same baseline. The [preparation record](../../data/experiments/peekable-input-stream/json-exceptions/preparation.json)
predates generation and retains its original preparation-only status.

## Original validation: stopped before compilation

All three Maven commands ran inside "D:/Projects/wit-up/commons-io":

| Command | Exit | Observed result |
| --- | ---: | --- |
| `mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" "-Dtest=org.apache.commons.io.input.buffer.PeekableInputStreamTest" clean test` | 1 | RAT rejected the local cache file before compilation and Surefire. |
| `mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" checkstyle:check` | 1 | Class-resolution diagnostics in unchanged production source; this does not establish a style failure in the generated test. |
| `mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" clean verify apache-rat:check clirr:check checkstyle:check javadoc:javadoc` | 1 | Stopped at the same RAT gate; also warned about the unknown Javadoc parameter `docEncoding`. |

The archived RAT report identifies ".ruff_cache/CACHEDIR.TAG". The target test's
license header is present. The later `clean` removed the intermediate
Checkstyle output; its command output remains preserved. The original checkout
has no Surefire reports for this attempt. Compilation, test execution, Clirr,
and Javadoc generation were not reached by the verification command.

The whitespace command
`git diff --no-index --check -- NUL src/test/java/org/apache/commons/io/input/buffer/PeekableInputStreamTest.java`
returned exit 1. Its retained output contains an LF-to-CRLF warning and no
whitespace-error diagnostic. This status is recorded separately from compilation
and test results.

## JSON inventory and scenario associations

The designated sources were
"D:/Projects/wit-up/commons-io-analysis-results/witup-results-commons-io-11f0abe7a.json"
and
"D:/Projects/wit-up/commons-io-analysis-results/witup-summaries-commons-io-11f0abe7a.json".

Independent programmatic extraction found 100 target records in each file.
Each `(artifact, pathId)` key has exactly one counterpart; overload metadata
and solver statuses agree: **31 SAT and 69 UNSAT**. The SAT summaries contain
15 `IllegalArgumentException`, four `NullPointerException`, and 12
`ArrayIndexOutOfBoundsException` records. SAT describes the exported model,
not proof of a constructible Java fixture.

| Exported signature | SAT | UNSAT | Tests / distinct associated SAT records |
| --- | ---: | ---: | ---: |
| `PeekableInputStream(InputStream, int)` | 1 | 1 | 1 |
| `peek(byte[])` | 11 | 38 | 3 |
| `peek(byte[], int, int)` | 19 | 30 | 7 |
| **Total** | **31** | **69** | **11** |

All associations below use artifact `commons-io-11f0abe7a.jar`. Prefixes expand
to these exact `pathId` values before adding `#n`:

- **C:** `<org.apache.commons.io.input.buffer.PeekableInputStream: void <init>(java.io.InputStream,int)>`.
- **W:** `<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte[])>`.
- **S:** `<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte[],int,int)>`.

| Generated test | Record | Expected exception | Fixture and concrete-value handling |
| --- | --- | --- | --- |
| `testConstructorRejectsZeroBufferSize` | C#0 | `IllegalArgumentException` | Nonnull empty input; capacity 0 retained from the model. |
| `testPeekArrayRejectsNullBuffer` | W#1 | `NullPointerException` | Null comparison; capacity 1 and empty input chosen where unspecified. |
| `testPeekArrayRejectsBufferLargerThanCapacity` | W#0 | `IllegalArgumentException` | Comparison length 1→2 and capacity 0→1 preserve length greater than capacity. |
| `testPeekArrayRejectsEmptyBuffer` | W#9 | `IllegalArgumentException` | Empty comparison retained; capacity 0→1; nonnegative occupancy assumed. |
| `testPeekSliceRejectsNullBuffer` | S#1 | `NullPointerException` | Null comparison; capacity 1, empty input, offset 0, and length 0 chosen where unspecified. |
| `testPeekSliceRejectsBufferLargerThanCapacity` | S#0 | `IllegalArgumentException` | Comparison length 1→2 and capacity 0→1; offset 0 and length 1 chosen where unspecified. |
| `testPeekSliceRejectsEmptyBuffer` | S#7 | `IllegalArgumentException` | Empty comparison and offset 0 retained; capacity 0→1; comparison length 0 chosen where unspecified. |
| `testPeekSliceRejectsNegativeOffset` | S#8 | `IllegalArgumentException` | Empty comparison and offset −1 retained; capacity 0→1; comparison length 0 chosen where unspecified. |
| `testPeekSliceRejectsNegativeLength` | S#10 | `IllegalArgumentException` | Capacity 1, comparison length 1, offset 0, and requested length −1 retained. A preparatory whole-array peek buffers a chosen zero byte. |
| `testPeekSliceRejectsLengthLargerThanCapacity` | S#9 | `IllegalArgumentException` | Requested length 1→2 and modeled internal capacity 0→1; receiver capacity 1, comparison length 1, and offset 0 retained. A preparatory peek buffers a chosen zero byte. |
| `testPeekSliceFailsWhenMatchingPrefixExceedsArrayBounds` | S#26 | `ArrayIndexOutOfBoundsException` | Input `{10,10}`, comparison `{10}`, offset 0, requested length 2; receiver capacity 1→2 and buffered count 2 replace the model's 0/1 occupancy values. Byte value 10 is retained. |

The [extracted records](../../data/experiments/peekable-input-stream/json-exceptions/target-json-records.json)
preserve the full target input records and zero-based source-array positions.
The [assessment data](../../data/experiments/peekable-input-stream/json-exceptions/assessment-data.json)
maps each test to its exact source key. Seven tests use changes to concrete
model values; choosing a value for an unspecified fixture element is a separate
assumption. The 11/31 association fraction (35.48%) is not path coverage.

## Fixture construction and oracle limits

Every exception assertion invokes a target constructor or a declared peek
overload. Stream creation and preparatory peeks stay outside the assertion.
A setup exception therefore cannot satisfy the target assertion. Stream fixtures
use `ByteArrayInputStream` and public APIs; no reflection or direct internal-state
mutation is present.

All 11 assertions use `assertThrows`. They accept the expected class or a
subclass and do not check the exact runtime class, message, cause, object identity,
or full internal trace. Try-with-resources closes the ten successfully created
streams; cleanup is outside the asserted invocation and does not count as a
separate behavior assertion.

Three tests prepare buffered content with a successful whole-array peek.
The negative-length and excessive-length fixtures buffer one zero byte.
The bounds fixture buffers two matching bytes, then compares a one-element
array over a requested length of two. The first comparison matches and the
second attempts to read beyond the comparison array. This explains an accessible
fixture for the observed exception; it does not establish a newly confirmed
production defect or reproduce all solver-local offsets and stack symbols.
These preparatory calls also contribute coverage, although their returned values
are not asserted.

The input artifact label refers to `11f0abe7a`, while generation and measurement
use the corrected production at `d7a3c884d`. The producing WIT-UP revision and
analyzed JAR bytes remain unverified. The previously changed buffer-length guard
makes this distinction material for stateful comparisons. Preserving an
exception category and selected predicates does not establish exact exported
path reproduction.

## Candidates not represented

| Candidate records | Generator's stated reason |
| --- | --- |
| W#3, S#3 | A null internal buffer was not established through a supported public fixture. |
| W#10, W#30 | Internal capacity smaller than receiver capacity was not established through public setup. |
| W#23, W#24, W#43, W#44; S#22, S#23, S#43, S#44 | Invalid internal circular-buffer offsets lacked a supported fixture. |
| W#29; S#28, S#29 | Negative buffered-byte counts in the concrete models lacked a supported fixture. |
| S#30, S#31 | Classified as redundant excessive-length and negative-length outcomes through a different buffering branch. |
| S#27, S#47, S#48 | Classified as redundant bounds-exception variants involving wrapping or another buffering branch. |

These are 20 unrepresented SAT records. The redundancy descriptions are the
generator's classifications, not proof that different state and branch conditions
are equivalent. No skipped JUnit tests represent these omissions.
The constructor C#1 record for `NegativeArraySizeException` is UNSAT and was
excluded. The target exports contain no other constructor signature or SAT
candidate naming `IOException` or `EOFException`.

## Repository conventions and generation context

The file contains a license header, imported simple type names, a class Javadoc,
and Javadocs for all 11 test methods. It has no tabs and its longest line has
113 characters, below the configured 160-character limit. Unlike the earlier
generated files, method documentation is present. These source observations do
not substitute for a successful direct test-source Checkstyle audit, which was
not recorded or performed.

The generation's CodeGraph query for an unrelated convention example returned
no matching code; the agent then read `ByteOrderMarkTestCase` for conventions.
The visible record shows programmatic target JSON joins and related constructor
records from the same designated JSON exports. It shows one test-file creation
and no post-validation rewrite, custom skill load, prior-suite retrieval, or
alternative target-source inspection. Three retrieved command outputs are
truncated, including convention/configuration and JSON output. The record is
therefore not a complete capture of every context input, and it does not prove
absence of all bias.

## Post-generation JaCoCo comparison

### Design and execution

This is a reconstructed before/after assessment, separate from generation.
Both states used the detached checkout
"D:/Projects/wit-up/.worktrees/commons-io-coverage" at the recorded baseline.
Before had no target test source; after added only the exact preserved generated
file. The active checkout, its cache, source, RAT report, and prompt files were
left unchanged.

The detached checkout started with committed baseline files. The unrelated
local ".ruff_cache" directory was absent there in both states. RAT remained
enabled and no exclusion, skip, threshold relaxation, or failure-ignore option
was added. This clean-checkout measurement does not convert the original
cache-blocked attempt into a successful generation-time build.

Both runs used Temurin `1.8.0_504`, Maven `3.9.16`, JUnit Jupiter `5.5.2`,
Surefire `2.22.2`, and JaCoCo `0.8.14` on Windows. The identical command was:

```powershell
mvn -B -Pjacoco "-Djacoco.skip=false" clean verify jacoco:report
```

Each build started with fresh execution data. The before artifacts were archived
before the after clean build. Common source bytes and compiled production
outputs were checked for identity; existing test identities and outcomes were
compared to distinguish the added target cases. Although the execution command
runs the repository suite, only target counters and target test outcomes are
reported here.

| Measurement state | Target cases | Passed | Failures | Errors | Skipped | Maven exit |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Before: target file absent | 0 | 0 | 0 | 0 | 0 | 0 |
| After: exact generated file added | 11 | 11 | 0 | 0 | 0 | 0 |

The before measurement ran locally from **23:25:51 to 23:29:13** and the after
measurement from **23:29:14 to 23:32:35** on October 11 (UTC−04:00).
Original generation and these later executions are distinct observations.
Both clean-checkout RAT checks passed with their configured rules enabled.

| Target counter | Before | After | Added covered units | Change |
| --- | ---: | ---: | ---: | ---: |
| Lines | 0/16 (0.00%) | 12/16 (75.00%) | 12 | +75.00 pp |
| Branches | 0/8 (0.00%) | 7/8 (87.50%) | 7 | +87.50 pp |
| Instructions | 0/98 (0.00%) | 85/98 (86.73%) | 85 | +86.73 pp |
| Methods, including constructors | 0/4 (0.00%) | 3/4 (75.00%) | 3 | +75.00 pp |

Percentages divide covered units by the target's totals; pp denotes percentage
points. CSV and XML target counters agree. All common source bytes and compiled
production bytes match between states and match the paired source condition's
baseline. The only added source and test cases belong to this generated class;
existing test identities and outcomes were unchanged.

The missed lines are **49, 50, 90, and 92**:

- Lines 49–50: the default-capacity constructor has no generated invocation.
- Line 90: the slice overload's refill call never executes. Its guard at line 89
  compares occupancy with the **comparison array length**, not the requested
  slice length. The relevant nonempty fixtures have already buffered content;
  empty arrays also do not require refill. This leaves one of the eight target
  branches uncovered.
- Line 92: the slice delegation is reached by validation and bounds cases, but
  those calls throw before a subsequent coverage probe records completion.
  A missed marker here does not mean the delegation was never entered.

The whole-array overload has **6/6 covered lines and 4/4 branches**; the slice
overload has **4/6 lines and 3/4 branches**. The sized constructor has 2/2 covered
lines, while the default constructor has 0/2. Three preparatory whole-array peeks
help cover that overload even though their return values are not asserted.

Coverage describes observed execution, including fixture setup. JaCoCo branch
coverage counts conditional alternatives and excludes exception handling from
its branch definition; it is not an exception-path completeness metric.
See the [JaCoCo counter definitions](https://www.jacoco.org/jacoco/trunk/doc/counters.html).
Exceptions can also interrupt execution before a later probe, leaving an entered
statement unmarked; see the [JaCoCo FAQ](https://www.jacoco.org/jacoco/trunk/doc/faq.html).

Complete Maven logs preserve their original diagnostics and exit statuses.
Inherited coverage warnings remain nonfatal under the unchanged configuration;
a successful Maven exit is not a claim that every coverage requirement passed.
The original generation failures remain separately archived.

### Paired comparison and interpretation

| Observation | Paired source exception suite | Current JSON exception suite |
| --- | ---: | ---: |
| Generated target cases | 17 | 11 |
| Original target execution | 17 passed | 0 executed; blocked before compilation |
| Later instrumented target execution | 17 passed | 11 passed |
| Lines before → after | 0/16 → 13/16 (81.25%) | 0/16 → 12/16 (75.00%) |
| Branches before → after | 0/8 → 8/8 (100.00%) | 0/8 → 7/8 (87.50%) |
| Instructions before → after | 0/98 → 87/98 (88.78%) | 0/98 → 85/98 (86.73%) |
| Methods before → after | 0/4 → 3/4 (75.00%) | 0/4 → 3/4 (75.00%) |
| Assertion detail | Exception types and 14 message assertions | Exception types only |

The current JSON output covers one fewer target line, one fewer branch, and
two fewer instructions than the paired source output. The source suite exercises
slice refill through throwing inputs, whereas the current JSON slice fixtures
do not take that branch. Passing both sets of tests does not establish equal
exception coverage or equal assertion strength.

The prompts match outside their scenario-source blocks, and both measurements
use the same corrected production baseline and toolchain. The JSON result adds
an explicit bounds fixture that the earlier JSON suite did not contain, and
uses buffered setup for its length checks. These are changes in the generated
scenarios, not proof of better overall adequacy.

The JSON exports constrain the available candidate families; the paired source
suite also includes null-constructor and I/O/EOF propagation cases absent from
this output. Neither suite checks the full normal-result and EOF-regression
scope of the reference suite. A single attempt per input source, the original
JSON build blocker, fixture assumptions, and the unknown export-producing JAR
limit causal interpretation. Mutation sensitivity remains unmeasured for both
generated exception suites.

## Evidence and reproduction

Recreate the recorded baseline in an isolated checkout without the target test,
run the coverage command, and preserve its outputs before cleaning. Add the
exact archived source, verify its hash, and repeat the same command. Preserve
failed statuses and compare source/class bytes before interpreting target deltas.
Do not rewrite the generated source to obtain a different outcome.

- [Unchanged generated Java file](../../data/experiments/peekable-input-stream/json-exceptions/PeekableInputStreamTest.java).
- [Retrieved generation record](../../data/experiments/peekable-input-stream/json-exceptions/generation-record.json) and [submitted prompt](../../data/experiments/peekable-input-stream/json-exceptions/submitted-prompt.txt).
- Original command output: [target run](../../data/experiments/peekable-input-stream/json-exceptions/generation-target-run.log), [Checkstyle](../../data/experiments/peekable-input-stream/json-exceptions/generation-checkstyle.log), [repository verification](../../data/experiments/peekable-input-stream/json-exceptions/generation-repository-verification.log), and [whitespace check](../../data/experiments/peekable-input-stream/json-exceptions/generation-whitespace-check.log).
- [Original RAT report](../../data/experiments/peekable-input-stream/json-exceptions/generation-rat.txt).
- Target JaCoCo HTML: [before](../../data/experiments/peekable-input-stream/json-exceptions/coverage/before/jacoco/org.apache.commons.io.input.buffer/PeekableInputStream.html) and [after](../../data/experiments/peekable-input-stream/json-exceptions/coverage/after/jacoco/org.apache.commons.io.input.buffer/PeekableInputStream.html).
- Original raw JaCoCo XML: [before](../../data/experiments/peekable-input-stream/json-exceptions/coverage/before/jacoco/jacoco.xml) and [after](../../data/experiments/peekable-input-stream/json-exceptions/coverage/after/jacoco/jacoco.xml).
- [Target outcomes after instrumentation](../../data/experiments/peekable-input-stream/json-exceptions/coverage/after/surefire-reports/TEST-org.apache.commons.io.input.buffer.PeekableInputStreamTest.xml).
- Measurement logs: [before](../../data/experiments/peekable-input-stream/json-exceptions/coverage/before/maven.log) and [after](../../data/experiments/peekable-input-stream/json-exceptions/coverage/after/maven.log).
- Command metadata and timestamps: [before](../../data/experiments/peekable-input-stream/json-exceptions/coverage/before/run.json) and [after](../../data/experiments/peekable-input-stream/json-exceptions/coverage/after/run.json).
- [Target coverage comparison](../../data/experiments/peekable-input-stream/json-exceptions/coverage/comparison.json), [original-file preservation manifest](../../data/experiments/peekable-input-stream/json-exceptions/original-file-manifest.json), and [verification](../../data/experiments/peekable-input-stream/json-exceptions/verification.json).
- [Artifact inventory](../../data/experiments/peekable-input-stream/json-exceptions/artifact-manifest.json).

Complete raw measurement artifacts are retained as execution evidence. Current
comparisons contain no project coverage totals or other-class coverage metrics.
The Java appendix below preserves the generated bytes, including all fixture
comments and Javadocs.

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

import static org.junit.jupiter.api.Assertions.assertThrows;

import java.io.ByteArrayInputStream;
import java.io.IOException;

import org.junit.jupiter.api.Test;

/**
 * Tests exceptional constructor and peek outcomes.
 *
 * Fixtures assume that a positive capacity initializes a nonnull circular buffer
 * with that capacity. Preparatory peeks buffer matching bytes through the public
 * API; they are fixture setup rather than independent behavior checks.
 */
public class PeekableInputStreamTest {

    /** Tests rejection of a zero buffer size. */
    @Test
    public void testConstructorRejectsZeroBufferSize() {
        final ByteArrayInputStream input = new ByteArrayInputStream(new byte[0]);
        assertThrows(IllegalArgumentException.class, () -> new PeekableInputStream(input, 0));
    }

    /**
     * Tests rejection of a null array by the whole-array overload.
     *
     * @throws IOException if stream cleanup fails
     */
    @Test
    public void testPeekArrayRejectsNullBuffer() throws IOException {
        try (PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(NullPointerException.class, () -> stream.peek(null));
        }
    }

    /**
     * Tests rejection of an array larger than the capacity by the whole-array overload.
     *
     * @throws IOException if stream cleanup fails
     */
    @Test
    public void testPeekArrayRejectsBufferLargerThanCapacity() throws IOException {
        final byte[] buffer = new byte[2];
        try (PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(buffer));
        }
    }

    /**
     * Tests rejection of an empty array by the whole-array overload.
     *
     * @throws IOException if stream cleanup fails
     */
    @Test
    public void testPeekArrayRejectsEmptyBuffer() throws IOException {
        final byte[] buffer = new byte[0];
        try (PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(buffer));
        }
    }

    /**
     * Tests rejection of a null array by the slice overload.
     *
     * @throws IOException if stream cleanup fails
     */
    @Test
    public void testPeekSliceRejectsNullBuffer() throws IOException {
        try (PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(NullPointerException.class, () -> stream.peek(null, 0, 0));
        }
    }

    /**
     * Tests rejection of an oversized array even when the requested slice fits the capacity.
     *
     * @throws IOException if stream cleanup fails
     */
    @Test
    public void testPeekSliceRejectsBufferLargerThanCapacity() throws IOException {
        final byte[] buffer = new byte[2];
        try (PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(buffer, 0, 1));
        }
    }

    /**
     * Tests rejection of offset zero when the slice array is empty.
     *
     * @throws IOException if stream cleanup fails
     */
    @Test
    public void testPeekSliceRejectsEmptyBuffer() throws IOException {
        final byte[] buffer = new byte[0];
        try (PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(buffer, 0, 0));
        }
    }

    /**
     * Tests rejection of a negative slice offset.
     *
     * @throws IOException if stream cleanup fails
     */
    @Test
    public void testPeekSliceRejectsNegativeOffset() throws IOException {
        final byte[] buffer = new byte[0];
        try (PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(buffer, -1, 0));
        }
    }

    /**
     * Tests rejection of a negative slice length after buffering a matching byte.
     *
     * @throws IOException if fixture setup or stream cleanup fails
     */
    @Test
    public void testPeekSliceRejectsNegativeLength() throws IOException {
        final byte[] buffer = {0};
        try (PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[] {0}), 1)) {
            stream.peek(buffer);
            assertThrows(IllegalArgumentException.class, () -> stream.peek(buffer, 0, -1));
        }
    }

    /**
     * Tests rejection of a slice length larger than the circular buffer capacity.
     *
     * @throws IOException if fixture setup or stream cleanup fails
     */
    @Test
    public void testPeekSliceRejectsLengthLargerThanCapacity() throws IOException {
        final byte[] buffer = {0};
        try (PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[] {0}), 1)) {
            stream.peek(buffer);
            assertThrows(IllegalArgumentException.class, () -> stream.peek(buffer, 0, 2));
        }
    }

    /**
     * Tests an array bounds exception after a matching prefix exceeds the slice array.
     *
     * @throws IOException if fixture setup or stream cleanup fails
     */
    @Test
    public void testPeekSliceFailsWhenMatchingPrefixExceedsArrayBounds() throws IOException {
        final byte[] prefix = {10, 10};
        final byte[] buffer = {10};
        try (PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(prefix), 2)) {
            stream.peek(prefix);
            assertThrows(ArrayIndexOutOfBoundsException.class, () -> stream.peek(buffer, 0, 2));
        }
    }
}
```
