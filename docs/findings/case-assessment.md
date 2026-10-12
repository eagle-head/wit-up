# Case assessment findings

[Documentation index](../README.md) | [Selection method](../methodology/case-selection.md) | [Assessment rubric](../methodology/case-assessment.md)

Generated at `2026-10-08T23:26:31.242217+00:00`. This is a purposive data-inspection sample: **20 paths**, **20 distinct method signatures**, and **20 declaring classes**. The quotas are 10 cases from each initial stratum. Selection and original input records are retained in `data/processed/case-inventory.json`.

## Cases

| Case document | Initial stratum | Reported exception | Origin | Classification review |
| --- | --- | --- | --- | --- |
| [LineIterator.remove](../cases/org-apache-commons-io-lineiterator-remove-no-parameters-path-0.md) | simple_signature_hypothesis | java.lang.UnsupportedOperationException | DIRECT_ATHROW | initial_tier_retained_with_setup_gaps |
| [SizeFileFilter.constructor](../cases/org-apache-commons-io-filefilter-sizefilefilter-constructor-long-path-0.md) | simple_signature_hypothesis | java.lang.IllegalArgumentException | CALLEE_PROPAGATED | initial_tier_retained_with_setup_gaps |
| [FileSystem.isOsNameMatch](../cases/org-apache-commons-io-filesystem-isosnamematch-java-lang-string-java-lang-string-path-1.md) | simple_signature_hypothesis | java.lang.NullPointerException | IMPLICIT | initial_tier_retained_with_setup_gaps |
| [ClosedOutputStream.write](../cases/org-apache-commons-io-output-closedoutputstream-write-int-path-0.md) | simple_signature_hypothesis | java.io.IOException | DIRECT_ATHROW | initial_tier_retained_with_setup_gaps |
| [ValidatingObjectInputStream.invalidClassNameFound](../cases/org-apache-commons-io-serialization-validatingobjectinputstream-invalidclassnamefound-java-lang-string-path-0.md) | simple_signature_hypothesis | java.io.InvalidClassException | DIRECT_ATHROW | initial_tier_retained_with_setup_gaps |
| [FileSystemUtils.freeSpaceKb](../cases/org-apache-commons-io-filesystemutils-freespacekb-java-lang-string-long-path-2.md) | simple_signature_hypothesis | java.lang.IllegalStateException | CALLEE_PROPAGATED | initial_tier_retained_with_setup_gaps |
| [CircularByteBuffer.constructor](../cases/org-apache-commons-io-input-buffer-circularbytebuffer-constructor-int-path-0.md) | simple_signature_hypothesis | java.lang.NegativeArraySizeException | IMPLICIT | initial_tier_retained_with_setup_gaps |
| [FileFilterUtils.sizeFileFilter](../cases/org-apache-commons-io-filefilter-filefilterutils-sizefilefilter-long-boolean-path-0.md) | simple_signature_hypothesis | java.lang.IllegalArgumentException | CALLEE_PROPAGATED | initial_tier_retained_with_setup_gaps |
| [IOCase.checkIndexOf](../cases/org-apache-commons-io-iocase-checkindexof-java-lang-string-int-java-lang-string-path-0.md) | simple_signature_hypothesis | java.lang.NullPointerException | IMPLICIT | initial_tier_retained_with_setup_gaps |
| [RegexFileFilter.constructor](../cases/org-apache-commons-io-filefilter-regexfilefilter-constructor-java-lang-string-int-path-0.md) | simple_signature_hypothesis | java.lang.IllegalArgumentException | DIRECT_ATHROW | initial_tier_retained_with_setup_gaps |
| [EndianUtils.readSwappedDouble](../cases/org-apache-commons-io-endianutils-readswappeddouble-java-io-inputstream-path-1.md) | null_argument_hypothesis | java.lang.NullPointerException | CALLEE_PROPAGATED | initial_tier_retained_with_setup_gaps |
| [FileDeleteStrategy$ForceFileDeleteStrategy.doDelete](../cases/org-apache-commons-io-filedeletestrategy-forcefiledeletestrategy-dodelete-java-io-file-path-3.md) | null_argument_hypothesis | java.lang.NullPointerException | CALLEE_PROPAGATED | initial_tier_retained_with_setup_gaps |
| [FileUtils.getFile](../cases/org-apache-commons-io-fileutils-getfile-java-lang-string-array-path-0.md) | null_argument_hypothesis | java.lang.NullPointerException | IMPLICIT | initial_tier_retained_with_setup_gaps |
| [IOUtils.toByteArray](../cases/org-apache-commons-io-ioutils-tobytearray-java-io-reader-path-0.md) | null_argument_hypothesis | java.lang.NullPointerException | CALLEE_PROPAGATED | initial_tier_needs_symbol_context |
| [ReverseComparator.constructor](../cases/org-apache-commons-io-comparator-reversecomparator-constructor-java-util-comparator-path-0.md) | null_argument_hypothesis | java.lang.IllegalArgumentException | DIRECT_ATHROW | initial_tier_retained_with_setup_gaps |
| [CleaningPathVisitor.accept](../cases/org-apache-commons-io-file-cleaningpathvisitor-accept-java-nio-file-path-path-0.md) | null_argument_hypothesis | java.lang.NullPointerException | IMPLICIT | initial_tier_retained_with_setup_gaps |
| [AgeFileFilter.constructor](../cases/org-apache-commons-io-filefilter-agefilefilter-constructor-java-util-date-path-0.md) | null_argument_hypothesis | java.lang.NullPointerException | CALLEE_PROPAGATED | initial_tier_retained_with_setup_gaps |
| [DelegateFileFilter.constructor](../cases/org-apache-commons-io-filefilter-delegatefilefilter-constructor-java-io-filefilter-path-0.md) | null_argument_hypothesis | java.lang.IllegalArgumentException | DIRECT_ATHROW | initial_tier_retained_with_setup_gaps |
| [MagicNumberFileFilter.constructor](../cases/org-apache-commons-io-filefilter-magicnumberfilefilter-constructor-byte-array-path-0.md) | null_argument_hypothesis | java.lang.IllegalArgumentException | CALLEE_PROPAGATED | initial_tier_retained_with_setup_gaps |
| [NameFileFilter.constructor](../cases/org-apache-commons-io-filefilter-namefilefilter-constructor-java-util-list-path-0.md) | null_argument_hypothesis | java.lang.IllegalArgumentException | CALLEE_PROPAGATED | initial_tier_retained_with_setup_gaps |

