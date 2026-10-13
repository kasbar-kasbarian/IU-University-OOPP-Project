"""Application service for managing a collection of Habit objects."""

from habit import Habit


class HabitManager:
    """Coordinate habit creation, lookup, deletion and check-offs."""

    def __init__(self, habits=None):
        """Initialise the manager with an optional habit collection."""
        self.habits = list(habits or [])

    def add_habit(self, name, periodicity):
        """Create and add a new habit, rejecting duplicate names."""
        if self.find_habit(name) is not None:
            raise ValueError("A habit with this name already exists.")
        habit = Habit(name, periodicity)
        self.habits.append(habit)
        return habit

    def find_habit(self, name):
        """Return a habit by case-insensitive name, or ``None``."""
        if not name:
            return None
        target = name.strip().lower()
        return next((habit for habit in self.habits if habit.name.lower() == target), None)

    def delete_habit(self, name):
        """Delete a habit by name and return whether it existed."""
        habit = self.find_habit(name)
        if habit is None:
            return False
        self.habits.remove(habit)
        return True

    def check_off_habit(self, name, completed_at=None):
        """Check off a named habit and return whether it existed."""
        habit = self.find_habit(name)
        if habit is None:
            return False
        habit.check_off(completed_at)
        return True
