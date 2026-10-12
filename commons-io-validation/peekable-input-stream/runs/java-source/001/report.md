# Independent Java-source exception-test generation

The prescribed initial Maven invocation completed successfully: 20 executed tests, 0 failures, 0 errors, and 0 skips. The additional repository license and configured production Checkstyle gates passed. A separate direct application of the unchanged Checkstyle rules to the frozen generated test failed with two style errors. The source remains unchanged after freezing and execution; no repair, additional case, renamed test, changed fixture, or second test execution was performed.

## Identity and preflight

- Checkout: `D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001`.
- Exact HEAD before generation and after all checks: `11f0abe7a3fb6954b2985ca4ab0697b2fb489e84`.
- The original metadata-only checks were `git rev-parse HEAD`, `git status --short`, `git diff --quiet 11f0abe7a3fb6954b2985ca4ab0697b2fb489e84 --`, and `Test-Path -LiteralPath src/test/java/org/apache/commons/io/input/buffer/PeekableInputStreamTest.java`. All Git commands exited 0; status was empty, baseline diff was empty, and the test did not exist. No source diff was printed. There was no `.codegraph` directory.
- Final tracked baseline comparison exited 0, final `git diff --check` exited 0, and the only nonignored checkout addition is the generated target test. Ignored native build outputs remain in `target/`.
- Generated target: `src/test/java/org/apache/commons/io/input/buffer/PeekableInputStreamTest.java`.
- Frozen SHA-256: `365a763fbc4b383087d993e659e05bf04952a4d4333a2ff16ac4417fe9eb43dd`; the live file has the same hash after all checks.
- Fresh-chat attestation was true: no earlier generated suite, candidate inventory, alternative prompt/source, execution feedback, reference test, study finding, or measurement was supplied or inspected. This is one independent generation, with procedural isolation rather than filesystem access control.
- The supplied global working agreements and their evidence-routing, implementation-integrity, and Git policies were read as mandatory working instructions. Their observed bytes are retained in `evidence/process/global-guidance/`; they supplied no target-specific oracle. The live study AGENTS file was read during attachment bootstrap and matched the supplied process instructions. Subsequent methodology use was from the assigned snapshot. No custom, installed, repository, or plugin skill was used.

## Toolchain and environment

Observed before generation and again in each invocation's process: Temurin OpenJDK `1.8.0_504`, runtime build `1.8.0_504-b01`, VM build `25.504-b01`; javac `1.8.0_504`; Apache Maven `3.9.16` (`2bdd9fddda4b155ebf8000e807eb73fd829a51d5`); Python `3.13.15`; PowerShell `7.6.5`; Windows OS build `10.0.26300`, X64. Each version-observation command exited 0. The baseline POM specifies Java source/target 1.8, JUnit Jupiter 5.5.2, and Surefire 2.22.2; the actual log shows Surefire 2.22.2.

Java and Maven executables are installed application files on C:. Only process environment was changed: JDK 8 was prepended to PATH, `MAVEN_OPTS=-DargLine=`, and TEMP/TMP were set under the assigned D: working directory. `MAVEN_ARGS=-Dmaven.repo.local=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001/maven-repository` places the dependency cache on D: without changing the checkout, dependencies, coverage selections, or quality gates. The complete executable locations, version stdout/stderr, OS, and process environment are retained in the generation environment observation and each manager-captured execution environment. The exact active model identifier, settings, and app build are unavailable and explicitly recorded as null with a reason; they were not invented.

The prepared source-repository backup `D:/Projects/experiment-backups/source-repositories/commons-io-11f0abe7a.bundle` still has SHA-256 `56c77e2d311dcabc39a69ba2873ef151d1ab2b78dad8792a152b4158eb117aee`, matching the preparation metadata. Its contents were not inspected as scenario input.

## Commands and observed outcomes

Each substantive check was verified live, reserved using `begin` with an absent/empty native Surefire destination, captured with both output streams at the returned exclusive log path, and finished using `record`. Exactly one invocation has phase `generated-tests`.

