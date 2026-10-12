# PeekableInputStream source-only generation assessment

[Documentation index](../README.md) | [Study log](../study-log.md) |
[Prepared prompt](../prompts/unit-test-generation.txt)

Initially assessed on October 9, 2026, using existing execution evidence only.
Supplemented on October 11 with the reconstructed JaCoCo comparison below.
The [initial report](../../data/experiments/peekable-input-stream/source-only/coverage/assessment-before-coverage.md)
is preserved. No generated tests, assertions, fixtures, production source,
dependencies, build configuration, or prompts were corrected. Only coverage
measurement and documentation were added; no mutation analysis was performed.

## Outcome

The generation produced a compilable JUnit suite with **26 test methods and 26
executed cases: 21 passed, 4 failed, 1 errored, and none were skipped**. The five
unsuccessful cases contain expectations inconsistent with the contract established
during reference-suite preparation. They do not confirm five production defects.
The suite cannot be adopted unchanged as a passing reference suite.

The later instrumented run reproduced all 26 original outcomes. Target coverage
increased from **0/16 to 16/16 lines** and **0/8 to 8/8 branches**, both reaching
100%. These measurements include execution by failing tests; full structural
coverage does not make their expectations correct or the suite passing.

The successful cases exercise meaningful behavior, including nonconsumption,
array preservation, refill across short reads, circular wraparound, input
validation, and propagated I/O failures. This is evidence that source-only
generation can construct executable fixtures for this target. It does not establish
reliable behavioral expectations or feasibility of generation from WIT-UP JSON.

## Trial identity and available evidence

| Item | Recorded value |
| --- | --- |
| Model and reasoning setting | User-reported **GPT-6.1 Sol Extra High**; the retrieved chat record does not independently expose the configured model or reasoning setting. |
| Generation chat | `Write PeekableInputStream tests`, ID `01a122a3-d1c9-79c2-aa52-12e88102a160`. |
| Condition | Source-only; current production source, repository instructions, documentation, and other existing checkout tests were permitted. |
| Commons IO branch | `test/peekable-input-stream-generation`. |
| Generation and measurement baseline commit | `d7a3c884d07ff5f1829b09087f34dcb8043f0f64`. |
| Production baseline | Original `11f0abe7a` plus the previously committed buffer length correction and tooling configuration. |
| Observed generation turns | One completed turn, with no follow-up repair prompt in the retrieved record. |
| Recorded turn timing | `2026-10-09T21:48:59Z` to `2026-10-09T21:54:21Z`; recorded duration `321827 ms`, approximately 5 minutes 22 seconds. This includes repository inspection, writing, and validation. |
| Generated source | "D:/Projects/wit-up/commons-io/src/test/java/org/apache/commons/io/input/buffer/PeekableInputStreamTest.java". |
| Generated source SHA-256 | `0FED5D696D728439ABE2B68A3D02820BD39556F07CBD84CD02815151D5C14858`. |
| Prepared prompt SHA-256 | `5C42887A243644EF99C0ACF2E25BD839507D6F9BAD7281CAE897A1A4E4FE37E1`. |
| Tokens and cost | Unavailable in the retrieved record; no estimate is substituted. |

The submitted prompt content matches the prepared prompt after trimming trailing
whitespace. The original chat retains the submitted message; the prepared-file
hash above identifies that local file, not an assertion of identical submitted
message bytes. The prompt was not revised after seeing these results.

The generation record contains two writes to the same target file before the
single test run: initial creation and simplification of a fixture. The second
write occurred before validation and was not a repair of failing assertions.
Git inspection at the initial assessment found no tracked production or
configuration changes. At that time, the target test was untracked alongside
the pre-existing local documentation directory. Its full source is preserved
in the appendix and was restored unchanged only in the measurement checkout.

Runtime evidence confirms Maven `3.9.16`, Temurin Java `1.8.0_504`, JUnit Jupiter
`5.5.2`, and Surefire `2.22.2`. The assessment inspected the generated source, the
generation chat and command outputs, the current source and Checkstyle
configuration, and the existing Surefire and Checkstyle XML reports. One command
output in the retrieved chat was truncated; the record is not a complete capture
of every instruction or internal context input.

## Original execution result

