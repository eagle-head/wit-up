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
 * Exception scenarios supported by the supplied analysis records.
 *
 * Fixtures assume that a positive constructor size becomes the stream's buffer size and initializes a non-null buffer.
 * A fresh stream over an empty input is assumed to have zero buffered bytes. These internal conditions are not inspected,
 * so the tests assert the recorded exceptions without claiming exact execution-path reproduction.
 */
public class PeekableInputStreamTest {

    @Test
    public void testConstructorRejectsNegativeBufferSize() {
        final ByteArrayInputStream input = new ByteArrayInputStream(new byte[0]);
        // The exported size is zero; -1 is an explicit variant of the false "pBufferSize > 0" constraint.
        assertThrows(IllegalArgumentException.class, () -> new PeekableInputStream(input, -1));
    }

    @Test
    public void testConstructorRejectsZeroBufferSize() {
        final ByteArrayInputStream input = new ByteArrayInputStream(new byte[0]);
        assertThrows(IllegalArgumentException.class, () -> new PeekableInputStream(input, 0));
    }

    @Test
    public void testPeekRejectsEmptyArray() throws IOException {
        final byte[] expected = new byte[0];
        // Use capacity 1 instead of the exported zero-capacity receiver; the empty-array constraints still hold.
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(expected));
        }
    }

    @Test
    public void testPeekRejectsNullArray() throws IOException {
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(NullPointerException.class, () -> stream.peek(null));
        }
    }

    @Test
    public void testPeekRejectsOversizedArray() throws IOException {
        final byte[] expected = new byte[2];
        // Replace exported length 1/capacity 0 with length 2/capacity 1, preserving length > capacity.
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(expected));
        }
    }

    @Test
    public void testPeekSliceRejectsEmptyArray() throws IOException {
        final byte[] expected = new byte[0];
        // Capacity 1 replaces exported capacity 0; offset 0 is still at the end of the empty array.
        // Length is unassigned in the model; use zero.
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(expected, 0, 0));
        }
    }

    @Test
    public void testPeekSliceRejectsNegativeLengthWithEmptyInput() throws IOException {
        final byte[] expected = new byte[1];
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(expected, 0, -1));
        }
    }

    @Test
    public void testPeekSliceRejectsNegativeOffsetForEmptyArray() throws IOException {
        final byte[] expected = new byte[0];
        // Capacity 1 replaces exported capacity 0. Keep the exported offset -1; choose unassigned length zero.
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(expected, -1, 0));
        }
    }

    @Test
    public void testPeekSliceRejectsNegativeOffsetWithEmptyInput() throws IOException {
        final byte[] expected = new byte[1];
        // Replace exported array length/capacity 0 and buffered count -1 with length/capacity 1 and count 0.
        // This preserves insufficient buffered bytes and offset -1; choose unassigned length 1.
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(expected, -1, 1));
        }
    }

    @Test
    public void testPeekSliceRejectsNullArray() throws IOException {
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(NullPointerException.class, () -> stream.peek(null, 0, 0));
        }
    }

    @Test
    public void testPeekSliceRejectsOffsetAtArrayEndWithEmptyInput() throws IOException {
        final byte[] expected = new byte[1];
        // Replace exported array length/capacity 0 and buffered count -1 with length/capacity 1 and count 0.
        // Offset changes from 0 to 1 to remain at the array end; choose unassigned length 1.
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(expected, 1, 1));
        }
    }

    @Test
    public void testPeekSliceRejectsOversizedArray() throws IOException {
        final byte[] expected = new byte[2];
        // Replace exported length 1/capacity 0 with length 2/capacity 1, preserving length > capacity.
        // Offset and length are unassigned in the model; choose the first byte only.
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(expected, 0, 1));
        }
    }
}
