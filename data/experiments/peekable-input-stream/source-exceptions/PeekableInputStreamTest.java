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
