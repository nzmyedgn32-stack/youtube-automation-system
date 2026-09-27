from __future__ import annotations

from typing import List
import xml.etree.ElementTree as ET

import requests

from app.config import settings


class TrendsService:
    def fetch_topics(self) -> List[str]:
        url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=TR"
        try:
            response = requests.get(url, timeout=20)
            response.raise_for_status()
            root = ET.fromstring(response.content)
            topics: List[str] = []
            for item in root.findall("./channel/item"):
                title = item.findtext("title")
                if title:
                    clean = title.replace("- Google Trends", "").strip()
                    if clean:
                        topics.append(clean)
            if topics:
                return topics[:10]
        except Exception:
            pass

        return [
            "AI ile YouTube kanalını otomatik yönetmek",
            "Yapay zekâ ile içerik üretimi",
            "YouTube SEO 2026 rehberi",
            "Dijital içerik üretim stratejileri",
            "Kısa video üretim akışı",
            "İçerik üretim otomasyonu",
        ]
