# Measurement preparation diagnostic

This linked evaluation is incomplete. Its only execution was tool preparation,
which exited 1 after all four Maven preparation goals succeeded. No test goal,
JaCoCo measurement, or PIT mutation invocation ran. This process failure does not
contribute a test failure or a zero coverage/mutation result.

The dependency-path extraction regular expression in the rendered preparation
script was invalid (unterminated character class). Therefore dependency hashes
were not written. The manager retained the missing-artifact protocol diagnostic
and unknown attributed suite counts. The original execution receipt is preserved.
A Python rendering warning about an invalid escape sequence preceded the faulty
PowerShell pattern; neither warning nor process error is reported as success.

The observed tools were Temurin 1.8.0_504-b01, javac 1.8.0_504, Maven 3.9.16,
JaCoCo 0.8.4, and the unchanged baseline's JUnit Jupiter 5.5.2/Surefire 2.22.2.
Both fetched JaCoCo JARs matched the canonical hashes. Exact executable locations,
version output, environment variables, commands, scripts, tool hashes, effective
POM, resolved dependencies, and the failure log remain in this record.

The generation remains sealed and unchanged, with 20 passed tests, zero failures,
zero errors, and zero skips. Its separate style findings are retained in the
parent report. This evaluation contributes zero independent generations.

Before and after measurements are unavailable in this record. A separate linked
evaluation may retry the original scope after correcting preparation tooling.
The correction must not modify the frozen Java or the canonical measurement plan.

## Reserved command

```powershell
pwsh -NoProfile -File "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/001/evidence/scripts/preflight.ps1"
```

The complete rendered command body is retained in `evidence/scripts/preflight.ps1`.

## Complete frozen Java source

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
```
