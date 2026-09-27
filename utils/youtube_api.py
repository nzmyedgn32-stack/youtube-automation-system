#!/usr/bin/env python3
"""
YouTube Data API Module
Uploads videos to YouTube and fetches analytics
"""

import logging
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2.service_account import Credentials as ServiceAccountCredentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

logger = logging.getLogger(__name__)


def upload_video_to_youtube(
    video_path: str,
    title: str,
    description: str,
    tags: list[str],
    client_id: str,
    client_secret: str,
    refresh_token: str,
    privacy_status: str = "private",
) -> dict:
    """
    Upload video to YouTube using OAuth2
    
    Args:
        video_path: Path to MP4 file
        title: Video title
        description: Video description
        tags: List of tags/keywords
        client_id: YouTube OAuth client ID
        client_secret: YouTube OAuth client secret
        refresh_token: OAuth refresh token
        privacy_status: 'public', 'private', 'unlisted'
    
    Returns:
        Upload result dict with video_id
    """
    if not Path(video_path).exists():
        logger.error(f"Video dosyası bulunamadı: {video_path}")
        return {"status": "error", "message": "Video file not found"}

    try:
        logger.info(f"YouTube OAuth başlatılıyor...")
        credentials = Credentials(
            token=None,
            refresh_token=refresh_token,
            token_uri="https://oauth2.googleapis.com/token",
            client_id=client_id,
            client_secret=client_secret,
            scopes=["https://www.googleapis.com/auth/youtube.upload"],
        )
        credentials.refresh(Request())

        logger.info("YouTube API client oluşturuluyor...")
        youtube = build("youtube", "v3", credentials=credentials)

        body = {
            "snippet": {
                "title": title,
                "description": description,
                "tags": tags,
                "categoryId": "22",
                "defaultLanguage": "tr",
                "defaultAudioLanguage": "tr",
            },
            "status": {
                "privacyStatus": privacy_status,
                "madeForKids": False,
            },
        }

        logger.info(f"Video yükleniyor: {title}")
        media = MediaFileUpload(
            video_path,
            chunksize=-1,
            resumable=True,
            mimetype="video/mp4",
        )
        request = youtube.videos().insert(
            part="snippet,status",
            body=body,
            media_body=media,
        )
        response = request.execute()
        video_id = response.get("id")
        logger.info(f"✅ Video yüklendi: {video_id}")

        return {
            "status": "success",
            "video_id": video_id,
            "title": title,
            "url": f"https://www.youtube.com/watch?v={video_id}",
        }
    except HttpError as e:
        logger.error(f"YouTube API hatası: {e}")
        return {"status": "error", "message": str(e)}
    except Exception as e:
        logger.error(f"Upload hatası: {e}")
        return {"status": "error", "message": str(e)}


def fetch_video_metrics(video_id: str, credentials) -> dict:
    """
    Fetch video metrics from YouTube Analytics
    
    Args:
        video_id: YouTube video ID
        credentials: OAuth2 credentials
    
    Returns:
        Dictionary with metrics (views, watch_time, etc.)
    """
    try:
        youtube = build("youtube", "v3", credentials=credentials)
        request = youtube.videos().list(
            part="statistics,snippet",
            id=video_id,
        )
        response = request.execute()
        if response["items"]:
            stats = response["items"][0].get("statistics", {})
            snippet = response["items"][0].get("snippet", {})
            return {
                "video_id": video_id,
                "title": snippet.get("title"),
                "views": int(stats.get("viewCount", 0)),
                "likes": int(stats.get("likeCount", 0)),
                "comments": int(stats.get("commentCount", 0)),
            }
    except Exception as e:
        logger.error(f"Metrik alma hatası: {e}")

    return {"video_id": video_id, "status": "error"}


if __name__ == "__main__":
    import os
    logging.basicConfig(level=logging.INFO)
    print("YouTube Data API modülü yüklendi")
