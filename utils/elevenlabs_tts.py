#!/usr/bin/env python3
"""
ElevenLabs TTS (Text-to-Speech) Module
Converts script text to natural-sounding audio
"""

import logging
from pathlib import Path

import requests

logger = logging.getLogger(__name__)


def generate_elevenlabs_audio(script: str, api_key: str, voice_id: str, output_path: str) -> bool:
    """
    Generate speech audio using ElevenLabs API
    
    Args:
        script: Text script to convert
        api_key: ElevenLabs API key
        voice_id: Voice ID (e.g., "21m00Tcm4TlvDq8ikWAM")
        output_path: Path to save MP3 file
    
    Returns:
        True if successful, False otherwise
    """
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    payload = {
        "text": script,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.8,
        },
    }
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json",
    }

    try:
        logger.info(f"ElevenLabs ile ses oluşturuluyor... ({len(script)} karakter)")
        response = requests.post(url, headers=headers, json=payload, timeout=120)
        response.raise_for_status()
        with open(output_path, "wb") as file:
            file.write(response.content)
        logger.info(f"✅ Ses dosyası kaydedildi: {output_path}")
        return True
    except Exception as e:
        logger.error(f"ElevenLabs TTS hatası: {e}")
        return False


if __name__ == "__main__":
    import os
    logging.basicConfig(level=logging.INFO)
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        print("ELEVENLABS_API_KEY ortam değişkeni gerekli")
    else:
        script = "Merhaba! Bu ses testi."  
        output = "test_audio.mp3"
        success = generate_elevenlabs_audio(script, api_key, "21m00Tcm4TlvDq8ikWAM", output)
        if success:
            print(f"✅ Ses dosyası oluşturuldu: {output}")
