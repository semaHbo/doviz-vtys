@echo off
echo [1/2] Docker ortamı başlatılıyor...
cd /d "%~dp0"
docker-compose up -d

echo [2/2] Python veri scripti başlatılıyor...
python doviz_yaz.py

pause