| Invocation | Exact command / scope | Process exit | Executed tests, failures, errors, skips |
| --- | --- | --- | --- |
| 001, generated-tests | `mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" "-Dtest=org.apache.commons.io.input.buffer.PeekableInputStreamTest" clean test` | 0 | 20, 0, 0, 0; native XML and log establish actual execution and BUILD SUCCESS |
| 002, infrastructure | `mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" apache-rat:check checkstyle:check` | 0 | 0, 0, 0, 0; tests were not started because only two quality-gate goals ran |
| 003, infrastructure | Exact rendered Java Checkstyle CLI command is included below and in `evidence/process/generated-test-style-command.txt`; same Checkstyle 8.19 and unchanged `checkstyle.xml`, only the frozen test file | 2 | 0, 0, 0, 0; style diagnostics are not executed-test failures |

All three `record` operations exited 0, with no protocol problems. The freeze operation exited 0. Live verification before each substantive invocation exited 0. The native initial XML was archived losslessly in `executions/001/surefire-reports.zip`. Full stdout/stderr remain in each execution's `output.log`; native license and style outputs are also retained in `evidence/quality-gates/`. Observation/reservation scripts and their output are retained in `evidence/process/`.

Invocation 001 took 31.098 seconds according to Maven. Its branch-detection warning is preserved: `Cannot get the branch information from the git repository` / `fatal: ref HEAD is not a symbolic ref`; the prepared detached HEAD is unchanged, and the warning did not stop compilation or execution. No suppression was applied. The driver status JSON's auxiliary `sequence` field is null because it read a nonexistent property; the original bytes are preserved. The manager reservation, request, result, and log authoritatively identify execution 001, and command/exit-status capture is unaffected.

Invocation 002's Rat summary reports 357 approved licenses, 0 unapproved, and 0 unknown. Its configured Checkstyle report lists 155 production files with no error entries and excludes the generated test, which is why the direct additional style check was performed. Invocation 003 reports exactly:

- Line 1: `Missing package-info.java file.` from `JavadocPackageCheck`.
- Line 252, column 9: `Missing a Javadoc comment.` from `JavadocMethodCheck`, for the private dependency-fixture constructor.

Neither error was repaired after freezing. The direct style check uses already resolved dependencies in the assigned Maven cache; it does not compile or execute the test. Native report files preserve the exact check output.

Coverage, mutation, JaCoCo/PIT baselines, full-suite execution, a second target-suite execution, external behavioral lookup, later commits, inherited-operation tests, and correctness comparison against an independent specification were not performed. The preservation-manager implementation was unchanged, so its unrelated Python test/static-analysis suite was not rerun. No `list` or collection analysis was used, which would expose other attempt metadata unnecessarily. No external upload or push was performed.

The requested closure outcome is `generation-complete`: one complete frozen generation with a known initial execution outcome and preserved supplemental quality-check failure. This outcome does not mean that every quality check passed, that measurements were completed, or that path coverage or independent specification correctness was established. The seal and final verification/backup outcomes are reported by the closure operations after this report is written.


# Source-derived exception analysis

The designated source is production Java at commit `11f0abe7a3fb6954b2985ca4ab0697b2fb489e84`. All paths below are relative to `D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001/src/main/java/org/apache/commons/io/input/buffer/`:

- **T**: `PeekableInputStream.java`.
- **S**: `CircularBufferInputStream.java`.
- **B**: `CircularByteBuffer.java`.

Only T, its superclass S, and its directly used buffer B supplied behavioral scenarios and exception oracles. `pom.xml`, `checkstyle.xml`, and the first 70 lines of the unrelated `ByteOrderMarkTestCase.java` supplied only Java/JUnit configuration, license, imports, and formatting conventions. No target, superclass, or buffer tests were read. No alternative source, previous attempt, reference suite, history, coverage, mutation, solver result, or external behavioral documentation was consulted. No skill was loaded or invoked. Isolation is procedural; this chat has no prohibited behavioral exposure.

## Generated test mapping

Every invocation asserts an exception from exactly one target constructor or declared peek call. All fixture construction happens outside the asserted executable. Streams are deterministic memory fixtures; no external handles need cleanup. The tests assert messages only where the source gives the exact literal or concatenation, and exception identity only where the call chain contains no catch or wrapping operation.

