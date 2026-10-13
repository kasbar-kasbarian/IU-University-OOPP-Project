from datetime import datetime

from cli import create_habit, run_cli, show_analytics
from habit import Habit
from manager import HabitManager


def test_create_habit_saves_and_reports():
    manager = HabitManager()
    calls = []
    inputs = iter(["Read", "daily"])
    output = []
    create_habit(manager, lambda habits: calls.append(list(habits)), lambda _: next(inputs), output.append)
    assert len(manager.habits) == 1
    assert len(calls) == 1
    assert output[-1] == "Created: Read (daily)"


def test_cli_can_exit():
    manager = HabitManager([Habit("Read", "daily")])
    inputs = iter(["6"])
    output = []
    run_cli(manager, lambda habits: None, lambda _: next(inputs), output.append)
    assert output[-1] == "Goodbye."


def test_analytics_menu_shows_overall_streak():
    habit = Habit("Read", "daily", completions=[
        datetime(2026, 8, 1, 12, 0), datetime(2026, 8, 2, 12, 0)
    ])
    inputs = iter(["3"])
    output = []
    show_analytics(HabitManager([habit]), lambda _: next(inputs), output.append)
    assert "Longest streak overall: 2 period(s)" in output
