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
