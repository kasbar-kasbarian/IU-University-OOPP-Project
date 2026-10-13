"""Command-line user interface for the habit tracker."""

from analytics import (
    all_habits,
    habits_by_periodicity,
    longest_streak_for_habit,
    longest_streak_overall,
)


MENU = (
    "1. Create habit",
    "2. Check off habit",
    "3. List habits",
    "4. View analytics",
    "5. Delete habit",
    "6. Exit",
)


def print_habits(habits, output=print):
    """Print habits as a numbered list."""
    habits = list(habits)
    if not habits:
        output("No habits found.")
        return
    for number, habit in enumerate(habits, start=1):
        output(f"{number}. {habit}")


def create_habit(manager, save, input_fn=input, output=print):
    """Collect user input, create a habit and persist the change."""
    name = input_fn("Habit name: ").strip()
    periodicity = input_fn("Periodicity (daily/weekly): ").strip().lower()
    try:
        habit = manager.add_habit(name, periodicity)
        save(manager.habits)
        output(f"Created: {habit}")
    except ValueError as error:
        output(str(error))


def check_off_habit(manager, save, input_fn=input, output=print):
    """Check off a selected habit and persist the new event."""
    print_habits(manager.habits, output)
    name = input_fn("Habit to check off: ").strip()
    if manager.check_off_habit(name):
        save(manager.habits)
        output("Habit checked off.")
    else:
        output("Habit not found.")


def show_analytics(manager, input_fn=input, output=print):
    """Display the four required functional analytics operations."""
    output("\nAnalytics")
    output("1. List all habits")
    output("2. List habits by periodicity")
    output("3. Longest streak overall")
    output("4. Longest streak for one habit")
    choice = input_fn("Choose 1-4: ").strip()

    if choice == "1":
        print_habits(all_habits(manager.habits), output)
    elif choice == "2":
        periodicity = input_fn("daily or weekly: ").strip().lower()
        print_habits(habits_by_periodicity(manager.habits, periodicity), output)
    elif choice == "3":
        output(f"Longest streak overall: {longest_streak_overall(manager.habits)} period(s)")
    elif choice == "4":
        name = input_fn("Habit name: ").strip()
        habit = manager.find_habit(name)
        if habit is None:
            output("Habit not found.")
        else:
            output(
                f"Longest streak for {habit.name}: "
                f"{longest_streak_for_habit(habit)} period(s)"
            )
    else:
        output("Invalid choice.")


def delete_habit(manager, save, input_fn=input, output=print):
    """Delete a habit after explicit confirmation."""
    print_habits(manager.habits, output)
    name = input_fn("Habit to delete: ").strip()
    habit = manager.find_habit(name)
    if habit is None:
        output("Habit not found.")
        return

    confirm = input_fn(f"Delete '{habit.name}'? (y/n): ").strip().lower()
    if confirm == "y":
        manager.delete_habit(name)
        save(manager.habits)
        output("Habit deleted.")
    else:
        output("Deletion cancelled.")


def run_cli(manager, save, input_fn=input, output=print):
    """Run the interactive menu until the user selects Exit."""
    while True:
        output("\nHabit Tracker")
        for item in MENU:
            output(item)
        choice = input_fn("Choose 1-6: ").strip()

        if choice == "1":
            create_habit(manager, save, input_fn, output)
        elif choice == "2":
            check_off_habit(manager, save, input_fn, output)
        elif choice == "3":
            print_habits(manager.habits, output)
        elif choice == "4":
            show_analytics(manager, input_fn, output)
        elif choice == "5":
            delete_habit(manager, save, input_fn, output)
        elif choice == "6":
            output("Goodbye.")
            return
        else:
            output("Invalid choice. Please enter a number from 1 to 6.") 
