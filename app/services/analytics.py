from __future__ import annotations


class AnalyticsService:
    def __init__(self) -> None:
        pass

    def fetch_metrics(self, video_id: str | None) -> dict:
        return {
            "video_id": video_id,
            "views": 0,
            "watch_time": 0,
            "ctr": 0.0,
            "retention": 0.0,
        }
