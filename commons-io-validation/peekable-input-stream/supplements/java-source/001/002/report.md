# Java-source exception-test evaluation

This evaluation is incomplete. The available native observations are reported below; unavailable measurements remain unavailable.

## Identity and scope

- Parent generation: `runs/java-source/001`; exact seal SHA-256 `28ac9b72af259f32261cb569e3ce65515007f3089213024d5065b60adcec9d5d`.
- Evaluation: `java-source-001/evaluation-002`; independent generation contribution: 0.
- Baseline commit: `11f0abe7a3fb6954b2985ca4ab0697b2fb489e84`.
- Frozen test SHA-256: `365a763fbc4b383087d993e659e05bf04952a4d4333a2ff16ac4417fe9eb43dd`.
- Original generation: 20 executed tests, 0 failures, 0 errors, 0 skips. The parent remains immutable.
- The canonical paired-full-suite plan selects every existing project test on both sides and adds only the frozen generated test after. The target production class alone is measured and mutated.
- The original additional Checkstyle findings (missing package-info.java and private fixture-constructor Javadoc) remain preserved in the generation report. They are separate from executed-test outcomes and were not repaired.
- A separate first evaluation stopped during tool preparation and is sealed incomplete. Its diagnostic does not contribute test failures or metrics to this pair.

## Before and after JaCoCo

| Counter | Before: covered / total | After: covered / total | Before missed | After missed |
| --- | --- | --- | --- | --- |
| INSTRUCTION | 0/98 (0.00%) | Unavailable | 98 | Unavailable |
| BRANCH | 0/8 (0.00%) | Unavailable | 8 | Unavailable |
| LINE | 0/16 (0.00%) | Unavailable | 16 | Unavailable |
| COMPLEXITY | 0/8 (0.00%) | Unavailable | 8 | Unavailable |
| METHOD | 0/4 (0.00%) | Unavailable | 4 | Unavailable |
| CLASS | 0/1 (0.00%) | Unavailable | 1 | Unavailable |

The before values above come from this evaluation's native measurement, rather than an inferred baseline. JaCoCo line/branch counters and PIT line counters are separate observations. JaCoCo does not count exception handling as branches; see the [official counter definitions](https://www.jacoco.org/jacoco/trunk/doc/counters.html).

## Before and after PIT

| Observation | Before | After |
| --- | --- | --- |
| Native mutants | Unavailable | Unavailable |
| Cumulative mutation-test executions | Unavailable | Unavailable |
| Mutation score: KILLED / total | Unavailable | Unavailable |
| Test strength: KILLED / (KILLED + SURVIVED) | Unavailable | Unavailable |