| Test and parameter invocation | Target signature | Exception oracle | Fixture assumptions and supporting source locator |
| --- | --- | --- | --- |
| `defaultConstructorRejectsNullInput` | `PeekableInputStream(InputStream)` | `NullPointerException`, message `InputStream` | Null input delegates through the unchanged default size 8192. T constructor lines 48-49; S constructors lines 60-61 and 43-46. |
| `sizedConstructorRejectsNullInputBeforeInvalidBufferSize` | `PeekableInputStream(InputStream,int)` | `NullPointerException`, message `InputStream` | Input null, size 0. Null validation precedes the nonpositive-size guard. T lines 38-39; S lines 43-46. |
| `sizedConstructorRejectsNonpositiveBufferSize(0)` | `PeekableInputStream(InputStream,int)` | `IllegalArgumentException`, message `Invalid buffer size: 0` | Non-null empty memory input passes null validation; zero satisfies `pBufferSize <= 0`. T lines 38-39; S lines 43-46. |
| `sizedConstructorRejectsNonpositiveBufferSize(-1)` | `PeekableInputStream(InputStream,int)` | `IllegalArgumentException`, message `Invalid buffer size: -1` | Non-null empty memory input; negative size satisfies the same guard on its negative side. T lines 38-39; S lines 43-46. |
| `peekArrayRejectsNullBuffer` | `peek(byte[])` | `NullPointerException`, message `Buffer` | Valid size-1 stream, null array. T lines 61-62. |
| `peekSliceRejectsNullBufferBeforeInvalidSlice` | `peek(byte[],int,int)` | `NullPointerException`, message `Buffer` | Valid size-1 stream; null array, offset -1 and length -1. Top-level null validation runs first. T lines 83-84. |
| `peekArrayRejectsArrayLargerThanInternalBuffer` | `peek(byte[])` | `IllegalArgumentException` | Capacity 1, non-null array length 2; whole-array guard precedes refill. T lines 61-68. |
| `peekSliceRejectsOversizedArrayEvenForZeroLength` | `peek(byte[],int,int)` | `IllegalArgumentException` | Capacity 1, array length 2, offset 0, requested length 0. The guard uses the entire array length, not the slice length. T lines 83-90. |
| `peekArrayRejectsEmptyArrayAtDelegatedOffsetGuard` | `peek(byte[])` | `IllegalArgumentException`, message `Invalid offset: 0` | Capacity 1, empty array. Initial count 0 is not less than array length 0, so refill is bypassed. Delegated offset 0 is at the empty array boundary. T lines 67-70; B `peek(byte[],int,int)` lines 146-149; B constructor lines 37-41. |
| `peekSliceRejectsEmptyArrayAtDelegatedOffsetGuard` | `peek(byte[],int,int)` | `IllegalArgumentException`, message `Invalid offset: 0` | Capacity 1, empty array, offset 0, length 0. No refill; delegated upper-offset guard throws. T lines 89-92; B lines 146-149 and 37-41. |
| `peekSliceRejectsInvalidOffsetBeforeInvalidLength(-1)` | `peek(byte[],int,int)` | `IllegalArgumentException`, message `Invalid offset: -1` | Capacity 1, input and comparison each one zero byte, offset -1, length -1. Refill first succeeds; negative-offset guard precedes length validation. T lines 89-92; S `fillBuffer()` lines 69-84; B lines 148-152. |
| `peekSliceRejectsInvalidOffsetBeforeInvalidLength(1)` | `peek(byte[],int,int)` | `IllegalArgumentException`, message `Invalid offset: 1` | Same size-1 fixture, offset equal to comparison length 1, length -1. The nonnegative upper-offset guard runs before length validation. Same locators as preceding invocation. |
| `peekSliceRejectsNegativeLength` | `peek(byte[],int,int)` | `IllegalArgumentException`, message `Invalid length: -1` | Capacity 1, one zero input byte, one zero comparison byte; offset 0 valid, length -1. Refill succeeds before delegated negative-length guard. T lines 89-92; S lines 69-84; B lines 148-152. |
| `peekSliceRejectsLengthLargerThanInternalBuffer` | `peek(byte[],int,int)` | `IllegalArgumentException`, message `Invalid length: 2` | Capacity 1, one zero input/comparison byte, offset 0, requested length 2. Entire comparison array fits; delegated length exceeds internal capacity. T lines 85-92; S lines 69-84; B lines 148-152. |
| `peekArrayPropagatesReadFailureDuringRefill(0)` | `peek(byte[])` | The fixture's `IOException` instance | Capacity and request length 2, initial internal count 0. First positive-length bulk read throws. T lines 67-68; S lines 65-76 and 84-85. |
| `peekArrayPropagatesReadFailureDuringRefill(1)` | `peek(byte[])` | The fixture's `IOException` instance | Same size-2 fixture; the first bulk read returns one zero byte, which is added, and the next read throws. T lines 67-68; S lines 73-83; B `add(byte[],int,int)` lines 182-199. |
| `peekSlicePropagatesReadFailureBeforeInvalidSlice(0)` | `peek(byte[],int,int)` | The fixture's `IOException` instance | Capacity/request-array length 2; offset -1 and length -1. Array-length-based refill reaches an immediate read failure before delegated argument guards. T lines 89-92; S lines 69-76. |
| `peekSlicePropagatesReadFailureBeforeInvalidSlice(1)` | `peek(byte[],int,int)` | The fixture's `IOException` instance | Same invalid slice; one zero byte is buffered before the second read throws. T lines 89-92; S lines 73-83; B `add(byte[],int,int)` lines 182-199. |
| `peekSlicePropagatesArrayBoundsFailureAfterMatchingPrefix(0)` | `peek(byte[],int,int)` | `ArrayIndexOutOfBoundsException` | Capacity 2, empty input, comparison array `[0,0]`, offset 1, length 2. Refill observes EOF, leaving internal count 0 and zero-initialized storage. Offset/length guards pass; `2 < 0` is false. The first comparison matches zero, then array index 2 throws. T lines 85-92; S lines 73-79; B constructor lines 37-41 and peek lines 148-163. |
| `peekSlicePropagatesArrayBoundsFailureAfterMatchingPrefix(2)` | `peek(byte[],int,int)` | `ArrayIndexOutOfBoundsException` | Capacity 2, input `[0,0]`, comparison `[0,0]`, offset 1, length 2. Refill fills both slots, count 2; `2 < 2` is false. First comparison matches; the next comparison reads comparison index 2. T lines 85-92; S lines 73-83; B add lines 182-199 and peek lines 148-163. |

