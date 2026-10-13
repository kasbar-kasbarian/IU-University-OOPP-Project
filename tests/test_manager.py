from datetime import datetime

import pytest

from manager import HabitManager


def test_add_and_find_habit():
    manager = HabitManager()
    manager.add_habit("Read", "daily")
    assert manager.find_habit("read").name == "Read"


def test_manager_copies_input_collection():
    habits = []
    manager = HabitManager(habits)
    habits.append("outside")
    assert manager.habits == []


def test_duplicate_name_is_rejected():
    manager = HabitManager()
    manager.add_habit("Read", "daily")
    with pytest.raises(ValueError):
        manager.add_habit("read", "weekly")


def test_delete_habit():
    manager = HabitManager()
    manager.add_habit("Read", "daily")
    assert manager.delete_habit("Read") is True
    assert manager.find_habit("Read") is None


def test_delete_missing_habit():
    assert HabitManager().delete_habit("Missing") is False


def test_check_off_habit():
    manager = HabitManager()
    manager.add_habit("Read", "daily")
    when = datetime(2026, 8, 1, 12, 0)
    assert manager.check_off_habit("Read", when) is True
    assert manager.find_habit("Read").completions == [when]


def test_check_off_missing_habit():
    assert HabitManager().check_off_habit("Missing") is False
