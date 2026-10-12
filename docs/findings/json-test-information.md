# 3. What information supports arranging inputs and writing assertions?

[Documentation index](../README.md) | [JSON analysis overview](../commons-io-json-analysis.md)

| Available data | Potential use in a later test | Boundary |
| --- | --- | --- |
| Class, method, return type, parameter types | Identify the intended operation and overload | Visibility, static/instance modifiers, parameter names, constructors and fixture recipes are absent. |
| constraints.symExpr and constraints.truthValue | Describe the condition a preparation should satisfy | A false truthValue negates the expression; all entries are conjoined. Strings are symbolic syntax, not executable Java. |
| modelValues | Suggest scalar values and nullness assignments | Object identities, temporaries, fields, arrays and call results may require reconstruction. A model symbol is not automatically a method argument. |
| exceptionType | Suggest an exception assertion on the intended operation | The same exception can arise during setup or elsewhere; exception type alone does not demonstrate the modeled scenario. |
| throwSiteKind and provenance(s) | Help interpret direct, implicit and propagated flows | There is no explicit source line or runtime event trace in these records. |
| solver verdict | Prioritize candidate rows while retaining uncertain rows | It does not establish constructibility, public API reachability, or intended behavior. |

| Observation | Count |
| --- | --- |
| Result rows with an empty model | 67,606 |
| SAT result rows with an empty model | 159 |
| Serialized model entries | 488,497 |
| Model keys ending in _is_null | 94,758 |
| Summary rows with no conditions | 102 |
| Total condition entries | 1,252,128 |
| Condition entries with truthValue=true | 925,271 |
| Condition entries with truthValue=false | 326,857 |
| Summary rows with nonempty representative provenance | 68,483 |
| Summary rows with multiple provenance alternatives | 361 |

Serialized model value kinds (denominator: model entries):

| Value | Rows | Share |
| --- | --- | --- |
| `IntValue` | 290,557 | 59.48% |
| `BoolValue` | 180,013 | 36.85% |
| `StringValue` | 10,938 | 2.24% |
| `solver_expression` | 6,989 | 1.43% |

An empty model can accompany a satisfiable path with no required scalar assignments; it is not automatically missing data. This phase keeps the strings intact, including `IntValue[...]`, `BoolValue[...]` and solver expressions. Numeric encodings may represent references rather than Java numbers.

The exports describe exceptional behavior. They do not supply normal return-value expectations, a complete public contract, argument-name/position mappings, or an independently validated oracle. A later exception test would initially characterize a reported scenario; correctness of that scenario requires separate evidence.
