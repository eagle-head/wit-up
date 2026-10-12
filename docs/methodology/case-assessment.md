# Case assessment rubric

[Documentation index](../README.md) | [Case findings](../findings/case-assessment.md)

## Evidence levels

- **Explicit export:** signature, exception, verdict, conditions with truth flags,
  model strings and provenance from the original parsed records.
- **Bounded interpretation:** required nullness or integer-predicate consistency
  for recognized expression forms; possible argument assignment from signature
  arity and model symbols; apparent preparation complexity.
- **Unresolved:** formal symbol binding, modifiers, fixtures, runtime exception
  site, intended public behavior and generation effectiveness.

An interpretation never upgrades an exported SAT label into an observed Java
execution. All case records retain their original tier and report a separate
classification-review outcome.

## Applied steps

1. Recover both original records and check their relationship to the derived row.
2. Record the target signature and reported exception as possible operation and
   assertion information, with provenance intact.
3. Recognize only simple identifier null comparisons and identifier/integer
   comparisons. Evaluate the comparison with `truthValue`, retaining negations.
4. Compare recognized null predicates with `_is_null` flags and integer predicates
   with IntValue strings. Record disagreements or unsupported syntax explicitly.
5. Describe argument-assignment information, including missing values, multiple
   parameters, and temporary-like symbols such as `stack_7`.
6. Record setup, accessibility, exception-site and contract-oracle gaps. Review
   whether the original simpler label still describes exported shape without
   implying a complete fixture.

The current patterns are deliberately limited; this is not a general symbolic
expression interpreter. Agreement on a recognized predicate does not validate
the full solver model. The assessment combines rule-derived checks with a
qualitative inspection of the selected original records.

## Classification-review outcomes

| Outcome | Meaning |
| --- | --- |
| `initial_tier_retained_with_setup_gaps` | The stored shape rule agrees; fixture, binding or oracle gaps remain. |
| `initial_tier_needs_symbol_context` | A temporary-like symbol prevents interpreting the null flag as a demonstrated formal-argument assignment. |
| `stored_rule_disagreement` | The recorded tier and current shape rule disagree; keep the discrepancy visible. |

No case is declared execution-ready. The outcome is
`not_established_from_exports`; this means the necessary evidence is outside this
phase, not that generation or reproduction is impossible.

## Gap definitions

| Gap | Interpretation |
| --- | --- |
| `formal_parameter_names_and_symbol_bindings_not_exported` | Parameter types are present, but formal names and a binding map are absent. |
| `multi_parameter_assignment_not_verified` | Several positions require assignment; model symbols alone do not establish the complete mapping. |
| `concrete_argument_values_not_reported` | The signature has parameters but the model is empty. Values chosen later would be additional assumptions. |
| `static_or_instance_invocation_not_exported` | The record does not export the invocation modifier. |
| `receiver_or_static_setup_not_determined` | The full preparation for invoking an ordinary method remains unspecified. |
| `accessibility_not_exported` | Public, protected, package or private visibility cannot be established from the fields. |
| `runtime_exception_site_not_verified` | No Java execution confirms that the reported operation is the exception source. |
| `public_contract_oracle_not_supplied` | The record reports a scenario; an independent expected-behavior contract is absent. |
| `temporary_like_symbol_cannot_be_bound_to_argument_from_export` | Naming such as stack_7 suggests a temporary; its origin or argument relation is unverified. |
| `propagated_call_context_not_reconstructed` | Provenance is available, but the preparation for the propagated flow has not been reconstructed. |
| `recognized_condition_and_model_disagree` | A recognized predicate contradicts its relevant serialized model value or null flag. |
| `nullness_model_flag_not_reported` | A recognized null comparison lacks its corresponding flag. |
| `condition_syntax_outside_assessment_subset` | A condition is outside the limited parser's recognized syntax. |

## Retention and later handoff

Keep every selected case, including ambiguous bindings, absent argument values
and propagated flows. The later generation study should receive original record
data and these gaps as separate fields, not synthesized assumptions presented as
facts. Any later context acquisition, API inspection, generation, compilation or
execution belongs to a separately recorded phase.