## Assessment outcomes

| Outcome | Cases |
| --- | --- |
| initial_tier_retained_with_setup_gaps | 19 |
| initial_tier_needs_symbol_context | 1 |

The initial labels describe exported shape. A retained label does not mean that a complete invocation is available. Ambiguities remain in the selected sample and are reported as separate outcomes.

## Reported exceptions

| Exception | Cases |
| --- | --- |
| java.lang.UnsupportedOperationException | 1 |
| java.lang.IllegalArgumentException | 7 |
| java.lang.NullPointerException | 8 |
| java.io.IOException | 1 |
| java.io.InvalidClassException | 1 |
| java.lang.IllegalStateException | 1 |
| java.lang.NegativeArraySizeException | 1 |

## Reported origins

| Origin | Cases |
| --- | --- |
| DIRECT_ATHROW | 6 |
| CALLEE_PROPAGATED | 9 |
| IMPLICIT | 5 |

## Information gaps

| Gap | Cases |
| --- | --- |
| static_or_instance_invocation_not_exported | 12 |
| receiver_or_static_setup_not_determined | 12 |
| accessibility_not_exported | 20 |
| runtime_exception_site_not_verified | 20 |
| public_contract_oracle_not_supplied | 20 |
| formal_parameter_names_and_symbol_bindings_not_exported | 19 |
| propagated_call_context_not_reconstructed | 9 |
| multi_parameter_assignment_not_verified | 5 |
| concrete_argument_values_not_reported | 2 |
| temporary_like_symbol_cannot_be_bound_to_argument_from_export | 1 |

Gap counts overlap. Denominator: the selected cases only. These observations cannot be extrapolated to the 221-path candidate pool, the full SAT population, or the library.

## Qualitative inspection of the selected records

Integer predicates retain their truth flags and model values, including negated comparisons. The linked records document how null flags relate to serialized strings or reference encodings. Some signatures require arguments even though their models supply no values; later argument choices would be additional assumptions. A temporary-like model symbol has clear nullness but an unresolved relationship to formal arguments; it remains in the sample. Numeric/null consistency checks validate only the recognized expression subset; they do not validate the complete solver encoding.

The exported exception supplies a candidate assertion target for each selected case. Ordinary-method invocation mode, accessibility, runtime exception location and an independent public-contract oracle remain unresolved. Constructors expose an operation signature, but public accessibility and formal parameter bindings are still absent from these records.

## Supported conclusion and next boundary

The sample provides traceable material for a later isolated generation experiment and reveals concrete preparation ambiguities. Execution readiness is not established from these exports. No LLM generation rate, compilation rate, exception reproduction rate, or test quality was measured. Keep this inventory fixed when defining that later experiment; changes to selection or assessment should be recorded as protocol revisions.
