$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-005'
$env:MAVEN_OPTS = '-DargLine='
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:copy '-Dartifact=org.jacoco:org.jacoco.agent:0.8.4:jar:runtime' '-DoutputDirectory=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/tools'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:copy '-Dartifact=org.jacoco:org.jacoco.cli:0.8.4:jar:nodeps' '-DoutputDirectory=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/tools'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$expectedTools = @{ 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/tools/org.jacoco.agent-0.8.4-runtime.jar'='1a7c1dc7280e535b9b6f383915bac5afbb9208c1af2019b4e674ca590c925c22'; 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/tools/org.jacoco.cli-0.8.4-nodeps.jar'='65de07ff32bcf2f945f18180d1d10cdf0e155eee2b508519bbc5f31904cd8288' }
foreach ($toolPath in $expectedTools.Keys) {
    $actualHash = (Get-FileHash -LiteralPath $toolPath -Algorithm SHA256).Hash.ToLowerInvariant()
    Write-Output "$actualHash  $toolPath"
    if ($actualHash -ne $expectedTools[$toolPath]) { throw 'Measurement tool checksum mismatch.' }
}
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-help-plugin:3.5.1:effective-pom '-Doutput=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/effective-pom.xml'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:list '-DoutputAbsoluteArtifactFilename=true' '-DoutputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/dependencies.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$dependencyHashes = @()
foreach ($dependencyLine in Get-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/dependencies.txt') {
    $dependencyParts = $dependencyLine.Trim() -split ':', 6
    if ($dependencyParts.Count -eq 6) {
        $artifactPath = $dependencyParts[5]
        if (!(Test-Path -LiteralPath $artifactPath -PathType Leaf)) { throw "A resolved dependency is missing: $artifactPath" }
        $dependencyHashes += [ordered]@{ path=$artifactPath; sha256=(Get-FileHash -LiteralPath $artifactPath -Algorithm SHA256).Hash.ToLowerInvariant(); bytes=(Get-Item -LiteralPath $artifactPath).Length }
    }
}
if ($dependencyHashes.Count -eq 0) { throw 'No resolved dependency artifacts were captured.' }
$dependencyHashes | ConvertTo-Json -Depth 3 | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/dependency-hashes.json' -Encoding utf8
mvn -B -ntp -f 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/inputs/pit-cli-pom.xml' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:build-classpath '-Dmdep.outputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/tool-classpath.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:build-classpath '-DincludeScope=test' '-Dmdep.outputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/project-classpath.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp -f 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/inputs/pit-cli-pom.xml' org.apache.maven.plugins:maven-help-plugin:3.5.1:effective-pom '-Doutput=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/launcher-effective-pom.xml'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp -f 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/inputs/pit-cli-pom.xml' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:list '-DoutputAbsoluteArtifactFilename=true' '-DoutputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/launcher-dependencies.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$toolClasspath = (Get-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/tool-classpath.txt' -Raw).Trim()
$projectClasspath = (Get-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/project-classpath.txt' -Raw).Trim()
java -cp $toolClasspath org.pitest.mutationtest.commandline.MutationCoverageReport -h
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$runtimeArtifacts = @($projectClasspath -split ';') + @($toolClasspath -split ';')
$runtimeHashes = @()
foreach ($artifactPath in @($runtimeArtifacts | Select-Object -Unique)) {
    $runtimeHashes += [ordered]@{ path=$artifactPath; sha256=(Get-FileHash -LiteralPath $artifactPath -Algorithm SHA256).Hash.ToLowerInvariant(); bytes=(Get-Item -LiteralPath $artifactPath).Length }
}
$runtimeHashes | ConvertTo-Json -Depth 3 | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/runtime-hashes.json' -Encoding utf8
$phaseClasspath = @('D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/before-checkout/target/classes', 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/before-checkout/target/test-classes') + $runtimeArtifacts
$phaseClasspath | Select-Object -Unique | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/pit-before-classpath.txt' -Encoding utf8NoBOM
$phaseClasspath = @('D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-005/target/classes', 'D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-005/target/test-classes') + $runtimeArtifacts
$phaseClasspath | Select-Object -Unique | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/pit-after-classpath.txt' -Encoding utf8NoBOM
exit 0
