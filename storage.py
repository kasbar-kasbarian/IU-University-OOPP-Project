"""JSON persistence layer for the habit tracking application."""

import json
from pathlib import Path

from habit import Habit


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
USER_DATA_FILE = DATA_DIR / "habit_data.json"
SAMPLE_DATA_FILE = DATA_DIR / "sample_data.json"


def load_habits(path=None):
    """Load habits from JSON, falling back to predefined sample data."""
    file_path = Path(path) if path else USER_DATA_FILE
    if path is None and not file_path.exists():
        file_path = SAMPLE_DATA_FILE
    if not file_path.exists():
        return []

    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, list):
            raise ValueError("Expected a list of habits.")
        return [Habit.from_dict(item) for item in data]
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        raise ValueError(f"Could not load habit data: {error}")


def save_habits(habits, path=None):
    """Persist all habits as formatted JSON and return the target path."""
    file_path = Path(path) if path else USER_DATA_FILE
    file_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = file_path.with_suffix(file_path.suffix + ".tmp")
    with temporary_path.open("w", encoding="utf-8") as file:
        json.dump([habit.to_dict() for habit in habits], file, indent=2)
        file.write("\n")
    temporary_path.replace(file_path)
    return file_path
