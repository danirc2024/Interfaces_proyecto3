@echo off
echo ====================================
echo   Iniciando NodeRed
echo ====================================
echo.

REM Verificar si Node.js está instalado
where node >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Node.js no esta instalado
    echo Por favor instala Node.js desde https://nodejs.org/
    pause
    exit /b 1
)

REM Verificar si NodeRed está instalado
where node-red >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: NodeRed no esta instalado
    echo Instalando NodeRed...
    npm install -g node-red
)

echo Iniciando NodeRed en el directorio actual...
echo Editor: http://localhost:1880
echo Dashboard: http://localhost:1880/ui
echo.
echo Presiona Ctrl+C para detener NodeRed
echo.

REM Navegar al directorio actual y ejecutar sin comillas
cd /d "%~dp0"
node-red --userDir ./

pause