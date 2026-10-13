from datetime import datetime

import pytest

from event import CompletionEvent
from habit import Habit


def test_create_daily_habit():
    habit = Habit("Read", "daily")
    assert habit.name == "Read"
    assert habit.periodicity == "daily"


def test_create_weekly_habit():
    habit = Habit("Review", "weekly")
    assert habit.periodicity == "weekly"


def test_input_is_normalised():
    habit = Habit("  Read  ", " DAILY ")
    assert habit.name == "Read"
    assert habit.periodicity == "daily"


def test_invalid_periodicity():
    with pytest.raises(ValueError):
        Habit("Read", "monthly")


def test_empty_name():
    with pytest.raises(ValueError):
        Habit("   ", "daily")


def test_check_off_creates_event():
    habit = Habit("Read", "daily")
    when = datetime(2026, 8, 1, 12, 0)
    habit.check_off(when)
    assert habit.completions == [when]
    assert habit.events == [CompletionEvent(when)]


def test_check_off_rejects_non_datetime():
    habit = Habit("Read", "daily")
    with pytest.raises(TypeError):
        habit.check_off("2026-08-01")


def test_to_dict_and_from_dict():
    when = datetime(2026, 8, 1, 12, 0)
    original = Habit("Read", "daily", created_date=when, events=[CompletionEvent(when)])
    restored = Habit.from_dict(original.to_dict())
    assert restored.name == original.name
    assert restored.periodicity == original.periodicity
    assert restored.created_date == original.created_date
    assert restored.events == original.events


def test_from_dict_accepts_phase1_completion_schema():
    when = datetime(2026, 8, 1, 12, 0)
    restored = Habit.from_dict({
        "name": "Read",
        "periodicity": "daily",
        "created_date": when.isoformat(),
        "completions": [when.isoformat()],
    })
    assert restored.completions == [when]
