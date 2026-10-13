$ErrorActionPreference = 'Stop'
$evaluationRoot = 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/004'
$workingDirectory = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-004'
$outputDirectory = "$workingDirectory/cli-discovery"
if (Test-Path -LiteralPath $outputDirectory) { throw 'CLI discovery output already exists.' }
New-Item -ItemType Directory -Path $outputDirectory | Out-Null
Set-Location -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-004'
$env:MAVEN_OPTS = '-DargLine='
mvn -B -ntp -f "$evaluationRoot/inputs/pit-cli-pom.xml" org.apache.maven.plugins:maven-dependency-plugin:3.6.1:build-classpath "-Dmdep.outputFile=$outputDirectory/tool-classpath.txt"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$toolClasspath = (Get-Content -LiteralPath "$outputDirectory/tool-classpath.txt" -Raw).Trim()
java -cp $toolClasspath org.pitest.mutationtest.commandline.MutationCoverageReport --help
$helpExit = $LASTEXITCODE
Write-Output "PIT CLI help exit code: $helpExit"
exit $helpExit
