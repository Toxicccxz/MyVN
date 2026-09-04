[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Get-RenPyCommand {
    if ([string]::IsNullOrWhiteSpace($env:RENPY_SDK)) {
        throw "RENPY_SDK is not set. Set it to the Ren'Py 8.5.3 SDK root, for example: `$env:RENPY_SDK = 'C:\Tools\renpy-8.5.3-sdk'"
    }

    if (-not (Test-Path -LiteralPath $env:RENPY_SDK -PathType Container)) {
        throw "RENPY_SDK does not point to an existing directory: $env:RENPY_SDK"
    }

    $sdkRoot = (Resolve-Path -LiteralPath $env:RENPY_SDK).Path
    $renpyScript = Join-Path $sdkRoot "renpy.py"
    if (-not (Test-Path -LiteralPath $renpyScript -PathType Leaf)) {
        throw "Ren'Py launcher script was not found: $renpyScript"
    }

    $bundledPython = Join-Path $sdkRoot "lib\py3-windows-x86_64\python.exe"
    if (Test-Path -LiteralPath $bundledPython -PathType Leaf) {
        $python = $bundledPython
    }
    else {
        $pythonCommand = Get-Command "python.exe" -ErrorAction SilentlyContinue
        if ($null -eq $pythonCommand) {
            throw "The SDK's bundled Python was not found at '$bundledPython', and python.exe is not available on PATH."
        }
        $python = $pythonCommand.Source
    }

    return @($python, $renpyScript)
}

$projectRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")).Path
$renpyCommand = Get-RenPyCommand

& $renpyCommand[0] $renpyCommand[1] $projectRoot run
exit $LASTEXITCODE

