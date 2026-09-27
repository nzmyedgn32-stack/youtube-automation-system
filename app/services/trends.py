from __future__ import annotations

from typing import List


class TrendsService:
    def __init__(self) -> None:
        self._topics = [
            "AI ile YouTube kanalını otomatik yönetmek",
            "Yapay zekâ ile içerik üretimi",
            "YouTube SEO 2026 rehberi",
            "Dijital içerik üretim stratejileri",
        ]

    def fetch_topics(self) -> List[str]:
        return self._topics
