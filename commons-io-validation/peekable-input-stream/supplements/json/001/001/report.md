# JSON-source exception-test evaluation

All four measurement processes succeeded.

## Identity and scope

- Parent generation: `runs/json/001`; exact seal SHA-256 `482c9deffe47d4fc69f8fee5e4380610991893d447a38fe0ca6973baece488fd`.
- Evaluation: `json-001/evaluation-001`; independent generation contribution: 0.
- Baseline commit: `11f0abe7a3fb6954b2985ca4ab0697b2fb489e84`.
- Frozen test SHA-256: `a29b1141af4aa61b9081d22e2056f69596e5ec602062773a4618b5567c3de926`.
- Historical authorized JDK 8 supplemental execution: 10 executed tests, 0 failures, 0 errors, 0 skips. The original generation and its diagnostics remain immutable.
- The canonical paired-full-suite plan selects every existing project test on both sides and adds only the frozen generated test after. The target production class alone is measured and mutated.
- The historical JSON-source record lacks exact generator settings, a machine attestation of fresh-chat isolation, and the original freeze timestamp. This measurement does not retroactively establish those facts or analyzed-JAR/WIT-UP provenance.
- This evaluation uses the exact revision-4 recipes from java-source-001/evaluation-005 with only evaluation-owned paths substituted. Native measurements here replace the historical narrower-scope measurements for the consolidated comparison; the original historical evidence is preserved.
- The prescribed generation command was `mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" "-Dtest=org.apache.commons.io.input.buffer.PeekableInputStreamTest" clean test`; the historical authorized JDK 8 supplemental execution exited 0 with 10 passed tests.

## Before and after JaCoCo

| Counter | Before: covered / total | After: covered / total | Before missed | After missed |
| --- | --- | --- | --- | --- |
| INSTRUCTION | 0/98 (0.00%) | 77/98 (78.57%) | 98 | 21 |
| BRANCH | 0/8 (0.00%) | 7/8 (87.50%) | 8 | 1 |
| LINE | 0/16 (0.00%) | 11/16 (68.75%) | 16 | 5 |
| COMPLEXITY | 0/8 (0.00%) | 6/8 (75.00%) | 8 | 2 |
| METHOD | 0/4 (0.00%) | 3/4 (75.00%) | 4 | 1 |
| CLASS | 0/1 (0.00%) | 1/1 (100.00%) | 1 | 0 |

The before values above come from this evaluation's native measurement, rather than an inferred baseline. JaCoCo line/branch counters and PIT line counters are separate observations. JaCoCo does not count exception handling as branches; see the [official counter definitions](https://www.jacoco.org/jacoco/trunk/doc/counters.html).

## Before and after PIT

| Observation | Before | After |
| --- | --- | --- |
| KILLED | 0 | 1 |
| NO_COVERAGE | 14 | 5 |
| SURVIVED | 0 | 8 |
| Native mutants | 14 | 14 |
| Cumulative mutation-test executions | 0 | 26 |
| Native target line coverage | 0/16 (0.00%) | 13/16 (81.25%) |
| Mutation score: KILLED / total | 0/14 (0.00%) | 1/14 (7.14%) |
| Test strength: KILLED / (KILLED + SURVIVED) | N/A | 1/9 (11.11%) |

