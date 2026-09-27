#!/usr/bin/env python3
"""
FFmpeg Video Rendering Module
Combines video, audio, subtitles, and effects
"""

import logging
import shutil
import subprocess
from pathlib import Path

logger = logging.getLogger(__name__)


def render_video_with_ffmpeg(
    output_path: str,
    audio_path: str = None,
    duration: int = 300,
    title: str = "YouTube Video",
) -> bool:
    """
    Render MP4 video using FFmpeg
    
    Args:
        output_path: Path to save MP4 file
        audio_path: Path to audio file (MP3/WAV)
        duration: Video duration in seconds
        title: Text to display on video
    
    Returns:
        True if successful, False otherwise
    """
    ffmpeg = shutil.which("ffmpeg")
    if ffmpeg is None:
        logger.error("FFmpeg bulunamadı. Lütfen yükleyin.")
        return False

    safe_title = title.replace("'", "\\'")[:50]
    cmd = [
        ffmpeg,
        "-y",
        "-f", "lavfi",
        "-i", f"color=c=0x111827:s=1920x1080:d={duration}",
        "-vf",
        (
            f"drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:"
            f"text='{safe_title}':fontcolor=white:fontsize=60:"
            f"x=(w-text_w)/2:y=(h-text_h)/2"
        ),
    ]

    if audio_path and Path(audio_path).exists():
        cmd.extend(["-i", audio_path])
        cmd.extend(["-shortest", "-c:v", "libx264", "-c:a", "aac", "-pix_fmt", "yuv420p"])
    else:
        cmd.extend(["-c:v", "libx264", "-pix_fmt", "yuv420p"])

    cmd.append(output_path)

    try:
        logger.info(f"FFmpeg ile video render ediliyor... ({duration} saniye)")
        subprocess.run(cmd, check=True, capture_output=True, timeout=600)
        logger.info(f"✅ Video dosyası kaydedildi: {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"FFmpeg render hatası: {e.stderr.decode()}")
        return False
    except Exception as e:
        logger.error(f"Video render hatası: {e}")
        return False


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    output = "test_video.mp4"
    success = render_video_with_ffmpeg(output, title="Test Video")
    if success:
        print(f"✅ Video oluşturuldu: {output}")
