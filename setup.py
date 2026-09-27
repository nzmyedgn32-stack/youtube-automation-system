#!/usr/bin/env python3
"""
Setup script for YouTube Automation System
Runs initial configuration and tests
"""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


def check_python_version():
    if sys.version_info < (3, 11):
        print("❌ Python 3.11+ gereklidir")
        sys.exit(1)
    print("✅ Python versiyonu uygun")


def check_env_file():
    if not Path(".env").exists():
        print("❌ .env dosyası bulunamadı")
        print("💡 .env.example dosyasını kopyala: cp .env.example .env")
        return False
    print("✅ .env dosyası bulundu")
    return True


def check_required_env_vars():
    required_vars = [
        "OPENAI_API_KEY",
        "ELEVENLABS_API_KEY",
        "YOUTUBE_CLIENT_ID",
        "YOUTUBE_CLIENT_SECRET",
    ]
    missing = [var for var in required_vars if not os.getenv(var)]
    if missing:
        print(f"❌ Eksik ortam değişkenleri: {', '.join(missing)}")
        return False
    print("✅ Tüm zorunlu ortam değişkenleri ayarlanmış")
    return True


def check_directories():
    dirs = ["data/output", "data/assets", "data/scripts", "data/topics"]
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
    print("✅ Tüm dizinler oluşturuldu")


def check_ffmpeg():
    import shutil
    if shutil.which("ffmpeg") is None:
        print("❌ FFmpeg bulunamadı")
        print("💡 Kurulum:")
        print("   Ubuntu/Debian: sudo apt-get install ffmpeg")
        print("   macOS: brew install ffmpeg")
        print("   Windows: winget install Gyan.Dev.FFmpeg")
        return False
    print("✅ FFmpeg kurulu")
    return True


def test_imports():
    try:
        from app.config import settings
        from app.services.trends import TrendsService
        from app.services.script_writer import ScriptWriterService
        from app.services.tts import TTSService
        from app.services.video_render import VideoRenderService
        from app.services.youtube_uploader import YouTubeUploaderService
        from app.services.analytics import AnalyticsService
        print("✅ Tüm modüller başarıyla import edildi")
        return True
    except ImportError as e:
        print(f"❌ Import hatası: {e}")
        return False


def main():
    print("\n🚀 YouTube Automation System - Kurulum Kontrolü\n")
    print("=" * 50)

    checks = [
        ("Python Versiyonu", check_python_version),
        (".env Dosyası", check_env_file),
        ("Ortam Değişkenleri", check_required_env_vars),
        ("Dizinler", check_directories),
        ("FFmpeg", check_ffmpeg),
        ("Python Modülleri", test_imports),
    ]

    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append(result)
        except Exception as e:
            print(f"❌ {name}: {e}")
            results.append(False)

    print("\n" + "=" * 50)
    if all(results):
        print("\n✅ Tüm kontroller başarılı!")
        print("\n📌 Sonraki adım:")
        print("   python -m app.pipeline")
        return 0
    else:
        print("\n❌ Bazı kontroller başarısız. Lütfen hataları düzelt.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
