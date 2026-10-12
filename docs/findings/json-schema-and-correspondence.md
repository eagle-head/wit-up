# 1. What fields exist, and how do the files relate?

[Documentation index](../README.md) | [JSON analysis overview](../commons-io-json-analysis.md)

Both inputs are arrays of objects. The tables below describe the fields observed across the complete files. Presence and missing counts are measured; meanings are interpretations informed by the exporter source cited below.

### results schema

| Field | Observed Python types | Present | Missing | Meaning |
| --- | --- | --- | --- | --- |
| `artifact` | str | 88,303 | 0 | External artifact label; the filename alone does not verify JAR contents. |
| `package` | str | 88,303 | 0 | Declaring package label. |
| `class` | str | 88,303 | 0 | Declaring class label. |
| `method` | str | 88,303 | 0 | Method name; `<init>` denotes a constructor. |
| `returnType` | str | 88,303 | 0 | Declared return type in the exported signature. |
| `params` | str | 88,303 | 0 | Comma-separated parameter types; parameter names are not supplied here. |
| `pathIndex` | int | 88,303 | 0 | Index within the exported method's observable path list. |
| `pathId` | str | 88,303 | 0 | Full method signature followed by # and pathIndex. |
| `status` | str | 88,303 | 0 | Solver verdict for a result row. |
| `modelValues` | dict | 88,303 | 0 | Symbol names mapped to serialized solver values, not ready-made Java fixtures. |

Schema issue count: **0**. Path/index disagreement count: **0**. Path/signature metadata disagreement count: **0**.

### summaries schema

| Field | Observed Python types | Present | Missing | Meaning |
| --- | --- | --- | --- | --- |
| `artifact` | str | 72,419 | 0 | External artifact label; the filename alone does not verify JAR contents. |
| `package` | str | 72,419 | 0 | Declaring package label. |
| `class` | str | 72,419 | 0 | Declaring class label. |
| `method` | str | 72,419 | 0 | Method name; `<init>` denotes a constructor. |
| `returnType` | str | 72,419 | 0 | Declared return type in the exported signature. |
| `params` | str | 72,419 | 0 | Comma-separated parameter types; parameter names are not supplied here. |
| `pathIndex` | int | 72,419 | 0 | Index within the exported method's observable path list. |
| `pathId` | str | 72,419 | 0 | Full method signature followed by # and pathIndex. |
| `exceptionType` | str, NoneType | 72,419 | 0 | Exception associated with the modeled path; a later test must confirm it. |
| `throwSiteKind` | str | 72,419 | 0 | Reported origin category: direct throw, implicit exception, propagated callee exception, or rethrow. |
| `provenance` | list | 72,419 | 0 | Representative call chain recorded for the flow. |
| `provenances` | list | 72,419 | 0 | Call-chain alternatives grouped into the summary row. |
| `solverStatus` | str | 72,419 | 0 | Solver verdict attached to the summary row. |
| `constraints` | list | 72,419 | 0 | Conjunction of symbolic expressions evaluated with their truthValue flags. |

Schema issue count: **0**. Path/index disagreement count: **0**. Path/signature metadata disagreement count: **0**.

### Join inventory

`exceptionType` is present in every summary, but **161** values are JSON null. This is retained as an unknown exception, not converted into an exception name or discarded. Structural validation permits this observed nullable field; the candidate inventory records its missing assertion information separately.

Use **(artifact, pathId)** as the cross-file key. The full signature includes the parameter types, so overloaded methods retain separate identities. Uniqueness is checked before the join. The relation is checked for matching statuses and signature metadata.

| Observation | Count |
| --- | --- |
| Duplicate result keys | 0 |
| Duplicate summary keys | 0 |
| Summary rows with a result | 72,419 |
| Summary rows without a result | 0 |
| Result rows without a summary | 15,884 |
| Matched status disagreements | 0 |
| Matched metadata disagreements | 0 |
| Method signatures found only in results | 0 |
| Method signatures found only in summaries | 0 |

Matched verdicts:

| Summary status | Result status | Rows |
| --- | --- | --- |
| UNSAT | UNSAT | 56,197 |
| SAT | SAT | 16,166 |
| MAYBE | MAYBE | 56 |

Statuses among result rows without a summary:

| Result status | Rows |
| --- | --- |
| UNSAT | 11,250 |
| SAT | 4,634 |

The inspected exporter produces a result per solved path and groups summary flows by (exceptionType, throwSiteKind, constraints), keeping the first path identifier and collecting provenance alternatives. This explains why equal row counts should not be assumed. The unmatched-result count is observed; attributing every unmatched row to grouping remains an interpretation because the producing WIT-UP revision and full path list are unavailable.
