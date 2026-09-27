from __future__ import annotations

from pathlib import Path


class ServiceRegistry:
    @staticmethod
    def get_services() -> dict:
        return {
            "trends": "app.services.trends:TrendsService",
            "script_writer": "app.services.script_writer:ScriptWriterService",
            "tts": "app.services.tts:TTSService",
            "render": "app.services.video_render:VideoRenderService",
            "youtube": "app.services.youtube_uploader:YouTubeUploaderService",
            "analytics": "app.services.analytics:AnalyticsService",
        }
