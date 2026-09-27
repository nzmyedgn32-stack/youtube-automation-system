from __future__ import annotations

from typing import List

from google import genai

from app.config import settings


class ScriptWriterService:
    def __init__(self) -> None:
        if settings.google_api_key:
            self.client = genai.Client(api_key=settings.google_api_key)
        else:
            self.client = None
        self.model_name = "gemini-flash-latest"

    def generate_titles(self, topics: List[str]) -> List[str]:
        if not topics:
            return ["AI ile içerik üretimi"]

        if self.client is None:
            print("GEMINI HATASI: google_api_key bos (client None)")
            return [f"{topic} için 7 adım" for topic in topics]

        try:
            prompt = (
                "Aşağıdaki konu listesinden en ilgi çekici olanı seç ve YouTube için "
                "tıklanabilir, Türkçe, en fazla 60 karakterlik bir başlık yaz. "
                "Sadece başlığı yaz, tırnak işareti veya başka bir şey ekleme.\n\n"
                "Konular: " + ", ".join(topics)
            )
            response = self.client.models.generate_content(model=self.model_name, contents=prompt)
            title = response.text.strip().strip('"')
            return [title] if title else [f"{topics[0]} için 7 adım"]
        except Exception as e:
            print(f"GEMINI HATASI: {e}")
            return [f"{topic} için 7 adım" for topic in topics]

    def generate_script(self, title: str) -> str:
        if self.client is None:
            return (
                f"Merhaba! Bu videoda {title} konusunu anlatacağım. "
                "Önce temel fikri açıklayacağız, sonra adım adım uygulamayı göreceğiz. "
                "Sonunda da pratik bir örnekle işi tamamlayacağız."
            )

        try:
            prompt = (
                f"'{title}' başlıklı bir YouTube videosu için 45-60 saniyelik, "
                "akıcı ve samimi bir Türkçe anlatım metni yaz. Sadece konuşma "
                "metnini yaz, başlık, yönerge veya emoji ekleme."
            )
            response = self.client.models.generate_content(model=self.model_name, contents=prompt)
            return response.text.strip()
        except Exception as e:
            print(f"GEMINI HATASI: {e}")
            return (
                f"Merhaba! Bu videoda {title} konusunu anlatacağım. "
                "Önce temel fikri açıklayacağız, sonra adım adım uygulamayı göreceğiz. "
                "Sonunda da pratik bir örnekle işi tamamlayacağız."
            )
