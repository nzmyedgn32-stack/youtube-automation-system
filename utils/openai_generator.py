#!/usr/bin/env python3
"""
OpenAI Script Generator
Generates video titles and scripts using OpenAI API
"""

import logging
from typing import List

import requests

logger = logging.getLogger(__name__)


def generate_titles_openai(topics: List[str], api_key: str) -> List[str]:
    """
    Generate catchy YouTube video titles using OpenAI
    
    Args:
        topics: List of topics
        api_key: OpenAI API key
    
    Returns:
        List of generated titles
    """
    prompt = (
        "YouTube için yüksek CTR ve yüksek izlenme potansiyeli olan 5 başlık üret. "
        "Başlıklar sadece tek satır olsun, numara ekleme. "
        "Türkçe yaz. "
        f"Konular: {', '.join(topics[:3])}"
    )
    try:
        logger.info("OpenAI ile başlık üretiliyor...")
        payload = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.8,
        }
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=60,
        )
        response.raise_for_status()
        data = response.json()
        content = data["choices"][0]["message"]["content"]
        titles = [line.strip(" -#0123456789. ") for line in content.splitlines() if line.strip()]
        logger.info(f"✅ {len(titles)} başlık oluşturuldu")
        return titles[:5]
    except Exception as e:
        logger.warning(f"OpenAI başlık üretimi hatası: {e}")
        return [f"{topic} için etkili 5 adım" for topic in topics[:5]]


def generate_script_openai(title: str, api_key: str) -> str:
    """
    Generate video script using OpenAI
    
    Args:
        title: Video title
        api_key: OpenAI API key
    
    Returns:
        Generated script
    """
    prompt = (
        "YouTube için etkili bir video scripti yaz. "
        "Format: kısa hook (5 saniye), açıklama (1 dakika), "
        "3-4 ana nokta, örnek ve CTA (sonuç). "
        "Toplam 4-6 dakikalık sesli okunuş için yazılsın. "
        "Türkçe yaz. "
        f"Başlık: {title}"
    )
    try:
        logger.info("OpenAI ile script üretiliyor...")
        payload = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
        }
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=60,
        )
        response.raise_for_status()
        data = response.json()
        content = data["choices"][0]["message"]["content"]
        logger.info("✅ Script oluşturuldu")
        return content.strip()
    except Exception as e:
        logger.warning(f"OpenAI script üretimi hatası: {e}")
        return f"Merhaba! Bu videoda {title} konusunu anlatacağım..."


if __name__ == "__main__":
    import os
    logging.basicConfig(level=logging.INFO)
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("OPENAI_API_KEY ortam değişkeni gerekli")
    else:
        titles = generate_titles_openai(["AI", "YouTube"], api_key)
        for title in titles:
            print(f"- {title}")
