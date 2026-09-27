# YouTube Automation System

Bu repository, YouTube kanalı için otomatik video üretim sistemi kurmak için hazırlanmış modüler bir başlangıç altyapısıdır.

## Amaç

- Trend ve konu keşfi
- Video başlığı ve script üretimi
- Seslendirme (TTS)
- Görsel ve thumbnail hazırlama
- Video render işlemi
- YouTube upload
- Performans analizi

## Mimarisi

Proje, aşağıdaki modüllerden oluşur:

- Trends: Trend ve konu üretimi
- Script Writer: Başlık, açıklama ve script oluşturma
- TTS: Seslendirme
- Video Render: Görsel + ses + yazı + altyazı birleştirme
- YouTube Uploader: YouTube upload ve yayınlanma
- Analytics: İzlenme, CTR, retention analizi

## Hızlı başlangıç

1. Sanal ortam oluştur
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   # .venv\Scripts\activate    # Windows
   ```

2. Bağımlılıkları kur
   ```bash
   pip install -r requirements.txt
   ```

3. Ortam değişkenlerini tanımla
   ```bash
   cp .env.example .env
   ```

4. Ayar dosyasını kontrol et
   ```bash
   cp config/settings.yaml.example config/settings.yaml
   ```

5. Akışı çalıştır
   ```bash
   python -m app.pipeline
   ```

## Dizin yapısı

```text
.
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── pipeline.py
│   └── services/
│       ├── __init__.py
│       ├── analytics.py
│       ├── script_writer.py
│       ├── trends.py
│       ├── tts.py
│       ├── video_render.py
│       └── youtube_uploader.py
├── config/
│   ├── settings.yaml.example
│   └── settings.yaml
├── docs/
│   ├── architecture.md
│   └── workflow.md
├── scripts/
│   └── run_pipeline.sh
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── .venv/
```

## Güvenlik notu

- API anahtarları `.env` dosyasında tutulmalıdır.
- `.env` dosyası Git'e eklenmemelidir.

## Geliştirme akışı

1. Trendleri al
2. Başlık ve konu üret
3. Script yaz
4. TTS ile ses üret
5. Video render et
6. Thumbnail oluştur
7. YouTube upload et
8. Performans analizi yap

## Geliştirilecek adımlar

- YouTube Data API entegrasyonu
- Google Trends arama modülü
- EleventLabs / Azure TTS bağlanması
- FFmpeg render pipeline
- Thumbnail üretimi ve otomatik upload
- PostgreSQL veritabanı takibi
- Dashboard ve raporlama

## Örnek yayın akışı

```text
Trendler -> Konu üretimi -> Başlık -> Script -> Görsel -> Ses -> Videolar -> Upload -> Analiz
```

## Lisans

Bu proje eğitim ve prototip amaçlıdır.
