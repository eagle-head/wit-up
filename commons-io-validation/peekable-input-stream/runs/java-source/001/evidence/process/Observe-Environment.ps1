param([Parameter(Mandatory = $true)][string]$Destination)

$ErrorActionPreference = 'Stop'
$workingDirectory = 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001'
$env:JAVA_HOME = 'C:/Users/edyko/AppData/Local/mise/installs/java/temurin-8.0.504+1'
$mavenDirectory = 'C:/Users/edyko/AppData/Local/mise/installs/maven/3.9.16/apache-maven-3.9.16'
$env:PATH = "$env:JAVA_HOME/bin;$mavenDirectory/bin;$env:PATH"
$env:MAVEN_OPTS = '-DargLine='
$env:MAVEN_ARGS = "-Dmaven.repo.local=$workingDirectory/maven-repository"
$env:TEMP = "$workingDirectory/temp"
$env:TMP = $env:TEMP
New-Item -ItemType Directory -Path $env:TEMP -Force | Out-Null
New-Item -ItemType Directory -Path "$workingDirectory/maven-repository" -Force | Out-Null

if (Test-Path -LiteralPath $Destination) {
    throw "Environment observation already exists: $Destination"
}

$observations = [ordered]@{}
foreach ($entry in @(
    @{Name = 'java'; Command = 'java'; Argument = '-version'},
    @{Name = 'javac'; Command = 'javac'; Argument = '-version'},
    @{Name = 'maven'; Command = 'mvn'; Argument = '-version'},
    @{Name = 'python'; Command = 'python'; Argument = '--version'}
)) {
    $executable = (Get-Command $entry.Command).Source
    $versionOutput = @(& $executable $entry.Argument 2>&1 | ForEach-Object { $_.ToString() })
    $versionExit = $LASTEXITCODE
    $observations[$entry.Name] = [ordered]@{
        executable = $executable
        command = "$($entry.Command) $($entry.Argument)"
        exitCode = $versionExit
        output = $versionOutput
    }
}

$processEnvironment = [ordered]@{}
foreach ($variableName in @('JAVA_HOME', 'PATH', 'MAVEN_OPTS', 'MAVEN_ARGS', 'TEMP', 'TMP', 'JAVA_TOOL_OPTIONS', 'JDK_JAVA_OPTIONS', '_JAVA_OPTIONS')) {
    $processEnvironment[$variableName] = [Environment]::GetEnvironmentVariable($variableName, 'Process')
}

$environmentRecord = [ordered]@{
    observedAt = [DateTime]::UtcNow.ToString('o')
    observationScope = 'Assigned independent generation; observed in the process environment used for the original Maven command.'
    java = $observations.java
    javac = $observations.javac
    maven = $observations.maven
    python = $observations.python
    os = [ordered]@{
        description = [Runtime.InteropServices.RuntimeInformation]::OSDescription
        version = [Environment]::OSVersion.ToString()
        architecture = [Runtime.InteropServices.RuntimeInformation]::OSArchitecture.ToString()
        powershell = $PSVersionTable.PSVersion.ToString()
    }
    processEnvironment = $processEnvironment
    generator = [ordered]@{
        model = $null
        settings = $null
        applicationBuild = $null
        reason = 'The exact active model identifier, sampling and reasoning settings, and running application build are not exposed in this chat context. The developer describes the agent as based on GPT-6.'
    }
}
$environmentRecord | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath $Destination -Encoding utf8NoBOM
Get-Content -LiteralPath $Destination
