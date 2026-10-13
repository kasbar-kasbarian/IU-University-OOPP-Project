"""Application entry point: compose storage, domain logic and CLI."""

from cli import run_cli
from manager import HabitManager
from storage import load_habits, save_habits


def main():
    """Load persisted/sample data and start the command-line interface."""
    try:
        manager = HabitManager(load_habits())
    except ValueError as error:
        print(error)
        manager = HabitManager()
    run_cli(manager, save_habits)


if __name__ == "__main__":
    main()
