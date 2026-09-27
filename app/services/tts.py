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
