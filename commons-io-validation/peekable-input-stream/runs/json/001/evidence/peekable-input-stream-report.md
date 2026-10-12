# PeekableInputStream Test Generation and Validation Report



Apache Commons IO 2.7-SNAPSHOT · October 12, 2026 · United States English



## Measured before and after results



**The measured before baseline is zero.** Removing the generated test and clean-compiling produced zero target-class coverage under the existing Surefire suite. With the generated suite, all ten tests passed and one of fourteen PIT mutants was killed.



| Target-class metric | Before | After |
| --- | --- | --- |
| JaCoCo instructions | 0/98 (0.00%) | 77/98 (78.57%) |
| JaCoCo branches | 0/8 (0.00%) | 7/8 (87.50%) |
| JaCoCo lines | 0/16 (0.00%) | 11/16 (68.75%) |
| JaCoCo complexity | 0/8 (0.00%) | 6/8 (75.00%) |
| JaCoCo methods | 0/4 (0.00%) | 3/4 (75.00%) |
| JaCoCo classes | 0/1 (0.00%) | 1/1 (100.00%) |
| PIT mutation score (killed / generated) | 0/14 (0.00%) | 1/14 (7.14%) |
| PIT covered mutants | 0/14 (0.00%) | 9/14 (64.29%) |
| PIT test strength (killed / covered mutants) | N/A (0/0) | 1/9 (11.11%) |
| PIT native line coverage | 0/16 (0.00%) | 13/16 (81.25%) |
| PIT mutant outcomes | 14 NO\_COVERAGE | 1 KILLED; 8 SURVIVED; 5 NO\_COVERAGE |



All JaCoCo counters refer only to PeekableInputStream. JaCoCo and PIT report different line-coverage observations; the PIT value does not substitute for the JaCoCo value. Native reports round percentages; this table calculates percentages from the raw counts.



PIT's native before report prints 100% test strength when no mutant is covered. This report marks 0/0 as N/A because the denominator is zero; it is not evidence of perfect test strength.



| Successful execution | Completed (UTC−04:00) | Reported cases | Failures / errors / skipped | Exit |
| --- | --- | --- | --- | --- |
| Authorized supplemental run, original command | 2026-10-12T15:29:30-04:00 | 10 | 0 / 0 / 0 | 0 |
| JaCoCo before, existing full Surefire suite | 2026-10-12T15:48:11-04:00 | 1,541 | 0 / 0 / 6 | 0 |
| PIT before, generated suite absent | 2026-10-12T15:53:55-04:00 | 0 generated tests | 14 mutants without coverage | 0 |
| JaCoCo after, generated suite | 2026-10-12T15:55:47-04:00 | 10 | 0 / 0 / 0 | 0 |
| PIT after, generated suite | 2026-10-12T15:56:05-04:00 | 10 distinct tests | 1 killed / 8 survived / 5 uncovered | 0 |



The baseline contains 136 Surefire report classes and 1,535 non-skipped case executions. Its six skipped cases come from the existing suite. The final generated-suite run took 0.018 seconds in Surefire. PIT reports 26 cumulative mutation-test executions, not 26 distinct generated tests; its final run has no timeout, run error, memory error, or non-viable mutant.



## Measurement scope and checkout integrity



The before baseline was reconstructed and measured after test generation on October 12, 2026. It is not an invented historical measurement. Only the generated source file was temporarily moved out of the checkout. A clean build removed its compiled test class, and the existing Surefire suite was run with the target-class JaCoCo agent. The source was restored in a finally block and verified byte for byte. PIT's successful before measurement ran while the generated compiled class was still absent; the successful after measurements followed a clean rebuild with the source restored.



The project already contained tests for other classes. The measured fact is zero coverage of PeekableInputStream under the existing Surefire suite. JaCoCo before uses that full suite; JaCoCo after uses only the ten generated tests. Both PIT phases use targetClasses = org.apache.commons.io.input.buffer.PeekableInputStream and targetTests = org.apache.commons.io.input.buffer.PeekableInputStreamTest. Their relevant configuration and fourteen mutant identities are identical. The before PIT score is the zero contribution of the absent generated suite; the after score is the contribution of that suite.



Full-project PIT validation was unsuccessful. The separate [execution diagnostics record](execution-diagnostics.md) preserves the failed exploratory attempts and the initial Maven startup failures. They do not enter the successful ten-test outcome totals, and no full-project PIT success is claimed.



| Integrity item | Verified value |
| --- | --- |
| Checkout HEAD | 11f0abe7a3fb6954b2985ca4ab0697b2fb489e84 |
| Tracked checkout difference | git diff --quiet against the fixed commit: exit 0 |
| Generated test SHA-256, frozen copy and restored checkout | a29b1141af4aa61b9081d22e2056f69596e5ec602062773a4618b5567c3de926 |
| Compiled production class SHA-256, before and final after | 7ab6a91f3618ccf5949692f1fc5d39b97174deab23925f872f0e31cb5a2591a1 |
| Final git status | ?? src/test/java/org/apache/commons/io/input/buffer/PeekableInputStreamTest.java |



The generated Java test is unchanged. No production source, existing test, checkout POM, dependency version, assertion, or quality threshold was edited during validation. JaCoCo and PIT read compiled classes mechanically. Their reports were generated without production source directories. No production source, Javadoc, decompiled code, or earlier reference test was used to create or revise the generated tests. No new tests were added in response to coverage or mutation feedback.



Apache RAT and Animal Sniffer passed in the successful Maven test lifecycle. Checkstyle and a full verify lifecycle were not executed. A successful targeted PIT command does not imply a high mutation score or a configured quality threshold passed.



## Generation inputs, oracles, and scenario traceability



Generation used only the two raw WIT-UP exports below. Records were selected for package org.apache.commons.io.input.buffer, class PeekableInputStream, and methods \<init\> or peek. The join uses both artifact and pathId; positions refer to the original top-level arrays and are zero-based.



| Raw source | Array records | SHA-256 |
| --- | --- | --- |
| D:\\Projects\\wit-up\\legacy\\commons-io-analysis-results\\witup-results-commons-io-11f0abe7a.json | 88303 | dcecb6911821347c37fef48dbba040740133ccf5598ae348abeebef42d74aaad |
| D:\\Projects\\wit-up\\legacy\\commons-io-analysis-results\\witup-summaries-commons-io-11f0abe7a.json | 72419 | 7a02a927431c15e1d3f4c0bdf1625e9647eddbe8f7664e2fce9a58f935205c1d |



There are 100 unique matching pairs: 31 SAT and 69 UNSAT. Selected join keys were checked for uniqueness across the original arrays. Shared method metadata and solver statuses agree. No missing, duplicate, contradictory, or unusable selected pair was found. Ten SAT records produced ten tests. The remaining twenty-one SAT records lacked sufficiently supported public fixtures, and the sixty-nine UNSAT records supplied no satisfiable concrete fixture.



The matching artifact label is commons-io-11f0abe7a.jar. The analyzed JAR bytes, the producing WIT-UP revision, and equivalence between that analyzed binary and this checkout remain unverified. The exact Codex generation model and application build were not recorded and are not inferred. Raw models, constraints, exception types, throw-site classifications, and propagation provenance are retained in [the complete scenario audit](test-scenarios.json). These are scenario observations, not independently established API specifications.



