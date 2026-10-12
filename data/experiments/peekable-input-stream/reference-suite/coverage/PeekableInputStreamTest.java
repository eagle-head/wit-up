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
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;
import java.util.stream.Stream;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;
import org.junit.jupiter.params.provider.ValueSource;

/**
 * Tests {@link PeekableInputStream}.
 */
class PeekableInputStreamTest {

    /**
     * Accepts the documented default capacity without consuming the matching bytes.
     *
     * @throws IOException if the stream cannot be read or closed
     */
    @Test
    void testPeekAtDefaultBufferCapacityDoesNotConsumeBytes() throws IOException {
        final byte[] input = new byte[8192];
        Arrays.fill(input, (byte) 0xA5);
        final byte[] expected = input.clone();
        final byte[] actual = new byte[input.length];
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input))) {
            final boolean matches = stream.peek(expected);
            final int bytesRead = stream.read(actual);
            assertTrue(matches);
            assertEquals(input.length, bytesRead);
            assertArrayEquals(input, actual);
        }
    }

    /**
     * Compares binary bytes at a nonzero array offset without consuming input.
     *
     * @throws IOException if the stream cannot be read or closed
     */
    @Test
    void testPeekSliceDoesNotConsumeBytes() throws IOException {
        final byte[] input = {(byte) 0x80, 0, (byte) 0xFF};
        final byte[] expected = {9, (byte) 0x80, 0, (byte) 0xFF, 9};
        final byte[] actual = new byte[input.length];
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 5)) {
            final boolean matches = stream.peek(expected, 1, input.length);
            final int bytesRead = stream.read(actual);
            assertTrue(matches);
            assertEquals(input.length, bytesRead);
            assertArrayEquals(input, actual);
        }
    }

    /**
     * Rejects a mismatching sequence at buffer capacity without consuming input.
     *
     * @throws IOException if the stream cannot be read or closed
     */
    @Test
    void testPeekMismatchDoesNotConsumeBytes() throws IOException {
        final byte[] input = {1, 2, 3};
        final byte[] expected = {1, 2, 4};
        final byte[] actual = new byte[input.length];
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 3)) {
            final boolean matches = stream.peek(expected);
            final int bytesRead = stream.read(actual);
            assertFalse(matches);
            assertEquals(input.length, bytesRead);
            assertArrayEquals(input, actual);
        }
    }

    /**
     * Rejects a mismatching array slice without consuming input.
     *
     * @throws IOException if the stream cannot be read or closed
     */
    @Test
    void testPeekSliceMismatchDoesNotConsumeBytes() throws IOException {
        final byte[] input = {1, 2, 3};
        final byte[] expected = {9, 1, 2, 4};
        final byte[] actual = new byte[input.length];
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 4)) {
            final boolean matches = stream.peek(expected, 1, input.length);
            final int bytesRead = stream.read(actual);
            assertFalse(matches);
            assertEquals(input.length, bytesRead);
            assertArrayEquals(input, actual);
        }
    }

    /**
     * Matches a sequence already buffered after a read.
     *
     * @throws IOException if the stream cannot be read or closed
     */
    @Test
    void testPeekAlreadyBufferedBytes() throws IOException {
        final byte[] input = {0, 1, 2, 3};
        final byte[] expected = {1, 2};
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 3)) {
            stream.read();
            final boolean matches = stream.peek(expected);
            assertTrue(matches);
        }
    }

    /**
     * Matches already buffered bytes through the offset-and-length overload.
     *
     * @throws IOException if the stream cannot be read or closed
     */
    @Test
    void testPeekAlreadyBufferedSlice() throws IOException {
        final byte[] input = {0, 1, 2, 3};
        final byte[] expected = {1, 2};
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 3)) {
            stream.read();
            final boolean matches = stream.peek(expected, 0, expected.length);
            assertTrue(matches);
        }
    }

    /**
     * Rejects a whole-array comparison that exceeds the configured capacity.
     *
     * @throws IOException if the stream cannot be closed
     */
    @Test
    void testPeekExceedsBufferSize() throws IOException {
        final byte[] input = {1, 2};
        final byte[] expected = {1, 2, 3};
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 2)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(expected));
        }
    }

    /**
     * Rejects an oversized comparison through the offset-and-length overload.
     *
     * @throws IOException if the stream cannot be closed
     */
    @Test
    void testPeekSliceExceedsBufferSize() throws IOException {
        final byte[] input = {1, 2};
        final byte[] expected = {1, 2, 3};
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 2)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(expected, 0, expected.length));
        }
    }

    /**
     * Repeatedly rejects a matching prefix shorter than the buffered input without consuming bytes.
     *
     * @throws IOException if the stream cannot be read or closed
     */
    @Test
    void testPeekPrefixDoesNotMatchLongerBufferedInput() throws IOException {
        final byte[] input = {1, 2, 3};
        final byte[] expected = {1, 2};
        final byte[] actual = new byte[input.length];
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 3)) {
            final boolean firstMatch = stream.peek(expected);
            final boolean repeatedMatch = stream.peek(expected);
            final int bytesRead = stream.read(actual);
            assertFalse(firstMatch);
            assertFalse(repeatedMatch);
            assertEquals(input.length, bytesRead);
            assertArrayEquals(input, actual);
        }
    }

    /**
     * Repeatedly rejects a matching slice shorter than the buffered input without consuming bytes.
     *
     * @throws IOException if the stream cannot be read or closed
     */
    @Test
    void testPeekSliceDoesNotMatchLongerBufferedInput() throws IOException {
        final byte[] input = {1, 2, 3};
        final byte[] expected = {9, 1, 2};
        final byte[] actual = new byte[input.length];
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 3)) {
            final boolean firstMatch = stream.peek(expected, 1, 2);
            final boolean repeatedMatch = stream.peek(expected, 1, 2);
            final int bytesRead = stream.read(actual);
            assertFalse(firstMatch);
            assertFalse(repeatedMatch);
            assertEquals(input.length, bytesRead);
            assertArrayEquals(input, actual);
        }
    }

    /**
     * Rejects comparisons requiring bytes beyond the remaining input.
     *
     * @param input the complete input sequence
     * @param expected the sequence requiring unavailable bytes
     * @param bytesToConsume the number of bytes consumed before comparison
     * @throws IOException if the stream cannot be read or closed
     */
    @ParameterizedTest
    @MethodSource("incompleteInputs")
    void testPeekInsufficientRemainingInputDoesNotConsumeBytes(
            final byte[] input, final byte[] expected, final int bytesToConsume) throws IOException {
        final byte[] remaining = Arrays.copyOfRange(input, bytesToConsume, input.length);
        final byte[] actual = new byte[remaining.length];
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 4)) {
            if (bytesToConsume > 0) {
                stream.read(new byte[bytesToConsume]);
            }
            final boolean matches = stream.peek(expected);
            final int bytesRead = remaining.length == 0 ? stream.read() : stream.read(actual);
            assertFalse(matches);
            assertEquals(remaining.length == 0 ? -1 : remaining.length, bytesRead);
            assertArrayEquals(remaining, actual);
        }
    }

    /**
     * Rejects slices requiring bytes beyond the remaining input.
     *
     * @param input the complete input sequence
     * @param expected the sequence requiring unavailable bytes
     * @param bytesToConsume the number of bytes consumed before comparison
     * @throws IOException if the stream cannot be read or closed
     */
    @ParameterizedTest
    @MethodSource("incompleteInputs")
    void testPeekSliceInsufficientRemainingInputDoesNotConsumeBytes(
            final byte[] input, final byte[] expected, final int bytesToConsume) throws IOException {
        final byte[] comparison = new byte[expected.length + 1];
        comparison[0] = 9;
        System.arraycopy(expected, 0, comparison, 1, expected.length);
        final byte[] remaining = Arrays.copyOfRange(input, bytesToConsume, input.length);
        final byte[] actual = new byte[remaining.length];
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 4)) {
            if (bytesToConsume > 0) {
                stream.read(new byte[bytesToConsume]);
            }
            final boolean matches = stream.peek(comparison, 1, expected.length);
            final int bytesRead = remaining.length == 0 ? stream.read() : stream.read(actual);
            assertFalse(matches);
            assertEquals(remaining.length == 0 ? -1 : remaining.length, bytesRead);
            assertArrayEquals(remaining, actual);
        }
    }

    /**
     * Rejects a null comparison array.
     *
     * @throws IOException if the stream cannot be closed
     */
    @Test
    void testPeekNullComparison() throws IOException {
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[] {1}))) {
            assertThrows(NullPointerException.class, () -> stream.peek(null));
        }
    }

    /**
     * Rejects a null array through the offset-and-length overload.
     *
     * @throws IOException if the stream cannot be closed
     */
    @Test
    void testPeekSliceNullComparison() throws IOException {
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[] {1}))) {
            assertThrows(NullPointerException.class, () -> stream.peek(null, 0, 1));
        }
    }

    /**
     * Rejects offsets outside the comparison array.
     *
     * @param offset the invalid start offset
     * @throws IOException if the stream cannot be closed
     */
    @ParameterizedTest
    @ValueSource(ints = {-1, 3})
    void testPeekSliceInvalidOffset(final int offset) throws IOException {
        final byte[] input = {1, 2, 3};
        final byte[] expected = {1, 2, 3};
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 3)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(expected, offset, 1));
        }
    }

    /**
     * Rejects negative lengths and lengths exceeding the buffer capacity.
     *
     * @param length the invalid comparison length
     * @throws IOException if the stream cannot be closed
     */
    @ParameterizedTest
    @ValueSource(ints = {-1, 4})
    void testPeekSliceInvalidLength(final int length) throws IOException {
        final byte[] input = {1, 2, 3};
        final byte[] expected = {1, 2, 3};
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 3)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(expected, 0, length));
        }
    }

    /**
     * Reports an input read failure during whole-array comparison.
     *
     * @throws IOException if the stream cannot be closed
     */
    @Test
    void testPeekPropagatesIOException() throws IOException {
        final IOException failure = new IOException("Input read failed");
        final byte[] expected = {1};
        try (final PeekableInputStream stream = new PeekableInputStream(unreadableInput(failure), 1)) {
            assertThrows(IOException.class, () -> stream.peek(expected));
        }
    }

    /**
     * Reports an input read failure during slice comparison.
     *
     * @throws IOException if the stream cannot be closed
     */
    @Test
    void testPeekSlicePropagatesIOException() throws IOException {
        final IOException failure = new IOException("Input read failed");
        final byte[] expected = {9, 1};
        try (final PeekableInputStream stream = new PeekableInputStream(unreadableInput(failure), 2)) {
            assertThrows(IOException.class, () -> stream.peek(expected, 1, 1));
        }
    }

    /**
     * Matches bytes across a circular-buffer boundary after partial reads and refill.
     *
     * @throws IOException if the stream cannot be read or closed
     */
    @Test
    void testPeekAcrossCircularBoundaryAfterPartialReadsDoesNotConsumeBytes() throws IOException {
        final byte[] input = {1, 2, 3, 4, 5};
        final byte[] expected = {3, 4, 5};
        final byte[] actual = new byte[expected.length];
        try (final PeekableInputStream stream = new PeekableInputStream(oneByteReads(input), 3)) {
            stream.read(new byte[2]);
            final boolean matches = stream.peek(expected);
            final int bytesRead = stream.read(actual);
            assertTrue(matches);
            assertEquals(expected.length, bytesRead);
            assertArrayEquals(expected, actual);
        }
    }

    /**
     * Matches a slice across a circular-buffer boundary after partial reads and refill.
     *
     * @throws IOException if the stream cannot be read or closed
     */
    @Test
    void testPeekSliceAcrossCircularBoundaryAfterPartialReadsDoesNotConsumeBytes() throws IOException {
        final byte[] input = {1, 2, 3, 4, 5, 6};
        final byte[] expected = {9, 4, 5, 6};
        final byte[] remaining = {4, 5, 6};
        final byte[] actual = new byte[remaining.length];
        try (final PeekableInputStream stream = new PeekableInputStream(oneByteReads(input), 4)) {
            stream.read(new byte[3]);
            final boolean matches = stream.peek(expected, 1, remaining.length);
            final int bytesRead = stream.read(actual);
            assertTrue(matches);
            assertEquals(remaining.length, bytesRead);
            assertArrayEquals(remaining, actual);
        }
    }

    /**
     * Rejects a null input when using the default buffer size.
     */
    @Test
    void testConstructorNullInput() {
        final InputStream input = null;
        assertThrows(NullPointerException.class, () -> new PeekableInputStream(input));
    }

    /**
     * Rejects a null input when using an explicit buffer size.
     */
    @Test
    void testConstructorNullInputWithBufferSize() {
        final InputStream input = null;
        assertThrows(NullPointerException.class, () -> new PeekableInputStream(input, 1));
    }

    /**
     * Rejects zero and negative buffer sizes.
     *
     * @param bufferSize the invalid buffer capacity
     * @throws IOException if the input cannot be closed
     */
    @ParameterizedTest
    @ValueSource(ints = {0, -1})
    void testConstructorNonPositiveBufferSize(final int bufferSize) throws IOException {
        try (final ByteArrayInputStream input = new ByteArrayInputStream(new byte[] {1})) {
            assertThrows(IllegalArgumentException.class, () -> new PeekableInputStream(input, bufferSize));
        }
    }

    /**
     * Matches a binary byte at the smallest supported buffer capacity.
     *
     * @throws IOException if the stream cannot be read or closed
     */
    @Test
    void testPeekWithOneByteBufferDoesNotConsumeBytes() throws IOException {
        final byte[] input = {(byte) 0xFF};
        final byte[] expected = {(byte) 0xFF};
        final byte[] actual = new byte[1];
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 1)) {
            final boolean matches = stream.peek(expected);
            final int bytesRead = stream.read(actual);
            assertTrue(matches);
            assertEquals(1, bytesRead);
            assertArrayEquals(input, actual);
        }
    }

    /**
     * Rejects a comparison one byte beyond the documented default capacity.
     *
     * @throws IOException if the stream cannot be closed
     */
    @Test
    void testPeekExceedsDefaultBufferCapacity() throws IOException {
        final byte[] expected = new byte[8193];
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]))) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(expected));
        }
    }

    /**
     * Preserves the historical rejection of an empty comparison array.
     *
     * @throws IOException if the stream cannot be closed
     */
    @Test
    void testPeekEmptyComparison() throws IOException {
        final byte[] input = {1};
        final byte[] expected = new byte[0];
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 1)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(expected));
        }
    }

    /**
     * Rejects a zero-length slice when input bytes are buffered without consuming them.
     *
     * @throws IOException if the stream cannot be read or closed
     */
    @Test
    void testPeekZeroLengthSliceWithBufferedInputDoesNotConsumeBytes() throws IOException {
        final byte[] input = {1};
        final byte[] expected = {9};
        final byte[] actual = new byte[input.length];
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(input), 1)) {
            final boolean matches = stream.peek(expected, 0, 0);
            final int bytesRead = stream.read(actual);
            assertFalse(matches);
            assertEquals(input.length, bytesRead);
            assertArrayEquals(input, actual);
        }
    }

    /**
     * Supplies empty, truncated, and exhausted input cases.
     *
     * @return the input, requested sequence, and number of bytes to consume
     */
    private static Stream<Arguments> incompleteInputs() {
        return Stream.of(
                Arguments.of(new byte[0], new byte[] {0}, 0),
                Arguments.of(new byte[] {1, 2}, new byte[] {1, 2, 0}, 0),
                Arguments.of(new byte[] {1, 2, 3, 4}, new byte[] {1, 2}, 4));
    }

    /**
     * Creates an input that returns at most one byte per bulk read.
     *
     * @param input the bytes supplied by the input
     * @return the input with deterministic partial reads
     */
    private static ByteArrayInputStream oneByteReads(final byte[] input) {
        return new ByteArrayInputStream(input) {
            @Override
            public synchronized int read(final byte[] buffer, final int offset, final int length) {
                return super.read(buffer, offset, Math.min(length, 1));
            }
        };
    }

    /**
     * Creates an input whose reads fail and whose close operation succeeds.
     *
     * @param failure the read failure to report
     * @return the failing input
     */
    private static InputStream unreadableInput(final IOException failure) {
        return new InputStream() {
            @Override
            public int read() throws IOException {
                throw failure;
            }
        };
    }
}
