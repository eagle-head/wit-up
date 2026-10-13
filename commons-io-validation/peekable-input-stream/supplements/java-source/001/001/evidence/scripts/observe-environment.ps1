param([Parameter(Mandatory)][string]$Destination)
$ErrorActionPreference = 'Stop'
function Observe-Version([string]$Executable, [string[]]$Arguments) {
    $command = Get-Command $Executable
    $output = @(& $command.Source @Arguments 2>&1 | ForEach-Object { $_.ToString() })
    $commandExit = $LASTEXITCODE
    if ($commandExit -ne 0) { throw "Version observation failed: $Executable ($commandExit)" }
    return [ordered]@{ executable=$command.Source; arguments=$Arguments; exitCode=$commandExit; output=$output }
}
$processSettings = [ordered]@{}
foreach ($variableName in @('JAVA_HOME','PATH','MAVEN_OPTS','MAVEN_ARGS','TEMP','TMP','JAVA_TOOL_OPTIONS','JDK_JAVA_OPTIONS','_JAVA_OPTIONS')) {
    $processSettings[$variableName] = [Environment]::GetEnvironmentVariable($variableName, 'Process')
}
$observation = [ordered]@{
    observedAt=[DateTime]::UtcNow.ToString('o')
    java=(Observe-Version 'java' @('-version'))
    javac=(Observe-Version 'javac' @('-version'))
    maven=(Observe-Version 'mvn' @('-version'))
    python=(Observe-Version 'python' @('--version'))
    os=[ordered]@{ description=[System.Runtime.InteropServices.RuntimeInformation]::OSDescription; version=[Environment]::OSVersion.VersionString; architecture=[System.Runtime.InteropServices.RuntimeInformation]::OSArchitecture.ToString(); powershell=$PSVersionTable.PSVersion.ToString() }
    processEnvironment=$processSettings
    generator=[ordered]@{ model=$null; settings=$null; applicationBuild=$null; reason='This is an evaluation of preserved test bytes, not a generation. Original generation settings remain unknown in the parent record.' }
}
$observation | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $Destination -Encoding utf8