| Generated test | Source path | Results / summaries positions | Exception oracle | Fixture and model changes |
| --- | --- | --- | --- | --- |
| testConstructorRejectsZeroBufferSize | \<org.apache.commons.io.input.buffer.PeekableInputStream: void \<init\>(java.io.InputStream,int)\>\#0 | 33288 / 46532 | java.lang.IllegalArgumentException | Empty ByteArrayInputStream; constructor buffer size 0.; No modeled value changed. |
| testPeekArrayRejectsNullBuffer | \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\])\>\#1 | 21965 / 54443 | java.lang.NullPointerException | Empty ByteArrayInputStream; constructor size 1; candidate null.; No modeled value changed. |
| testPeekArrayRejectsBufferLargerThanCapacity | \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\])\>\#0 | 21964 / 54442 | java.lang.IllegalArgumentException | Empty ByteArrayInputStream; constructor size 1; candidate byte\[2\].; this.bufferSize: 0 -\> 1; pBuffer.length: 1 -\> 2 |
| testPeekArrayRejectsEmptyBuffer | \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\])\>\#9 | 21973 / 54451 | java.lang.IllegalArgumentException | Empty ByteArrayInputStream; constructor size 1; candidate byte\[0\].; this.bufferSize: 0 -\> 1 |
| testPeekSliceRejectsNullBuffer | \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\],int,int)\>\#1 | 13743 / 61200 | java.lang.NullPointerException | Empty ByteArrayInputStream; constructor size 1; candidate null; offset 0; length 0.; No modeled value changed. |
| testPeekSliceRejectsBufferLargerThanCapacity | \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\],int,int)\>\#0 | 13742 / 61199 | java.lang.IllegalArgumentException | Empty ByteArrayInputStream; constructor size 1; candidate byte\[2\]; offset 0; length 1.; this.bufferSize: 0 -\> 1; pBuffer.length: 1 -\> 2 |
| testPeekSliceRejectsOffsetAtEmptyBufferEnd | \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\],int,int)\>\#7 | 13749 / 61206 | java.lang.IllegalArgumentException | Empty ByteArrayInputStream; constructor size 1; candidate byte\[0\]; offset 0; length 0.; this.bufferSize: 0 -\> 1 |
| testPeekSliceRejectsNegativeOffset | \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\],int,int)\>\#8 | 13750 / 61207 | java.lang.IllegalArgumentException | Empty ByteArrayInputStream; constructor size 1; candidate byte\[0\]; offset -1; length 0.; this.bufferSize: 0 -\> 1 |
| testPeekSliceRejectsNegativeLength | \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\],int,int)\>\#31 | 13773 / 61230 | java.lang.IllegalArgumentException | Empty ByteArrayInputStream; constructor size 1; candidate byte\[1\]; offset 0; length -1.; No modeled value changed. |
| testPeekSliceRejectsLengthLargerThanCapacity | \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\],int,int)\>\#30 | 13772 / 61229 | java.lang.IllegalArgumentException | Empty ByteArrayInputStream; constructor size 1; candidate byte\[1\]; offset 0; length 2.; this.buffer.buffer.length: 0 -\> 1; pLength: 1 -\> 2 |



#### testConstructorRejectsZeroBufferSize — source model and fixture assumptions



The input stream is an unconstrained public argument in this record; a standard in-memory stream supplies it.



```json
{
  "artifact": "commons-io-11f0abe7a.jar",
  "pathId": "<org.apache.commons.io.input.buffer.PeekableInputStream: void <init>(java.io.InputStream,int)>#0",
  "resultsPosition": 33288,
  "summariesPosition": 46532,
  "status": "SAT",
  "signature": "<org.apache.commons.io.input.buffer.PeekableInputStream: void <init>(java.io.InputStream,int)>",
  "exceptionType": "java.lang.IllegalArgumentException",
  "constraints": [
    {
      "symExpr": "(pBufferSize > 0)",
      "truthValue": false
    }
  ],
  "modelValues": {
    "pBufferSize": "IntValue[value=0]"
  },
  "throwSiteKind": "CALLEE_PROPAGATED",
  "propagationProvenance": [
    [
      "<org.apache.commons.io.input.buffer.CircularBufferInputStream: void <init>(java.io.InputStream,int)>"
    ]
  ]
}
```



#### testPeekArrayRejectsNullBuffer — source model and fixture assumptions



Positive-size construction succeeds. The null condition is taken from the explicit null constraint and flag, not from the serialized reference identity.



```json
{
  "artifact": "commons-io-11f0abe7a.jar",
  "pathId": "<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte[])>#1",
  "resultsPosition": 21965,
  "summariesPosition": 54443,
  "status": "SAT",
  "signature": "<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte[])>",
  "exceptionType": "java.lang.NullPointerException",
  "constraints": [
    {
      "symExpr": "(pBuffer == null)",
      "truthValue": true
    }
  ],
  "modelValues": {
    "pBuffer": "IntValue[value=0]",
    "pBuffer_is_null": "BoolValue[value=true]"
  },
  "throwSiteKind": "IMPLICIT",
  "propagationProvenance": [
    []
  ]
}
```



#### testPeekArrayRejectsBufferLargerThanCapacity — source model and fixture assumptions



The constructor size maps to receiver capacity. Changing both values permits positive-size construction while preserving pBuffer.length \> this.bufferSize.



```json
{
  "artifact": "commons-io-11f0abe7a.jar",
  "pathId": "<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte[])>#0",
  "resultsPosition": 21964,
  "summariesPosition": 54442,
  "status": "SAT",
  "signature": "<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte[])>",
  "exceptionType": "java.lang.IllegalArgumentException",
  "constraints": [
    {
      "symExpr": "(pBuffer.length <= this.bufferSize)",
      "truthValue": false
    }
  ],
  "modelValues": {
    "pBuffer.length": "IntValue[value=1]",
    "this.bufferSize": "IntValue[value=0]"
  },
  "throwSiteKind": "DIRECT_ATHROW",
  "propagationProvenance": [
    []
  ]
}
```



#### testPeekArrayRejectsEmptyBuffer — source model and fixture assumptions



Positive-size construction creates a non-null, initially empty internal buffer. The empty candidate and remaining constraints are preserved under this assumption.



```json
{
  "artifact": "commons-io-11f0abe7a.jar",
  "pathId": "<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte[])>#9",
  "resultsPosition": 21973,
  "summariesPosition": 54451,
  "status": "SAT",
  "signature": "<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte[])>",
  "exceptionType": "java.lang.IllegalArgumentException",
  "constraints": [
    {
      "symExpr": "(pBuffer != null)",
      "truthValue": true
    },
    {
      "symExpr": "(pBuffer.length <= this.bufferSize)",
      "truthValue": true
    },
    {
      "symExpr": "(this.buffer != null)",
      "truthValue": true
    },
    {
      "symExpr": "(this.buffer.getCurrentNumberOfBytes() >= pBuffer.length)",
      "truthValue": true
    },
    {
      "symExpr": "(0 < pBuffer.length)",
      "truthValue": false
    }
  ],
  "modelValues": {
    "pBuffer.length": "IntValue[value=0]",
    "expr_1_int": "IntValue[value=0]",
    "this.bufferSize": "IntValue[value=0]",
    "this.buffer_is_null": "BoolValue[value=false]",
    "this": "IntValue[value=2]",
    "this.buffer": "IntValue[value=0]",
    "pBuffer": "IntValue[value=0]",
    "pBuffer_is_null": "BoolValue[value=false]",
    "expr_2.getCurrentNumberOfBytes()": "IntValue[value=0]"
  },
  "throwSiteKind": "CALLEE_PROPAGATED",
  "propagationProvenance": [
    [
      "<org.apache.commons.io.input.buffer.CircularByteBuffer: boolean peek(byte[],int,int)>"
    ]
  ]
}
```



