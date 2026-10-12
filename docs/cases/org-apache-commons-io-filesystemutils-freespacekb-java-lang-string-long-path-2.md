# `<org.apache.commons.io.FileSystemUtils: long freeSpaceKb(java.lang.String,long)>#2`

[Documentation index](../README.md) | [Case findings](../findings/case-assessment.md) | [Assessment rubric](../methodology/case-assessment.md)

## Record identity and selection

| Property | Value |
| --- | --- |
| Artifact | `commons-io-11f0abe7a.jar` |
| Initial stratum | `simple_signature_hypothesis` |
| Selection order | 6 |
| Novel dimensions when selected | class, exception, parameters |
| Result locator | `witup-results-commons-io-11f0abe7a.json`, array record 16402 |
| Summary locator | `witup-summaries-commons-io-11f0abe7a.json`, array record 57346 |

Array record numbers are 1-based. The artifact/pathId pair is the semantic locator. Input byte identities are recorded in `data/processed/case-inventory.json`. The source records below preserve parsed values; whitespace and object-key ordering are not byte-for-byte copies.

## Explicit exported information

| Property | Exported value |
| --- | --- |
| Parameter types | `java.lang.String,long` |
| Reported exception | `java.lang.IllegalStateException` |
| Reported origin | `CALLEE_PROPAGATED` |
| Summary / result verdict | SAT / SAT |
| Condition entries | 1 |
| Model entries | 2 |

### Original parsed result

```json
{
  "artifact": "commons-io-11f0abe7a.jar",
  "package": "org.apache.commons.io",
  "class": "FileSystemUtils",
  "method": "freeSpaceKb",
  "returnType": "long",
  "params": "java.lang.String,long",
  "pathIndex": 2,
  "pathId": "<org.apache.commons.io.FileSystemUtils: long freeSpaceKb(java.lang.String,long)>#2",
  "status": "SAT",
  "modelValues": {
    "path": "StringValue[value=]",
    "path_is_null": "BoolValue[value=false]"
  }
}
```

### Original parsed summary

```json
{
  "artifact": "commons-io-11f0abe7a.jar",
  "package": "org.apache.commons.io",
  "class": "FileSystemUtils",
  "method": "freeSpaceKb",
  "returnType": "long",
  "params": "java.lang.String,long",
  "pathIndex": 2,
  "pathId": "<org.apache.commons.io.FileSystemUtils: long freeSpaceKb(java.lang.String,long)>#2",
  "exceptionType": "java.lang.IllegalStateException",
  "throwSiteKind": "CALLEE_PROPAGATED",
  "provenance": [
    "<org.apache.commons.io.FileSystemUtils: long freeSpaceOS(java.lang.String,int,boolean,long)>"
  ],
  "provenances": [
    [
      "<org.apache.commons.io.FileSystemUtils: long freeSpaceOS(java.lang.String,int,boolean,long)>"
    ]
  ],
  "solverStatus": "SAT",
  "constraints": [
    {
      "symExpr": "(path != null)",
      "truthValue": true
    }
  ]
}
```

## Rule-derived interpretation

| Dimension | Assessment |
| --- | --- |
| Argument assignment | multiple_argument_assignment_hypothesis |
| Initial classification review | initial_tier_retained_with_setup_gaps |
| Execution readiness | not_established_from_exports |

Argument assignments are hypotheses; the export does not supply a complete Java invocation or an independently verified test oracle.

### Nullness conditions

| Symbol | Expression | truthValue | Required null | Model agrees |
| --- | --- | --- | --- | --- |
| path | `(path != null)` | True | False | True |

## Information gaps retained for later work

- `formal_parameter_names_and_symbol_bindings_not_exported`
- `multi_parameter_assignment_not_verified`
- `static_or_instance_invocation_not_exported`
- `receiver_or_static_setup_not_determined`
- `accessibility_not_exported`
- `runtime_exception_site_not_verified`
- `public_contract_oracle_not_supplied`
- `propagated_call_context_not_reconstructed`

These gaps concern exported information. They are not findings about correctness, accessibility, or runtime behavior of the Java implementation. No Java source was inspected for this case.
