# Döviz Kuru Takip ve Görselleştirme Sistemi

Bu proje, belirli döviz çiftlerinin anlık kur verilerini toplayıp *InfluxDB* veritabanına yazan ve ardından *Grafana* ile görselleştirilmesini sağlayan bir sistemdir.

## Proje Yapısı

- *InfluxDB*: Döviz kuru verilerini saklamak için kullanılır.
- *Grafana*: InfluxDB'deki verileri görselleştirir.
- *Python Script (doviz_yaz.py)*: API'den döviz kurlarını alır ve InfluxDB'ye kaydeder.
- *Docker Compose (docker-compose.yml)*: InfluxDB ve Grafana konteynerlerini birlikte yönetir.

## Kullanılan Teknolojiler

- Python 3
- InfluxDB 2.7
- Grafana
- Docker & Docker Compose
- [open.er-api.com](https://open.er-api.com/) döviz kuru API'si

## Kurulum ve Çalıştırma Adımları

### 1. Projeyi Klonlayın

bash
git clone <repo-link>
cd proje-dizini


### 2. Docker Servislerini Başlatın
Docker ve Docker Compose kurulu olmalıdır.

bash
docker-compose up -d

InfluxDB → http://localhost:8086

Grafana → http://localhost:3000

İlk çalıştırmada InfluxDB kendiliğinden admin kullanıcısı ile ayarlanır (username: admin, password: password).

### 3. Python Ortamını Hazırlayın
Gerekli Python kütüphanelerini yükleyin:

bash
pip install requests influxdb-client

### 4. Veri Yazım Scriptini Çalıştırın
bash
python doviz_yaz.py

Bu script her 10 saniyede bir USD/TRY, EUR/TRY ve GBP/TRY döviz kurlarını çekip InfluxDB'ye yazar.

### 5. Grafana Üzerinden Verileri Görüntüleyin
- http://localhost:3000 adresine gidin.

- İlk giriş:

Kullanıcı adı: admin

Şifre: admin (İlk girişte değiştirmeniz istenebilir.)

- Datasource olarak InfluxDB'yi ekleyin (http://influxdb:8086 adresi ve mytoken token'ı ile).

- Kendi panolarınızı oluşturun ve doviz ölçümünden (measurement) verileri çekerek grafikler çizin.

## Proje Detayları
### Docker Compose
yaml
services:
  influxdb:
    image: influxdb:2.7
    ports:
      - "8086:8086"
    environment:
      - DOCKER_INFLUXDB_INIT_USERNAME=admin
      - DOCKER_INFLUXDB_INIT_PASSWORD=password
      - DOCKER_INFLUXDB_INIT_ORG=my-org
      - DOCKER_INFLUXDB_INIT_BUCKET=kur-bucket
      - DOCKER_INFLUXDB_INIT_ADMIN_TOKEN=mytoken

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"

## Python Script
- Döviz API'sinden alınan rate bilgisi doviz isimli ölçüm altında saklanır.

- Veriler InfluxDB'ye pair etiketi ile (örneğin: USD/TRY) ve rate alanı olarak kaydedilir.

- Hatalar ve başarılı kayıtlar terminalde yazdırılır.

### Notlar
- API istekleri sırasında internet bağlantısı gereklidir.

- API limiti veya geçici kesintiler olması halinde hata mesajları terminalde görünür.

- İsterseniz doviz_yaz.py içindeki kurlar listesine farklı döviz çiftleri de ekleyebilirsiniz.
  
### 👩‍💻 Hazırlayanlar
Zeynep Merve Koyuncu

Sema Hacıbekiroğlu

Mihriban Melis Kömbe
