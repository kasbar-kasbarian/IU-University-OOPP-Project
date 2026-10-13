from pathlib import Path

from storage import load_habits


def test_predefined_fixture_has_five_habits_and_two_periodicities():
    path = Path(__file__).resolve().parents[1] / "data" / "sample_data.json"
    habits = load_habits(path)
    assert len(habits) == 5
    assert {habit.periodicity for habit in habits} == {"daily", "weekly"}


def test_predefined_fixture_contains_four_weeks_of_data():
    path = Path(__file__).resolve().parents[1] / "data" / "sample_data.json"
    habits = load_habits(path)
    weekly = next(habit for habit in habits if habit.periodicity == "weekly")
    assert len(weekly.events) == 4
    daily = next(habit for habit in habits if habit.periodicity == "daily")
    assert len({event.timestamp.date() for event in daily.events}) >= 20
