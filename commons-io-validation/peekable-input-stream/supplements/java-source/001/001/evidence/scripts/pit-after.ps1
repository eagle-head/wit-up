$ErrorActionPreference = 'Stop'
$analysisPom = 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/001/inputs/pit-analysis-pom.xml'
$phaseCheckout = 'D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-001'
$phaseOutput = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-001/measurements/pit-after'
$phaseBuild = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-001/pit-build/pit-after'
$temporaryDirectory = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-001/temp'
Set-Location -LiteralPath $phaseCheckout
$env:MAVEN_OPTS = '-DargLine='
mvn -B -ntp -f $analysisPom "-Danalysis.checkout=$phaseCheckout" "-Danalysis.output=$phaseOutput" "-Danalysis.build=$phaseBuild" "-Danalysis.temp=$temporaryDirectory" org.pitest:pitest-maven:1.15.2:mutationCoverage
$pitExit = $LASTEXITCODE
Write-Output "PIT exit code: $pitExit"
exit $pitExit
