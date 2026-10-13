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
import java.io.InputStream;

import org.junit.jupiter.api.Test;

public class PeekableInputStreamTest {

    @Test
    public void testConstructorRejectsZeroBufferSize() {
        // Arrange
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final int bufferSize = 0;

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> new PeekableInputStream(input, bufferSize));
    }

    @Test
    public void testPeekArrayRejectsNullBuffer() {
        // Arrange
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = null;

        // Act and Assert
        assertThrows(NullPointerException.class, () -> stream.peek(candidate));
    }

    @Test
    public void testPeekArrayRejectsBufferLargerThanCapacity() {
        // Arrange
        // Assume the constructor size becomes the receiver's buffer size.
        // Change modeled capacity 0 to 1 and array length 1 to 2, preserving length > capacity.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[2];

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate));
    }

    @Test
    public void testPeekArrayRejectsEmptyBuffer() {
        // Arrange
        // Assume size 1 creates a non-null, empty buffer. Modeled receiver size 0 becomes 1.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[0];

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate));
    }

    @Test
    public void testPeekSliceRejectsNullBuffer() {
        // Arrange
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = null;
        final int offset = 0;
        final int length = 0;

        // Act and Assert
        assertThrows(NullPointerException.class, () -> stream.peek(candidate, offset, length));
    }

    @Test
    public void testPeekSliceRejectsBufferLargerThanCapacity() {
        // Arrange
        // Assume the constructor size becomes the receiver's buffer size.
        // Change modeled capacity 0 to 1 and array length 1 to 2, preserving length > capacity.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[2];
        final int offset = 0;
        final int length = 1;

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate, offset, length));
    }

    @Test
    public void testPeekSliceRejectsOffsetAtEmptyBufferEnd() {
        // Arrange
        // Assume size 1 creates a non-null, empty buffer. Modeled receiver size 0 becomes 1.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[0];
        final int offset = 0;
        final int length = 0;

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate, offset, length));
    }

    @Test
    public void testPeekSliceRejectsNegativeOffset() {
        // Arrange
        // Assume size 1 creates a non-null, empty buffer. Modeled receiver size 0 becomes 1.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[0];
        final int offset = -1;
        final int length = 0;

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate, offset, length));
    }

    @Test
    public void testPeekSliceRejectsNegativeLength() {
        // Arrange
        // Assume size 1 creates a non-null buffer with an initial byte count of 0.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[1];
        final int offset = 0;
        final int length = -1;

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate, offset, length));
    }

    @Test
    public void testPeekSliceRejectsLengthLargerThanCapacity() {
        // Arrange
        // Assume size 1 creates a non-null buffer of capacity 1 with an initial byte count of 0.
        // Change modeled internal capacity 0 to 1 and requested length 1 to 2, preserving length > capacity.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[1];
        final int offset = 0;
        final int length = 2;

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate, offset, length));
    }
}
