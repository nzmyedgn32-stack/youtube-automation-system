from __future__ import annotations

from typing import List


class ScriptWriterService:
    def __init__(self) -> None:
        pass

    def generate_titles(self, topics: List[str]) -> List[str]:
        return [f"{topic} için 7 adım" for topic in topics]

    def generate_script(self, title: str) -> str:
        return (
            f"Merhaba! Bu videoda {title} konusunu anlatacağım. "
            "Önce temel fikri açıklayacağız, sonra adım adım uygulamayı göreceğiz. "
            "Sonunda da pratik bir örnekle işi tamamlayacağız."
        )

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

from __future__ import annotations

from pathlib import Path


class TTSService:
    def __init__(self) -> None:
        self.output_dir = Path("./data/output")
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_audio(self, script: str) -> str:
        output_path = self.output_dir / "voiceover.wav"
        # TODO: Replace with ElevenLabs or Azure TTS integration.
        output_path.write_text("placeholder", encoding="utf-8")
        return str(output_path)

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

        audio_input = audio_file
        cmd = [
            ffmpeg,
            "-y",
            "-f", "lavfi",
            "-i", f"color=c=0x111827:s=1920x1080:d={duration}",
            "-vf",
            (
                "drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:"
                f"text='{safe_title}':fontcolor=white:fontsize=52:x=(w-text_w)/2:y=(h-text_h)/2"
            ),
        ]

        if audio_input.endswith(".mp3") or audio_input.endswith(".wav"):
            cmd.extend(["-i", audio_input])
            cmd.extend(["-shortest", "-c:v", "libx264", "-c:a", "aac", "-pix_fmt", "yuv420p", str(output_path)])
        else:
            cmd.extend(["-c:v", "libx264", "-pix_fmt", "yuv420p", str(output_path)])

        subprocess.run(cmd, check=True)
        return str(output_path)

    def create_thumbnail(self, title: str) -> str:
        thumbnail_path = self.output_dir / f"{title.lower().replace(' ', '-')}.jpg"
        thumbnail_path.write_bytes(b"placeholder-thumbnail")
        return str(thumbnail_path)

from __future__ import annotations

import os
from typing import Any

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from app.config import settings


class YouTubeUploaderService:
    def upload(self, video_path: str, thumbnail_path: str, title: str, description: str) -> dict[str, Any]:
        if not all(
            [
                settings.youtube_client_id,
                settings.youtube_client_secret,
                settings.youtube_refresh_token,
            ]
        ):
            return {
                "status": "skipped",
                "reason": "missing_youtube_credentials",
                "video_path": video_path,
                "thumbnail_path": thumbnail_path,
            }

        credentials = Credentials(
            token=None,
            refresh_token=settings.youtube_refresh_token,
            token_uri="https://oauth2.googleapis.com/token",
            client_id=settings.youtube_client_id,
            client_secret=settings.youtube_client_secret,
            scopes=["https://www.googleapis.com/auth/youtube.upload"],
        )

        youtube = build("youtube", "v3", credentials=credentials)
        body = {
            "snippet": {
                "title": title,
                "description": description,
                "tags": ["youtube", "automation", "ai", "content"],
                "categoryId": "22",
            },
            "status": {"privacyStatus": "private"},
        }

        media = MediaFileUpload(video_path, chunksize=-1, resumable=True, mimetype="video/mp4")
        request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
        response = request.execute()

        return {
            "status": "uploaded",
            "video_id": response.get("id"),
            "title": title,
            "description": description,
            "video_path": video_path,
            "thumbnail_path": thumbnail_path,
        }

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
