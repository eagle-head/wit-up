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
