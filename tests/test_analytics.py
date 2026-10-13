from datetime import datetime

from analytics import (
    all_habits,
    completed_periods,
    habits_by_periodicity,
    longest_streak_for_habit,
    longest_streak_overall,
)
from habit import Habit


def test_all_habits_returns_copy():
    habits = [Habit("Read", "daily")]
    result = all_habits(habits)
    assert result == habits
    assert result is not habits


def test_filter_by_periodicity():
    habits = [Habit("Read", "daily"), Habit("Review", "weekly")]
    assert [h.name for h in habits_by_periodicity(habits, "daily")] == ["Read"]


def test_daily_completed_periods_are_unique_and_sorted():
    habit = Habit("Read", "daily", completions=[])
    habit.check_off(datetime(2026, 8, 2, 12, 0))
    habit.check_off(datetime(2026, 8, 1, 12, 0))
    habit.check_off(datetime(2026, 8, 1, 18, 0))
    assert completed_periods(habit) == [datetime(2026, 8, 1).date(), datetime(2026, 8, 2).date()]


def test_daily_longest_streak():
    habit = Habit("Read", "daily", completions=[
        datetime(2026, 8, 1, 12, 0), datetime(2026, 8, 2, 12, 0),
        datetime(2026, 8, 3, 12, 0), datetime(2026, 8, 5, 12, 0),
    ])
    assert longest_streak_for_habit(habit) == 3


def test_duplicate_same_day_counts_once():
    habit = Habit("Read", "daily", completions=[
        datetime(2026, 8, 1, 12, 0), datetime(2026, 8, 1, 18, 0),
        datetime(2026, 8, 2, 12, 0),
    ])
    assert longest_streak_for_habit(habit) == 2


def test_weekly_completed_periods_use_monday():
    habit = Habit("Review", "weekly", completions=[
        datetime(2026, 7, 5, 12, 0), datetime(2026, 7, 12, 12, 0)
    ])
    assert len(completed_periods(habit)) == 2
    assert completed_periods(habit)[0].weekday() == 0


def test_weekly_longest_streak():
    habit = Habit("Review", "weekly", completions=[
        datetime(2026, 7, 5, 12, 0), datetime(2026, 7, 12, 12, 0),
        datetime(2026, 7, 19, 12, 0), datetime(2026, 8, 2, 12, 0),
    ])
    assert longest_streak_for_habit(habit) == 3


def test_empty_habit_streak_is_zero():
    assert longest_streak_for_habit(Habit("Empty", "daily")) == 0


def test_longest_streak_overall():
    a = Habit("A", "daily", completions=[datetime(2026, 8, 1, 12, 0), datetime(2026, 8, 2, 12, 0)])
    b = Habit("B", "daily", completions=[
        datetime(2026, 8, 1, 12, 0), datetime(2026, 8, 2, 12, 0),
        datetime(2026, 8, 3, 12, 0), datetime(2026, 8, 4, 12, 0),
    ])
    assert longest_streak_overall([a, b]) == 4


def test_analytics_do_not_mutate_events():
    habit = Habit("Read", "daily", completions=[datetime(2026, 8, 1, 12, 0)])
    before = list(habit.events)
    longest_streak_for_habit(habit)
    assert habit.events == before