No mutation score or zero baseline is inferred from a failed baseline-validation process or absent native XML. PIT cumulative executions do not represent unique generated tests. Coverage and mutation scores do not establish completeness or correctness against an independent specification. See [PIT's official concepts](https://pitest.org/quickstart/basic_concepts/).
The baseline console's `Test strength 100%` is PIT's zero-denominator display convention. Under the frozen protocol, 0 / (0 + 0) is not applicable, so the report records N/A and preserves the original console output. PIT target line counts above come from the native CLI summary; its per-test line-coverage XML is retained independently.

## Executions and diagnostics

| Phase | Process exit | Native tests | Failures | Errors | Skips | Surefire suite attribution |
| --- | --- | --- | --- | --- | --- | --- |
| preflight | 0 | 0 | 0 | 0 | 0 | not_started |
| jacoco-before | 0 | 1541 | 0 | 0 | 6 | passed |
| pit-before | 0 | Unknown | Unknown | Unknown | Unknown | unknown |
| jacoco-after | 0 | 1551 | 0 | 0 | 6 | passed |
| pit-after | 0 | Unknown | Unknown | Unknown | Unknown | unknown |

Surefire counts are losslessly archived per execution. Intrinsic existing skips remain visible. PIT has no Surefire report destination; its process diagnostics and native mutation artifacts are retained separately. Infrastructure operations and missing measurements are not included as failures of the 10 generated tests.

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
| PIT CLI / entry / core | 1.15.2 |
| PIT JUnit 5 adapter | 1.2.2 |
| Maven dependency plugin used for preparation | 3.6.1 |
| Maven help plugin used for preparation | 3.5.1 |
| Python | 3.13.15 |
| PowerShell | 7.6.5 |
| OS | Microsoft Windows 10.0.26300; X64 |

### Complete resolved project dependency graph

```text

The following files have been resolved:
   org.junit.jupiter:junit-jupiter:jar:5.5.2:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\org\junit\jupiter\junit-jupiter\5.5.2\junit-jupiter-5.5.2.jar
   org.junit.jupiter:junit-jupiter-api:jar:5.5.2:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\org\junit\jupiter\junit-jupiter-api\5.5.2\junit-jupiter-api-5.5.2.jar
   org.apiguardian:apiguardian-api:jar:1.1.0:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\org\apiguardian\apiguardian-api\1.1.0\apiguardian-api-1.1.0.jar
   org.opentest4j:opentest4j:jar:1.2.0:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\org\opentest4j\opentest4j\1.2.0\opentest4j-1.2.0.jar
   org.junit.platform:junit-platform-commons:jar:1.5.2:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\org\junit\platform\junit-platform-commons\1.5.2\junit-platform-commons-1.5.2.jar
   org.junit.jupiter:junit-jupiter-params:jar:5.5.2:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\org\junit\jupiter\junit-jupiter-params\5.5.2\junit-jupiter-params-5.5.2.jar
   org.junit.jupiter:junit-jupiter-engine:jar:5.5.2:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\org\junit\jupiter\junit-jupiter-engine\5.5.2\junit-jupiter-engine-5.5.2.jar
   org.junit.platform:junit-platform-engine:jar:1.5.2:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\org\junit\platform\junit-platform-engine\1.5.2\junit-platform-engine-1.5.2.jar
   org.junit-pioneer:junit-pioneer:jar:0.3.0:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\org\junit-pioneer\junit-pioneer\0.3.0\junit-pioneer-0.3.0.jar
   org.mockito:mockito-core:jar:3.0.0:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\org\mockito\mockito-core\3.0.0\mockito-core-3.0.0.jar
   net.bytebuddy:byte-buddy:jar:1.9.10:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\net\bytebuddy\byte-buddy\1.9.10\byte-buddy-1.9.10.jar
   net.bytebuddy:byte-buddy-agent:jar:1.9.10:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\net\bytebuddy\byte-buddy-agent\1.9.10\byte-buddy-agent-1.9.10.jar
   org.objenesis:objenesis:jar:2.6:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\org\objenesis\objenesis\2.6\objenesis-2.6.jar
   com.google.jimfs:jimfs:jar:1.1:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\com\google\jimfs\jimfs\1.1\jimfs-1.1.jar
   com.google.guava:guava:jar:18.0:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\com\google\guava\guava\18.0\guava-18.0.jar
   org.apache.commons:commons-lang3:jar:3.9:test:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\org\apache\commons\commons-lang3\3.9\commons-lang3-3.9.jar
```

The companion `dependency-hashes` artifact records the exact SHA-256 and byte size of every resolved project JAR. The effective-POM artifact retains inherited configuration and plugin versions. The frozen CLI POM declares the launcher dependency graph. Exact invocation flags are preserved in the plan and rendered scripts; the earlier auxiliary mutation POM remains a recipe reference and is not invoked by this pair.

### Complete PIT launcher dependency graph

```text

The following files have been resolved:
   org.pitest:pitest-command-line:jar:1.15.2:compile:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\org\pitest\pitest-command-line\1.15.2\pitest-command-line-1.15.2.jar
   org.pitest:pitest-entry:jar:1.15.2:compile:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\org\pitest\pitest-entry\1.15.2\pitest-entry-1.15.2.jar
   org.pitest:pitest:jar:1.15.2:compile:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\org\pitest\pitest\1.15.2\pitest-1.15.2.jar
   org.apache.commons:commons-text:jar:1.10.0:compile:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\org\apache\commons\commons-text\1.10.0\commons-text-1.10.0.jar
   org.apache.commons:commons-lang3:jar:3.12.0:compile:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\org\apache\commons\commons-lang3\3.12.0\commons-lang3-3.12.0.jar
   org.pitest:pitest-junit5-plugin:jar:1.2.2:compile:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\org\pitest\pitest-junit5-plugin\1.2.2\pitest-junit5-plugin-1.2.2.jar
   org.junit.platform:junit-platform-launcher:jar:1.5.2:compile:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\org\junit\platform\junit-platform-launcher\1.5.2\junit-platform-launcher-1.5.2.jar
   org.apiguardian:apiguardian-api:jar:1.1.0:compile:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\org\apiguardian\apiguardian-api\1.1.0\apiguardian-api-1.1.0.jar
   org.junit.platform:junit-platform-engine:jar:1.5.2:compile:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\org\junit\platform\junit-platform-engine\1.5.2\junit-platform-engine-1.5.2.jar
   org.opentest4j:opentest4j:jar:1.2.0:compile:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\org\opentest4j\opentest4j\1.2.0\opentest4j-1.2.0.jar
   org.junit.platform:junit-platform-commons:jar:1.5.2:compile:D:\Projects\experiment-workspaces\peekable-input-stream\.working\json-001-evaluation-001\maven-repository\org\junit\platform\junit-platform-commons\1.5.2\junit-platform-commons-1.5.2.jar
```

The captured runtime-hashes artifact records all project and launcher JAR bytes. Launcher dependencies (including Commons Text 1.10.0 and its Commons Lang 3.12.0 dependency) are distinguished from the baseline project's Commons Lang 3.9. Classpath files preserve the actual ordered entries and before/after directory substitutions.

### Pinned PIT CLI dependency configuration

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>org.apache.commons</groupId>
  <artifactId>peekable-input-stream-mutation-launcher</artifactId>
  <version>1.0</version>
  <dependencies>
    <dependency><groupId>org.pitest</groupId><artifactId>pitest-command-line</artifactId><version>1.15.2</version></dependency>
    <dependency><groupId>org.pitest</groupId><artifactId>pitest-junit5-plugin</artifactId><version>1.2.2</version></dependency>
    <dependency><groupId>org.junit.platform</groupId><artifactId>junit-platform-launcher</artifactId><version>1.5.2</version></dependency>
  </dependencies>
</project>
```


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
| dependency | 3.6.1 | build-classpath |
| dependency | 3.6.1 | copy |
| dependency | 3.6.1 | list |
| enforcer | 3.0.0-M2 | enforce |
| help | 3.5.1 | effective-pom |
| remote-resources | 1.5 | process |
| resources | 3.1.0 | resources |
| resources | 3.1.0 | testResources |
| surefire | 2.22.2 | test |

### Observed environment and executable locations

```json
{
  "observedAt": "2026-10-13T01:00:45.7609866Z",
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
    "executable": "C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\maven\\3.9.16\\apache-maven-3.9.16\\bin\\mvn.cmd",
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
    "executable": "D:\\Projects\\wit-up\\.venv\\Scripts\\python.exe",
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
    "PATH": "C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-8.0.504+1\\bin;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\maven\\3.9.16\\apache-maven-3.9.16\\bin;D:\\Projects\\wit-up\\.venv\\Scripts;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-25.0.4+101.0.LTS\\bin;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\maven\\3.9.16\\apache-maven-3.9.16/bin;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\node\\22.23.2;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\python\\3.13.15;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\python\\3.13.15\\Scripts;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\uv\\0.12.23;C:\\Users\\edyko\\AppData\\Local\\mise\\shims;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell;C:\\Users\\edyko\\.codex\\tmp\\arg0\\codex-arg0pgGc3k;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\libheif\\libheif\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\jxrlib\\jxrlib\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\poppler\\Library\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\bin\\override;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA App\\NvDLISR;C:\\Program Files\\dotnet\\;C:\\Users\\edyko\\AppData\\Local\\Android\\Sdk\\platform-tools;C:\\Users\\edyko\\AppData\\Local\\Android\\Sdk\\emulator;C:\\Users\\edyko\\AppData\\Local\\Android\\Sdk\\cmdline-tools\\latest\\bin;C:\\Program Files\\GitHub CLI\\;C:\\Program Files\\Docker\\Docker\\resources\\bin;C:\\Program Files\\Git\\cmd;C:\\Users\\edyko\\AppData\\Local\\codegraph\\current\\bin;C:\\Users\\edyko\\AppData\\Local\\Programs\\OpenAI\\Codex\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell;C:\\Users\\edyko\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\edyko\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Program Files\\JetBrains\\PyCharm 2026.2.1\\bin;C:\\Program Files\\JetBrains\\IntelliJ IDEA 2026.2.1\\bin;C:\\Users\\edyko\\AppData\\Local\\Microsoft\\WinGet\\Packages\\jdx.mise_Microsoft.Winget.Source_8wekyb3d8bbwe\\mise\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\bin\\fallback;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\node\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\git\\cmd;C:\\Users\\edyko\\AppData\\Local\\OpenAI\\Codex\\bin\\9a7ba4b9ea0c44a3;C:\\Users\\edyko\\AppData\\Local\\OpenAI\\Codex\\bin\\2e5e00daee91c61d",
    "MAVEN_OPTS": "-DargLine=",
    "MAVEN_ARGS": null,
    "TEMP": "D:\\Projects\\experiment-workspaces\\peekable-input-stream\\.preparation\\json-001-evaluation-001\\temp",
    "TMP": "D:\\Projects\\experiment-workspaces\\peekable-input-stream\\.preparation\\json-001-evaluation-001\\temp",
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
  "configurationRevision": 4,
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
  "pitSourceDiscovery": "Use the assigned checkout's src/main/java and src/test/java, with compiled outputs from its own preceding JaCoCo build.",
  "pitLauncher": "PIT 1.15.2 command-line launcher executed natively from the phase checkout; both native and Java relative fixture roots match Surefire.",
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
  "evaluationRoot": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001",
  "workingDirectory": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001",
  "javaHome": "C:/Users/edyko/AppData/Local/mise/installs/java/temurin-8.0.504+1",
  "agentJar": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/tools/org.jacoco.agent-0.8.4-runtime.jar",
  "cliJar": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/tools/org.jacoco.cli-0.8.4-nodeps.jar",
  "phases": {
    "jacoco-before": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/before-checkout",
      "output": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/jacoco-before",
      "build": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/pit-build/jacoco-before",
      "temp": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/temp",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/jacoco-before.ps1",
      "scope": "Full existing project suite; frozen generated test present only after; target production class only",
      "reports": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/before-checkout/target/surefire-reports",
      "artifacts": {
        "production-class": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/before-checkout/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class",
        "jacoco-xml": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/jacoco-before/jacoco.xml",
        "jacoco-exec": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/jacoco-before/jacoco.exec"
      }
    },
    "pit-before": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/before-checkout",
      "output": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/pit-before",
      "build": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/pit-build/pit-before",
      "temp": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/temp",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/pit-before.ps1",
      "scope": "Full existing project suite; frozen generated test present only after; target production class only",
      "reports": null,
      "artifacts": {
        "production-class": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/before-checkout/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class",
        "pit-mutations": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/pit-before/mutations.xml",
        "pit-linecoverage": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/pit-before/linecoverage.xml"
      },
      "phaseClasspathFile": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/pit-before-classpath.txt",
      "toolClasspathFile": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/tool-classpath.txt"
    },
    "jacoco-after": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001",
      "output": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/jacoco-after",
      "build": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/pit-build/jacoco-after",
      "temp": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/temp",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/jacoco-after.ps1",
      "scope": "Full existing project suite; frozen generated test present only after; target production class only",
      "reports": "D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001/target/surefire-reports",
      "artifacts": {
        "production-class": "D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class",
        "jacoco-xml": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/jacoco-after/jacoco.xml",
        "jacoco-exec": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/jacoco-after/jacoco.exec"
      }
    },
    "pit-after": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001",
      "output": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/pit-after",
      "build": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/pit-build/pit-after",
      "temp": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/temp",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/pit-after.ps1",
      "scope": "Full existing project suite; frozen generated test present only after; target production class only",
      "reports": null,
      "artifacts": {
        "production-class": "D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class",
        "pit-mutations": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/pit-after/mutations.xml",
        "pit-linecoverage": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/pit-after/linecoverage.xml"
      },
      "phaseClasspathFile": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/pit-after-classpath.txt",
      "toolClasspathFile": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/tool-classpath.txt"
    },
    "preflight": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/preflight.ps1",
      "scope": "Fetch and verify pinned JaCoCo tools; preserve effective POM and exact resolved project dependencies; no test execution",
      "reports": null,
      "artifacts": {
        "effective-pom": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/effective-pom.xml",
        "dependencies": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/dependencies.txt",
        "dependency-hashes": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/dependency-hashes.json",
        "launcher-classpath": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/tool-classpath.txt",
        "project-classpath": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/project-classpath.txt",
        "launcher-effective-pom": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/launcher-effective-pom.xml",
        "launcher-dependencies": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/launcher-dependencies.txt",
        "runtime-hashes": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/runtime-hashes.json",
        "before-classpath": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/pit-before-classpath.txt",
        "after-classpath": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/pit-after-classpath.txt"
      }
    }
  },
  "pitLauncherPom": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/inputs/pit-cli-pom.xml"
}
```


### Support tool versions

```json
{
  "uv": [
    "uv 0.12.23 (46b84fd0b 2026-10-03 x86_64-pc-windows-msvc)"
  ],
  "git": [
    "git version 2.56.0.windows.2"
  ],
  "ruff": [
    "ruff 0.16.10"
  ],
  "pyright": [
    "pyright 1.1.414"
  ]
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
Set-Location -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001'
$env:MAVEN_OPTS = '-DargLine='
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:copy '-Dartifact=org.jacoco:org.jacoco.agent:0.8.4:jar:runtime' '-DoutputDirectory=D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/tools'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:copy '-Dartifact=org.jacoco:org.jacoco.cli:0.8.4:jar:nodeps' '-DoutputDirectory=D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/tools'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$expectedTools = @{ 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/tools/org.jacoco.agent-0.8.4-runtime.jar'='1a7c1dc7280e535b9b6f383915bac5afbb9208c1af2019b4e674ca590c925c22'; 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/tools/org.jacoco.cli-0.8.4-nodeps.jar'='65de07ff32bcf2f945f18180d1d10cdf0e155eee2b508519bbc5f31904cd8288' }
foreach ($toolPath in $expectedTools.Keys) {
    $actualHash = (Get-FileHash -LiteralPath $toolPath -Algorithm SHA256).Hash.ToLowerInvariant()
    Write-Output "$actualHash  $toolPath"
    if ($actualHash -ne $expectedTools[$toolPath]) { throw 'Measurement tool checksum mismatch.' }
}
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-help-plugin:3.5.1:effective-pom '-Doutput=D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/effective-pom.xml'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:list '-DoutputAbsoluteArtifactFilename=true' '-DoutputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/dependencies.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$dependencyHashes = @()
foreach ($dependencyLine in Get-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/dependencies.txt') {
    $dependencyParts = $dependencyLine.Trim() -split ':', 6
    if ($dependencyParts.Count -eq 6) {
        $artifactPath = $dependencyParts[5]
        if (!(Test-Path -LiteralPath $artifactPath -PathType Leaf)) { throw "A resolved dependency is missing: $artifactPath" }
        $dependencyHashes += [ordered]@{ path=$artifactPath; sha256=(Get-FileHash -LiteralPath $artifactPath -Algorithm SHA256).Hash.ToLowerInvariant(); bytes=(Get-Item -LiteralPath $artifactPath).Length }
    }
}
if ($dependencyHashes.Count -eq 0) { throw 'No resolved dependency artifacts were captured.' }
$dependencyHashes | ConvertTo-Json -Depth 3 | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/dependency-hashes.json' -Encoding utf8
mvn -B -ntp -f 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/inputs/pit-cli-pom.xml' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:build-classpath '-Dmdep.outputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/tool-classpath.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:build-classpath '-DincludeScope=test' '-Dmdep.outputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/project-classpath.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp -f 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/inputs/pit-cli-pom.xml' org.apache.maven.plugins:maven-help-plugin:3.5.1:effective-pom '-Doutput=D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/launcher-effective-pom.xml'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp -f 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/inputs/pit-cli-pom.xml' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:list '-DoutputAbsoluteArtifactFilename=true' '-DoutputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/launcher-dependencies.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$toolClasspath = (Get-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/tool-classpath.txt' -Raw).Trim()
$projectClasspath = (Get-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/project-classpath.txt' -Raw).Trim()
java -cp $toolClasspath org.pitest.mutationtest.commandline.MutationCoverageReport -h
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$runtimeArtifacts = @($projectClasspath -split ';') + @($toolClasspath -split ';')
$runtimeHashes = @()
foreach ($artifactPath in @($runtimeArtifacts | Select-Object -Unique)) {
    $runtimeHashes += [ordered]@{ path=$artifactPath; sha256=(Get-FileHash -LiteralPath $artifactPath -Algorithm SHA256).Hash.ToLowerInvariant(); bytes=(Get-Item -LiteralPath $artifactPath).Length }
}
$runtimeHashes | ConvertTo-Json -Depth 3 | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/runtime-hashes.json' -Encoding utf8
$phaseClasspath = @('D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/before-checkout/target/classes', 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/before-checkout/target/test-classes') + $runtimeArtifacts
$phaseClasspath | Select-Object -Unique | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/pit-before-classpath.txt' -Encoding utf8NoBOM
$phaseClasspath = @('D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001/target/classes', 'D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001/target/test-classes') + $runtimeArtifacts
$phaseClasspath | Select-Object -Unique | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/pit-after-classpath.txt' -Encoding utf8NoBOM
exit 0
```

### jacoco-before.ps1

```powershell
$ErrorActionPreference = 'Stop'
$phaseCheckout = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/before-checkout'
$phaseOutput = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/jacoco-before'
$agentJar = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/tools/org.jacoco.agent-0.8.4-runtime.jar'
$cliJar = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/tools/org.jacoco.cli-0.8.4-nodeps.jar'
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
$phaseCheckout = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/before-checkout'
$phaseOutput = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/pit-before'
$temporaryDirectory = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/temp'
$phaseClasspathFile = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/pit-before-classpath.txt'
$toolClasspathFile = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/tool-classpath.txt'
Set-Location -LiteralPath $phaseCheckout
git rev-parse HEAD
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
git diff --quiet 11f0abe7a3fb6954b2985ca4ab0697b2fb489e84 --
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$preflight = Get-Content -LiteralPath 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/executions/001/result.json' -Raw | ConvertFrom-Json
foreach ($role in @('before-classpath', 'launcher-classpath')) {
    $path = if ($role -eq 'launcher-classpath') { $toolClasspathFile } else { $phaseClasspathFile }
    if ((Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant() -ne $preflight.artifacts.$role.sha256) { throw 'A captured PIT classpath changed.' }
}
$toolClasspath = (Get-Content -LiteralPath $toolClasspathFile -Raw).Trim()
$env:MAVEN_OPTS = '-DargLine='
Write-Output "PIT native launch location: $((Get-Location).Path)"
java '-XshowSettings:properties' -version
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
java "-Djava.io.tmpdir=$temporaryDirectory" -cp $toolClasspath org.pitest.mutationtest.commandline.MutationCoverageReport --reportDir $phaseOutput --targetClasses org.apache.commons.io.input.buffer.PeekableInputStream --targetTests 'org.apache.commons.io.*' --sourceDirs "$phaseCheckout/src/main/java" --classPathFile $phaseClasspathFile --includeLaunchClasspath false --mutationEngine gregor --mutators DEFAULTS --threads 1 --timeoutFactor 1.25 --timeoutConst 3000 --jvmArgs "-Xmx256m,-Djava.io.tmpdir=$temporaryDirectory" --outputFormats XML --timestampedReports false --exportLineCoverage true --failWhenNoMutations true --skipFailingTests false --projectBase $phaseCheckout --inputEncoding UTF-8 --outputEncoding UTF-8
$pitExit = $LASTEXITCODE
Write-Output "PIT exit code: $pitExit"
exit $pitExit
```

### jacoco-after.ps1

```powershell
$ErrorActionPreference = 'Stop'
$phaseCheckout = 'D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001'
$phaseOutput = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/jacoco-after'
$agentJar = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/tools/org.jacoco.agent-0.8.4-runtime.jar'
$cliJar = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/tools/org.jacoco.cli-0.8.4-nodeps.jar'
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
$phaseCheckout = 'D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001'
$phaseOutput = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/pit-after'
$temporaryDirectory = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/temp'
$phaseClasspathFile = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/pit-after-classpath.txt'
$toolClasspathFile = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/tool-classpath.txt'
Set-Location -LiteralPath $phaseCheckout
git rev-parse HEAD
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
git diff --quiet 11f0abe7a3fb6954b2985ca4ab0697b2fb489e84 --
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$preflight = Get-Content -LiteralPath 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/executions/001/result.json' -Raw | ConvertFrom-Json
foreach ($role in @('after-classpath', 'launcher-classpath')) {
    $path = if ($role -eq 'launcher-classpath') { $toolClasspathFile } else { $phaseClasspathFile }
    if ((Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant() -ne $preflight.artifacts.$role.sha256) { throw 'A captured PIT classpath changed.' }
}
$toolClasspath = (Get-Content -LiteralPath $toolClasspathFile -Raw).Trim()
$env:MAVEN_OPTS = '-DargLine='
Write-Output "PIT native launch location: $((Get-Location).Path)"
java '-XshowSettings:properties' -version
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
java "-Djava.io.tmpdir=$temporaryDirectory" -cp $toolClasspath org.pitest.mutationtest.commandline.MutationCoverageReport --reportDir $phaseOutput --targetClasses org.apache.commons.io.input.buffer.PeekableInputStream --targetTests 'org.apache.commons.io.*' --sourceDirs "$phaseCheckout/src/main/java" --classPathFile $phaseClasspathFile --includeLaunchClasspath false --mutationEngine gregor --mutators DEFAULTS --threads 1 --timeoutFactor 1.25 --timeoutConst 3000 --jvmArgs "-Xmx256m,-Djava.io.tmpdir=$temporaryDirectory" --outputFormats XML --timestampedReports false --exportLineCoverage true --failWhenNoMutations true --skipFailingTests false --projectBase $phaseCheckout --inputEncoding UTF-8 --outputEncoding UTF-8
$pitExit = $LASTEXITCODE
Write-Output "PIT exit code: $pitExit"
exit $pitExit
```

## Pairing and preservation

Observed target-class hashes: `7ab6a91f3618ccf5949692f1fc5d39b97174deab23925f872f0e31cb5a2591a1`.
The preserved script inventory fixes rendered phase-script hashes before execution. The source-pairing inventory verifies every tracked file's raw bytes are equal in both checkouts. The before checkout contains no generated target test; the after checkout contains exactly the parent frozen bytes. Metadata-only Git checks and the manager verify the baseline and original test hash.

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

import static org.junit.jupiter.api.Assertions.assertThrows;

import java.io.ByteArrayInputStream;
import java.io.InputStream;

import org.junit.jupiter.api.Test;

public class PeekableInputStreamTest {

    @Test
    public void testConstructorRejectsZeroBufferSize() {
        // Arrange
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final int bufferSize = 0;

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> new PeekableInputStream(input, bufferSize));
    }

    @Test
    public void testPeekArrayRejectsNullBuffer() {
        // Arrange
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = null;

        // Act and Assert
        assertThrows(NullPointerException.class, () -> stream.peek(candidate));
    }

    @Test
    public void testPeekArrayRejectsBufferLargerThanCapacity() {
        // Arrange
        // Assume the constructor size becomes the receiver's buffer size.
        // Change modeled capacity 0 to 1 and array length 1 to 2, preserving length > capacity.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[2];

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate));
    }

    @Test
    public void testPeekArrayRejectsEmptyBuffer() {
        // Arrange
        // Assume size 1 creates a non-null, empty buffer. Modeled receiver size 0 becomes 1.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[0];

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate));
    }

    @Test
    public void testPeekSliceRejectsNullBuffer() {
        // Arrange
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = null;
        final int offset = 0;
        final int length = 0;

        // Act and Assert
        assertThrows(NullPointerException.class, () -> stream.peek(candidate, offset, length));
    }

    @Test
    public void testPeekSliceRejectsBufferLargerThanCapacity() {
        // Arrange
        // Assume the constructor size becomes the receiver's buffer size.
        // Change modeled capacity 0 to 1 and array length 1 to 2, preserving length > capacity.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[2];
        final int offset = 0;
        final int length = 1;

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate, offset, length));
    }

    @Test
    public void testPeekSliceRejectsOffsetAtEmptyBufferEnd() {
        // Arrange
        // Assume size 1 creates a non-null, empty buffer. Modeled receiver size 0 becomes 1.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[0];
        final int offset = 0;
        final int length = 0;

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate, offset, length));
    }

    @Test
    public void testPeekSliceRejectsNegativeOffset() {
        // Arrange
        // Assume size 1 creates a non-null, empty buffer. Modeled receiver size 0 becomes 1.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[0];
        final int offset = -1;
        final int length = 0;

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate, offset, length));
    }

    @Test
    public void testPeekSliceRejectsNegativeLength() {
        // Arrange
        // Assume size 1 creates a non-null buffer with an initial byte count of 0.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[1];
        final int offset = 0;
        final int length = -1;

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate, offset, length));
    }

    @Test
    public void testPeekSliceRejectsLengthLargerThanCapacity() {
        // Arrange
        // Assume size 1 creates a non-null buffer of capacity 1 with an initial byte count of 0.
        // Change modeled internal capacity 0 to 1 and requested length 1 to 2, preserving length > capacity.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[1];
        final int offset = 0;
        final int length = 2;

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate, offset, length));
    }
}
```


Before and after have the same 14 native mutant identities (class, method, descriptor, line, mutator, indexes, and blocks).


`jacoco-before`: 1541 native reported cases, including 6 intrinsic skips; 1535 non-skipped cases. These full-suite counts are separate from the 10 generated cases.

`jacoco-after`: 1551 native reported cases, including 6 intrinsic skips; 1545 non-skipped cases. These full-suite counts are separate from the 10 generated cases.