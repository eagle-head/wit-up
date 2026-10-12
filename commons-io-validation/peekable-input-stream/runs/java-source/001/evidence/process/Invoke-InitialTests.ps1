$ErrorActionPreference = 'Stop'
$workingDirectory = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001'
$runDirectory = 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/runs/java-source/001'
$manager = 'D:/Projects/wit-up/tools/experiment_runs.py'

. "$workingDirectory/Observe-Environment.ps1" -Destination "$workingDirectory/environment-execution.json" *> "$workingDirectory/environment-execution-observation.log"

python $manager verify --run $runDirectory --live *> "$workingDirectory/live-verification.log"
$verificationExit = $LASTEXITCODE
Get-Content -LiteralPath "$workingDirectory/live-verification.log"
if ($verificationExit -ne 0) {
    throw "Live verification failed with exit code $verificationExit; Maven was not invoked."
}

$mavenCommand = 'mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" "-Dtest=org.apache.commons.io.input.buffer.PeekableInputStreamTest" clean test'
python $manager begin --run $runDirectory --phase generated-tests --command $mavenCommand --scope 'Frozen PeekableInputStreamTest only; clean/test lifecycle compiles baseline production and test sources' --environment "$workingDirectory/environment-execution.json" --reports 'D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001/target/surefire-reports' *> "$workingDirectory/begin.log"
$beginExit = $LASTEXITCODE
Get-Content -LiteralPath "$workingDirectory/begin.log"
if ($beginExit -ne 0) {
    throw "Execution reservation failed with exit code $beginExit; Maven was not invoked."
}

$reservation = Get-Content -LiteralPath "$workingDirectory/begin.log" -Raw | ConvertFrom-Json
$reservation | ConvertTo-Json -Depth 10
$executionLog = $reservation.log
if ([string]::IsNullOrWhiteSpace($executionLog)) {
    throw 'The reservation did not return a log path; Maven was not invoked.'
}

mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" "-Dtest=org.apache.commons.io.input.buffer.PeekableInputStreamTest" clean test *> $executionLog
$executionExit = $LASTEXITCODE
[ordered]@{
    command = $mavenCommand
    exitCode = $executionExit
    completedAt = [DateTime]::UtcNow.ToString('o')
    log = $executionLog
    sequence = $reservation.sequence
} | ConvertTo-Json | Set-Content -LiteralPath "$workingDirectory/execution-status.json" -Encoding utf8NoBOM
Write-Output "MAVEN_EXIT: $executionExit"
