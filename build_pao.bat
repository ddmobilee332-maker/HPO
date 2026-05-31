@echo off
title PAO EXE BUILDER
echo [+] Installing requirements...
pip install -r requirements.txt pyinstaller
echo [+] Compiling to เปา.exe...
pyinstaller --onefile --name=เปา main.py
echo [✓] Done! Check dist folder.
pause