## Concrete fixture values and limitations

The Java source contains symbolic constructor and method parameters, not a fixed scenario table. Arguments 0, -1, 1, and 2 instantiate the visible equality/inequality boundaries. Explicit capacities 1 and 2 keep allocations and refills small; they use the public sized constructor rather than altering the source's default 8192. The default-constructor test retains 8192. No source bytes or fixed source conditions were changed. The resulting guards retain their original polarity and order.

Zero input and comparison values are deliberately selected, not copied from an example: they establish the matching prefix needed to reach the implicit array access failure. Empty input in one invocation leaves Java's initial zero-filled buffer storage intact; the other fills it with two zeros. Neither test claims general array-overrun reachability for mismatching bytes or for `pLength < currentNumberOfBytes`, where B returns false earlier.

`PrefixThenFailInputStream` models a checked failure from S's `in.read(buf, 0, space)` call. It supplies zero or one successful byte, then throws a single precreated `IOException`. Each actual bulk request has offset 0, positive length, and a sufficiently large array; each successful return count 1 is within that request. The fixture is intentionally confined to those supported target calls. Its failure text is synthetic and is not asserted as a Commons IO message. Exception identity follows the source's direct propagation, without catches in T or S.

B's `pLength < currentNumberOfBytes` condition and absent combined offset-plus-length check are recorded as source observations. No independent specification was consulted to classify them as correctness defects, and production was not changed. A passing exception assertion establishes the observed fixture outcome, not complete internal path coverage or correctness against an independent specification.

## Candidates not represented

