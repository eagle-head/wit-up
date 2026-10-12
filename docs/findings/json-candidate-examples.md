# Initial illustrative candidate examples

[Documentation index](../README.md) | [Candidate tiers](json-candidate-tiers.md)

Up to six distinct method signatures per simpler tier are selected deterministically, preferring direct throws and fewer conditions/model entries. This illustrates the input data; it is not a representative effectiveness sample or an approved set of generated tests.

#### `<org.apache.commons.io.LineIterator: void remove()>#0`

Tier: `simple_signature_hypothesis`; exception: `java.lang.UnsupportedOperationException`; origin: `DIRECT_ATHROW`; solver status: `SAT`.

```json
{
  "constraints": [],
  "modelValues": {}
}
```

#### `<org.apache.commons.io.input.SwappedDataInputStream: java.lang.String readLine()>#0`

Tier: `simple_signature_hypothesis`; exception: `java.lang.UnsupportedOperationException`; origin: `DIRECT_ATHROW`; solver status: `SAT`.

```json
{
  "constraints": [],
  "modelValues": {}
}
```

#### `<org.apache.commons.io.input.SwappedDataInputStream: java.lang.String readUTF()>#0`

Tier: `simple_signature_hypothesis`; exception: `java.lang.UnsupportedOperationException`; origin: `DIRECT_ATHROW`; solver status: `SAT`.

```json
{
  "constraints": [],
  "modelValues": {}
}
```

#### `<org.apache.commons.io.input.UnixLineEndingInputStream: void mark(int)>#0`

Tier: `simple_signature_hypothesis`; exception: `java.lang.UnsupportedOperationException`; origin: `DIRECT_ATHROW`; solver status: `SAT`.

```json
{
  "constraints": [],
  "modelValues": {}
}
```

#### `<org.apache.commons.io.input.WindowsLineEndingInputStream: void mark(int)>#0`

Tier: `simple_signature_hypothesis`; exception: `java.lang.UnsupportedOperationException`; origin: `DIRECT_ATHROW`; solver status: `SAT`.

```json
{
  "constraints": [],
  "modelValues": {}
}
```

#### `<org.apache.commons.io.output.ClosedOutputStream: void flush()>#0`

Tier: `simple_signature_hypothesis`; exception: `java.io.IOException`; origin: `DIRECT_ATHROW`; solver status: `SAT`.

```json
{
  "constraints": [],
  "modelValues": {}
}
```

#### `<org.apache.commons.io.LineIterator: void <init>(java.io.Reader)>#0`

Tier: `null_argument_hypothesis`; exception: `java.lang.IllegalArgumentException`; origin: `DIRECT_ATHROW`; solver status: `SAT`.

```json
{
  "constraints": [
    {
      "symExpr": "(reader != null)",
      "truthValue": false
    }
  ],
  "modelValues": {
    "reader": "IntValue[value=0]",
    "reader_is_null": "BoolValue[value=true]"
  }
}
```

#### `<org.apache.commons.io.comparator.ReverseComparator: void <init>(java.util.Comparator)>#0`

Tier: `null_argument_hypothesis`; exception: `java.lang.IllegalArgumentException`; origin: `DIRECT_ATHROW`; solver status: `SAT`.

```json
{
  "constraints": [
    {
      "symExpr": "(delegate != null)",
      "truthValue": false
    }
  ],
  "modelValues": {
    "delegate": "IntValue[value=0]",
    "delegate_is_null": "BoolValue[value=true]"
  }
}
```

#### `<org.apache.commons.io.filefilter.DelegateFileFilter: void <init>(java.io.FileFilter)>#0`

Tier: `null_argument_hypothesis`; exception: `java.lang.IllegalArgumentException`; origin: `DIRECT_ATHROW`; solver status: `SAT`.

```json
{
  "constraints": [
    {
      "symExpr": "(filter != null)",
      "truthValue": false
    }
  ],
  "modelValues": {
    "filter": "IntValue[value=0]",
    "filter_is_null": "BoolValue[value=true]"
  }
}
```

#### `<org.apache.commons.io.filefilter.DelegateFileFilter: void <init>(java.io.FilenameFilter)>#0`

Tier: `null_argument_hypothesis`; exception: `java.lang.IllegalArgumentException`; origin: `DIRECT_ATHROW`; solver status: `SAT`.

```json
{
  "constraints": [
    {
      "symExpr": "(filter != null)",
      "truthValue": false
    }
  ],
  "modelValues": {
    "filter": "IntValue[value=0]",
    "filter_is_null": "BoolValue[value=true]"
  }
}
```

#### `<org.apache.commons.io.filefilter.FileFilterUtils: java.util.List toList(org.apache.commons.io.filefilter.IOFileFilter[])>#0`

Tier: `null_argument_hypothesis`; exception: `java.lang.IllegalArgumentException`; origin: `DIRECT_ATHROW`; solver status: `SAT`.

```json
{
  "constraints": [
    {
      "symExpr": "(filters != null)",
      "truthValue": false
    }
  ],
  "modelValues": {
    "filters_is_null": "BoolValue[value=true]",
    "filters": "IntValue[value=0]"
  }
}
```

#### `<org.apache.commons.io.filefilter.NotFileFilter: void <init>(org.apache.commons.io.filefilter.IOFileFilter)>#0`

Tier: `null_argument_hypothesis`; exception: `java.lang.IllegalArgumentException`; origin: `DIRECT_ATHROW`; solver status: `SAT`.

```json
{
  "constraints": [
    {
      "symExpr": "(filter != null)",
      "truthValue": false
    }
  ],
  "modelValues": {
    "filter": "IntValue[value=0]",
    "filter_is_null": "BoolValue[value=true]"
  }
}
```
