$ErrorActionPreference = 'Stop'
$phaseCheckout = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-001/before-checkout'
$phaseOutput = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-001/measurements/jacoco-before'
$agentJar = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-001/tools/org.jacoco.agent-0.8.4-runtime.jar'
$cliJar = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-001/tools/org.jacoco.cli-0.8.4-nodeps.jar'
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
