$ErrorActionPreference = 'Stop'
$evaluationRoot = 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/004'
$workingDirectory = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-004'
$analysisPom = "$evaluationRoot/inputs/pit-analysis-pom.xml"
$checkout = 'D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-004'
$outputDirectory = "$workingDirectory/toolchain-metadata"
if (Test-Path -LiteralPath $outputDirectory) { throw 'Toolchain metadata output already exists.' }
New-Item -ItemType Directory -Path $outputDirectory | Out-Null
$env:MAVEN_OPTS = '-DargLine='
Set-Location -LiteralPath $checkout
mvn -B -ntp -f $analysisPom "-Danalysis.checkout=$checkout" "-Danalysis.output=$outputDirectory/pit-output" "-Danalysis.build=$outputDirectory/build" "-Danalysis.temp=$workingDirectory/temp" org.apache.maven.plugins:maven-help-plugin:3.5.1:effective-pom "-Doutput=$outputDirectory/pit-effective-pom.xml"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp -f $analysisPom "-Danalysis.checkout=$checkout" "-Danalysis.output=$outputDirectory/pit-output" "-Danalysis.build=$outputDirectory/build" "-Danalysis.temp=$workingDirectory/temp" org.apache.maven.plugins:maven-dependency-plugin:3.6.1:resolve-plugins '-DincludeGroupIds=org.pitest' "-DoutputFile=$outputDirectory/plugin-dependencies.txt"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$cacheFiles = @(rg --files "$workingDirectory/maven-repository" -g '*.jar')
$artifactNames = @()
foreach ($line in Get-Content -LiteralPath "$outputDirectory/plugin-dependencies.txt") {
    if ($line -match '([A-Za-z0-9._-]+\.jar)') { $artifactNames += $Matches[1] }
}
$artifactNames += 'pitest-junit5-plugin-1.2.2.jar', 'org.jacoco.agent-0.8.4-runtime.jar', 'org.jacoco.cli-0.8.4-nodeps.jar'
$artifactHashes = @()
foreach ($name in @($artifactNames | Sort-Object -Unique)) {
    $paths = @($cacheFiles | Where-Object { [System.IO.Path]::GetFileName($_) -eq $name })
    if (!$paths.Count) { throw "A resolved plugin artifact is absent: $name" }
    foreach ($path in $paths) {
        $artifactHashes += [ordered]@{ path=$path; sha256=(Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant(); bytes=(Get-Item -LiteralPath $path).Length }
    }
}
if (!$artifactHashes.Count) { throw 'No plugin artifacts were captured.' }
$artifactHashes | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath "$outputDirectory/plugin-hashes.json" -Encoding utf8
exit 0
