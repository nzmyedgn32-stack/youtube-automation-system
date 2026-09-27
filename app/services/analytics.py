from __future__ import annotations

from typing import Any, Dict


class AnalyticsService:
    def fetch_metrics(self, video_id: str | None) -> Dict[str, Any]:
        return {
            "video_id": video_id or "unknown",
            "views": 0,
            "watch_time": 0,
            "ctr": 0.0,
            "retention": 0.0,
            "status": "placeholder",
        }
