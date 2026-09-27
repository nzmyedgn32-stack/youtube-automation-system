#!/usr/bin/env python3
"""
YouTube Automation System - Main Pipeline
Runs the complete workflow: trends -> script -> audio -> video -> upload -> analytics
"""

import json
import logging
import sys
from pathlib import Path

from app.config import settings
from app.pipeline import VideoAutomationPipeline

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def save_result(result: dict) -> Path:
    """
    Save pipeline result to JSON file
    """
    result_path = settings.base_output_dir / "latest_result.json"
    with open(result_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2, default=str)
    logger.info(f"Sonuç kaydedildi: {result_path}")
    return result_path


def main() -> int:
    """
    Run the complete pipeline
    """
    logger.info("🚀 YouTube Automation Pipeline başlıyor...")
    logger.info(f"Çıktı dizini: {settings.base_output_dir}")

    try:
        pipeline = VideoAutomationPipeline()
        logger.info("Pipeline oluşturuldu")

        logger.info("\n1️⃣ Trendler alınıyor...")
        result = pipeline.run()

        logger.info("\n📊 Pipeline sonuçları:")
        logger.info(f"  - Konu sayısı: {len(result['topics'])}")
        logger.info(f"  - Seçilen başlık: {result['selected_title']}")
        logger.info(f"  - Script uzunluğu: {len(result['script'])} karakter")
        logger.info(f"  - Ses dosyası: {Path(result['audio_file']).name}")
        logger.info(f"  - Video dosyası: {Path(result['video_path']).name}")
        logger.info(f"  - Thumbnail: {Path(result['thumbnail_path']).name}")
        logger.info(f"  - Upload durumu: {result['upload_result'].get('status')}")

        result_path = save_result(result)
        logger.info(f"\n✅ Pipeline başarıyla tamamlandı!")
        logger.info(f"   Detaylı sonuçlar: {result_path}")

        return 0

    except Exception as e:
        logger.error(f"❌ Pipeline hatası: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
