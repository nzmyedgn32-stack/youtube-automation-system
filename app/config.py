import os
from pathlib import Path


class Settings:
    def __init__(self) -> None:
        self.app_env = os.getenv("APP_ENV", "development")
        self.log_level = os.getenv("LOG_LEVEL", "INFO")
        self.base_output_dir = Path(os.getenv("BASE_OUTPUT_DIR", "./data/output")).resolve()
        self.asset_dir = Path(os.getenv("ASSET_DIR", "./data/assets")).resolve()
        self.script_dir = Path(os.getenv("SCRIPT_DIR", "./data/scripts")).resolve()
        self.topic_dir = Path(os.getenv("TOPIC_DIR", "./data/topics")).resolve()

        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.youtube_client_id = os.getenv("YOUTUBE_CLIENT_ID")
        self.youtube_client_secret = os.getenv("YOUTUBE_CLIENT_SECRET")
        self.youtube_refresh_token = os.getenv("YOUTUBE_REFRESH_TOKEN")
        self.elevenlabs_voice_id = os.getenv("ELEVENLABS_VOICE_ID", "21m00Tcm4TlvDq8ikWAM")

        self.ensure_directories()

    def ensure_directories(self) -> None:
        for path in [
            self.base_output_dir,
            self.asset_dir,
            self.script_dir,
            self.topic_dir,
        ]:
            path.mkdir(parents=True, exist_ok=True)


settings = Settings()
