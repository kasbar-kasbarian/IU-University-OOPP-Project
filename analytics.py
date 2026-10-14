"""Pure, read-only analytics functions for habit data."""

from datetime import timedelta


def all_habits(habits):
    """Return a new list containing all currently tracked habits."""
    return list(habits)


def habits_by_periodicity(habits, periodicity):
    """Return habits matching ``daily`` or ``weekly`` without mutation."""
    periodicity = periodicity.lower().strip()
    return list(filter(lambda habit: habit.periodicity == periodicity, habits))


def completed_periods(habit):
    """Return sorted unique completed calendar periods for one habit."""
    if habit.periodicity == "daily":
        periods = {event.timestamp.date() for event in habit.events}
    else:
        periods = {
            event.timestamp.date() - timedelta(days=event.timestamp.weekday())
            for event in habit.events
        }
    return sorted(periods)


def longest_streak_for_habit(habit):
    """Return the longest run of consecutive completed periods."""
    periods = completed_periods(habit)
    if not periods:
        return 0

    step = timedelta(days=1 if habit.periodicity == "daily" else 7)
    pairs = zip(periods, periods[1:])
    runs = []
    current = 1
    for previous, current_period in pairs:
        if current_period - previous == step:
            current += 1
        else:
            runs.append(current)
            current = 1
    runs.append(current)
    return max(runs)


def longest_streak_overall(habits):
    """Return the greatest streak value across all supplied habits."""
    return max(map(longest_streak_for_habit, habits), default=0) 
