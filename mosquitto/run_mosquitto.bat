@echo off
echo ====================================
echo   Iniciando Mosquitto Broker
echo ====================================
echo.

REM 
where mosquitto >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Mosquitto no esta instalado
    echo Por favor instala Mosquitto desde https://mosquitto.org/download/
    pause
    exit /b 1
)

REM 
if not exist "data" mkdir data

echo Iniciando broker en puerto 1883...
echo Presiona Ctrl+C para detener
echo.

mosquitto -c "%~dp0mosquitto.conf" -v

pause
