# PeekableInputStream exception-only Java-source generation assessment

[Documentation index](../README.md) | [Study log](../study-log.md) |
[Prepared source prompt](../prompts/exception-test-generation-source.txt)

Assessed on October 11, 2026. This report reviews the completed generation
attempt and existing execution evidence. It preserves the entire generated
test file in one Java block. No tests, assertions, production, dependencies,
or build configuration were corrected. No additional Java test, Checkstyle,
coverage, or mutation run was performed for this assessment.

## Outcome

The generated suite contains **17 test methods and 17 executed cases: all passed,
with no failures, errors, or skips**. It stays within the requested exception-only
scope. Expectations are consistent with the inspected production source and the
observed execution. No unsuccessful test or newly confirmed production defect
is reported by this run.

The broader repository run also returned exit code 0. Its 137 Surefire XML
reports contain **1,558 reported cases: 1,552 passed and 6 skipped, with no
failures or errors**. The generated class passed again in that run.

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

Coverage profiles were disabled in both commands. No JaCoCo or PIT measurement
was produced for this generated suite, and none was run for the assessment.

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
new exception-only scope. This output establishes selected exception outcomes;
its adequacy and comparative effectiveness remain bounded by the unmeasured
properties described above.

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
