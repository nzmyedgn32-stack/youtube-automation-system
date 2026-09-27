from app.services.analytics import AnalyticsService
from app.services.script_writer import ScriptWriterService
from app.services.trends import TrendsService
from app.services.tts import TTSService
from app.services.video_render import VideoRenderService
from app.services.youtube_uploader import YouTubeUploaderService


class VideoAutomationPipeline:
    def __init__(self) -> None:
        self.trends_service = TrendsService()
        self.script_writer = ScriptWriterService()
        self.tts_service = TTSService()
        self.render_service = VideoRenderService()
        self.uploader_service = YouTubeUploaderService()
        self.analytics_service = AnalyticsService()

    def run(self) -> dict:
        topics = self.trends_service.fetch_topics()
        titles = self.script_writer.generate_titles(topics)
        selected_title = titles[0] if titles else "AI ile otomasyon"
        script = self.script_writer.generate_script(selected_title)
        audio_file = self.tts_service.generate_audio(script, selected_title)
        video_path = self.render_service.render_video(selected_title, audio_file)
        thumbnail_path = self.render_service.create_thumbnail(selected_title)
        upload_result = self.uploader_service.upload(video_path, thumbnail_path, selected_title, script)
        metrics = self.analytics_service.fetch_metrics(upload_result.get("video_id"))
        return {
            "topics": topics,
            "titles": titles,
            "selected_title": selected_title,
            "script": script,
            "audio_file": audio_file,
            "video_path": video_path,
            "thumbnail_path": thumbnail_path,
            "upload_result": upload_result,
            "metrics": metrics,
        }


if __name__ == "__main__":
    pipeline = VideoAutomationPipeline()
    result = pipeline.run()
    print(result)
