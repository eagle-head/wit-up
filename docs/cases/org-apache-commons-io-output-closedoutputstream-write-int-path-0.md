# `<org.apache.commons.io.output.ClosedOutputStream: void write(int)>#0`

[Documentation index](../README.md) | [Case findings](../findings/case-assessment.md) | [Assessment rubric](../methodology/case-assessment.md)

## Record identity and selection

| Property | Value |
| --- | --- |
| Artifact | `commons-io-11f0abe7a.jar` |
| Initial stratum | `simple_signature_hypothesis` |
| Selection order | 4 |
| Novel dimensions when selected | class, exception, parameters |
| Result locator | `witup-results-commons-io-11f0abe7a.json`, array record 46469 |
| Summary locator | `witup-summaries-commons-io-11f0abe7a.json`, array record 34984 |

Array record numbers are 1-based. The artifact/pathId pair is the semantic locator. Input byte identities are recorded in `data/processed/case-inventory.json`. The source records below preserve parsed values; whitespace and object-key ordering are not byte-for-byte copies.

## Explicit exported information

| Property | Exported value |
| --- | --- |
| Parameter types | `int` |
| Reported exception | `java.io.IOException` |
| Reported origin | `DIRECT_ATHROW` |
| Summary / result verdict | SAT / SAT |
| Condition entries | 0 |
| Model entries | 0 |

### Original parsed result

```json
{
  "artifact": "commons-io-11f0abe7a.jar",
  "package": "org.apache.commons.io.output",
  "class": "ClosedOutputStream",
  "method": "write",
  "returnType": "void",
  "params": "int",
  "pathIndex": 0,
  "pathId": "<org.apache.commons.io.output.ClosedOutputStream: void write(int)>#0",
  "status": "SAT",
  "modelValues": {}
}
```

### Original parsed summary

```json
{
  "artifact": "commons-io-11f0abe7a.jar",
  "package": "org.apache.commons.io.output",
  "class": "ClosedOutputStream",
  "method": "write",
  "returnType": "void",
  "params": "int",
  "pathIndex": 0,
  "pathId": "<org.apache.commons.io.output.ClosedOutputStream: void write(int)>#0",
  "exceptionType": "java.io.IOException",
  "throwSiteKind": "DIRECT_ATHROW",
  "provenance": [],
  "provenances": [
    []
  ],
  "solverStatus": "SAT",
  "constraints": []
}
```

## Rule-derived interpretation

| Dimension | Assessment |
| --- | --- |
| Argument assignment | argument_choices_not_exported |
| Initial classification review | initial_tier_retained_with_setup_gaps |
| Execution readiness | not_established_from_exports |

Argument assignments are hypotheses; the export does not supply a complete Java invocation or an independently verified test oracle.

## Information gaps retained for later work

- `formal_parameter_names_and_symbol_bindings_not_exported`
- `concrete_argument_values_not_reported`
- `static_or_instance_invocation_not_exported`
- `receiver_or_static_setup_not_determined`
- `accessibility_not_exported`
- `runtime_exception_site_not_verified`
- `public_contract_oracle_not_supplied`

These gaps concern exported information. They are not findings about correctness, accessibility, or runtime behavior of the Java implementation. No Java source was inspected for this case.
