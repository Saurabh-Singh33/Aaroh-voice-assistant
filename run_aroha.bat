@echo off
cd /d "%~dp0"
.\.venv_new\Scripts\python.exe main.py %*
pause
