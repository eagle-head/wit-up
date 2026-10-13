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
