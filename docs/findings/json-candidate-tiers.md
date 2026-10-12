# 4. Which rows are simpler candidates for an initial experiment?

[Documentation index](../README.md) | [JSON analysis overview](../commons-io-json-analysis.md)

The following mutually exclusive labels are data-level preparation hypotheses. They are assigned in priority order: unavailable/disagreeing join or non-SAT verdict; an unreported exception type; state references; call syntax; symbolic/compound model values; basic signatures; a single-reference null hypothesis; other object fixtures. State/call flags use textual patterns, so both missed complexity and conservative false positives are possible.

Basic signatures have no parameters or only primitive/String parameter types. Null hypotheses have one other parameter type and an identifier-shaped `_is_null` flag whose value is `BoolValue[value=true]`. Both require a matching SAT result and summary. Neither proves that a symbol is an argument, that an instance can be built, or that the operation is publicly accessible.

| Tier | Rows | Share of summaries | Rule / interpretation |
| --- | --- | --- | --- |
| `solver_not_sat` | 56,253 | 77.68% | Both records agree, but the verdict is not SAT; retained for inventory, outside the initial candidate pool. |
| `state_context_required` | 12,815 | 17.70% | SAT pair; receiver or signature-qualified state appears in expressions/model keys. |
| `call_context_required` | 2,170 | 3.00% | SAT pair; method-call syntax appears in conditions/model keys. |
| `object_fixture_required` | 444 | 0.61% | SAT pair; richer parameter types suggest a stream/file/object fixture. |
| `model_reconstruction_required` | 355 | 0.49% | SAT pair; symbolic solver values or compound/temporary model keys need interpretation. |
| `exception_not_reported` | 161 | 0.22% | SAT pair with exceptionType=null; no named exception is supplied for an assertion. |
| `null_argument_hypothesis` | 156 | 0.22% | SAT pair; one other parameter type and an identifier-shaped true null flag. Its mapping to that argument still needs confirmation. |
| `simple_signature_hypothesis` | 65 | 0.09% | SAT pair; only primitive/String parameters (or none), without detected state/call/model complexity. |

Preparation flags below overlap and cover all summary rows, including non-SAT rows:

| Flag | Rows |
| --- | --- |
| receiver_state | 22,848 |
| static_state | 48,897 |
| method_calls | 69,549 |
| symbolic_values | 3,532 |
| complex_model_keys | 15,452 |

[Initial illustrative examples](json-candidate-examples.md) are kept separately from the later 20-case inspection sample.

### What this first phase supports

The inventories and example rows identify material that can be packaged for a later isolated generation experiment. Prefer a small spread of simpler signatures, null hypotheses and richer fixtures rather than taking the most frequent exception alone. Keep unavailable or complex preparations as explicit outcomes. Actual generation success, compilation, execution, scenario reproduction and assertion quality remain unmeasured.