#### testPeekSliceRejectsNullBuffer — source model and fixture assumptions



Positive-size construction succeeds. Offset and length are unconstrained in the record and are chosen as 0; the null condition is unchanged.



```json
{
  "artifact": "commons-io-11f0abe7a.jar",
  "pathId": "<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte[],int,int)>#1",
  "resultsPosition": 13743,
  "summariesPosition": 61200,
  "status": "SAT",
  "signature": "<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte[],int,int)>",
  "exceptionType": "java.lang.NullPointerException",
  "constraints": [
    {
      "symExpr": "(pBuffer == null)",
      "truthValue": true
    }
  ],
  "modelValues": {
    "pBuffer": "IntValue[value=0]",
    "pBuffer_is_null": "BoolValue[value=true]"
  },
  "throwSiteKind": "IMPLICIT",
  "propagationProvenance": [
    []
  ]
}
```



#### testPeekSliceRejectsBufferLargerThanCapacity — source model and fixture assumptions



The constructor size maps to receiver capacity. The inequality is preserved. Offset and length are unconstrained and chosen as 0 and 1.



```json
{
  "artifact": "commons-io-11f0abe7a.jar",
  "pathId": "<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte[],int,int)>#0",
  "resultsPosition": 13742,
  "summariesPosition": 61199,
  "status": "SAT",
  "signature": "<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte[],int,int)>",
  "exceptionType": "java.lang.IllegalArgumentException",
  "constraints": [
    {
      "symExpr": "(pBuffer.length <= this.bufferSize)",
      "truthValue": false
    }
  ],
  "modelValues": {
    "pBuffer.length": "IntValue[value=1]",
    "this.bufferSize": "IntValue[value=0]"
  },
  "throwSiteKind": "DIRECT_ATHROW",
  "propagationProvenance": [
    []
  ]
}
```



#### testPeekSliceRejectsOffsetAtEmptyBufferEnd — source model and fixture assumptions



Positive-size construction creates a non-null, initially empty buffer. Offset 0 is at the end of the empty candidate. Length is unconstrained and chosen as 0.



```json
{
  "artifact": "commons-io-11f0abe7a.jar",
  "pathId": "<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte[],int,int)>#7",
  "resultsPosition": 13749,
  "summariesPosition": 61206,
  "status": "SAT",
  "signature": "<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte[],int,int)>",
  "exceptionType": "java.lang.IllegalArgumentException",
  "constraints": [
    {
      "symExpr": "(pBuffer != null)",
      "truthValue": true
    },
    {
      "symExpr": "(pBuffer.length <= this.bufferSize)",
      "truthValue": true
    },
    {
      "symExpr": "(this.buffer != null)",
      "truthValue": true
    },
    {
      "symExpr": "(this.buffer.getCurrentNumberOfBytes() >= pBuffer.length)",
      "truthValue": true
    },
    {
      "symExpr": "(pOffset < 0)",
      "truthValue": false
    },
    {
      "symExpr": "(pOffset < pBuffer.length)",
      "truthValue": false
    }
  ],
  "modelValues": {
    "pBuffer.length": "IntValue[value=0]",
    "expr_1_int": "IntValue[value=0]",
    "pOffset": "IntValue[value=0]",
    "this.bufferSize": "IntValue[value=0]",
    "this.buffer_is_null": "BoolValue[value=false]",
    "this": "IntValue[value=2]",
    "this.buffer": "IntValue[value=0]",
    "pBuffer": "IntValue[value=0]",
    "pBuffer_is_null": "BoolValue[value=false]",
    "expr_2.getCurrentNumberOfBytes()": "IntValue[value=0]"
  },
  "throwSiteKind": "CALLEE_PROPAGATED",
  "propagationProvenance": [
    [
      "<org.apache.commons.io.input.buffer.CircularByteBuffer: boolean peek(byte[],int,int)>"
    ]
  ]
}
```



#### testPeekSliceRejectsNegativeOffset — source model and fixture assumptions



Positive-size construction creates a non-null, initially empty buffer. The negative offset is unchanged; length is unconstrained and chosen as 0.



```json
{
  "artifact": "commons-io-11f0abe7a.jar",
  "pathId": "<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte[],int,int)>#8",
  "resultsPosition": 13750,
  "summariesPosition": 61207,
  "status": "SAT",
  "signature": "<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte[],int,int)>",
  "exceptionType": "java.lang.IllegalArgumentException",
  "constraints": [
    {
      "symExpr": "(pBuffer != null)",
      "truthValue": true
    },
    {
      "symExpr": "(pBuffer.length <= this.bufferSize)",
      "truthValue": true
    },
    {
      "symExpr": "(this.buffer != null)",
      "truthValue": true
    },
    {
      "symExpr": "(this.buffer.getCurrentNumberOfBytes() >= pBuffer.length)",
      "truthValue": true
    },
    {
      "symExpr": "(pOffset < 0)",
      "truthValue": true
    }
  ],
  "modelValues": {
    "pBuffer.length": "IntValue[value=0]",
    "expr_1_int": "IntValue[value=0]",
    "pOffset": "IntValue[value=-1]",
    "this.bufferSize": "IntValue[value=0]",
    "this.buffer_is_null": "BoolValue[value=false]",
    "this": "IntValue[value=2]",
    "this.buffer": "IntValue[value=0]",
    "pBuffer": "IntValue[value=0]",
    "pBuffer_is_null": "BoolValue[value=false]",
    "expr_2.getCurrentNumberOfBytes()": "IntValue[value=0]"
  },
  "throwSiteKind": "CALLEE_PROPAGATED",
  "propagationProvenance": [
    [
      "<org.apache.commons.io.input.buffer.CircularByteBuffer: boolean peek(byte[],int,int)>"
    ]
  ]
}
```



#### testPeekSliceRejectsNegativeLength — source model and fixture assumptions



Positive-size construction creates a non-null buffer with initial count 0. Modeled scalar values are unchanged.



