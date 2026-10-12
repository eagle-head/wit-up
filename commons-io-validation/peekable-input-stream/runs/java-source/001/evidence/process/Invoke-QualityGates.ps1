$ErrorActionPreference = 'Stop'
$workingDirectory = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001'
$runDirectory = 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/runs/java-source/001'
$manager = 'D:/Projects/wit-up/tools/experiment_runs.py'

. "$workingDirectory/Observe-Environment.ps1" -Destination "$workingDirectory/environment-quality-gates.json" *> "$workingDirectory/environment-quality-gates-observation.log"
python $manager verify --run $runDirectory --live *> "$workingDirectory/quality-gates-live-verification.log"
$verificationExit = $LASTEXITCODE
Get-Content -LiteralPath "$workingDirectory/quality-gates-live-verification.log"
if ($verificationExit -ne 0) {
    throw "Live verification failed with exit code $verificationExit; quality gates were not invoked."
}

$mavenCommand = 'mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" apache-rat:check checkstyle:check'
python $manager begin --run $runDirectory --phase infrastructure --command $mavenCommand --scope 'Configured repository license and Checkstyle gates; no test lifecycle or test execution' --environment "$workingDirectory/environment-quality-gates.json" --reports "$workingDirectory/quality-gates/surefire-reports" *> "$workingDirectory/quality-gates-begin.log"
$beginExit = $LASTEXITCODE
Get-Content -LiteralPath "$workingDirectory/quality-gates-begin.log"
if ($beginExit -ne 0) {
    throw "Execution reservation failed with exit code $beginExit; quality gates were not invoked."
}
$reservation = Get-Content -LiteralPath "$workingDirectory/quality-gates-begin.log" -Raw | ConvertFrom-Json
$executionLog = $reservation.log
if ([string]::IsNullOrWhiteSpace($executionLog)) {
    throw 'The reservation did not return a log path; quality gates were not invoked.'
}
mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" apache-rat:check checkstyle:check *> $executionLog
$executionExit = $LASTEXITCODE
[ordered]@{
    command = $mavenCommand
    exitCode = $executionExit
    completedAt = [DateTime]::UtcNow.ToString('o')
    log = $executionLog
    execution = $reservation.execution
} | ConvertTo-Json | Set-Content -LiteralPath "$workingDirectory/quality-gates-status.json" -Encoding utf8NoBOM
Write-Output "QUALITY_GATES_EXIT: $executionExit"
