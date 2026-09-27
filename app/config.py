from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

load_dotenv()


@dataclass
class AppSettings:
    env: str = "development"
    log_level: str = "INFO"
    base_output_dir: str = "./data/output"


def get_base_dir() -> Path:
    return Path(__file__).resolve().parent.parent


def get_settings() -> AppSettings:
    return AppSettings()
