@echo off
setlocal

:: Set the variables
set "sevenZipPath=C:\Program Files\7-Zip\7z.exe"
set "archiveFilePath=D:\OneDrive\onBIM\Eventos\Curso Python for Dynamo 2024\CursoPythonDynamoForRevit\docs\*.zip"
set "destinationFolder=D:\OneDrive\onBIM\Eventos\Curso Python for Dynamo 2024\CursoPythonDynamoForRevit\docs"

:: Extract the archive
"%sevenZipPath%" x "%archiveFilePath%" -o"%destinationFolder%"

:: Check if extraction was successful
if %errorlevel% equ 0 (
    echo Extraction successful, deleting the archive file: "%archiveFilePath%"
    del "%archiveFilePath%"
) else (
    echo Extraction failed, cannot delete the archive file.
)

endlocal