The generation agent ran the following command from
"D:/Projects/wit-up/commons-io":

```text
mvn -Dtest=org.apache.commons.io.input.buffer.PeekableInputStreamTest -Djacoco.skip=true clean test
```

Surefire reported 26 tests, 4 failures, 1 error, and 0 skips. Maven returned a
failed build. The observed pass fraction is **21/26, or 80.77%**; this is a run
result, not a correctness rate for the generated assertions.

| Test method | Generated expectation | Observed result | Assessment |
| --- | --- | --- | --- |
| `testPeekMatchesPrefixOfFullBuffer` | A two-byte matching prefix of four buffered bytes returns `true`. | `false`; assertion failure at line 113. | The comparison length differs from the buffered byte count. The established exact-length contract requires `false`. |
| `testPeekSliceMatchesPrefix` | A matching two-byte slice of four buffered bytes returns `true`. | `false`; assertion failure at line 125. | The slice has the same shorter-prefix interpretation problem. |
| `testPeekMatchesPrefixAlreadyBuffered` | After reading one byte, a one-byte prefix of three remaining buffered bytes returns `true`. | `false`; assertion failure at line 138. | Existing buffered content must still be compared at its complete length. |
| `testPeekZeroLengthSlice` | A zero-length slice returns `true` with two buffered bytes. | `false`; assertion failure at line 293. | Zero comparison length does not equal the nonzero buffered byte count. |
| `testPeekEmptyArray` | Passing an empty array returns `true`. | `IllegalArgumentException: Invalid offset: 0`; error at line 285. | The empty array has no valid offset under the existing argument validation. |

The valid zero-length slice on an empty stream is a distinct case:
`testPeekZeroLengthSliceAtEndOfStream` passed. Its nonempty comparison array has a
valid offset, and both the requested comparison length and buffered byte count
are zero. This does not imply that an empty comparison array is accepted or that
zero-length slices match nonempty buffered content.

The generation agent saw the current exact-length guard and explicitly chose a
prefix interpretation in its progress update. The local `PeekableInputStream`
Javadoc can suggest prefix behavior when read alone, but the established contract
review and delegated `CircularByteBuffer.peek` behavior require exact buffered
length. The failures therefore concern interpretation of the expected behavior,
rather than compilation or missing dependencies. That contract history is
recorded in the [reference-suite study log](../study-log.md).

Assertions following the first failure in each unsuccessful method were not
reached. They must not be counted as verified nonconsumption or byte-preservation
checks merely because they appear in the source.

## Behavioral strengths and remaining gaps

The generated suite has 132 assertion call sites by a direct source count. This
is not the number of assertions executed: one test contains a loop, some
assertions are nested, and failing methods terminate early. It is also not a
coverage or mutation metric.

| Behavior | Evidence in the generated suite | Limit |
| --- | --- | --- |
| Constructors and capacity | Null inputs, nonpositive sizes, the 8192-byte default, and oversized requests are exercised. | These passing checks do not validate every slice/capacity combination. |
| Matching, mismatching, and nonconsumption | Repeated peeks, mismatch at each position, nonzero slice offsets, array preservation, and subsequent byte reads pass. | Nonconsumption checks after a failing prefix assertion did not execute. |
| Refill and circular state | Short-read fixtures and multiple refill/wraparound operations pass. | Exact fixture read counts describe these fixtures and implementation paths, not every possible input stream. |
| EOF and remaining content | Empty input, insufficient remaining bytes, exhausted input, and one-byte buffers are exercised. | The empty/truncated negative fixtures do not discriminate all zero-padding false positives in the original length defect. |
| I/O exceptions and cleanup | Exception identity, buffered-byte preservation after refill failure, and closing the underlying source are checked. | This is a bounded set of fixtures, not a complete inherited-stream contract assessment. |

The EOF limitation is material to comparison with the reference suite. The empty
stream test compares against `{10}`, while the original unused buffer bytes are
zero. The truncated-stream test compares `{10, 20, 30}` after only `{10, 20}` were
read; its third comparison byte differs from the unused zero byte. Both fixtures
can return `false` even with the original defective length guard. Missing
zero-matching cases, such as comparison with `{0}` on empty input or a zero-padded
comparison after truncated input, limit regression sensitivity for that defect.
This conclusion is a static trace of the fixtures and original guard. The later
coverage execution retained the corrected production baseline; no source
reversion or original-versus-corrected production experiment was performed.

