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
