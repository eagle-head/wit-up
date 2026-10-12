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
