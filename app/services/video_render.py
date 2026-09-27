from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from app.config import settings


class VideoRenderService:
    def __init__(self) -> None:
        self.output_dir = settings.base_output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def render_video(self, title: str, audio_file: str) -> str:
        output_path = self.output_dir / f"{title.lower().replace(' ', '-')}.mp4"
        duration = 8
        safe_title = title.replace("'", "\\'")

        ffmpeg = shutil.which("ffmpeg")
        if ffmpeg is None:
            output_path.write_bytes(b"placeholder-video")
            return str(output_path)

        drawtext_filter = (
            "drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:"
            f"text='{safe_title}':fontcolor=white:fontsize=52:x=(w-text_w)/2:y=(h-text_h)/2"
        )

        cmd = [
            ffmpeg,
            "-y",
            "-f", "lavfi",
            "-i", f"color=c=0x111827:s=1920x1080:d={duration}",
        ]

        audio_input = audio_file
        has_audio = audio_input.endswith(".mp3") or audio_input.endswith(".wav")

        if has_audio:
            cmd.extend(["-i", audio_input, "-shortest"])

        cmd.extend(["-vf", drawtext_filter])

        if has_audio:
            cmd.extend(["-c:v", "libx264", "-c:a", "aac", "-pix_fmt", "yuv420p", str(output_path)])
        else:
            cmd.extend(["-c:v", "libx264", "-pix_fmt", "yuv420p", str(output_path)])

        subprocess.run(cmd, check=True)
        return str(output_path)

    def create_thumbnail(self, title: str) -> str:
        thumbnail_path = self.output_dir / f"{title.lower().replace(' ', '-')}.jpg"
        thumbnail_path.write_bytes(b"placeholder-thumbnail")
        return str(thumbnail_path)