```json
{
  "artifact": "commons-io-11f0abe7a.jar",
  "pathId": "<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte[],int,int)>#31",
  "resultsPosition": 13773,
  "summariesPosition": 61230,
  "status": "SAT",
  "signature": "<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte[],int,int)>",
  "exceptionType": "java.lang.IllegalArgumentException",
  "constraints": [
    {
      "symExpr": "(pBuffer != null)",
      "truthValue": true
    },
    {
      "symExpr": "(pBuffer.length <= this.bufferSize)",
      "truthValue": true
    },
    {
      "symExpr": "(this.buffer != null)",
      "truthValue": true
    },
    {
      "symExpr": "(this.buffer.getCurrentNumberOfBytes() >= pBuffer.length)",
      "truthValue": false
    },
    {
      "symExpr": "(pOffset < 0)",
      "truthValue": false
    },
    {
      "symExpr": "(pOffset < pBuffer.length)",
      "truthValue": true
    },
    {
      "symExpr": "(pLength < 0)",
      "truthValue": true
    }
  ],
  "modelValues": {
    "pBuffer.length": "IntValue[value=1]",
    "expr_1_int": "IntValue[value=0]",
    "pOffset": "IntValue[value=0]",
    "this.bufferSize": "IntValue[value=1]",
    "this.buffer_is_null": "BoolValue[value=false]",
    "this": "IntValue[value=2]",
    "this.buffer": "IntValue[value=0]",
    "pBuffer": "IntValue[value=0]",
    "pLength": "IntValue[value=-1]",
    "pBuffer_is_null": "BoolValue[value=false]",
    "expr_2.getCurrentNumberOfBytes()": "IntValue[value=0]"
  },
  "throwSiteKind": "CALLEE_PROPAGATED",
  "propagationProvenance": [
    [
      "<org.apache.commons.io.input.buffer.CircularByteBuffer: boolean peek(byte[],int,int)>"
    ]
  ]
}
```



#### testPeekSliceRejectsLengthLargerThanCapacity — source model and fixture assumptions



The constructor creates internal capacity 1 and initial count 0. Substitutions preserve requested length greater than internal capacity while permitting positive-size construction.



```json
{
  "artifact": "commons-io-11f0abe7a.jar",
  "pathId": "<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte[],int,int)>#30",
  "resultsPosition": 13772,
  "summariesPosition": 61229,
  "status": "SAT",
  "signature": "<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte[],int,int)>",
  "exceptionType": "java.lang.IllegalArgumentException",
  "constraints": [
    {
      "symExpr": "(pBuffer != null)",
      "truthValue": true
    },
    {
      "symExpr": "(pBuffer.length <= this.bufferSize)",
      "truthValue": true
    },
    {
      "symExpr": "(this.buffer != null)",
      "truthValue": true
    },
    {
      "symExpr": "(this.buffer.getCurrentNumberOfBytes() >= pBuffer.length)",
      "truthValue": false
    },
    {
      "symExpr": "(pOffset < 0)",
      "truthValue": false
    },
    {
      "symExpr": "(pOffset < pBuffer.length)",
      "truthValue": true
    },
    {
      "symExpr": "(pLength < 0)",
      "truthValue": false
    },
    {
      "symExpr": "(pLength <= this.buffer.buffer.length)",
      "truthValue": false
    }
  ],
  "modelValues": {
    "pBuffer.length": "IntValue[value=1]",
    "this.buffer.buffer.length": "IntValue[value=0]",
    "expr_1_int": "IntValue[value=0]",
    "pOffset": "IntValue[value=0]",
    "this.bufferSize": "IntValue[value=1]",
    "this.buffer_is_null": "BoolValue[value=false]",
    "this": "IntValue[value=2]",
    "this.buffer": "IntValue[value=0]",
    "pBuffer": "IntValue[value=0]",
    "pLength": "IntValue[value=1]",
    "pBuffer_is_null": "BoolValue[value=false]",
    "expr_2.getCurrentNumberOfBytes()": "IntValue[value=0]"
  },
  "throwSiteKind": "CALLEE_PROPAGATED",
  "propagationProvenance": [
    [
      "<org.apache.commons.io.input.buffer.CircularByteBuffer: boolean peek(byte[],int,int)>"
    ]
  ]
}
```



### SAT records without generated public fixtures



| Source path | Results / summaries positions | Reason |
| --- | --- | --- |
| \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\])\>\#10 | 21974 / 54452 | Insufficient fixture support: internal capacity is smaller than the candidate length while receiver capacity admits the candidate. |
| \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\])\>\#23 | 21987 / 54465 | Insufficient fixture support: negative private start offsets and, where applicable, additional symbolic array state are required. |
| \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\])\>\#24 | 21988 / 54466 | Insufficient fixture support: negative private start offsets and, where applicable, additional symbolic array state are required. |
| \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\])\>\#29 | 21993 / 54471 | Insufficient fixture support: a negative internal byte count is required. |
| \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\])\>\#3 | 21967 / 54445 | Insufficient fixture support: a null private internal buffer is required. |
| \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\])\>\#30 | 21994 / 54472 | Insufficient fixture support: internal capacity is smaller than the candidate length while receiver capacity admits the candidate. |
| \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\])\>\#43 | 22007 / 54485 | Insufficient fixture support: negative private start offsets and, where applicable, additional symbolic array state are required. |
| \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\])\>\#44 | 22008 / 54486 | Insufficient fixture support: negative private start offsets and, where applicable, additional symbolic array state are required. |
| \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\],int,int)\>\#10 | 13752 / 61209 | Insufficient fixture support: the populated-buffer condition is not established by the exports. |
| \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\],int,int)\>\#22 | 13764 / 61221 | Insufficient fixture support: negative private start offsets and, where applicable, additional symbolic array state are required. |
| \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\],int,int)\>\#23 | 13765 / 61222 | Insufficient fixture support: negative private start offsets and, where applicable, additional symbolic array state are required. |
| \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\],int,int)\>\#26 | 13768 / 61225 | Insufficient fixture support: private capacity, start offset, byte-count, and matched-content conditions lack supported public setup. |
| \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\],int,int)\>\#27 | 13769 / 61226 | Insufficient fixture support: private capacity, start offset, byte-count, and matched-content conditions lack supported public setup. |
| \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\],int,int)\>\#28 | 13770 / 61227 | Insufficient fixture support: a negative internal byte count is required. |
| \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\],int,int)\>\#29 | 13771 / 61228 | Insufficient fixture support: a negative internal byte count is required. |
| \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\],int,int)\>\#3 | 13745 / 61202 | Insufficient fixture support: a null private internal buffer is required. |
| \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\],int,int)\>\#43 | 13785 / 61242 | Insufficient fixture support: negative private start offsets and, where applicable, additional symbolic array state are required. |
| \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\],int,int)\>\#44 | 13786 / 61243 | Insufficient fixture support: negative private start offsets and, where applicable, additional symbolic array state are required. |
| \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\],int,int)\>\#47 | 13789 / 61246 | Insufficient fixture support: private capacity, start offset, byte-count, and matched-content conditions lack supported public setup. |
| \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\],int,int)\>\#48 | 13790 / 61247 | Insufficient fixture support: private capacity, start offset, byte-count, and matched-content conditions lack supported public setup. |
| \<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte\[\],int,int)\>\#9 | 13751 / 61208 | Insufficient fixture support: a populated buffer and the modeled internal capacity mismatch are required. |



Unrepresented records are not counted as generated tests, reproduced paths, test failures, or covered scenarios. Equivalent exception class names do not make their fixture requirements interchangeable. Exact internal path reproduction is not established for any generated test. Passing assertions establish the observed exception class for each concrete fixture only. The positive-size constructor, initial empty buffer, and capacity mapping assumptions are explicit in the frozen test comments and scenario audit.



