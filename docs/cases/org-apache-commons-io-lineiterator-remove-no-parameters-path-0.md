# `<org.apache.commons.io.LineIterator: void remove()>#0`

[Documentation index](../README.md) | [Case findings](../findings/case-assessment.md) | [Assessment rubric](../methodology/case-assessment.md)

## Record identity and selection

| Property | Value |
| --- | --- |
| Artifact | `commons-io-11f0abe7a.jar` |
| Initial stratum | `simple_signature_hypothesis` |
| Selection order | 1 |
| Novel dimensions when selected | class, exception, origin, parameters, operation, conditions |
| Result locator | `witup-results-commons-io-11f0abe7a.json`, array record 19121 |
| Summary locator | `witup-summaries-commons-io-11f0abe7a.json`, array record 57009 |

Array record numbers are 1-based. The artifact/pathId pair is the semantic locator. Input byte identities are recorded in `data/processed/case-inventory.json`. The source records below preserve parsed values; whitespace and object-key ordering are not byte-for-byte copies.

## Explicit exported information

| Property | Exported value |
| --- | --- |
| Parameter types | No formal parameters |
| Reported exception | `java.lang.UnsupportedOperationException` |
| Reported origin | `DIRECT_ATHROW` |
| Summary / result verdict | SAT / SAT |
| Condition entries | 0 |
| Model entries | 0 |

### Original parsed result

```json
{
  "artifact": "commons-io-11f0abe7a.jar",
  "package": "org.apache.commons.io",
  "class": "LineIterator",
  "method": "remove",
  "returnType": "void",
  "params": "",
  "pathIndex": 0,
  "pathId": "<org.apache.commons.io.LineIterator: void remove()>#0",
  "status": "SAT",
  "modelValues": {}
}
```

### Original parsed summary

```json
{
  "artifact": "commons-io-11f0abe7a.jar",
  "package": "org.apache.commons.io",
  "class": "LineIterator",
  "method": "remove",
  "returnType": "void",
  "params": "",
  "pathIndex": 0,
  "pathId": "<org.apache.commons.io.LineIterator: void remove()>#0",
  "exceptionType": "java.lang.UnsupportedOperationException",
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
| Argument assignment | no_formal_arguments |
| Initial classification review | initial_tier_retained_with_setup_gaps |
| Execution readiness | not_established_from_exports |

Argument assignments are hypotheses; the export does not supply a complete Java invocation or an independently verified test oracle.

## Information gaps retained for later work

- `static_or_instance_invocation_not_exported`
- `receiver_or_static_setup_not_determined`
- `accessibility_not_exported`
- `runtime_exception_site_not_verified`
- `public_contract_oracle_not_supplied`

These gaps concern exported information. They are not findings about correctness, accessibility, or runtime behavior of the Java implementation. No Java source was inspected for this case.
