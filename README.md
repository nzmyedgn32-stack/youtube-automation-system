# YouTube Automation System

Bu repository, YouTube kanalı için otomatik video üretim sistemi kurmak için modüler bir başlangıç altyapısıdır.

## Hızlı başlangıç

1. Sanal ortam oluştur
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Bağımlılıklar kur
   ```bash
   pip install -r requirements.txt
   ```

3. Ortam değişkenleri hazırlanır
   ```bash
   cp .env.example .env
   ```

4. Konfigürasyon dosyasını hazırla
   ```bash
   cp config/settings.yaml.example config/settings.yaml
   ```

5. Akışı çalıştır
   ```bash
   python -m app.pipeline
   ```

## Entegre edilen modüller

- Google Trends / RSS tabanlı konu üretimi
- OpenAI tabanlı başlık ve script üretimi
- ElevenLabs tabanlı seslendirme
- FFmpeg tabanlı video render
- YouTube Data API tabanlı upload
- Placeholder analytics çıktısı

## Gerekli ortam değişkenleri

```bash
OPENAI_API_KEY=your_openai_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
ELEVENLABS_VOICE_ID=21m00Tcm4TlvDq8ikWAM
GOOGLE_API_KEY=your_google_api_key
YOUTUBE_CLIENT_ID=your_youtube_client_id
YOUTUBE_CLIENT_SECRET=your_youtube_client_secret
YOUTUBE_REFRESH_TOKEN=your_youtube_refresh_token
BASE_OUTPUT_DIR=./data/output
APP_ENV=development
LOG_LEVEL=INFO
```

## İş akışı

```text
Trendler -> Başlık -> Script -> Ses -> Video -> Thumbnail -> Upload -> Analiz
```

## Notlar

- YouTube upload için Google OAuth refresh token gereklidir.
- FFmpeg sistemde kurulu olmalıdır.
- API anahtarları `.env` içinde tutulmalıdır.
