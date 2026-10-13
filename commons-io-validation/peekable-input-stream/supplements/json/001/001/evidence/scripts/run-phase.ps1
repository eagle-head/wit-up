param([Parameter(Mandatory)][ValidateSet('preflight','jacoco-before','pit-before','jacoco-after','pit-after')][string]$Phase)
$ErrorActionPreference = 'Stop'
$scriptRoot = Split-Path -Parent $PSCommandPath
$evidenceRoot = Split-Path -Parent $scriptRoot
$evaluationRoot = Split-Path -Parent $evidenceRoot
$substitutions = Get-Content -LiteralPath "$evidenceRoot/substitutions.json" -Raw | ConvertFrom-Json
$assignment = $substitutions.phases.$Phase
$workingDirectory = $substitutions.workingDirectory
$env:JAVA_HOME = $substitutions.javaHome
$env:PATH = "$env:JAVA_HOME/bin;$env:PATH"
$env:TEMP = "$workingDirectory/temp"
$env:TMP = $env:TEMP
$env:MAVEN_ARGS = "-Dmaven.repo.local=$workingDirectory/maven-repository"
$env:MAVEN_OPTS = '-DargLine='
if ($Phase.StartsWith('jacoco')) {
    $env:MAVEN_OPTS = "-DargLine=-javaagent:$($substitutions.agentJar)=destfile=$($assignment.output)/jacoco.exec,append=true,includes=org.apache.commons.io.input.buffer.PeekableInputStream"
}
$environmentPath = "$workingDirectory/environments/$Phase.json"
$artifactPath = "$evidenceRoot/$Phase-artifacts.json"
if ((Test-Path -LiteralPath $environmentPath) -or (Test-Path -LiteralPath $artifactPath)) { throw 'A phase reservation input already exists.' }
& "$scriptRoot/observe-environment.ps1" -Destination $environmentPath
$assignment.artifacts | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath $artifactPath -Encoding utf8
$manager = 'D:/Projects/wit-up/tools/experiment_runs.py'
$command = "pwsh -NoProfile -File `"$($assignment.script)`""
$arguments = @($manager, 'begin', '--run', $evaluationRoot, '--phase', $Phase, '--command', $command, '--scope', $assignment.scope, '--environment', $environmentPath, '--artifacts', $artifactPath)
if ($assignment.reports) { $arguments += @('--reports', $assignment.reports) }
$reservationText = & python @arguments
$reservationExit = $LASTEXITCODE
if ($reservationExit -ne 0) { throw "Phase reservation failed ($reservationExit)." }
$reservation = $reservationText | ConvertFrom-Json
& pwsh -NoProfile -File $assignment.script *> $reservation.log
$executionExit = $LASTEXITCODE
$recordArguments = @($manager, 'record', '--run', $evaluationRoot, '--execution', $reservation.execution, '--exit-code', $executionExit)
if ($Phase -eq 'preflight') {
    $recordArguments += @('--tests-not-started', '--reason', 'Only dependency-copy, effective-POM, and dependency-list goals ran; no compilation or test goal was invoked.')
}
& python @recordArguments
if ($LASTEXITCODE -ne 0) { throw 'Execution recording failed; preserve all pending evidence.' }
Write-Output "Recorded $Phase, execution $($reservation.execution), process exit $executionExit."
exit $executionExit
