@echo off
echo [1/2] Docker ortam� ba�lat�l�yor...
cd /d "%~dp0"
docker-compose up -d

echo [2/2] Python veri scripti ba�lat�l�yor...
python doviz_yaz.py

pause
