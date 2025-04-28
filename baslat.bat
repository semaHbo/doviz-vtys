@echo off
echo [1/2] Docker ortamý baþlatýlýyor...
cd /d "%~dp0"
docker-compose up -d

echo [2/2] Python veri scripti baþlatýlýyor...
python doviz_yaz.py

pause