No mutation score or zero baseline is inferred from a failed baseline-validation process or absent native XML. PIT cumulative executions do not represent unique generated tests. Coverage and mutation scores do not establish completeness or correctness against an independent specification. See [PIT's official concepts](https://pitest.org/quickstart/basic_concepts/).

## Executions and diagnostics

| Phase | Process exit | Native tests | Failures | Errors | Skips | Attribution |
| --- | --- | --- | --- | --- | --- | --- |
| preflight | 0 | 0 | 0 | 0 | 0 | not_started |
| jacoco-before | 0 | 1541 | 0 | 0 | 6 | passed |
| pit-before | 0 | Unknown | Unknown | Unknown | Unknown | unknown |

### pit-before diagnostic

```text
[INFO] Skipping project because:
[INFO]   - Project has either no tests or no production code.
```


Protocol problems for `pit-before`: Missing declared artifact: pit-mutations; Missing declared artifact: pit-linecoverage


Surefire counts are losslessly archived per execution. Intrinsic existing skips remain visible. PIT has no Surefire report destination; its process diagnostics and native mutation artifacts are retained separately. Infrastructure operations and missing measurements are not included as failures of the 20 generated tests.

## Exact toolchain and libraries

| Component | Exact version or build |
| --- | --- |
| Java vendor | Eclipse Temurin |
| Java language and bytecode target | 1.8 / 1.8 |
| Java runtime | 1.8.0_504-b01 |
| Java VM | 25.504-b01 |
| javac | 1.8.0_504 |
| Maven | 3.9.16; 2bdd9fddda4b155ebf8000e807eb73fd829a51d5 |
| Commons IO | 2.7-SNAPSHOT; Apache Commons parent 50 |
| JUnit Jupiter | 5.5.2 |
| Surefire | 2.22.2 |
| JaCoCo agent and CLI | 0.8.4 |
| PIT Maven plugin / engine | 1.15.2 |
| PIT JUnit 5 adapter | 1.2.2 |
| Maven dependency plugin used for preparation | 3.6.1 |
| Maven help plugin used for preparation | 3.5.1 |
| Python | 3.13.15 |
| PowerShell | 7.6.5 |
| OS | Microsoft Windows 10.0.26300; X64 |

### Complete resolved project dependency graph

```text

The following files have been resolved:
   org.junit.jupiter:junit-jupiter:jar:5.5.2:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\java-source-001-evaluation-002\maven-repository\org\junit\jupiter\junit-jupiter\5.5.2\junit-jupiter-5.5.2.jar
   org.junit.jupiter:junit-jupiter-api:jar:5.5.2:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\java-source-001-evaluation-002\maven-repository\org\junit\jupiter\junit-jupiter-api\5.5.2\junit-jupiter-api-5.5.2.jar
   org.apiguardian:apiguardian-api:jar:1.1.0:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\java-source-001-evaluation-002\maven-repository\org\apiguardian\apiguardian-api\1.1.0\apiguardian-api-1.1.0.jar
   org.opentest4j:opentest4j:jar:1.2.0:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\java-source-001-evaluation-002\maven-repository\org\opentest4j\opentest4j\1.2.0\opentest4j-1.2.0.jar
   org.junit.platform:junit-platform-commons:jar:1.5.2:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\java-source-001-evaluation-002\maven-repository\org\junit\platform\junit-platform-commons\1.5.2\junit-platform-commons-1.5.2.jar
   org.junit.jupiter:junit-jupiter-params:jar:5.5.2:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\java-source-001-evaluation-002\maven-repository\org\junit\jupiter\junit-jupiter-params\5.5.2\junit-jupiter-params-5.5.2.jar
   org.junit.jupiter:junit-jupiter-engine:jar:5.5.2:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\java-source-001-evaluation-002\maven-repository\org\junit\jupiter\junit-jupiter-engine\5.5.2\junit-jupiter-engine-5.5.2.jar
   org.junit.platform:junit-platform-engine:jar:1.5.2:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\java-source-001-evaluation-002\maven-repository\org\junit\platform\junit-platform-engine\1.5.2\junit-platform-engine-1.5.2.jar
   org.junit-pioneer:junit-pioneer:jar:0.3.0:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\java-source-001-evaluation-002\maven-repository\org\junit-pioneer\junit-pioneer\0.3.0\junit-pioneer-0.3.0.jar
   org.mockito:mockito-core:jar:3.0.0:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\java-source-001-evaluation-002\maven-repository\org\mockito\mockito-core\3.0.0\mockito-core-3.0.0.jar
   net.bytebuddy:byte-buddy:jar:1.9.10:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\java-source-001-evaluation-002\maven-repository\net\bytebuddy\byte-buddy\1.9.10\byte-buddy-1.9.10.jar
   net.bytebuddy:byte-buddy-agent:jar:1.9.10:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\java-source-001-evaluation-002\maven-repository\net\bytebuddy\byte-buddy-agent\1.9.10\byte-buddy-agent-1.9.10.jar
   org.objenesis:objenesis:jar:2.6:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\java-source-001-evaluation-002\maven-repository\org\objenesis\objenesis\2.6\objenesis-2.6.jar
   com.google.jimfs:jimfs:jar:1.1:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\java-source-001-evaluation-002\maven-repository\com\google\jimfs\jimfs\1.1\jimfs-1.1.jar
   com.google.guava:guava:jar:18.0:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\java-source-001-evaluation-002\maven-repository\com\google\guava\guava\18.0\guava-18.0.jar
   org.apache.commons:commons-lang3:jar:3.9:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\java-source-001-evaluation-002\maven-repository\org\apache\commons\commons-lang3\3.9\commons-lang3-3.9.jar
```

The companion `dependency-hashes` artifact records the exact SHA-256 and byte size of every resolved project JAR. The effective-POM artifact retains inherited configuration and plugin versions. The frozen PIT POM declares its dependency graph and exact plugin settings.

### Invoked Maven plugins and goals

| Plugin prefix emitted by Maven | Version | Goal |
| --- | --- | --- |
| animal-sniffer | 1.18 | check |
| antrun | 1.8 | run |
| apache-rat | 0.13 | check |
| build-helper | 3.0.0 | parse-version |
| buildnumber | 1.4 | create |
| bundle | 4.2.1 | manifest |
| clean | 3.1.0 | clean |
| compiler | 3.8.1 | compile |
| compiler | 3.8.1 | testCompile |
| dependency | 3.6.1 | copy |
| dependency | 3.6.1 | list |
| enforcer | 3.0.0-M2 | enforce |
| help | 3.5.1 | effective-pom |
| pitest | 1.15.2 | mutationCoverage |
| remote-resources | 1.5 | process |
| resources | 3.1.0 | resources |
| resources | 3.1.0 | testResources |
| surefire | 2.22.2 | test |

### Observed environment and executable locations

```json
{
  "observedAt": "2026-10-12T23:19:53.6154234Z",
  "java": {
    "executable": "C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-8.0.504+1\\bin\\java.exe",
    "arguments": [
      "-version"
    ],
    "exitCode": 0,
    "output": [
      "openjdk version \"1.8.0_504\"",
      "OpenJDK Runtime Environment (Temurin)(build 1.8.0_504-b01)",
      "OpenJDK 64-Bit Server VM (Temurin)(build 25.504-b01, mixed mode)"
    ]
  },
  "javac": {
    "executable": "C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-8.0.504+1\\bin\\javac.exe",
    "arguments": [
      "-version"
    ],
    "exitCode": 0,
    "output": [
      "javac 1.8.0_504"
    ]
  },
  "maven": {
    "executable": "C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\maven\\3.9.16\\apache-maven-3.9.16/bin\\mvn.cmd",
    "arguments": [
      "-version"
    ],
    "exitCode": 0,
    "output": [
      "Apache Maven 3.9.16 (2bdd9fddda4b155ebf8000e807eb73fd829a51d5)",
      "Maven home: C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\maven\\3.9.16\\apache-maven-3.9.16",
      "Java version: 1.8.0_504, vendor: Temurin, runtime: C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-8.0.504+1\\jre",
      "Default locale: en_US, platform encoding: Cp1252",
      "OS name: \"windows 11\", version: \"10.0\", arch: \"amd64\", family: \"windows\""
    ]
  },
  "python": {
    "executable": "C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\python\\3.13.15\\python.exe",
    "arguments": [
      "--version"
    ],
    "exitCode": 0,
    "output": [
      "Python 3.13.15"
    ]
  },
  "os": {
    "description": "Microsoft Windows 10.0.26300",
    "version": "Microsoft Windows NT 10.0.26300.0",
    "architecture": "X64",
    "powershell": "7.6.5"
  },
  "processEnvironment": {
    "JAVA_HOME": "C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-8.0.504+1",
    "PATH": "C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-8.0.504+1\\bin;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-25.0.4+101.0.LTS\\bin;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\maven\\3.9.16\\apache-maven-3.9.16/bin;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\node\\22.23.2;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\python\\3.13.15;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\python\\3.13.15\\Scripts;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\uv\\0.12.23;C:\\Users\\edyko\\AppData\\Local\\mise\\shims;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell;C:\\Users\\edyko\\.codex\\tmp\\arg0\\codex-arg0pgGc3k;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\libheif\\libheif\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\jxrlib\\jxrlib\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\poppler\\Library\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\bin\\override;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA App\\NvDLISR;C:\\Program Files\\dotnet\\;C:\\Users\\edyko\\AppData\\Local\\Android\\Sdk\\platform-tools;C:\\Users\\edyko\\AppData\\Local\\Android\\Sdk\\emulator;C:\\Users\\edyko\\AppData\\Local\\Android\\Sdk\\cmdline-tools\\latest\\bin;C:\\Program Files\\GitHub CLI\\;C:\\Program Files\\Docker\\Docker\\resources\\bin;C:\\Program Files\\Git\\cmd;C:\\Users\\edyko\\AppData\\Local\\codegraph\\current\\bin;C:\\Users\\edyko\\AppData\\Local\\Programs\\OpenAI\\Codex\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell;C:\\Users\\edyko\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\edyko\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Program Files\\JetBrains\\PyCharm 2026.2.1\\bin;C:\\Program Files\\JetBrains\\IntelliJ IDEA 2026.2.1\\bin;C:\\Users\\edyko\\AppData\\Local\\Microsoft\\WinGet\\Packages\\jdx.mise_Microsoft.Winget.Source_8wekyb3d8bbwe\\mise\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\bin\\fallback;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\node\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\git\\cmd;C:\\Users\\edyko\\AppData\\Local\\OpenAI\\Codex\\bin\\9a7ba4b9ea0c44a3;C:\\Users\\edyko\\AppData\\Local\\OpenAI\\Codex\\bin\\2e5e00daee91c61d",
    "MAVEN_OPTS": "-DargLine=",
    "MAVEN_ARGS": "-Dmaven.repo.local=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/maven-repository",
    "TEMP": "D:\\Projects\\experiment-workspaces\\peekable-input-stream\\.preparation\\java-source-001-evaluation-002\\temp",
    "TMP": "D:\\Projects\\experiment-workspaces\\peekable-input-stream\\.preparation\\java-source-001-evaluation-002\\temp",
    "JAVA_TOOL_OPTIONS": null,
    "JDK_JAVA_OPTIONS": null,
    "_JAVA_OPTIONS": null
  },
  "generator": {
    "model": null,
    "settings": null,
    "applicationBuild": null,
    "reason": "This is an evaluation of preserved test bytes, not a generation. Original generation settings remain unknown in the parent record."
  }
}
```

Process-only JAVA_HOME selects JDK 8, PATH prepends its bin directory, TEMP/TMP and Maven's dependency cache are on D:. Each invocation captures a fresh environment observation; the initial preparation observation above is not substituted for those observations.

### Measurement configuration

```json
{
  "schemaVersion": 1,
  "protocol": "paired-full-suite",
  "baselineCommit": "11f0abe7a3fb6954b2985ca4ab0697b2fb489e84",
  "javaRuntime": "1.8.0_504-b01",
  "javac": "1.8.0_504",
  "maven": "3.9.16",
  "surefire": "2.22.2",
  "junitJupiter": "5.5.2",
  "jacoco": "0.8.4",
  "pit": "1.15.2",
  "pitJunit5Adapter": "1.2.2",
  "targetClass": "org.apache.commons.io.input.buffer.PeekableInputStream",
  "jacocoTestSelection": "all existing project tests; add only the frozen generated file after",
  "pitTestSelection": "org.apache.commons.io.*",
  "mutationEngine": "gregor",
  "mutators": ["DEFAULTS"],
  "threads": 1,
  "timeoutFactor": 1.25,
  "timeoutConstantMilliseconds": 3000,
  "jvmArguments": ["-Xmx256m"],
  "jacocoAppend": true,
  "jacocoFreshExecutionFileRequired": true,
  "pairing": "Identical production class bytes, configuration, and existing tests; only the frozen generated test differs.",
  "mutationScore": "KILLED / total native mutants, retaining NO_COVERAGE; zero denominator is not applicable.",
  "testStrength": "KILLED / (KILLED + SURVIVED); zero denominator is not applicable.",
  "invalidMutationStatuses": ["TIMED_OUT", "RUN_ERROR", "MEMORY_ERROR", "NON_VIABLE"],
  "baselineFailurePolicy": "Preserve diagnostics and seal the evaluation incomplete; do not change scope, skip tests, or relax gates."
}
```

## Exact commands and substitutions

The following map fixes all before/after checkout, output, tool, environment, and script paths before measurement. Each request retains the exact wrapper command, scope, timestamp, declared artifact roles, and observed environment. The wrapper reserves before execution, captures both streams, and records the process exit immediately.

```json
{
  "evaluationRoot": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/002",
  "workingDirectory": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002",
  "javaHome": "C:/Users/edyko/AppData/Local/mise/installs/java/temurin-8.0.504+1",
  "agentJar": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/tools/org.jacoco.agent-0.8.4-runtime.jar",
  "cliJar": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/tools/org.jacoco.cli-0.8.4-nodeps.jar",
  "phases": {
    "jacoco-before": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/before-checkout",
      "output": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/measurements/jacoco-before",
      "build": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/pit-build/jacoco-before",
      "temp": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/temp",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/002/evidence/scripts/jacoco-before.ps1",
      "scope": "Full existing project suite; frozen generated test present only after; target production class only",
      "reports": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/before-checkout/target/surefire-reports",
      "artifacts": {
        "production-class": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/before-checkout/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class",
        "jacoco-xml": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/measurements/jacoco-before/jacoco.xml",
        "jacoco-exec": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/measurements/jacoco-before/jacoco.exec"
      }
    },
    "pit-before": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/before-checkout",
      "output": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/measurements/pit-before",
      "build": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/pit-build/pit-before",
      "temp": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/temp",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/002/evidence/scripts/pit-before.ps1",
      "scope": "Full existing project suite; frozen generated test present only after; target production class only",
      "reports": null,
      "artifacts": {
        "production-class": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/before-checkout/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class",
        "pit-mutations": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/measurements/pit-before/mutations.xml",
        "pit-linecoverage": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/measurements/pit-before/linecoverage.xml"
      }
    },
    "jacoco-after": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-002",
      "output": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/measurements/jacoco-after",
      "build": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/pit-build/jacoco-after",
      "temp": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/temp",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/002/evidence/scripts/jacoco-after.ps1",
      "scope": "Full existing project suite; frozen generated test present only after; target production class only",
      "reports": "D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-002/target/surefire-reports",
      "artifacts": {
        "production-class": "D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-002/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class",
        "jacoco-xml": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/measurements/jacoco-after/jacoco.xml",
        "jacoco-exec": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/measurements/jacoco-after/jacoco.exec"
      }
    },
    "pit-after": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-002",
      "output": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/measurements/pit-after",
      "build": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/pit-build/pit-after",
      "temp": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/temp",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/002/evidence/scripts/pit-after.ps1",
      "scope": "Full existing project suite; frozen generated test present only after; target production class only",
      "reports": null,
      "artifacts": {
        "production-class": "D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-002/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class",
        "pit-mutations": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/measurements/pit-after/mutations.xml",
        "pit-linecoverage": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/measurements/pit-after/linecoverage.xml"
      }
    },
    "preflight": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-002",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/002/evidence/scripts/preflight.ps1",
      "scope": "Fetch and verify pinned JaCoCo tools; preserve effective POM and exact resolved project dependencies; no test execution",
      "reports": null,
      "artifacts": {
        "effective-pom": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/preflight/effective-pom.xml",
        "dependencies": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/preflight/dependencies.txt",
        "dependency-hashes": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/preflight/dependency-hashes.json"
      }
    }
  }
}
```

### run-phase.ps1

```powershell
param([Parameter(Mandatory)][ValidateSet('preflight','jacoco-before','pit-before','jacoco-after','pit-after')][string]$Phase)
$ErrorActionPreference = 'Stop'
$scriptRoot = Split-Path -Parent $PSCommandPath
$evidenceRoot = Split-Path -Parent $scriptRoot
$evaluationRoot = Split-Path -Parent $evidenceRoot
$substitutions = Get-Content -LiteralPath "$evidenceRoot/substitutions.json" -Raw | ConvertFrom-Json
$assignment = $substitutions.phases.$Phase
$workingDirectory = $substitutions.workingDirectory
$env:JAVA_HOME = $substitutions.javaHome
$env:PATH = "$env:JAVA_HOME/bin;$env:PATH"
$env:TEMP = "$workingDirectory/temp"
$env:TMP = $env:TEMP
$env:MAVEN_ARGS = "-Dmaven.repo.local=$workingDirectory/maven-repository"
$env:MAVEN_OPTS = '-DargLine='
if ($Phase.StartsWith('jacoco')) {
    $env:MAVEN_OPTS = "-DargLine=-javaagent:$($substitutions.agentJar)=destfile=$($assignment.output)/jacoco.exec,append=true,includes=org.apache.commons.io.input.buffer.PeekableInputStream"
}
$environmentPath = "$workingDirectory/environments/$Phase.json"
$artifactPath = "$evidenceRoot/$Phase-artifacts.json"
if ((Test-Path -LiteralPath $environmentPath) -or (Test-Path -LiteralPath $artifactPath)) { throw 'A phase reservation input already exists.' }
& "$scriptRoot/observe-environment.ps1" -Destination $environmentPath
$assignment.artifacts | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath $artifactPath -Encoding utf8
$manager = 'D:/Projects/wit-up/tools/experiment_runs.py'
$command = "pwsh -NoProfile -File `"$($assignment.script)`""
$arguments = @($manager, 'begin', '--run', $evaluationRoot, '--phase', $Phase, '--command', $command, '--scope', $assignment.scope, '--environment', $environmentPath, '--artifacts', $artifactPath)
if ($assignment.reports) { $arguments += @('--reports', $assignment.reports) }
$reservationText = & python @arguments
$reservationExit = $LASTEXITCODE
if ($reservationExit -ne 0) { throw "Phase reservation failed ($reservationExit)." }
$reservation = $reservationText | ConvertFrom-Json
& pwsh -NoProfile -File $assignment.script *> $reservation.log
$executionExit = $LASTEXITCODE
$recordArguments = @($manager, 'record', '--run', $evaluationRoot, '--execution', $reservation.execution, '--exit-code', $executionExit)
if ($Phase -eq 'preflight') {
    $recordArguments += @('--tests-not-started', '--reason', 'Only dependency-copy, effective-POM, and dependency-list goals ran; no compilation or test goal was invoked.')
}
& python @recordArguments
if ($LASTEXITCODE -ne 0) { throw 'Execution recording failed; preserve all pending evidence.' }
Write-Output "Recorded $Phase, execution $($reservation.execution), process exit $executionExit."
exit $executionExit
```

### observe-environment.ps1

```powershell
param([Parameter(Mandatory)][string]$Destination)
$ErrorActionPreference = 'Stop'
function Observe-Version([string]$Executable, [string[]]$Arguments) {
    $command = Get-Command $Executable
    $output = @(& $command.Source @Arguments 2>&1 | ForEach-Object { $_.ToString() })
    $commandExit = $LASTEXITCODE
    if ($commandExit -ne 0) { throw "Version observation failed: $Executable ($commandExit)" }
    return [ordered]@{ executable=$command.Source; arguments=$Arguments; exitCode=$commandExit; output=$output }
}
$processSettings = [ordered]@{}
foreach ($variableName in @('JAVA_HOME','PATH','MAVEN_OPTS','MAVEN_ARGS','TEMP','TMP','JAVA_TOOL_OPTIONS','JDK_JAVA_OPTIONS','_JAVA_OPTIONS')) {
    $processSettings[$variableName] = [Environment]::GetEnvironmentVariable($variableName, 'Process')
}
$observation = [ordered]@{
    observedAt=[DateTime]::UtcNow.ToString('o')
    java=(Observe-Version 'java' @('-version'))
    javac=(Observe-Version 'javac' @('-version'))
    maven=(Observe-Version 'mvn' @('-version'))
    python=(Observe-Version 'python' @('--version'))
    os=[ordered]@{ description=[System.Runtime.InteropServices.RuntimeInformation]::OSDescription; version=[Environment]::OSVersion.VersionString; architecture=[System.Runtime.InteropServices.RuntimeInformation]::OSArchitecture.ToString(); powershell=$PSVersionTable.PSVersion.ToString() }
    processEnvironment=$processSettings
    generator=[ordered]@{ model=$null; settings=$null; applicationBuild=$null; reason='This is an evaluation of preserved test bytes, not a generation. Original generation settings remain unknown in the parent record.' }
}
$observation | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $Destination -Encoding utf8
```

### preflight.ps1

```powershell
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-002'
$env:MAVEN_OPTS = '-DargLine='
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:copy '-Dartifact=org.jacoco:org.jacoco.agent:0.8.4:jar:runtime' '-DoutputDirectory=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/tools'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:copy '-Dartifact=org.jacoco:org.jacoco.cli:0.8.4:jar:nodeps' '-DoutputDirectory=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/tools'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$expectedTools = @{ 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/tools/org.jacoco.agent-0.8.4-runtime.jar'='1a7c1dc7280e535b9b6f383915bac5afbb9208c1af2019b4e674ca590c925c22'; 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/tools/org.jacoco.cli-0.8.4-nodeps.jar'='65de07ff32bcf2f945f18180d1d10cdf0e155eee2b508519bbc5f31904cd8288' }
foreach ($toolPath in $expectedTools.Keys) {
    $actualHash = (Get-FileHash -LiteralPath $toolPath -Algorithm SHA256).Hash.ToLowerInvariant()
    Write-Output "$actualHash  $toolPath"
    if ($actualHash -ne $expectedTools[$toolPath]) { throw 'Measurement tool checksum mismatch.' }
}
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-help-plugin:3.5.1:effective-pom '-Doutput=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/preflight/effective-pom.xml'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:list '-DoutputAbsoluteArtifactFilename=true' '-DoutputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/preflight/dependencies.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$dependencyHashes = @()
foreach ($dependencyLine in Get-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/preflight/dependencies.txt') {
    $dependencyParts = $dependencyLine.Trim() -split ':', 6
    if ($dependencyParts.Count -eq 6) {
        $artifactPath = $dependencyParts[5]
        if (!(Test-Path -LiteralPath $artifactPath -PathType Leaf)) { throw "A resolved dependency is missing: $artifactPath" }
        $dependencyHashes += [ordered]@{ path=$artifactPath; sha256=(Get-FileHash -LiteralPath $artifactPath -Algorithm SHA256).Hash.ToLowerInvariant(); bytes=(Get-Item -LiteralPath $artifactPath).Length }
    }
}
if ($dependencyHashes.Count -eq 0) { throw 'No resolved dependency artifacts were captured.' }
$dependencyHashes | ConvertTo-Json -Depth 3 | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/preflight/dependency-hashes.json' -Encoding utf8
exit 0
```

### jacoco-before.ps1

```powershell
$ErrorActionPreference = 'Stop'
$phaseCheckout = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/before-checkout'
$phaseOutput = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/measurements/jacoco-before'
$agentJar = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/tools/org.jacoco.agent-0.8.4-runtime.jar'
$cliJar = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/tools/org.jacoco.cli-0.8.4-nodeps.jar'
Set-Location -LiteralPath $phaseCheckout
git rev-parse HEAD
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
git diff --quiet 11f0abe7a3fb6954b2985ca4ab0697b2fb489e84 --
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
git status --short
$executionData = Join-Path $phaseOutput 'jacoco.exec'
$coverageXml = Join-Path $phaseOutput 'jacoco.xml'
if ((Test-Path -LiteralPath $executionData) -or (Test-Path -LiteralPath $coverageXml)) { throw 'Measurement output already exists.' }
New-Item -ItemType Directory -Path $phaseOutput -Force | Out-Null
$env:MAVEN_OPTS = "-DargLine=-javaagent:$agentJar=destfile=$executionData,append=true,includes=org.apache.commons.io.input.buffer.PeekableInputStream"
mvn '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' clean test
$mavenExit = $LASTEXITCODE
Write-Output "Maven exit code: $mavenExit"
if ($mavenExit -ne 0) { exit $mavenExit }
$classFile = Join-Path $phaseCheckout 'target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class'
java -jar $cliJar report $executionData --classfiles $classFile --xml $coverageXml --name 'PeekableInputStream paired measurement'
$reportExit = $LASTEXITCODE
Write-Output "JaCoCo report exit code: $reportExit"
exit $reportExit
```

### pit-before.ps1

```powershell
$ErrorActionPreference = 'Stop'
$analysisPom = 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/002/inputs/pit-analysis-pom.xml'
$phaseCheckout = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/before-checkout'
$phaseOutput = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/measurements/pit-before'
$phaseBuild = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/pit-build/pit-before'
$temporaryDirectory = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/temp'
Set-Location -LiteralPath $phaseCheckout
$env:MAVEN_OPTS = '-DargLine='
mvn -B -ntp -f $analysisPom "-Danalysis.checkout=$phaseCheckout" "-Danalysis.output=$phaseOutput" "-Danalysis.build=$phaseBuild" "-Danalysis.temp=$temporaryDirectory" org.pitest:pitest-maven:1.15.2:mutationCoverage
$pitExit = $LASTEXITCODE
Write-Output "PIT exit code: $pitExit"
exit $pitExit
```

### jacoco-after.ps1

```powershell
$ErrorActionPreference = 'Stop'
$phaseCheckout = 'D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-002'
$phaseOutput = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/measurements/jacoco-after'
$agentJar = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/tools/org.jacoco.agent-0.8.4-runtime.jar'
$cliJar = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/tools/org.jacoco.cli-0.8.4-nodeps.jar'
Set-Location -LiteralPath $phaseCheckout
git rev-parse HEAD
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
git diff --quiet 11f0abe7a3fb6954b2985ca4ab0697b2fb489e84 --
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
git status --short
$executionData = Join-Path $phaseOutput 'jacoco.exec'
$coverageXml = Join-Path $phaseOutput 'jacoco.xml'
if ((Test-Path -LiteralPath $executionData) -or (Test-Path -LiteralPath $coverageXml)) { throw 'Measurement output already exists.' }
New-Item -ItemType Directory -Path $phaseOutput -Force | Out-Null
$env:MAVEN_OPTS = "-DargLine=-javaagent:$agentJar=destfile=$executionData,append=true,includes=org.apache.commons.io.input.buffer.PeekableInputStream"
mvn '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' clean test
$mavenExit = $LASTEXITCODE
Write-Output "Maven exit code: $mavenExit"
if ($mavenExit -ne 0) { exit $mavenExit }
$classFile = Join-Path $phaseCheckout 'target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class'
java -jar $cliJar report $executionData --classfiles $classFile --xml $coverageXml --name 'PeekableInputStream paired measurement'
$reportExit = $LASTEXITCODE
Write-Output "JaCoCo report exit code: $reportExit"
exit $reportExit
```

### pit-after.ps1

```powershell
$ErrorActionPreference = 'Stop'
$analysisPom = 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/002/inputs/pit-analysis-pom.xml'
$phaseCheckout = 'D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-002'
$phaseOutput = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/measurements/pit-after'
$phaseBuild = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/pit-build/pit-after'
$temporaryDirectory = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-002/temp'
Set-Location -LiteralPath $phaseCheckout
$env:MAVEN_OPTS = '-DargLine='
mvn -B -ntp -f $analysisPom "-Danalysis.checkout=$phaseCheckout" "-Danalysis.output=$phaseOutput" "-Danalysis.build=$phaseBuild" "-Danalysis.temp=$temporaryDirectory" org.pitest:pitest-maven:1.15.2:mutationCoverage
$pitExit = $LASTEXITCODE
Write-Output "PIT exit code: $pitExit"
exit $pitExit
```

## Pairing and preservation

Observed target-class hashes: `7ab6a91f3618ccf5949692f1fc5d39b97174deab23925f872f0e31cb5a2591a1`.
The preserved script inventory fixes rendered script hashes before execution. The before checkout contains no generated target test; the after checkout contains exactly the parent frozen bytes. Metadata-only Git checks and the manager verify the baseline and original test hash. Missing PIT mutant XML prevents mutant-universe equality from being established.

## Complete frozen Java source

```java
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.apache.commons.io.input.buffer;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertSame;
import static org.junit.jupiter.api.Assertions.assertThrows;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

/**
 * Exception tests for the declared constructors and peek overloads.
 * Fixtures use only memory streams and require no external resources.
 */
public class PeekableInputStreamTest {

    /** Tests null input validation in the default-size constructor. */
    @Test
    public void defaultConstructorRejectsNullInput() {
        // Arrange
        final InputStream input = null;

        // Act and Assert
        final NullPointerException exception = assertThrows(NullPointerException.class,
                () -> new PeekableInputStream(input));
        assertEquals("InputStream", exception.getMessage());
    }

    /** Tests that null input validation precedes invalid buffer-size validation. */
    @Test
    public void sizedConstructorRejectsNullInputBeforeInvalidBufferSize() {
        // Arrange
        final InputStream input = null;
        final int bufferSize = 0;

        // Act and Assert
        final NullPointerException exception = assertThrows(NullPointerException.class,
                () -> new PeekableInputStream(input, bufferSize));
        assertEquals("InputStream", exception.getMessage());
    }

    /**
     * Tests both the zero boundary and the negative side of the size guard.
     * @param bufferSize the nonpositive internal buffer size
     */
    @ParameterizedTest
    @ValueSource(ints = {0, -1})
    public void sizedConstructorRejectsNonpositiveBufferSize(final int bufferSize) {
        // Arrange
        final InputStream input = new ByteArrayInputStream(new byte[0]);

        // Act and Assert
        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class,
                () -> new PeekableInputStream(input, bufferSize));
        assertEquals("Invalid buffer size: " + bufferSize, exception.getMessage());
    }

    /** Tests null array validation for the whole-array overload. */
    @Test
    public void peekArrayRejectsNullBuffer() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1);
        final byte[] requested = null;

        // Act and Assert
        final NullPointerException exception = assertThrows(NullPointerException.class, () -> stream.peek(requested));
        assertEquals("Buffer", exception.getMessage());
    }

    /** Tests null validation before slice validation. */
    @Test
    public void peekSliceRejectsNullBufferBeforeInvalidSlice() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1);
        final byte[] requested = null;

        // Act and Assert
        final NullPointerException exception = assertThrows(NullPointerException.class,
                () -> stream.peek(requested, -1, -1));
        assertEquals("Buffer", exception.getMessage());
    }

    /** Tests the whole-array size guard. */
    @Test
    public void peekArrayRejectsArrayLargerThanInternalBuffer() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1);
        final byte[] requested = new byte[2];

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(requested));
    }

    /** Tests that the sliced overload checks the entire array even for an empty slice. */
    @Test
    public void peekSliceRejectsOversizedArrayEvenForZeroLength() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1);
        final byte[] requested = new byte[2];

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(requested, 0, 0));
    }

    /** Tests the delegated offset guard for an empty whole array. */
    @Test
    public void peekArrayRejectsEmptyArrayAtDelegatedOffsetGuard() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1);
        final byte[] requested = new byte[0];

        // Act and Assert
        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class, () -> stream.peek(requested));
        assertEquals("Invalid offset: 0", exception.getMessage());
    }

    /** Tests the delegated offset guard for an empty sliced array. */
    @Test
    public void peekSliceRejectsEmptyArrayAtDelegatedOffsetGuard() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1);
        final byte[] requested = new byte[0];

        // Act and Assert
        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class,
                () -> stream.peek(requested, 0, 0));
        assertEquals("Invalid offset: 0", exception.getMessage());
    }

    /**
     * Tests both sides of offset validation before negative-length validation.
     * @param offset the negative offset or the array-length boundary
     */
    @ParameterizedTest
    @ValueSource(ints = {-1, 1})
    public void peekSliceRejectsInvalidOffsetBeforeInvalidLength(final int offset) {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[] {0}), 1);
        final byte[] requested = new byte[] {0};

        // Act and Assert
        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class,
                () -> stream.peek(requested, offset, -1));
        assertEquals("Invalid offset: " + offset, exception.getMessage());
    }

    /** Tests negative-length validation after a valid offset. */
    @Test
    public void peekSliceRejectsNegativeLength() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[] {0}), 1);
        final byte[] requested = new byte[] {0};

        // Act and Assert
        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class,
                () -> stream.peek(requested, 0, -1));
        assertEquals("Invalid length: -1", exception.getMessage());
    }

    /** Tests the delegated length guard against internal capacity. */
    @Test
    public void peekSliceRejectsLengthLargerThanInternalBuffer() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[] {0}), 1);
        final byte[] requested = new byte[] {0};

        // Act and Assert
        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class,
                () -> stream.peek(requested, 0, 2));
        assertEquals("Invalid length: 2", exception.getMessage());
    }

    /**
     * Tests original read-failure propagation immediately and after one byte is buffered.
     * @param prefixLength the number of successful one-byte reads before failure
     */
    @ParameterizedTest
    @ValueSource(ints = {0, 1})
    public void peekArrayPropagatesReadFailureDuringRefill(final int prefixLength) {
        // Arrange
        final IOException failure = new IOException("Fixture read failure");
        final InputStream input = new PrefixThenFailInputStream(prefixLength, failure);
        final PeekableInputStream stream = new PeekableInputStream(input, 2);
        final byte[] requested = new byte[2];

        // Act and Assert
        final IOException exception = assertThrows(IOException.class, () -> stream.peek(requested));
        assertSame(failure, exception);
    }

    /**
     * Tests that read failures precede delegated offset and length validation.
     * @param prefixLength the number of successful one-byte reads before failure
     */
    @ParameterizedTest
    @ValueSource(ints = {0, 1})
    public void peekSlicePropagatesReadFailureBeforeInvalidSlice(final int prefixLength) {
        // Arrange
        final IOException failure = new IOException("Fixture read failure");
        final InputStream input = new PrefixThenFailInputStream(prefixLength, failure);
        final PeekableInputStream stream = new PeekableInputStream(input, 2);
        final byte[] requested = new byte[2];

        // Act and Assert
        final IOException exception = assertThrows(IOException.class, () -> stream.peek(requested, -1, -1));
        assertSame(failure, exception);
    }

    /**
     * Tests slice-array overrun after a matching prefix, with an empty or full internal buffer.
     * @param inputLength zero for immediate end of input, or two for a full buffer
     */
    @ParameterizedTest
    @ValueSource(ints = {0, 2})
    public void peekSlicePropagatesArrayBoundsFailureAfterMatchingPrefix(final int inputLength) {
        // Arrange
        // Zero-filled input and request arrays prevent an earlier comparison mismatch.
        // With empty input, the internal array also retains its initial zero values.
        final InputStream input = new ByteArrayInputStream(new byte[inputLength]);
        final PeekableInputStream stream = new PeekableInputStream(input, 2);
        final byte[] requested = new byte[2];

        // Act and Assert
        assertThrows(ArrayIndexOutOfBoundsException.class, () -> stream.peek(requested, 1, 2));
    }

    /** Supplies a small zero-byte prefix followed by the same checked read failure. */
    private static final class PrefixThenFailInputStream extends InputStream {
        private int remainingBytes;
        private final IOException failure;

        private PrefixThenFailInputStream(final int prefixLength, final IOException failure) {
            remainingBytes = prefixLength;
            this.failure = failure;
        }

        @Override
        public int read() throws IOException {
            if (remainingBytes > 0) {
                remainingBytes--;
                return 0;
            }
            throw failure;
        }

        @Override
        public int read(final byte[] bytes, final int offset, final int length) throws IOException {
            final int value = read();
            bytes[offset] = (byte) value;
            return 1;
        }
    }
}
```