The exhausted-stream tests do use previously read byte values, so they provide
checks against stale-byte matching. The suite therefore has partial coverage of
the defect's behavioral family, rather than no relevant EOF checks.

The previously validated reference contained 27 methods and 34 executed cases,
with recorded full target coverage and 14/14 killed target mutations. Those are
historical measurements of a different suite. Neither their values nor the
similarity in test counts can be assigned to the generated output. This suite's
own later JaCoCo results are reported below. Its adequacy against mutations
remains unmeasured; no PIT result is assigned from the reference suite.

## Repository conventions and prompt compliance

The generation agent ran `mvn -B -ntp checkstyle:check`, which returned success.
However, its XML lists 155 files and **no test-source files**. In particular,
"PeekableInputStreamTest.java" is absent. That result does not validate the
generated test file's style.

Source inspection found no method Javadocs on the 26 test methods, while the
configured `JavadocMethod` rule requires them in the checked scope. The prior
reference style review had already encountered this requirement. No direct
test-source audit was run for this report, so an exact Checkstyle diagnostic
count for the generated file is not claimed. The passing Maven command does not
close this gap.

The observed generation command record shows repository/source inspection and
consultation of other permitted current-checkout tests. It shows no skill loading,
retrieval of the removed reference test, inspection of WIT-UP exports, or coverage
or mutation analysis. The agent retained the failing assertions and did not edit
production to make them pass. These observations support compliance with the
visible workflow restrictions. They do not independently establish that skill
discovery, memory, injected instructions, or all model context were isolated.

The generation occurred in a separate chat whose first recorded turn contains
the prepared prompt. It was not a continuation of this reference-building
conversation. No claim of a fully bias-free experiment follows from that fact
alone.

## Artifact availability and interpretation boundary

The generation command included `clean`. The old "commons-io/target/coverage",
"commons-io/target/pit-reports", and "commons-io/target/site/jacoco" directories
are now absent. Consequently, the original coverage, mutation, and reference
validation files previously linked from the study log are no longer available
at their recorded paths. Their historical measurements remain documented; no
replacement reports were fabricated or represented as the original runs.

The clean build also removed stale reference classes before compiling the new
suite, so the 26-test result is consistent with the generated source rather than
the previous 34-case reference class. The generation reports were initially
temporary build artifacts. During later preparation for the JSON condition,
byte-identical copies were preserved outside "commons-io/target":