- **Justified redundancy:** Other negative sizes, negative offsets, offsets above rather than equal to the array length, negative lengths, and larger oversize arrays repeat the same predicates and outcomes. Null input with a valid explicit size repeats S's first guard; the chosen zero-size null case additionally tests validation order. Null arrays with different slice arguments repeat T's first guard. Additional valid-slice read failures use the same refill propagation sites already represented; sliced failures with invalid arguments additionally discriminate validation order.
- **Shadowed or unreachable through the permitted target:** B's second null-array validation is preceded by T's null guard. B's negative allocation size is blocked by S's nonpositive-size guard. Default-constructor size rejection is unavailable because it delegates with 8192. Whole-array delegated negative/oversize-length rejection is unavailable because length comes from an array already checked against capacity. An inherited read or close exception is not a target-constructor/peek outcome and is outside scope.
- **Missing exception oracle:** B returns false when `pLength < currentNumberOfBytes` or when a compared byte differs. A mere shortage of input does not throw a supported IllegalStateException from B.peek. Normal returns, EOF, matching bytes, and nonthrowing early returns are excluded as requested.
- **Insufficient fixture support:** Resource-exhaustion failures from array allocation have no small deterministic fixture or environment-independent supported oracle. Buffer-add argument/space failures would require a dependency read count outside the valid requested range, private-state changes, or another unsupported condition; the supplied well-behaved fixtures do not establish them. Arbitrary unchecked dependency exceptions have no specific source-backed type/message oracle and are not invented.
- **No inconsistent data or solver verdict:** This condition uses production Java only. There are no JSON associations, solver verdicts, or source-record counts to interpret as path coverage.

## Preexecution review

The completed suite has one exception assertion per invocation and distinct overload mappings. Imports use simple type names and explicit non-wildcard imports. The Apache license header is present; test names describe behavior, and comments use Arrange / Act and Assert sections. No run identifier occurs in Java names. All lines are within the configured 160-character limit. Review was by source inspection, without compilation or execution before freezing.


## Exact additional Checkstyle command

~~~powershell

java -cp "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001/maven-repository/com/puppycrawl/tools/checkstyle/8.19/checkstyle-8.19.jar;D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001/maven-repository/info/picocli/picocli/3.9.5/picocli-3.9.5.jar;D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001/maven-repository/antlr/antlr/2.7.7/antlr-2.7.7.jar;D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001/maven-repository/org/antlr/antlr4-runtime/4.7.2/antlr4-runtime-4.7.2.jar;D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001/maven-repository/commons-beanutils/commons-beanutils/1.9.3/commons-beanutils-1.9.3.jar;D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001/maven-repository/commons-logging/commons-logging/1.1.1/commons-logging-1.1.1.jar;D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001/maven-repository/commons-collections/commons-collections/3.2.2/commons-collections-3.2.2.jar;D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001/maven-repository/com/google/guava/guava/27.1-jre/guava-27.1-jre.jar;D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001/maven-repository/com/google/guava/failureaccess/1.0.1/failureaccess-1.0.1.jar" com.puppycrawl.tools.checkstyle.Main -c checkstyle.xml -f xml -o "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001/checkstyle-generated-test.xml" src/test/java/org/apache/commons/io/input/buffer/PeekableInputStreamTest.java


~~~

## Complete frozen Java source

~~~java

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
import static org.junit.jupiter.api.Assertions.assertSame;
import static org.junit.jupiter.api.Assertions.assertThrows;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

/**
 * Exception tests for the declared constructors and peek overloads.
 * Fixtures use only memory streams and require no external resources.
 */
public class PeekableInputStreamTest {

    /** Tests null input validation in the default-size constructor. */
    @Test
    public void defaultConstructorRejectsNullInput() {
        // Arrange
        final InputStream input = null;

        // Act and Assert
        final NullPointerException exception = assertThrows(NullPointerException.class,
                () -> new PeekableInputStream(input));
        assertEquals("InputStream", exception.getMessage());
    }

    /** Tests that null input validation precedes invalid buffer-size validation. */
    @Test
    public void sizedConstructorRejectsNullInputBeforeInvalidBufferSize() {
        // Arrange
        final InputStream input = null;
        final int bufferSize = 0;

        // Act and Assert
        final NullPointerException exception = assertThrows(NullPointerException.class,
                () -> new PeekableInputStream(input, bufferSize));
        assertEquals("InputStream", exception.getMessage());
    }

