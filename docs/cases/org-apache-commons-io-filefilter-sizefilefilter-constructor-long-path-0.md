# `<org.apache.commons.io.filefilter.SizeFileFilter: void <init>(long)>#0`

[Documentation index](../README.md) | [Case findings](../findings/case-assessment.md) | [Assessment rubric](../methodology/case-assessment.md)

## Record identity and selection

| Property | Value |
| --- | --- |
| Artifact | `commons-io-11f0abe7a.jar` |
| Initial stratum | `simple_signature_hypothesis` |
| Selection order | 2 |
| Novel dimensions when selected | class, exception, origin, parameters, operation, conditions |
| Result locator | `witup-results-commons-io-11f0abe7a.json`, array record 21822 |
| Summary locator | `witup-summaries-commons-io-11f0abe7a.json`, array record 54622 |

Array record numbers are 1-based. The artifact/pathId pair is the semantic locator. Input byte identities are recorded in `data/processed/case-inventory.json`. The source records below preserve parsed values; whitespace and object-key ordering are not byte-for-byte copies.

## Explicit exported information

| Property | Exported value |
| --- | --- |
| Parameter types | `long` |
| Reported exception | `java.lang.IllegalArgumentException` |
| Reported origin | `CALLEE_PROPAGATED` |
| Summary / result verdict | SAT / SAT |
| Condition entries | 1 |
| Model entries | 1 |

### Original parsed result

```json
{
  "artifact": "commons-io-11f0abe7a.jar",
  "package": "org.apache.commons.io.filefilter",
  "class": "SizeFileFilter",
  "method": "<init>",
  "returnType": "void",
  "params": "long",
  "pathIndex": 0,
  "pathId": "<org.apache.commons.io.filefilter.SizeFileFilter: void <init>(long)>#0",
  "status": "SAT",
  "modelValues": {
    "size": "IntValue[value=-1]"
  }
}
```

### Original parsed summary

```json
{
  "artifact": "commons-io-11f0abe7a.jar",
  "package": "org.apache.commons.io.filefilter",
  "class": "SizeFileFilter",
  "method": "<init>",
  "returnType": "void",
  "params": "long",
  "pathIndex": 0,
  "pathId": "<org.apache.commons.io.filefilter.SizeFileFilter: void <init>(long)>#0",
  "exceptionType": "java.lang.IllegalArgumentException",
  "throwSiteKind": "CALLEE_PROPAGATED",
  "provenance": [
    "<org.apache.commons.io.filefilter.SizeFileFilter: void <init>(long,boolean)>"
  ],
  "provenances": [
    [
      "<org.apache.commons.io.filefilter.SizeFileFilter: void <init>(long,boolean)>"
    ]
  ],
  "solverStatus": "SAT",
  "constraints": [
    {
      "symExpr": "(size >= 0)",
      "truthValue": false
    }
  ]
}
```

## Rule-derived interpretation

| Dimension | Assessment |
| --- | --- |
| Argument assignment | single_argument_assignment_hypothesis |
| Initial classification review | initial_tier_retained_with_setup_gaps |
| Execution readiness | not_established_from_exports |

Argument assignments are hypotheses; the export does not supply a complete Java invocation or an independently verified test oracle.

### Integer conditions

| Symbol | Expression | truthValue | Model value | Model agrees |
| --- | --- | --- | --- | --- |
| size | `(size >= 0)` | False | -1 | True |

## Information gaps retained for later work

- `formal_parameter_names_and_symbol_bindings_not_exported`
- `accessibility_not_exported`
- `runtime_exception_site_not_verified`
- `public_contract_oracle_not_supplied`
- `propagated_call_context_not_reconstructed`

These gaps concern exported information. They are not findings about correctness, accessibility, or runtime behavior of the Java implementation. No Java source was inspected for this case.