## Complete generated Java test code



This is the complete frozen Java source, including the license header, imports, fixture setup, and assertions. The downloadable copy is [PeekableInputStreamTest.java](test-source/PeekableInputStreamTest.java). Each assertThrows lambda invokes only its intended constructor or peek call; setup occurs outside the assertion. No expected message text or unsupported successful-return behavior was added.



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
```



## Exact environment, dependencies, and plugins



Versions were read from the installed tools, the effective POM, resolved dependencies, native logs, and JAR manifests. Runtime installation and Maven cache locations on C: are application state; the checkout, report, copied analysis tools, and temporary analysis files are stored on D:.



| Component | Exact version or value |
| --- | --- |
| Java distribution | Eclipse Temurin OpenJDK 1.8.0\_504 |
| Java runtime | 1.8.0\_504-b01 |
| HotSpot 64-bit VM | 25.504-b01, mixed mode |
| javac | 1.8.0\_504 |
| Maven | 3.9.16; build 2bdd9fddda4b155ebf8000e807eb73fd829a51d5 |
| Project / parent | commons-io:commons-io:2.7-SNAPSHOT / org.apache.commons:commons-parent:50 |
| Compiler source / target | 1.8 / 1.8 |
| Surefire | 2.22.2 |
| JaCoCo runtime agent / CLI | 0.8.4 / 0.8.4 |
| PIT Maven plugin / Gregor engine | 1.15.2 / 1.15.2 |
| PIT JUnit 5 adapter | org.pitest:pitest-junit5-plugin:1.2.2 |
| PIT-added JUnit Platform launcher | 1.5.2 |
| PowerShell | 7.6.5, Core |
| Python, evidence assembly | 3.13.15 |
| Git | 2.56.0.windows.2 |
| Operating system | Windows 11; 10.0.26300.0; AMD64 |
| Locale / JVM platform encoding | en\_US / Cp1252 |
| Maven filtered resources / new report files | iso-8859-1 / UTF-8 |
| Local time zone | America/New\_York; Windows ID Eastern Standard Time; execution offset UTC−04:00 |
| JAVA\_HOME | C:/Users/edyko/AppData/Local/mise/installs/java/temurin-8.0.504+1 |
| Maven home | C:/Users/edyko/AppData/Local/mise/installs/maven/3.9.16/apache-maven-3.9.16 |



### Resolved project libraries



| Maven coordinate | Exact version | Scope |
| --- | --- | --- |
| org.junit.jupiter:junit-jupiter | 5.5.2 | test |
| org.junit.jupiter:junit-jupiter-api | 5.5.2 | test |
| org.apiguardian:apiguardian-api | 1.1.0 | test |
| org.opentest4j:opentest4j | 1.2.0 | test |
| org.junit.platform:junit-platform-commons | 1.5.2 | test |
| org.junit.jupiter:junit-jupiter-params | 5.5.2 | test |
| org.junit.jupiter:junit-jupiter-engine | 5.5.2 | test |
| org.junit.platform:junit-platform-engine | 1.5.2 | test |
| org.junit-pioneer:junit-pioneer | 0.3.0 | test |
| org.mockito:mockito-core | 3.0.0 | test |
| net.bytebuddy:byte-buddy | 1.9.10 | test |
| net.bytebuddy:byte-buddy-agent | 1.9.10 | test |
| org.objenesis:objenesis | 2.6 | test |
| com.google.jimfs:jimfs | 1.1 | test |
| com.google.guava:guava | 18.0 | test |
| org.apache.commons:commons-lang3 | 3.9 | test |



These sixteen resolved JAR entries describe the project's test dependency graph. PIT's JUnit Platform launcher is an additional analysis runtime component. The external PIT project retains the same five direct test dependencies and their versions. The actual Surefire JAR paths are archived in [surefire-classpath.json](toolchain/surefire-classpath.json).



```text
commons-io:commons-io:jar:2.7-SNAPSHOT
+- org.junit.jupiter:junit-jupiter:jar:5.5.2:test
|  +- org.junit.jupiter:junit-jupiter-api:jar:5.5.2:test
|  |  +- org.apiguardian:apiguardian-api:jar:1.1.0:test
|  |  +- org.opentest4j:opentest4j:jar:1.2.0:test
|  |  \- org.junit.platform:junit-platform-commons:jar:1.5.2:test
|  +- org.junit.jupiter:junit-jupiter-params:jar:5.5.2:test
|  \- org.junit.jupiter:junit-jupiter-engine:jar:5.5.2:test
|     \- org.junit.platform:junit-platform-engine:jar:1.5.2:test
+- org.junit-pioneer:junit-pioneer:jar:0.3.0:test
+- org.mockito:mockito-core:jar:3.0.0:test
|  +- net.bytebuddy:byte-buddy:jar:1.9.10:test
|  +- net.bytebuddy:byte-buddy-agent:jar:1.9.10:test
|  \- org.objenesis:objenesis:jar:2.6:test
+- com.google.jimfs:jimfs:jar:1.1:test
|  \- com.google.guava:guava:jar:18.0:test
\- org.apache.commons:commons-lang3:jar:3.9:test
```



### Maven build plugin inventory



| Build plugin | Effective version | Observed status |
| --- | --- | --- |
| org.apache.maven.plugins:maven-remote-resources-plugin | 1.5 | Executed in final clean test |
| org.apache.maven.plugins:maven-assembly-plugin | 3.2.0 | Declared; no execution claimed |
| org.apache.maven.plugins:maven-antrun-plugin | 1.8 | Executed in final clean test |
| org.apache.maven.plugins:maven-compiler-plugin | 3.8.1 | Executed in final clean test |
| org.apache.maven.plugins:maven-enforcer-plugin | 3.0.0-M2 | Executed in final clean test |
| org.apache.maven.plugins:maven-site-plugin | 3.8.2 | Declared; no execution claimed |
| org.apache.maven.plugins:maven-jar-plugin | 3.2.0 | Declared; no execution claimed |
| org.apache.maven.plugins:maven-source-plugin | 3.2.0 | Declared; no execution claimed |
| org.apache.maven.plugins:maven-surefire-plugin | 2.22.2 | Executed in final clean test |
| org.apache.commons:commons-build-plugin | 1.11 | Declared; no execution claimed |
| org.apache.felix:maven-bundle-plugin | 4.2.1 | Executed in final clean test |
| org.apache.rat:apache-rat-plugin | 0.13 | Executed in final clean test |
| org.apache.maven.plugins:maven-checkstyle-plugin | 3.1.0 | Declared; no execution claimed |
| org.apache.maven.plugins:maven-scm-publish-plugin | 3.0.0 | Declared; no execution claimed |
| org.codehaus.mojo:build-helper-maven-plugin | 3.0.0 | Executed in final clean test |
| org.codehaus.mojo:animal-sniffer-maven-plugin | 1.18 | Executed in final clean test |
| org.codehaus.mojo:buildnumber-maven-plugin | 1.4 | Executed in final clean test |
| org.apache.maven.plugins:maven-clean-plugin | 3.1.0 | Executed in final clean test |
| org.apache.maven.plugins:maven-resources-plugin | 3.1.0 | Executed in final clean test |
| org.apache.maven.plugins:maven-install-plugin | 2.5.2 | Declared; no execution claimed |
| org.apache.maven.plugins:maven-deploy-plugin | 2.8.2 | Declared; no execution claimed |



The metadata and tool-download commands additionally use maven-help-plugin 3.4.0 and maven-dependency-plugin 3.6.1. Animal Sniffer checked org.codehaus.mojo.signature:java18:1.0. The effective POM preserves inherited configuration and plugin-management details beyond the directly listed build plugins.



The complete resolved PIT Maven-plugin dependency inventory is [pit-plugin-dependencies.txt](toolchain/pit-plugin-dependencies.txt). It includes tooling dependencies such as Commons IO 2.6, Commons Lang 3.12.0, Commons Text 1.10.0, Jackson 2.13.3, Maven libraries 3.8.6, and Surefire libraries 3.0.0-M7. These are analysis-plugin dependencies; they do not change the tested local Commons IO 2.7-SNAPSHOT class, the installed Maven 3.9.16, or the project's libraries above.



### Analysis JAR identity



| Coordinate | Manifest version fields | SHA-256 |
| --- | --- | --- |
| org.jacoco:org.jacoco.agent:0.8.4:runtime | \{"Implementation-Version": "0.8.4"\} | 1a7c1dc7280e535b9b6f383915bac5afbb9208c1af2019b4e674ca590c925c22 |
| org.jacoco:org.jacoco.cli:0.8.4:nodeps | \{"Implementation-Version": "0.8.4"\} | 65de07ff32bcf2f945f18180d1d10cdf0e155eee2b508519bbc5f31904cd8288 |
| org.pitest:pitest-maven:1.15.2 | \{\} | 18674572d7c5e1e30561d941fd69e73d1b3ed18c7d43e215b612b505b618e81c |
| org.pitest:pitest:1.15.2 | \{"Implementation-Version": "1.15.2"\} | 29befcf6733680375aff5089ad02dab9166aa18760f82fc085adb6c4959362b6 |
| org.pitest:pitest-junit5-plugin:1.2.2 | \{"Implementation-Version": "1.2.2"\} | 2dbf5bbbc714ff702eb2e82c047a5b44a74c47cc9171c3a7a8dc78783bf099b9 |
| org.junit.platform:junit-platform-launcher:1.5.2 | \{"Specification-Version": "1.5.2", "Implementation-Version": "1.5.2"\} | c1f6473ddd343550b42e94072aff9417ff38398f8b6bafe27b785aebcdaa660b |



[Raw tool-version output](toolchain/versions.txt) · [Effective POM](toolchain/effective-pom.xml) · [Analysis JAR manifest data](toolchain/analysis-artifacts.json)



## Executed commands and analysis configuration



All project Maven commands ran from D:/Projects/wit-up/commons-io. The original suite command is reproduced exactly below. JDK selection, argLine initialization, and temporary directories were process environment adjustments; no persistent Maven or checkout configuration was changed.



```powershell
mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" "-Dtest=org.apache.commons.io.input.buffer.PeekableInputStreamTest" clean test
```



### Process environment for the authorized plain JDK 8 run



```powershell
$env:JAVA_HOME = 'C:\Users\edyko\AppData\Local\mise\installs\java\temurin-8.0.504+1'
$env:Path = "$env:JAVA_HOME\bin;$env:Path"
$env:TEMP = 'D:\Projects\wit-up\commons-io-validation\temporary'
$env:TMP = $env:TEMP
$env:MAVEN_OPTS = '-DargLine='
mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" "-Dtest=org.apache.commons.io.input.buffer.PeekableInputStreamTest" clean test
```



The plain run initializes the otherwise unresolved $\{argLine\} property. The project's existing Surefire -Xmx25M argument remains in effect. For JaCoCo, the same process property supplies the agent instead of an empty value. The original profile-deactivation argument is retained; the standalone agent and CLI produce the requested JaCoCo evidence.



### Before: measured baseline



The frozen file was moved to the external test-source snapshot after verifying its SHA-256. A try/finally block restored it with Copy-Item and checked the same hash, even when the exploratory full-project PIT attempt failed. The successful targeted PIT before run occurred afterward, before any rebuild could recreate the generated compiled class. The initial record remains archived separately.



```powershell
Move-Item -LiteralPath 'D:\Projects\wit-up\commons-io\src\test\java\org\apache\commons\io\input\buffer\PeekableInputStreamTest.java' -Destination 'D:\Projects\wit-up\commons-io-validation\peekable-input-stream\test-source\PeekableInputStreamTest.java'
$env:MAVEN_OPTS = '-DargLine=-javaagent:D:/Projects/wit-up/commons-io-validation/peekable-input-stream/tools/org.jacoco.agent-0.8.4-runtime.jar=destfile=D:/Projects/wit-up/commons-io-validation/peekable-input-stream/jacoco/before/jacoco.exec,append=true,includes=org.apache.commons.io.input.buffer.PeekableInputStream'
mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" clean test
java -jar 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/tools/org.jacoco.cli-0.8.4-nodeps.jar' report 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/jacoco/before/jacoco.exec' --classfiles 'D:/Projects/wit-up/commons-io/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class' --html 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/jacoco/before/html' --xml 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/jacoco/before/jacoco.xml' --csv 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/jacoco/before/jacoco.csv' --name 'PeekableInputStream baseline without generated tests'
# Executed in finally; restore the source without recreating its compiled class.
Copy-Item -LiteralPath 'D:\Projects\wit-up\commons-io-validation\peekable-input-stream\test-source\PeekableInputStreamTest.java' -Destination 'D:\Projects\wit-up\commons-io\src\test\java\org\apache\commons\io\input\buffer\PeekableInputStreamTest.java'
$env:MAVEN_OPTS = '-DargLine='
mvn -B -ntp -f "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/pit/pit-baseline-pom.xml" org.pitest:pitest-maven:1.15.2:mutationCoverage
```



The before agent used append=true with a newly created execution file to collect existing-suite forks. The archived baseline reports verify that the generated compiled test class was absent. The move shown above describes the recorded execution; the snapshot already exists now, so this historical sequence should not be run unchanged over the archived evidence.



### After: final frozen-suite measurements



```powershell
$env:MAVEN_OPTS = '-DargLine=-javaagent:D:/Projects/wit-up/commons-io-validation/peekable-input-stream/tools/org.jacoco.agent-0.8.4-runtime.jar=destfile=D:/Projects/wit-up/commons-io-validation/peekable-input-stream/jacoco/after/jacoco.exec,append=false,includes=org.apache.commons.io.input.buffer.PeekableInputStream'
mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" "-Dtest=org.apache.commons.io.input.buffer.PeekableInputStreamTest" clean test
java -jar 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/tools/org.jacoco.cli-0.8.4-nodeps.jar' report 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/jacoco/after/jacoco.exec' --classfiles 'D:/Projects/wit-up/commons-io/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class' --html 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/jacoco/after/html' --xml 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/jacoco/after/jacoco.xml' --csv 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/jacoco/after/jacoco.csv' --name 'PeekableInputStream exception tests'
$env:MAVEN_OPTS = '-DargLine='
mvn -B -ntp -f "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/pit/pit-analysis-pom.xml" org.pitest:pitest-maven:1.15.2:mutationCoverage
```



JaCoCo's includes filter and CLI classfile input select only the target class. No sourcefiles argument was supplied. Each Maven test, CLI report, and final targeted PIT command exited 0. Raw stdout and stderr are archived in the corresponding maven.log and report.log files.



### PIT configuration used in both final phases



The external POM reads the existing checkout target/classes and target/test-classes and uses empty external source roots. It pins DEFAULTS mutators, one thread, Gregor, HTML/XML output, exportLineCoverage=true, timestampedReports=false, failWhenNoMutations=true, the original projectBase, -Xmx256m, and the D: temporary directory. Both configurations differ only in reportsDirectory. No mutation threshold or baseline-validation guard was weakened.



```xml
<?xml version='1.0' encoding='utf-8'?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>org.apache.commons.io.analysis</groupId>
  <artifactId>peekable-input-stream-analysis</artifactId>
  <version>1.0</version>
  <name>PeekableInputStream Mutation Analysis</name>
  <description>External analysis of unchanged compiled classes using the frozen generated test suite.</description>
  <properties>
    <maven.compiler.source>1.8</maven.compiler.source>
    <maven.compiler.target>1.8</maven.compiler.target>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>
  <dependencies>
    <dependency>
      <groupId>org.junit.jupiter</groupId>
      <artifactId>junit-jupiter</artifactId>
      <version>5.5.2</version>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>org.junit-pioneer</groupId>
      <artifactId>junit-pioneer</artifactId>
      <version>0.3.0</version>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>org.mockito</groupId>
      <artifactId>mockito-core</artifactId>
      <version>3.0.0</version>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>com.google.jimfs</groupId>
      <artifactId>jimfs</artifactId>
      <version>1.1</version>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>org.apache.commons</groupId>
      <artifactId>commons-lang3</artifactId>
      <version>3.9</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
  <build>
    <directory>D:/Projects/wit-up/commons-io-validation/peekable-input-stream/pit/build</directory>
    
    <sourceDirectory>D:/Projects/wit-up/commons-io-validation/peekable-input-stream/pit/sources</sourceDirectory>
    <testSourceDirectory>D:/Projects/wit-up/commons-io-validation/peekable-input-stream/pit/test-sources</testSourceDirectory>
    <outputDirectory>D:/Projects/wit-up/commons-io/target/classes</outputDirectory>
    <testOutputDirectory>D:/Projects/wit-up/commons-io/target/test-classes</testOutputDirectory>
    <plugins>
      <plugin>
        <groupId>org.pitest</groupId>
        <artifactId>pitest-maven</artifactId>
        <version>1.15.2</version>
        <dependencies>
          <dependency>
            <groupId>org.pitest</groupId>
            <artifactId>pitest-junit5-plugin</artifactId>
            <version>1.2.2</version>
          </dependency>
        </dependencies>
        <configuration>
          <targetClasses><param>org.apache.commons.io.input.buffer.PeekableInputStream</param></targetClasses>
          <targetTests><param>org.apache.commons.io.input.buffer.PeekableInputStreamTest</param></targetTests>
          <mutators><mutator>DEFAULTS</mutator></mutators>
          <threads>1</threads>
          <outputFormats><param>HTML</param><param>XML</param></outputFormats>
          <reportsDirectory>D:/Projects/wit-up/commons-io-validation/peekable-input-stream/pit/after</reportsDirectory>
          <timestampedReports>false</timestampedReports>
          <exportLineCoverage>true</exportLineCoverage>
          <failWhenNoMutations>true</failWhenNoMutations>
          <jvmArgs>
            <jvmArg>-Xmx256m</jvmArg>
            <jvmArg>-Djava.io.tmpdir=D:/Projects/wit-up/commons-io-validation/temporary</jvmArg>
          </jvmArgs>
        <projectBase>D:/Projects/wit-up/commons-io</projectBase></configuration>
      </plugin>
    </plugins>
  </build>