- [Preserved Surefire XML](../../data/experiments/peekable-input-stream/source-only/surefire.xml)
- [Preserved Surefire text report](../../data/experiments/peekable-input-stream/source-only/surefire.txt)
- [Preserved Checkstyle XML](../../data/experiments/peekable-input-stream/source-only/checkstyle.xml)
- [Complete generated test source](#appendix-complete-generated-java-source)

This report was the only project file created during the initial assessment.
No repair iteration or additional validation run occurred at that stage. During subsequent branch
preparation, the generated test source was verified against the appendix, then
removed from the checkout along with its stale compiled classes. The appendix
preserves the complete generated code; the original prompt remains unchanged.
The linked report copies preserve the source-only execution independently of
future build cleanup.

This single trial supports a bounded result: the reported model produced
compilable tests and useful fixtures, but its independent behavioral expectations
were not sufficient to yield a correct passing suite for this target. The later
[JSON-conditioned trial](peekable-input-stream-json-generation.md) is documented
separately. No replicated model comparison, token/cost study, or estimate of
population-level effectiveness is established. The corrected production baseline
also differs from the program identified by the original WIT-UP export label;
that difference remains relevant to any later JSON-conditioned comparison.

## Post-generation JaCoCo comparison

This October 11 measurement reconstructs the before/after states after generation
was complete. It does not recover a generation-time coverage report. The before
state used commit `d7a3c884d07ff5f1829b09087f34dcb8043f0f64` without the target
test. The after state added only the exact Java appendix, verified against its
recorded SHA-256. No assertion, fixture, or test case was edited.

Both runs used the same detached checkout,
"D:/Projects/wit-up/.worktrees/commons-io-coverage", with Temurin `1.8.0_504`,
Maven `3.9.16`, JUnit Jupiter `5.5.2`, Surefire `2.22.2`, and JaCoCo `0.8.14`.
The identical full-suite command was:

```powershell
mvn -B -Pjacoco "-Djacoco.skip=false" clean verify jacoco:report
```

Each clean build started with fresh execution data. The first run's artifacts
were archived before the second clean build. All 398 common files under "src"
and all compiled production outputs were byte-identical between the two states.
No test exclusions or coverage filters were added. The same existing test
identities and outcomes, including six skips, were retained.

| State | Suite XML files | Reported cases | Passed | Failures | Errors | Skipped | Build exit |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Before | 136 | 1,541 | 1,535 | 0 | 0 | 6 | 0 |
| After | 137 | 1,567 | 1,556 | 4 | 1 | 6 | 1 |

The 26 added cases have exactly the same names and outcomes as the original
preserved Surefire XML. The failed after build stopped at Surefire, before
the verify-phase JaCoCo check and final report goal. A separate command read
the already captured execution data without rerunning or changing the tests:

```powershell
mvn -B -Pjacoco "-Djacoco.skip=false" jacoco:report
```

The report-only command returned exit code 0. **The test/build result remains
exit code 1**, with four failures and one error. No failure-ignore option was used.

| Target counter | Before | After | Added covered units | Change |
| --- | ---: | ---: | ---: | ---: |
| Lines | 0/16 (0.00%) | 16/16 (100.00%) | 16 | +100.00 pp |
| Branches | 0/8 (0.00%) | 8/8 (100.00%) | 8 | +100.00 pp |
| Instructions | 0/98 (0.00%) | 98/98 (100.00%) | 98 | +100.00 pp |
| Methods, including constructors | 0/4 (0.00%) | 4/4 (100.00%) | 4 | +100.00 pp |

Percentages divide covered units by their totals; pp denotes percentage points.
There are no missed target lines or branches in this run. Coverage includes
setup and execution before failed assertions. Assertions after a failure remain
unverified. This result demonstrates why coverage must be interpreted alongside
test outcomes and oracle quality. JaCoCo branch coverage also does not enumerate
exception paths; see the
[counter definitions](https://www.jacoco.org/jacoco/trunk/doc/counters.html).

| Delegated class | Lines before | Lines after | Branches before | Branches after |
| --- | ---: | ---: | ---: | ---: |
| CircularBufferInputStream | 34/47 (72.34%) | 44/47 (93.62%) | 15/22 (68.18%) | 18/22 (81.82%) |
| CircularByteBuffer | 25/74 (33.78%) | 43/74 (58.11%) | 12/58 (20.69%) | 29/58 (50.00%) |

Project line coverage changed from 5,430/6,087 (89.21%) to 5,474/6,087 (89.93%),
and branches from 2,511/2,910 (86.29%) to 2,536/2,910 (87.15%). Those are observed
deltas of +44 lines (+0.72 pp) and +25 branches (+0.86 pp). Coverage in
`FileEntry`, outside the generated fixtures, lost three covered branches and one
covered instruction between runs. The global delta is therefore contextual and
is not wholly attributed to the added target tests. The
[comparison JSON](../../data/experiments/peekable-input-stream/source-only/coverage/comparison.json)
retains all target, delegated-class, project, and class-level difference counters.

The before build emitted five inherited project-wide coverage-rule warnings.
Commons Parent 50 already sets `commons.jacoco.haltOnFailure=false`; neither
this setting nor any threshold was changed. The after coverage check was not
executed because tests failed; zero check warnings in that log is not a passing
check. Complete logs retain compiler diagnostics, skips, and the detached
checkout's branch-information warning.

To reproduce, use the same production baseline and toolchain, measure without
the target test, archive that run, then restore the exact appendix and repeat.
Preserve failures and use the separate report-only command when needed. Compare
source/class hashes and test identities before interpreting the coverage delta.
This single pair does not establish repeated-run stability or mutation adequacy.

- [Before HTML](../../data/experiments/peekable-input-stream/source-only/coverage/before/jacoco/index.html), [XML](../../data/experiments/peekable-input-stream/source-only/coverage/before/jacoco/jacoco.xml), and [CSV](../../data/experiments/peekable-input-stream/source-only/coverage/before/jacoco/jacoco.csv).
- [After HTML](../../data/experiments/peekable-input-stream/source-only/coverage/after/jacoco/index.html), [XML](../../data/experiments/peekable-input-stream/source-only/coverage/after/jacoco/jacoco.xml), and [CSV](../../data/experiments/peekable-input-stream/source-only/coverage/after/jacoco/jacoco.csv).
- Full logs: [before](../../data/experiments/peekable-input-stream/source-only/coverage/before/maven.log), [failed after build](../../data/experiments/peekable-input-stream/source-only/coverage/after/maven.log), and [report-only command](../../data/experiments/peekable-input-stream/source-only/coverage/after/report-only.log).
- Metadata and timestamps: [before](../../data/experiments/peekable-input-stream/source-only/coverage/before/run.json) and [after](../../data/experiments/peekable-input-stream/source-only/coverage/after/run.json).
- Test identities and outcomes: [before](../../data/experiments/peekable-input-stream/source-only/coverage/before/suite-summary.json) and [after](../../data/experiments/peekable-input-stream/source-only/coverage/after/suite-summary.json).
- [Restored source](../../data/experiments/peekable-input-stream/source-only/coverage/PeekableInputStreamTest.java) and [artifact inventory](../../data/experiments/peekable-input-stream/source-only/coverage/artifact-manifest.json).

Each run also retains "jacoco.exec", every Surefire report, environment output,
source and compiled-output hash manifests, and compiled production ZIPs outside
the checkout. The raw Maven logs retain their original Windows encoding. The
initial report, prompts, original execution reports, and Java appendix remain
preserved; no corrected test alternative is included.

## Appendix: complete generated Java source

The following Java block reproduces the complete assessed file, including its
license header, imports, fixtures, 26 test methods, and original assertions.
It preserves the generated output, including the five unsuccessful cases discussed
above. The source line numbers in the result table refer to the original Java
file, whose SHA-256 is recorded in the trial identity table.

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

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertSame;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

import org.junit.jupiter.api.Test;

/**
 * Tests for {@link PeekableInputStream}.
 */
public class PeekableInputStreamTest {

    private static class ShortReadInputStream extends ByteArrayInputStream {
        private int readCount;
        private boolean closed;

        ShortReadInputStream(final byte[] bytes) {
            super(bytes);
        }

        @Override
        public int read(final byte[] bytes, final int offset, final int length) {
            readCount++;
            return super.read(bytes, offset, Math.min(length, 1));
        }

        @Override
        public void close() throws IOException {
            closed = true;
            super.close();
        }
    }

    @Test
    public void testDefaultBufferSize() throws IOException {
        final byte[] input = new byte[8193];
        Arrays.fill(input, (byte) 42);
        final byte[] expected = Arrays.copyOf(input, 8192);
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input))) {
            assertTrue(stream.peek(expected));
            assertTrue(stream.peek(expected, 0, expected.length));
            assertThrows(IllegalArgumentException.class, () -> stream.peek(input));
            assertThrows(IllegalArgumentException.class, () -> stream.peek(input, 0, input.length));
            final byte[] actual = new byte[expected.length];
            assertEquals(actual.length, stream.read(actual));
            assertArrayEquals(expected, actual);
            assertEquals(42, stream.read());
            assertEquals(-1, stream.read());
        }
    }

    @Test
    public void testConstructorRejectsNullInput() {
        assertThrows(NullPointerException.class, () -> new PeekableInputStream(null));
        assertThrows(NullPointerException.class, () -> new PeekableInputStream(null, 4));
    }

    @Test
    public void testConstructorRejectsNonPositiveBufferSize() {
        assertThrows(IllegalArgumentException.class,
                () -> new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 0));
        assertThrows(IllegalArgumentException.class,
                () -> new PeekableInputStream(new ByteArrayInputStream(new byte[0]), -1));
    }

    @Test
    public void testPeekRepeatedlyWithoutConsumingOrChangingBytes() throws IOException {
        final byte[] input = { 0, 127, (byte) 128, (byte) 255, 42 };
        final byte[] expected = Arrays.copyOf(input, 4);
        final byte[] original = expected.clone();
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 4)) {
            assertTrue(stream.peek(expected));
            assertTrue(stream.peek(expected));
            assertTrue(stream.peek(expected, 0, expected.length));
            assertArrayEquals(original, expected);
            final byte[] actual = new byte[4];
            assertEquals(4, stream.read(actual));
            assertArrayEquals(original, actual);
            assertEquals(42, stream.read());
            assertEquals(-1, stream.read());
        }
    }

    @Test
    public void testPeekMatchesPrefixOfFullBuffer() throws IOException {
        final byte[] input = { 10, 20, 30, 40 };
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 4)) {
            assertTrue(stream.peek(new byte[] { 10, 20 }));
            final byte[] actual = new byte[4];
            assertEquals(4, stream.read(actual));
            assertArrayEquals(input, actual);
        }
    }

    @Test
    public void testPeekSliceMatchesPrefix() throws IOException {
        final byte[] input = { 10, 20, 30, 40 };
        final byte[] expected = { 99, 10, 20, 98 };
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 4)) {
            assertTrue(stream.peek(expected, 1, 2));
            final byte[] actual = new byte[4];
            assertEquals(4, stream.read(actual));
            assertArrayEquals(input, actual);
        }
    }

    @Test
    public void testPeekMatchesPrefixAlreadyBuffered() throws IOException {
        final byte[] input = { 10, 20, 30, 40 };
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 4)) {
            assertTrue(stream.peek(input));
            assertEquals(10, stream.read());
            assertTrue(stream.peek(new byte[] { 20 }));
            assertEquals(20, stream.read());
        }
    }

    @Test
    public void testPeekMismatchAtEachPositionDoesNotConsumeBytes() throws IOException {
        final byte[] input = { 0, 127, (byte) 128, (byte) 255 };
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 4)) {
            for (int i = 0; i < input.length; i++) {
                final byte[] mismatch = input.clone();
                mismatch[i] ^= 1;
                assertFalse(stream.peek(mismatch), "Mismatch at index " + i);
                assertFalse(stream.peek(mismatch, 0, mismatch.length), "Slice mismatch at index " + i);
            }
            assertTrue(stream.peek(input));
            final byte[] actual = new byte[4];
            assertEquals(4, stream.read(actual));
            assertArrayEquals(input, actual);
        }
    }

    @Test
    public void testPeekSliceUsesOffsetAndLengthWithoutChangingArray() throws IOException {
        final byte[] input = { 10, 20, 30 };
        final byte[] expected = { 99, 10, 20, 30, 98 };
        final byte[] original = expected.clone();
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 5)) {
            assertTrue(stream.peek(expected, 1, 3));
            assertTrue(stream.peek(expected, 1, 3));
            assertFalse(stream.peek(new byte[] { 99, 10, 20, 31, 98 }, 1, 3));
            assertArrayEquals(original, expected);
            final byte[] actual = new byte[3];
            assertEquals(3, stream.read(actual));
            assertArrayEquals(input, actual);
            assertEquals(-1, stream.read());
        }
    }

    @Test
    public void testPeekFillsBufferAcrossShortReads() throws IOException {
        final byte[] input = { 10, 20, 30, 40, 50 };
        final ShortReadInputStream source = new ShortReadInputStream(input);
        try (final PeekableInputStream stream = new PeekableInputStream(source, 4)) {
            assertEquals(0, source.readCount);
            assertTrue(stream.peek(new byte[] { 10, 20, 30, 40 }));
            assertEquals(4, source.readCount);
            assertTrue(stream.peek(new byte[] { 10, 20, 30, 40 }, 0, 4));
            assertEquals(4, source.readCount);
            final byte[] actual = new byte[4];
            assertEquals(4, stream.read(actual));
            assertArrayEquals(new byte[] { 10, 20, 30, 40 }, actual);
            assertTrue(stream.peek(new byte[] { 50 }));
            assertEquals(50, stream.read());
            assertEquals(-1, stream.read());
        }
    }

    @Test
    public void testPeekSliceFillsBufferAcrossShortReads() throws IOException {
        final byte[] input = { 10, 20, 30 };
        final ShortReadInputStream source = new ShortReadInputStream(input);
        try (final PeekableInputStream stream = new PeekableInputStream(source, 5)) {
            assertTrue(stream.peek(new byte[] { 99, 10, 20, 30, 98 }, 1, 3));
            assertEquals(4, source.readCount);
            final byte[] actual = new byte[3];
            assertEquals(3, stream.read(actual));
            assertArrayEquals(input, actual);
        }
    }

    @Test
    public void testPeekRefillsAndWrapsWithoutLosingBufferedBytes() throws IOException {
        final byte[] input = { 10, 20, 30, 40, 50, 60, 70, 80, 90 };
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 4)) {
            assertEquals(10, stream.read());
            assertEquals(20, stream.read());
            assertTrue(stream.peek(new byte[] { 30, 40, 50, 60 }));
            assertFalse(stream.peek(new byte[] { 30, 40, 51, 60 }, 0, 4));
            assertTrue(stream.peek(new byte[] { 30, 40, 50, 60 }, 0, 4));
            final byte[] actual = new byte[3];
            assertEquals(3, stream.read(actual));
            assertArrayEquals(new byte[] { 30, 40, 50 }, actual);
            assertTrue(stream.peek(new byte[] { 60, 70, 80, 90 }, 0, 4));
            final byte[] remaining = new byte[4];
            assertEquals(4, stream.read(remaining));
            assertArrayEquals(new byte[] { 60, 70, 80, 90 }, remaining);
            assertEquals(-1, stream.read());
        }
    }

    @Test
    public void testPeekWithOneByteBuffer() throws IOException {
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[] { 10, 20 }), 1)) {
            assertTrue(stream.peek(new byte[] { 10 }));
            assertFalse(stream.peek(new byte[] { 20 }, 0, 1));
            assertEquals(10, stream.read());
            assertTrue(stream.peek(new byte[] { 20 }, 0, 1));
            assertEquals(20, stream.read());
            assertFalse(stream.peek(new byte[] { 20 }));
            assertEquals(-1, stream.read());
        }
    }

    @Test
    public void testPeekInsufficientBytesAtEndPreservesRemainingBytes() throws IOException {
        final byte[] input = { 10, 20 };
        final ShortReadInputStream source = new ShortReadInputStream(input);
        try (final PeekableInputStream stream = new PeekableInputStream(source, 4)) {
            assertFalse(stream.peek(new byte[] { 10, 20, 30 }));
            assertFalse(stream.peek(new byte[] { 99, 10, 20, 30 }, 1, 3));
            assertTrue(stream.peek(input));
            assertTrue(stream.peek(new byte[] { 99, 10, 20 }, 1, 2));
            final byte[] actual = new byte[2];
            assertEquals(2, stream.read(actual));
            assertArrayEquals(input, actual);
            assertEquals(-1, stream.read());
            assertFalse(stream.peek(new byte[] { 10 }));
            assertEquals(3, source.readCount);
        }
    }

    @Test
    public void testPeekAtEndOfStream() throws IOException {
        final ShortReadInputStream source = new ShortReadInputStream(new byte[] { 10 });
        try (final PeekableInputStream stream = new PeekableInputStream(source, 1)) {
            assertTrue(stream.peek(new byte[] { 10 }));
            assertEquals(10, stream.read());
            assertFalse(stream.peek(new byte[] { 10 }));
            assertFalse(stream.peek(new byte[] { 10 }, 0, 1));
            assertEquals(-1, stream.read());
            assertEquals(2, source.readCount);
        }
    }

    @Test
    public void testPeekEmptyStream() throws IOException {
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 2)) {
            assertFalse(stream.peek(new byte[] { 10 }));
            assertFalse(stream.peek(new byte[] { 99, 10 }, 1, 1));
            assertEquals(-1, stream.read());
        }
    }

    @Test
    public void testPeekEmptyArray() throws IOException {
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[] { 10 }), 1)) {
            assertTrue(stream.peek(new byte[0]));
            assertEquals(10, stream.read());
        }
    }

    @Test
    public void testPeekZeroLengthSlice() throws IOException {
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[] { 10, 20 }), 2)) {
            assertTrue(stream.peek(new byte[] { 99 }, 0, 0));
            assertEquals(10, stream.read());
            assertEquals(20, stream.read());
        }
    }

    @Test
    public void testPeekZeroLengthSliceAtEndOfStream() throws IOException {
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertTrue(stream.peek(new byte[] { 99 }, 0, 0));
            assertEquals(-1, stream.read());
        }
    }

    @Test
    public void testPeekRejectsNullArrayWithoutReading() throws IOException {
        final ShortReadInputStream source = new ShortReadInputStream(new byte[] { 10 });
        try (final PeekableInputStream stream = new PeekableInputStream(source, 1)) {
            assertThrows(NullPointerException.class, () -> stream.peek(null));
            assertThrows(NullPointerException.class, () -> stream.peek(null, 0, 1));
            assertEquals(0, source.readCount);
            assertEquals(10, stream.read());
        }
    }

    @Test
    public void testPeekRejectsRequestsLargerThanBufferWithoutReading() throws IOException {
        final ShortReadInputStream source = new ShortReadInputStream(new byte[] { 10, 20 });
        try (final PeekableInputStream stream = new PeekableInputStream(source, 2)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(new byte[3]));
            assertThrows(IllegalArgumentException.class, () -> stream.peek(new byte[3], 0, 3));
            assertEquals(0, source.readCount);
            assertTrue(stream.peek(new byte[] { 10, 20 }));
        }
    }

    @Test
    public void testPeekSliceRejectsInvalidOffset() throws IOException {
        final byte[] input = { 10, 20 };
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 2)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(input, -1, 1));
            assertThrows(IllegalArgumentException.class, () -> stream.peek(input, input.length, 1));
            assertThrows(IllegalArgumentException.class, () -> stream.peek(input, input.length + 1, 1));
            assertTrue(stream.peek(input));
        }
    }

    @Test
    public void testPeekSliceRejectsInvalidLength() throws IOException {
        final byte[] input = { 10, 20 };
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 2)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(input, 0, -1));
            assertThrows(IllegalArgumentException.class, () -> stream.peek(input, 0, 3));
            assertTrue(stream.peek(input));
        }
    }

    @Test
    public void testPeekPropagatesReadFailure() throws IOException {
        final IOException failure = new IOException("Unable to read input");
        final InputStream source = new InputStream() {
            @Override
            public int read() throws IOException {
                throw failure;
            }
        };
        try (final PeekableInputStream stream = new PeekableInputStream(source, 2)) {
            assertSame(failure, assertThrows(IOException.class, () -> stream.peek(new byte[] { 10 })));
            assertSame(failure, assertThrows(IOException.class, () -> stream.peek(new byte[] { 99, 10 }, 1, 1)));
        }
    }

    @Test
    public void testPeekPropagatesRefillFailureAndPreservesBufferedByte() throws IOException {
        final IOException failure = new IOException("Unable to refill input");
        final InputStream source = new ByteArrayInputStream(new byte[] { 10, 20 });
        final InputStream failingSource = new InputStream() {
            @Override
            public int read() throws IOException {
                final int result = source.read();
                if (result == -1) {
                    throw failure;
                }
                return result;
            }

            @Override
            public void close() throws IOException {
                source.close();
            }
        };
        try (final PeekableInputStream stream = new PeekableInputStream(failingSource, 2)) {
            assertTrue(stream.peek(new byte[] { 10, 20 }));
            assertEquals(10, stream.read());
            assertSame(failure, assertThrows(IOException.class, () -> stream.peek(new byte[] { 20, 30 })));
            assertSame(failure, assertThrows(IOException.class, () -> stream.peek(new byte[] { 20, 30 }, 0, 2)));
            assertEquals(20, stream.read());
        }
    }

    @Test
    public void testCloseDiscardsPeekedBytesAndClosesSource() throws IOException {
        final ShortReadInputStream source = new ShortReadInputStream(new byte[] { 10, 20, 30 });
        try (final PeekableInputStream stream = new PeekableInputStream(source, 2)) {
            assertTrue(stream.peek(new byte[] { 10, 20 }));
            assertFalse(source.closed);
            stream.close();
            assertTrue(source.closed);
            assertFalse(stream.peek(new byte[] { 10 }));
            assertFalse(stream.peek(new byte[] { 10 }, 0, 1));
            assertEquals(-1, stream.read());
            assertEquals(2, source.readCount);
        }
    }
}
```
