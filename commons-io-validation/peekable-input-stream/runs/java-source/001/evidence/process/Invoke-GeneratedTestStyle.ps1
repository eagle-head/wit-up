$ErrorActionPreference = 'Stop'
$workingDirectory = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001'
$runDirectory = 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/runs/java-source/001'
$manager = 'D:/Projects/wit-up/tools/experiment_runs.py'
. "$workingDirectory/Observe-Environment.ps1" -Destination "$workingDirectory/environment-generated-test-style.json" *> "$workingDirectory/environment-generated-test-style-observation.log"

$dependencyPaths = @(
    'com/puppycrawl/tools/checkstyle/8.19/checkstyle-8.19.jar',
    'info/picocli/picocli/3.9.5/picocli-3.9.5.jar',
    'antlr/antlr/2.7.7/antlr-2.7.7.jar',
    'org/antlr/antlr4-runtime/4.7.2/antlr4-runtime-4.7.2.jar',
    'commons-beanutils/commons-beanutils/1.9.3/commons-beanutils-1.9.3.jar',
    'commons-logging/commons-logging/1.1.1/commons-logging-1.1.1.jar',
    'commons-collections/commons-collections/3.2.2/commons-collections-3.2.2.jar',
    'com/google/guava/guava/27.1-jre/guava-27.1-jre.jar',
    'com/google/guava/failureaccess/1.0.1/failureaccess-1.0.1.jar'
)
$classpathEntries = @($dependencyPaths | ForEach-Object { "$workingDirectory/maven-repository/$_" })
foreach ($entry in $classpathEntries) {
    if (-not (Test-Path -LiteralPath $entry)) {
        throw "Required already-resolved Checkstyle dependency is absent: $entry"
    }
}
$classpath = $classpathEntries -join ';'
$styleReport = "$workingDirectory/checkstyle-generated-test.xml"
$sourceFile = 'src/test/java/org/apache/commons/io/input/buffer/PeekableInputStreamTest.java'
$command = 'java -cp "' + $classpath + '" com.puppycrawl.tools.checkstyle.Main -c checkstyle.xml -f xml -o "' + $styleReport + '" ' + $sourceFile
$command | Set-Content -LiteralPath "$workingDirectory/generated-test-style-command.txt" -Encoding utf8NoBOM

python $manager verify --run $runDirectory --live *> "$workingDirectory/generated-test-style-live-verification.log"
$verificationExit = $LASTEXITCODE
if ($verificationExit -ne 0) {
    throw "Live verification failed with exit code $verificationExit; Checkstyle was not invoked."
}
python $manager begin --run $runDirectory --phase infrastructure --command $command --scope 'Checkstyle 8.19 with unchanged repository rules applied to the frozen generated Java file; no compilation or test execution' --environment "$workingDirectory/environment-generated-test-style.json" --reports "$workingDirectory/generated-test-style/surefire-reports" *> "$workingDirectory/generated-test-style-begin.log"
$beginExit = $LASTEXITCODE
Get-Content -LiteralPath "$workingDirectory/generated-test-style-begin.log"
if ($beginExit -ne 0) {
    throw "Execution reservation failed with exit code $beginExit; Checkstyle was not invoked."
}
$reservation = Get-Content -LiteralPath "$workingDirectory/generated-test-style-begin.log" -Raw | ConvertFrom-Json
$executionLog = $reservation.log
if ([string]::IsNullOrWhiteSpace($executionLog)) {
    throw 'The reservation did not return a log path; Checkstyle was not invoked.'
}
java -cp $classpath com.puppycrawl.tools.checkstyle.Main -c checkstyle.xml -f xml -o $styleReport $sourceFile *> $executionLog
$executionExit = $LASTEXITCODE
[ordered]@{
    command = $command
    exitCode = $executionExit
    completedAt = [DateTime]::UtcNow.ToString('o')
    log = $executionLog
    execution = $reservation.execution
} | ConvertTo-Json | Set-Content -LiteralPath "$workingDirectory/generated-test-style-status.json" -Encoding utf8NoBOM
Write-Output "GENERATED_TEST_STYLE_EXIT: $executionExit"
Get-Content -LiteralPath $executionLog
if (Test-Path -LiteralPath $styleReport) {
    Get-Content -LiteralPath $styleReport
}
