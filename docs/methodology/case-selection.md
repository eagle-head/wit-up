# Case selection method

[Documentation index](../README.md) | [Case findings](../findings/case-assessment.md)

## Frame, units, and quotas

Selection policy version: **1**. The frame is the 221 rows in the existing
candidate table labeled `simple_signature_hypothesis` or
`null_argument_hypothesis`. Both exported verdicts must be SAT; the result must
exist, its signature metadata must match, and its exception type must be named.
The stored tier is recomputed and checked before selection.

The first stratum has 65 paths, 53 distinct methods and 25 classes. The second has
156 paths, 148 distinct methods and 56 classes. Select **10 paths per stratum**,
with at most one path per full method signature across the sample. The size is a
practical exploratory quota agreed before this inspection, not a statistical
power calculation. Other tiers and verdicts remain outside this particular frame.

## Deterministic purposive diversity rule

Process the simple-signature stratum first, then the null-argument stratum.
Maintain the method signatures and dimension values already selected across both
strata. At each step, consider only rows whose method signature has not yet been
selected and prefer new values in this **lexicographic priority order**:

1. Fully qualified declaring class.
2. Reported exception type.
3. Reported exception origin.
4. Exact parameter type list.
5. Constructor versus ordinary method.
6. Number of exported conditions.

If novelty is tied, prefer fewer conditions, then fewer model entries, then sort
by artifact and full pathId. This favors class diversity first and introduces
other visible contrasts when possible. It does not rank actual test-generation
success. No random seed applies because no random sampling is used.

The procedure must meet both quotas or fail; it does not silently reduce the
sample. Duplicate pool keys, absent original records, or conflicting metadata
also stop the command. Selection order, newly covered dimensions and tie-breaker
values are stored with each case.

## Traceability and consistency

For each selected key, reread both complete original JSON arrays and retain the
matching records with 1-based array positions. Compare their contents with the
derived candidate record and verify original signature metadata. Persist input
filenames, project-relative paths, byte sizes and SHA-256 values. These hashes
identify input bytes, not semantic quality or test feasibility.

`data/processed/case-inventory.json` retains the entire 221-key selection frame,
policy, selected original records, source locators and assessments. A case's
artifact/pathId pair is its identity; document names describe its signature.

## Decisions, preview, and limits

The policy was chosen with knowledge of the population inventory, and its first
preview was examined before the durable inventory was saved. This is not a
preregistration. The preview exposed a temporary-like `stack_7` symbol; the case
was retained and flagged, not replaced. No selection rule was changed to remove
that ambiguity or improve apparent readiness.

The quotas deliberately oversample simpler exported shapes. Class novelty,
lexical ties, stratum order and the preference for fewer conditions introduce
selection bias. The 20 cases support examples and preparation lessons only;
sample percentages must not be interpreted as population rates, LLM success
rates, or estimates for Commons IO as a whole.

## Reproduction

```powershell
uv run --locked witup-analysis inspect-cases
```

The command uses the existing full inventory and original JSON inputs. Altering
`--per-stratum`, inputs, or selection rules constitutes a protocol revision and
must be recorded in the study log before drawing comparisons.
