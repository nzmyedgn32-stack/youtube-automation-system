from __future__ import annotations

from pathlib import Path


class VideoRenderService:
    def __init__(self) -> None:
        self.output_dir = Path("./data/output")
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def render_video(self, script: str, audio_file: str) -> str:
        output_path = self.output_dir / "rendered-video.mp4"
        return str(output_path)

    def create_thumbnail(self, video_path: str) -> str:
        thumbnail_path = self.output_dir / "thumbnail.jpg"
        return str(thumbnail_path)
