# `<org.apache.commons.io.IOCase: int checkIndexOf(java.lang.String,int,java.lang.String)>#0`

[Documentation index](../README.md) | [Case findings](../findings/case-assessment.md) | [Assessment rubric](../methodology/case-assessment.md)

## Record identity and selection

| Property | Value |
| --- | --- |
| Artifact | `commons-io-11f0abe7a.jar` |
| Initial stratum | `simple_signature_hypothesis` |
| Selection order | 9 |
| Novel dimensions when selected | class, parameters |
| Result locator | `witup-results-commons-io-11f0abe7a.json`, array record 74842 |
| Summary locator | `witup-summaries-commons-io-11f0abe7a.json`, array record 10754 |

Array record numbers are 1-based. The artifact/pathId pair is the semantic locator. Input byte identities are recorded in `data/processed/case-inventory.json`. The source records below preserve parsed values; whitespace and object-key ordering are not byte-for-byte copies.

## Explicit exported information

| Property | Exported value |
| --- | --- |
| Parameter types | `java.lang.String,int,java.lang.String` |
| Reported exception | `java.lang.NullPointerException` |
| Reported origin | `IMPLICIT` |
| Summary / result verdict | SAT / SAT |
| Condition entries | 1 |
| Model entries | 2 |

### Original parsed result

```json
{
  "artifact": "commons-io-11f0abe7a.jar",
  "package": "org.apache.commons.io",
  "class": "IOCase",
  "method": "checkIndexOf",
  "returnType": "int",
  "params": "java.lang.String,int,java.lang.String",
  "pathIndex": 0,
  "pathId": "<org.apache.commons.io.IOCase: int checkIndexOf(java.lang.String,int,java.lang.String)>#0",
  "status": "SAT",
  "modelValues": {
    "str": "StringValue[value=]",
    "str_is_null": "BoolValue[value=true]"
  }
}
```

### Original parsed summary

```json
{
  "artifact": "commons-io-11f0abe7a.jar",
  "package": "org.apache.commons.io",
  "class": "IOCase",
  "method": "checkIndexOf",
  "returnType": "int",
  "params": "java.lang.String,int,java.lang.String",
  "pathIndex": 0,
  "pathId": "<org.apache.commons.io.IOCase: int checkIndexOf(java.lang.String,int,java.lang.String)>#0",
  "exceptionType": "java.lang.NullPointerException",
  "throwSiteKind": "IMPLICIT",
  "provenance": [],
  "provenances": [
    []
  ],
  "solverStatus": "SAT",
  "constraints": [
    {
      "symExpr": "(str == null)",
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
| str | `(str == null)` | True | True | True |

- The null flag for str requires null even though its serialized StringValue contains text; use both pieces of information together.

## Information gaps retained for later work

- `formal_parameter_names_and_symbol_bindings_not_exported`
- `multi_parameter_assignment_not_verified`
- `static_or_instance_invocation_not_exported`
- `receiver_or_static_setup_not_determined`
- `accessibility_not_exported`
- `runtime_exception_site_not_verified`
- `public_contract_oracle_not_supplied`

These gaps concern exported information. They are not findings about correctness, accessibility, or runtime behavior of the Java implementation. No Java source was inspected for this case.
