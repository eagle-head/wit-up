# 2. How many methods, paths, exception types, and solver verdicts appear?

[Documentation index](../README.md) | [JSON analysis overview](../commons-io-json-analysis.md)

| Unit | results | summaries |
| --- | --- | --- |
| Rows / unique cross-file path keys | 88,303 | 72,419 |
| Full method signatures, including constructors | 1,127 | 1,127 |
| Declaring classes | 134 | 134 |
| Rows referring to constructors | 11,555 | 6,431 |
| Distinct named exception types | Not exported | 19 |

These are units represented by the supplied exports, not all methods or all runtime paths in the library. Methods with no exported exception paths and analysis failures cannot be counted from these two files alone.

### Result verdicts

| Value | Rows | Share |
| --- | --- | --- |
| `UNSAT` | 67,447 | 76.38% |
| `SAT` | 20,800 | 23.56% |
| `MAYBE` | 56 | 0.06% |

### Summary verdicts

| Value | Rows | Share |
| --- | --- | --- |
| `UNSAT` | 56,197 | 77.60% |
| `SAT` | 16,166 | 22.32% |
| `MAYBE` | 56 | 0.08% |

`SAT` means satisfiable in the encoded constraint model. `UNSAT` means unsatisfiable in that model. `UNKNOWN` is an undecided solver verdict. In the inspected implementation, `MAYBE` can record incomplete constraint handling or a failed solver task. The verdict is a prioritization input for later experiments, not evidence that a Java fixture reaches the reported exception.

### Exception origins

| Value | Rows | Share |
| --- | --- | --- |
| `CALLEE_PROPAGATED` | 68,483 | 94.56% |
| `IMPLICIT` | 3,409 | 4.71% |
| `DIRECT_ATHROW` | 508 | 0.70% |
| `RETHROW` | 19 | 0.03% |

### Most frequent exception types

| Value | Rows | Share |
| --- | --- | --- |
| `java.lang.NullPointerException` | 54,010 | 74.58% |
| `java.io.IOException` | 9,594 | 13.25% |
| `java.lang.ArrayIndexOutOfBoundsException` | 7,142 | 9.86% |
| `java.lang.IllegalArgumentException` | 600 | 0.83% |
| `java.lang.NegativeArraySizeException` | 323 | 0.45% |
| `<null>` | 161 | 0.22% |
| `org.apache.commons.io.input.XmlStreamReaderException` | 129 | 0.18% |
| `java.lang.IllegalStateException` | 113 | 0.16% |
| `java.io.FileNotFoundException` | 97 | 0.13% |
| `java.lang.UnsupportedOperationException` | 57 | 0.08% |
| `java.io.EOFException` | 40 | 0.06% |
| `java.lang.ArithmeticException` | 31 | 0.04% |
| `org.apache.commons.io.IOExceptionList` | 26 | 0.04% |
| `java.lang.IndexOutOfBoundsException` | 22 | 0.03% |
| `java.nio.file.NotDirectoryException` | 22 | 0.03% |

The complete exception distribution is available in `data/processed/statistics.json`.

`<null>` in the distribution is a display label for JSON null, not a Java exception type.

### Methods with the most summary paths

| Signature | Summary paths | SAT paths |
| --- | --- | --- |
| `<org.apache.commons.io.monitor.FileAlterationMonitor: void run()>` | 4,285 | 264 |
| `<org.apache.commons.io.FilenameUtils: java.lang.String concat(java.lang.String,java.lang.String)>` | 3,476 | 339 |
| `<org.apache.commons.io.FileSystemUtils: long freeSpaceOS(java.lang.String,int,boolean,long)>` | 3,168 | 1,234 |
| `<org.apache.commons.io.FileSystemUtils: long freeSpaceKb()>` | 1,868 | 818 |
| `<org.apache.commons.io.FileSystemUtils: long freeSpaceKb(java.lang.String)>` | 1,868 | 818 |
| `<org.apache.commons.io.FileSystemUtils: long freeSpaceKb(java.lang.String,long)>` | 1,868 | 818 |
| `<org.apache.commons.io.FileSystemUtils: long freeSpaceKb(long)>` | 1,868 | 818 |
| `<org.apache.commons.io.FileSystemUtils: long freeSpace(java.lang.String)>` | 1,867 | 818 |
| `<org.apache.commons.io.FilenameUtils: boolean equals(java.lang.String,java.lang.String,boolean,org.apache.commons.io.IOCase)>` | 1,436 | 148 |
| `<org.apache.commons.io.FilenameUtils: boolean equalsNormalized(java.lang.String,java.lang.String)>` | 1,428 | 146 |
| `<org.apache.commons.io.FilenameUtils: boolean equalsNormalizedOnSystem(java.lang.String,java.lang.String)>` | 1,428 | 146 |
| `<org.apache.commons.io.FilenameUtils: java.lang.String normalize(java.lang.String,boolean)>` | 1,426 | 156 |
| `<org.apache.commons.io.FilenameUtils: java.lang.String normalizeNoEndSeparator(java.lang.String,boolean)>` | 1,426 | 156 |
| `<org.apache.commons.io.FileSystemUtils: long freeSpaceWindows(java.lang.String,long)>` | 1,301 | 417 |
| `<org.apache.commons.io.FileUtils: void copyToDirectory(java.io.File,java.io.File)>` | 1,269 | 304 |