</project>
```



### Metadata, dependency, and tool retrieval commands



```powershell
mvn -B -ntp "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" org.apache.maven.plugins:maven-help-plugin:3.4.0:effective-pom "-Doutput=D:/Projects/wit-up/commons-io-validation/peekable-input-stream/toolchain/effective-pom.xml"

mvn -B -ntp "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" org.apache.maven.plugins:maven-dependency-plugin:3.6.1:copy "-Dartifact=org.jacoco:org.jacoco.agent:0.8.4:jar:runtime" "-DoutputDirectory=D:/Projects/wit-up/commons-io-validation/peekable-input-stream/tools"

mvn -B -ntp "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" org.apache.maven.plugins:maven-dependency-plugin:3.6.1:copy "-Dartifact=org.jacoco:org.jacoco.cli:0.8.4:jar:nodeps" "-DoutputDirectory=D:/Projects/wit-up/commons-io-validation/peekable-input-stream/tools"

mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" org.apache.maven.plugins:maven-dependency-plugin:3.6.1:tree "-DoutputFile=D:/Projects/wit-up/commons-io-validation/peekable-input-stream/toolchain/dependency-tree.txt" "-DoutputType=text"

mvn -B -ntp -f "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/pit/pit-analysis-pom.xml" org.apache.maven.plugins:maven-dependency-plugin:3.6.1:tree "-DoutputFile=D:/Projects/wit-up/commons-io-validation/peekable-input-stream/toolchain/pit-project-dependency-tree.txt" "-DoutputType=text"

