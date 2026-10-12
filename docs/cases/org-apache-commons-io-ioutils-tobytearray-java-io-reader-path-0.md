# `<org.apache.commons.io.IOUtils: byte[] toByteArray(java.io.Reader)>#0`

[Documentation index](../README.md) | [Case findings](../findings/case-assessment.md) | [Assessment rubric](../methodology/case-assessment.md)

## Record identity and selection

| Property | Value |
| --- | --- |
| Artifact | `commons-io-11f0abe7a.jar` |
| Initial stratum | `null_argument_hypothesis` |
| Selection order | 14 |
| Novel dimensions when selected | class, parameters |
| Result locator | `witup-results-commons-io-11f0abe7a.json`, array record 45767 |
| Summary locator | `witup-summaries-commons-io-11f0abe7a.json`, array record 35647 |

Array record numbers are 1-based. The artifact/pathId pair is the semantic locator. Input byte identities are recorded in `data/processed/case-inventory.json`. The source records below preserve parsed values; whitespace and object-key ordering are not byte-for-byte copies.

## Explicit exported information

| Property | Exported value |
| --- | --- |
| Parameter types | `java.io.Reader` |
| Reported exception | `java.lang.NullPointerException` |
| Reported origin | `CALLEE_PROPAGATED` |
| Summary / result verdict | SAT / SAT |
| Condition entries | 1 |
| Model entries | 2 |

### Original parsed result

```json
{
  "artifact": "commons-io-11f0abe7a.jar",
  "package": "org.apache.commons.io",
  "class": "IOUtils",
  "method": "toByteArray",
  "returnType": "byte[]",
  "params": "java.io.Reader",
  "pathIndex": 0,
  "pathId": "<org.apache.commons.io.IOUtils: byte[] toByteArray(java.io.Reader)>#0",
  "status": "SAT",
  "modelValues": {
    "stack_7_is_null": "BoolValue[value=true]",
    "stack_7": "IntValue[value=0]"
  }
}
```

### Original parsed summary

```json
{
  "artifact": "commons-io-11f0abe7a.jar",
  "package": "org.apache.commons.io",
  "class": "IOUtils",
  "method": "toByteArray",
  "returnType": "byte[]",
  "params": "java.io.Reader",
  "pathIndex": 0,
  "pathId": "<org.apache.commons.io.IOUtils: byte[] toByteArray(java.io.Reader)>#0",
  "exceptionType": "java.lang.NullPointerException",
  "throwSiteKind": "CALLEE_PROPAGATED",
  "provenance": [
    "<org.apache.commons.io.IOUtils: byte[] toByteArray(java.io.Reader,java.nio.charset.Charset)>"
  ],
  "provenances": [
    [
      "<org.apache.commons.io.IOUtils: byte[] toByteArray(java.io.Reader,java.nio.charset.Charset)>"
    ]
  ],
  "solverStatus": "SAT",
  "constraints": [
    {
      "symExpr": "(stack_7 == null)",
      "truthValue": true
    }
  ]
}
```

## Rule-derived interpretation

| Dimension | Assessment |
| --- | --- |
| Argument assignment | argument_binding_ambiguous |
| Initial classification review | initial_tier_needs_symbol_context |
| Execution readiness | not_established_from_exports |

Argument assignments are hypotheses; the export does not supply a complete Java invocation or an independently verified test oracle.

### Nullness conditions

| Symbol | Expression | truthValue | Required null | Model agrees |
| --- | --- | --- | --- | --- |
| stack_7 | `(stack_7 == null)` | True | True | True |

- A temporary-like symbol is visible in the model. Its origin and relationship to formal parameters are not established by these JSON records.
- The serialized integer for stack_7 is a symbolic reference value in this null condition; it is not an instruction to pass a Java integer.

## Information gaps retained for later work

- `formal_parameter_names_and_symbol_bindings_not_exported`
- `static_or_instance_invocation_not_exported`
- `receiver_or_static_setup_not_determined`
- `accessibility_not_exported`
- `runtime_exception_site_not_verified`
- `public_contract_oracle_not_supplied`
- `temporary_like_symbol_cannot_be_bound_to_argument_from_export`
- `propagated_call_context_not_reconstructed`

These gaps concern exported information. They are not findings about correctness, accessibility, or runtime behavior of the Java implementation. No Java source was inspected for this case.
