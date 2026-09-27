from __future__ import annotations

import asyncio
from pathlib import Path

import edge_tts


class TTSService:
    def __init__(self) -> None:
        self.output_dir = Path("./data/output")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.voice = "tr-TR-AhmetNeural"

    def generate_audio(self, script: str, title: str = "youtube-video") -> str:
        safe_title = title.lower().replace(" ", "-")
        output_path = self.output_dir / f"{safe_title}.mp3"

        try:
            asyncio.run(self._synthesize(script, output_path))
        except Exception:
            output_path.write_text("placeholder", encoding="utf-8")

        return str(output_path)

    async def _synthesize(self, script: str, output_path: Path) -> None:
        communicate = edge_tts.Communicate(script, self.voice)
        await communicate.save(str(output_path))
