from datetime import datetime

from habit import Habit
from manager import HabitManager
from storage import load_habits, save_habits


def test_create_checkoff_save_reload_flow(tmp_path):
    path = tmp_path / "habits.json"
    manager = HabitManager()
    manager.add_habit("Study", "daily")
    manager.check_off_habit("Study", datetime(2026, 8, 31, 20, 0))
    save_habits(manager.habits, path)

    reloaded = HabitManager(load_habits(path))
    assert reloaded.find_habit("Study").completions == [datetime(2026, 8, 31, 20, 0)]


def test_delete_then_save_persists_deletion(tmp_path):
    path = tmp_path / "habits.json"
    manager = HabitManager([Habit("Read", "daily")])
    manager.delete_habit("Read")
    save_habits(manager.habits, path)
    assert load_habits(path) == []
