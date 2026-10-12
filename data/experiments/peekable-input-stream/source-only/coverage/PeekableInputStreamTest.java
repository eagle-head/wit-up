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
