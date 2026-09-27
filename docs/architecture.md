# Architecture overview

## Proje hedefi

Bu proje, YouTube kanalı için otomatik video üretim ve yükleme akışı sağlar.

## Katmanlar

### 1. Trend ve konu katmanı
- Google Trends ve arama verileri
- Anahtar kelime analizi
- Konu listesi oluşturma

### 2. Script üretimi katmanı
- Başlık üretimi
- Hook, ana bölüm, sonuç
- Açıklama ve hashtaglar

### 3. Görsel ve ses katmanı
- Stock görsel ve video seçimi
- Thumbnail oluşturma
- TTS ile seslendirme

### 4. Video render katmanı
- Görsel + ses + altyazı birleştirme
- MP4 çıkışı
- Düzenleme sonrası eklemeler

### 5. Yükleme katmanı
- YouTube Data API kullanımı
- Başlık, açıklama, etiketler, kategori, gizlilik ayarı
- Planlı veya ani yayın

### 6. Analiz katmanı
- İzlenme, CTR, retention, watch time
- Başarılı başlık formatları ve içerik türleri

## En uygun teknoloji kombinasyonu

- OpenAI / Claude / Gemini
- EleventLabs / Azure TTS
- Pexels / Pixabay / Unsplash
- FFmpeg / CapCut / Runway
- n8n veya Python worker pipeline
- PostgreSQL / Supabase