    /**
     * Tests both the zero boundary and the negative side of the size guard.
     * @param bufferSize the nonpositive internal buffer size
     */
    @ParameterizedTest
    @ValueSource(ints = {0, -1})
    public void sizedConstructorRejectsNonpositiveBufferSize(final int bufferSize) {
        // Arrange
        final InputStream input = new ByteArrayInputStream(new byte[0]);

        // Act and Assert
        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class,
                () -> new PeekableInputStream(input, bufferSize));
        assertEquals("Invalid buffer size: " + bufferSize, exception.getMessage());
    }

    /** Tests null array validation for the whole-array overload. */
    @Test
    public void peekArrayRejectsNullBuffer() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1);
        final byte[] requested = null;

        // Act and Assert
        final NullPointerException exception = assertThrows(NullPointerException.class, () -> stream.peek(requested));
        assertEquals("Buffer", exception.getMessage());
    }

    /** Tests null validation before slice validation. */
    @Test
    public void peekSliceRejectsNullBufferBeforeInvalidSlice() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1);
        final byte[] requested = null;

        // Act and Assert
        final NullPointerException exception = assertThrows(NullPointerException.class,
                () -> stream.peek(requested, -1, -1));
        assertEquals("Buffer", exception.getMessage());
    }

    /** Tests the whole-array size guard. */
    @Test
    public void peekArrayRejectsArrayLargerThanInternalBuffer() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1);
        final byte[] requested = new byte[2];

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(requested));
    }

    /** Tests that the sliced overload checks the entire array even for an empty slice. */
    @Test
    public void peekSliceRejectsOversizedArrayEvenForZeroLength() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1);
        final byte[] requested = new byte[2];

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(requested, 0, 0));
    }

    /** Tests the delegated offset guard for an empty whole array. */
    @Test
    public void peekArrayRejectsEmptyArrayAtDelegatedOffsetGuard() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1);
        final byte[] requested = new byte[0];

        // Act and Assert
        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class, () -> stream.peek(requested));
        assertEquals("Invalid offset: 0", exception.getMessage());
    }

    /** Tests the delegated offset guard for an empty sliced array. */
    @Test
    public void peekSliceRejectsEmptyArrayAtDelegatedOffsetGuard() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1);
        final byte[] requested = new byte[0];

        // Act and Assert
        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class,
                () -> stream.peek(requested, 0, 0));
        assertEquals("Invalid offset: 0", exception.getMessage());
    }

    /**
     * Tests both sides of offset validation before negative-length validation.
     * @param offset the negative offset or the array-length boundary
     */
    @ParameterizedTest
    @ValueSource(ints = {-1, 1})
    public void peekSliceRejectsInvalidOffsetBeforeInvalidLength(final int offset) {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[] {0}), 1);
        final byte[] requested = new byte[] {0};

        // Act and Assert
        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class,
                () -> stream.peek(requested, offset, -1));
        assertEquals("Invalid offset: " + offset, exception.getMessage());
    }

    /** Tests negative-length validation after a valid offset. */
    @Test
    public void peekSliceRejectsNegativeLength() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[] {0}), 1);
        final byte[] requested = new byte[] {0};

        // Act and Assert
        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class,
                () -> stream.peek(requested, 0, -1));
        assertEquals("Invalid length: -1", exception.getMessage());
    }

    /** Tests the delegated length guard against internal capacity. */
    @Test
    public void peekSliceRejectsLengthLargerThanInternalBuffer() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[] {0}), 1);
        final byte[] requested = new byte[] {0};

        // Act and Assert
        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class,
                () -> stream.peek(requested, 0, 2));
        assertEquals("Invalid length: 2", exception.getMessage());
    }

    /**
     * Tests original read-failure propagation immediately and after one byte is buffered.
     * @param prefixLength the number of successful one-byte reads before failure
     */
    @ParameterizedTest
    @ValueSource(ints = {0, 1})
    public void peekArrayPropagatesReadFailureDuringRefill(final int prefixLength) {
        // Arrange
        final IOException failure = new IOException("Fixture read failure");
        final InputStream input = new PrefixThenFailInputStream(prefixLength, failure);
        final PeekableInputStream stream = new PeekableInputStream(input, 2);
        final byte[] requested = new byte[2];

        // Act and Assert
        final IOException exception = assertThrows(IOException.class, () -> stream.peek(requested));
        assertSame(failure, exception);
    }

    /**
     * Tests that read failures precede delegated offset and length validation.
     * @param prefixLength the number of successful one-byte reads before failure
     */
    @ParameterizedTest
    @ValueSource(ints = {0, 1})
    public void peekSlicePropagatesReadFailureBeforeInvalidSlice(final int prefixLength) {
        // Arrange
        final IOException failure = new IOException("Fixture read failure");
        final InputStream input = new PrefixThenFailInputStream(prefixLength, failure);
        final PeekableInputStream stream = new PeekableInputStream(input, 2);
        final byte[] requested = new byte[2];

        // Act and Assert
        final IOException exception = assertThrows(IOException.class, () -> stream.peek(requested, -1, -1));
        assertSame(failure, exception);
    }

    /**
     * Tests slice-array overrun after a matching prefix, with an empty or full internal buffer.
     * @param inputLength zero for immediate end of input, or two for a full buffer
     */
    @ParameterizedTest
    @ValueSource(ints = {0, 2})
    public void peekSlicePropagatesArrayBoundsFailureAfterMatchingPrefix(final int inputLength) {
        // Arrange
        // Zero-filled input and request arrays prevent an earlier comparison mismatch.
        // With empty input, the internal array also retains its initial zero values.
        final InputStream input = new ByteArrayInputStream(new byte[inputLength]);
        final PeekableInputStream stream = new PeekableInputStream(input, 2);
        final byte[] requested = new byte[2];

        // Act and Assert
        assertThrows(ArrayIndexOutOfBoundsException.class, () -> stream.peek(requested, 1, 2));
    }

    /** Supplies a small zero-byte prefix followed by the same checked read failure. */
    private static final class PrefixThenFailInputStream extends InputStream {
        private int remainingBytes;
        private final IOException failure;

        private PrefixThenFailInputStream(final int prefixLength, final IOException failure) {
            remainingBytes = prefixLength;
            this.failure = failure;
        }

        @Override
        public int read() throws IOException {
            if (remainingBytes > 0) {
                remainingBytes--;
                return 0;
            }
            throw failure;
        }

        @Override
        public int read(final byte[] bytes, final int offset, final int length) throws IOException {
            final int value = read();
            bytes[offset] = (byte) value;
            return 1;
        }
    }
}


