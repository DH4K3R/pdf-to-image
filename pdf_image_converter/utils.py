from pathlib import Path
from typing import Iterable


def ensure_directory(path: str) -> Path:
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def find_images(paths: Iterable[str]) -> list[Path]:
    return [Path(path) for path in paths if Path(path).exists()]