mvn -B -ntp -f "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/pit/pit-analysis-pom.xml" org.apache.maven.plugins:maven-dependency-plugin:3.6.1:resolve-plugins "-DincludeArtifactIds=pitest-maven" "-DoutputFile=D:/Projects/wit-up/commons-io-validation/peekable-input-stream/toolchain/pit-plugin-dependencies.txt"

java -version
javac -version
mvn -version
python --version
git --version

git rev-parse HEAD
git diff --quiet 11f0abe7a3fb6954b2985ca4ab0697b2fb489e84 --
git status --short
Get-FileHash -Algorithm SHA256 -LiteralPath 'D:\Projects\wit-up\commons-io\src\test\java\org\apache\commons\io\input\buffer\PeekableInputStreamTest.java'

```



## Coverage and mutation detail



### JaCoCo method-level after counters



| Method descriptor | Instructions | Lines | Branches | Methods |
| --- | --- | --- | --- | --- |
| \<init\>(Ljava/io/InputStream;I)V | 5/5 (100.00%) | 2/2 (100.00%) | N/A | 1/1 (100.00%) |
| \<init\>(Ljava/io/InputStream;)V | 0/4 (0.00%) | 0/2 (0.00%) | N/A | 0/1 (0.00%) |
| peek(\[B)Z | 35/45 (77.78%) | 4/6 (66.67%) | 3/4 (75.00%) | 1/1 (100.00%) |
| peek(\[BII)Z | 37/44 (84.09%) | 5/6 (83.33%) | 4/4 (100.00%) | 1/1 (100.00%) |



The one-argument InputStream constructor appears in compiled-class coverage metadata and remains unexecuted. The selected WIT-UP exports did not supply a scenario oracle for that signature, so no additional test was invented for it.



### Actually emitted PIT mutators



| Mutator | Generated | Killed | Survived | No coverage |
| --- | --- | --- | --- | --- |
| org.pitest.mutationtest.engine.gregor.mutators.ConditionalsBoundaryMutator | 4 | 0 | 4 | 0 |
| org.pitest.mutationtest.engine.gregor.mutators.RemoveConditionalMutator\_ORDER\_ELSE | 4 | 1 | 3 | 0 |
| org.pitest.mutationtest.engine.gregor.mutators.VoidMethodCallMutator | 2 | 0 | 1 | 1 |
| org.pitest.mutationtest.engine.gregor.mutators.returns.BooleanFalseReturnValsMutator | 2 | 0 | 0 | 2 |
| org.pitest.mutationtest.engine.gregor.mutators.returns.BooleanTrueReturnValsMutator | 2 | 0 | 0 | 2 |



### All fourteen after mutant outcomes



| Method / descriptor | Line | Mutator | Indexes / blocks | Status | Killing test |
| --- | --- | --- | --- | --- | --- |
| peek(\[B)Z | 63 | org.pitest.mutationtest.engine.gregor.mutators.ConditionalsBoundaryMutator | 13/1 | SURVIVED | None |
| peek(\[B)Z | 67 | org.pitest.mutationtest.engine.gregor.mutators.ConditionalsBoundaryMutator | 44/12 | SURVIVED | None |
| peek(\[B)Z | 63 | org.pitest.mutationtest.engine.gregor.mutators.RemoveConditionalMutator\_ORDER\_ELSE | 13/1 | SURVIVED | None |
| peek(\[B)Z | 67 | org.pitest.mutationtest.engine.gregor.mutators.RemoveConditionalMutator\_ORDER\_ELSE | 44/12 | SURVIVED | None |
| peek(\[B)Z | 68 | org.pitest.mutationtest.engine.gregor.mutators.VoidMethodCallMutator | 48/13 | NO\_COVERAGE | None |
| peek(\[B)Z | 70 | org.pitest.mutationtest.engine.gregor.mutators.returns.BooleanFalseReturnValsMutator | 59/15 | NO\_COVERAGE | None |
| peek(\[B)Z | 70 | org.pitest.mutationtest.engine.gregor.mutators.returns.BooleanTrueReturnValsMutator | 59/15 | NO\_COVERAGE | None |
| peek(\[BII)Z | 85 | org.pitest.mutationtest.engine.gregor.mutators.ConditionalsBoundaryMutator | 13/1 | SURVIVED | None |
| peek(\[BII)Z | 89 | org.pitest.mutationtest.engine.gregor.mutators.ConditionalsBoundaryMutator | 44/12 | SURVIVED | None |
| peek(\[BII)Z | 85 | org.pitest.mutationtest.engine.gregor.mutators.RemoveConditionalMutator\_ORDER\_ELSE | 13/1 | KILLED | org.apache.commons.io.input.buffer.PeekableInputStreamTest.\[engine:junit-jupiter\]/\[class:org.apache.commons.io.input.buffer.PeekableInputStreamTest\]/\[method:testPeekSliceRejectsBufferLargerThanCapacity()\] |
| peek(\[BII)Z | 89 | org.pitest.mutationtest.engine.gregor.mutators.RemoveConditionalMutator\_ORDER\_ELSE | 44/12 | SURVIVED | None |
| peek(\[BII)Z | 90 | org.pitest.mutationtest.engine.gregor.mutators.VoidMethodCallMutator | 48/13 | SURVIVED | None |
| peek(\[BII)Z | 92 | org.pitest.mutationtest.engine.gregor.mutators.returns.BooleanFalseReturnValsMutator | 58/15 | NO\_COVERAGE | None |
| peek(\[BII)Z | 92 | org.pitest.mutationtest.engine.gregor.mutators.returns.BooleanTrueReturnValsMutator | 58/15 | NO\_COVERAGE | None |



The killed mutant is associated with testPeekSliceRejectsBufferLargerThanCapacity. Eight mutants survived despite test coverage and five were not covered. This establishes limited mutation detection for the generated exception suite. It does not establish the cause or equivalence of surviving mutants, exact symbolic path coverage, overall API correctness, or analyzed-JAR equivalence.



## Native reports and reproducibility evidence



| Evidence | Before | After |
| --- | --- | --- |
| JaCoCo XML | [XML before](jacoco/before/jacoco.xml) | [XML after](jacoco/after/jacoco.xml) |
| JaCoCo execution data | [Execution data before](jacoco/before/jacoco.exec) | [Execution data after](jacoco/after/jacoco.exec) |
| Maven test logs | [Baseline suite log](jacoco/before/maven.log) | [Generated suite log](jacoco/after/maven.log) |
| JaCoCo CLI report logs | [Report log before](jacoco/before/report.log) | [Report log after](jacoco/after/report.log) |
| PIT mutation XML | [Mutations before](pit/before/mutations.xml) | [Mutations after](pit/after/mutations.xml) |
| PIT block-to-test coverage XML | [Coverage before](pit/before/linecoverage.xml) | [Coverage after](pit/after/linecoverage.xml) |
| PIT Maven logs | [PIT log before](pit/before/maven.log) | [PIT log after](pit/after/maven.log) |
| External PIT POM | [Configuration before](pit/pit-baseline-pom.xml) | [Configuration after](pit/pit-analysis-pom.xml) |
| Surefire evidence | [Existing-suite totals](jacoco/before/suite-result.json); [all 136 native XML reports](jacoco/before/surefire-reports.zip) | [Generated-suite native XML](jacoco/after/TEST-org.apache.commons.io.input.buffer.PeekableInputStreamTest.xml) |



Additional evidence: [Authorized plain-run record](result.json) · [Plain-run Maven log](maven-jdk8.log) · [Plain-run Surefire XML](TEST-org.apache.commons.io.input.buffer.PeekableInputStreamTest.xml) · [Consolidated raw-count measurements](measurements.json) · [Complete scenario audit](test-scenarios.json) · [Artifact SHA-256 inventory](artifact-manifest.json) · [Separate execution diagnostics](execution-diagnostics.md).



The plain-run result.json is an immutable record of that earlier successful execution. Its checksNotPerformed list describes that run only. The later coverage and mutation results are recorded in measurements.json and the native report directories above. Hashes establish file identity, not scenario truth, specification correctness, or test adequacy.

The retained evidence consists of the frozen Java test, scenario audit, exact toolchain metadata, native XML reports, JaCoCo execution data, analysis configuration, and raw execution logs. The 136 existing-suite XML reports are compressed without content changes in surefire-reports.zip; their totals were checked against suite-result.json. Rendered HTML assets, duplicate CSV and text summaries, downloaded analysis JARs, successful metadata-retrieval logs, the report assembly script, and temporary files were moved to local storage at `D:/Projects/validation-archive/commons-io-regenerable-output`, outside this repository. The execution commands above retain their original output paths; those commands can recreate presentation files and retrieve the analysis JARs when needed. Pipeline diagnostics remain separate from generated-suite outcome counts.



Report assembled directly from archived measurements. All generated report prose and artifacts use United States English. Existing diagnostics and external method signatures retain their original exact values.