~~~

## Observed environment before generation

~~~json

{
  "observedAt": "2026-10-12T22:43:57.8148314Z",
  "observationScope": "Assigned independent generation; observed in the process environment used for the original Maven command.",
  "java": {
    "executable": "C:/Users/edyko/AppData/Local/mise/installs/java/temurin-8.0.504+1/bin\\java.exe",
    "command": "java -version",
    "exitCode": 0,
    "output": [
      "openjdk version \"1.8.0_504\"",
      "OpenJDK Runtime Environment (Temurin)(build 1.8.0_504-b01)",
      "OpenJDK 64-Bit Server VM (Temurin)(build 25.504-b01, mixed mode)"
    ]
  },
  "javac": {
    "executable": "C:/Users/edyko/AppData/Local/mise/installs/java/temurin-8.0.504+1/bin\\javac.exe",
    "command": "javac -version",
    "exitCode": 0,
    "output": [
      "javac 1.8.0_504"
    ]
  },
  "maven": {
    "executable": "C:/Users/edyko/AppData/Local/mise/installs/maven/3.9.16/apache-maven-3.9.16/bin\\mvn.cmd",
    "command": "mvn -version",
    "exitCode": 0,
    "output": [
      "Apache Maven 3.9.16 (2bdd9fddda4b155ebf8000e807eb73fd829a51d5)",
      "Maven home: C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\maven\\3.9.16\\apache-maven-3.9.16",
      "Java version: 1.8.0_504, vendor: Temurin, runtime: C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-8.0.504+1\\jre",
      "Default locale: en_US, platform encoding: Cp1252",
      "OS name: \"windows 11\", version: \"10.0\", arch: \"amd64\", family: \"windows\""
    ]
  },
  "python": {
    "executable": "C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\python\\3.13.15\\python.exe",
    "command": "python --version",
    "exitCode": 0,
    "output": [
      "Python 3.13.15"
    ]
  },
  "os": {
    "description": "Microsoft Windows 10.0.26300",
    "version": "Microsoft Windows NT 10.0.26300.0",
    "architecture": "X64",
    "powershell": "7.6.5"
  },
  "processEnvironment": {
    "JAVA_HOME": "C:/Users/edyko/AppData/Local/mise/installs/java/temurin-8.0.504+1",
    "PATH": "C:/Users/edyko/AppData/Local/mise/installs/java/temurin-8.0.504+1/bin;C:/Users/edyko/AppData/Local/mise/installs/maven/3.9.16/apache-maven-3.9.16/bin;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-25.0.4+101.0.LTS\\bin;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\maven\\3.9.16\\apache-maven-3.9.16/bin;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\node\\22.23.2;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\python\\3.13.15;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\python\\3.13.15\\Scripts;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\uv\\0.12.23;C:\\Users\\edyko\\AppData\\Local\\mise\\shims;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell;C:\\Users\\edyko\\.codex\\tmp\\arg0\\codex-arg0pgGc3k;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\libheif\\libheif\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\jxrlib\\jxrlib\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\poppler\\Library\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\bin\\override;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA App\\NvDLISR;C:\\Program Files\\dotnet\\;C:\\Users\\edyko\\AppData\\Local\\Android\\Sdk\\platform-tools;C:\\Users\\edyko\\AppData\\Local\\Android\\Sdk\\emulator;C:\\Users\\edyko\\AppData\\Local\\Android\\Sdk\\cmdline-tools\\latest\\bin;C:\\Program Files\\GitHub CLI\\;C:\\Program Files\\Docker\\Docker\\resources\\bin;C:\\Program Files\\Git\\cmd;C:\\Users\\edyko\\AppData\\Local\\codegraph\\current\\bin;C:\\Users\\edyko\\AppData\\Local\\Programs\\OpenAI\\Codex\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell;C:\\Users\\edyko\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\edyko\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Program Files\\JetBrains\\PyCharm 2026.2.1\\bin;C:\\Program Files\\JetBrains\\IntelliJ IDEA 2026.2.1\\bin;C:\\Users\\edyko\\AppData\\Local\\Microsoft\\WinGet\\Packages\\jdx.mise_Microsoft.Winget.Source_8wekyb3d8bbwe\\mise\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\bin\\fallback;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\node\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\git\\cmd;C:\\Users\\edyko\\AppData\\Local\\OpenAI\\Codex\\bin\\9a7ba4b9ea0c44a3;C:\\Users\\edyko\\AppData\\Local\\OpenAI\\Codex\\bin\\2e5e00daee91c61d",
    "MAVEN_OPTS": "-DargLine=",
    "MAVEN_ARGS": "-Dmaven.repo.local=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001/maven-repository",
    "TEMP": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001/temp",
    "TMP": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001/temp",
    "JAVA_TOOL_OPTIONS": null,
    "JDK_JAVA_OPTIONS": null,
    "_JAVA_OPTIONS": null
  },
  "generator": {
    "model": null,
    "settings": null,
    "applicationBuild": null,
    "reason": "The exact active model identifier, sampling and reasoning settings, and running application build are not exposed in this chat context. The developer describes the agent as based on GPT-6."
  }
}


~~~

## Final checkout observation

~~~json

{
  "head": "11f0abe7a3fb6954b2985ca4ab0697b2fb489e84",
  "headExitCode": 0,
  "trackedBaselineDiffExitCode": 0,
  "status": [
    "?? src/test/java/org/apache/commons/io/input/buffer/PeekableInputStreamTest.java"
  ],
  "statusExitCode": 0,
  "whitespaceCheckExitCode": 0,
  "generatedTestSHA256": "365a763fbc4b383087d993e659e05bf04952a4d4333a2ff16ac4417fe9eb43dd"
}


~~~

## Preserved closure diagnostic

The first seal operation exited 1 because its report argument pointed into the assigned working directory rather than inside the record directory: 'Artifact path must stay inside its record directory.' The failed output is preserved in evidence/process/seal-report-location-failure.log. The same report was copied into this record directory, and only report placement was corrected before retrying sealing. No test source, input, execution, assertion, fixture, or diagnostic was changed.

