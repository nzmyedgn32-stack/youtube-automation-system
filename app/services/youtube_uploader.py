from __future__ import annotations


class YouTubeUploaderService:
    def __init__(self) -> None:
        pass

    def upload(self, video_path: str, thumbnail_path: str, script: str) -> dict:
        return {
            "video_id": "sample_video_id",
            "status": "draft",
            "video_path": video_path,
            "thumbnail_path": thumbnail_path,
            "title": "Sample YouTube Video",
            "description": script,
        }
