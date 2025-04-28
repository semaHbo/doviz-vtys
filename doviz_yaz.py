import requests
import time
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# InfluxDB ayarları
bucket = "kur-bucket"
org = "my-org"
token = "mytoken"
url = "http://localhost:8086"
client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Takip edilecek kurlar (XAU çıkarıldı)
kurlar = {
    "USD/TRY": ("USD", "TRY"),
    "EUR/TRY": ("EUR", "TRY"),
    "GBP/TRY": ("GBP", "TRY")
}

while True:
    for name, (base, symbol) in kurlar.items():
        try:
            url = f"https://open.er-api.com/v6/latest/{base}"
            response = requests.get(url)
            data = response.json()
            rate = data.get("rates", {}).get(symbol)

            if rate is None:
                print(f"❌ {name} kuru alınamadı. Veri:", data)
            else:
                print(f"{name}: {rate}")
                point = Point("doviz").tag("pair", name).field("rate", rate)
                write_api.write(bucket=bucket, org=org, record=point)
                print(f"✅ {name} verisi yazıldı")

        except Exception as e:
            print(f"🚨 {name} hata:", e)

    time.sleep(10)
