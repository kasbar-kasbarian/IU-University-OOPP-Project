from datetime import datetime

import pytest

from habit import Habit
from storage import load_habits, save_habits


def test_save_and_load_event_log(tmp_path):
    path = tmp_path / "habits.json"
    habit = Habit("Read", "daily", created_date=datetime(2026, 8, 1, 10, 0))
    habit.check_off(datetime(2026, 8, 1, 20, 0))
    save_habits([habit], path)
    loaded = load_habits(path)
    assert len(loaded) == 1
    assert loaded[0].name == "Read"
    assert loaded[0].events[0].timestamp == datetime(2026, 8, 1, 20, 0)


def test_saved_json_uses_event_log_schema(tmp_path):
    path = tmp_path / "habits.json"
    habit = Habit("Read", "daily")
    save_habits([habit], path)
    text = path.read_text(encoding="utf-8")
    assert '"events"' in text
    assert '"completions"' not in text


def test_missing_file_returns_empty_list(tmp_path):
    assert load_habits(tmp_path / "missing.json") == []


def test_invalid_json_raises_value_error(tmp_path):
    path = tmp_path / "broken.json"
    path.write_text("not json", encoding="utf-8")
    with pytest.raises(ValueError):
        load_habits(path)
