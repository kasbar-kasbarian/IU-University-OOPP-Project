# Habit Tracking App

Habit Tracking App – a small command-line application for creating, managing and analysing daily and weekly habits.

## Requirements and installation

Python 3.7 or newer.

The application itself uses only Python standard library modules.

For running the test suite, `pytest` is required.

|Library|Installation|
|-|-|
|pytest|`pip install pytest`|

Or install the test dependency with:

```bash
pip install -r requirements.txt
```

No additional package is required to run the application itself.



Then run the application with:

```bash
python main.py
```



## Data

The application uses JSON files to store habit data between sessions.

The project contains:

* `data/sample\_data.json` – five predefined habits with four weeks of example tracking data
* `data/habit\_data.json` – saved user habit data
* `habit.py` – Habit class
* `manager.py` – HabitManager class
* `storage.py` – JSON loading and saving
* `analytics.py` – analytics and streak calculations
* `main.py` – command-line interface
* `tests/` – unit tests for the main application components

On the first run, the application loads the predefined sample data if no user data file exists.

## Execution

### Start the application

Open a terminal in the project folder and run:

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

After starting the application, the following menu is displayed:

```text
Habit Tracker
1. Create habit
2. Check off habit
3. List habits
4. View analytics
5. Delete habit
6. Exit
```

Enter the number of the desired action.

### Create a habit

Example:

```text
Choose 1-6: 1
Habit name: Read
Periodicity (daily/weekly): daily
Created: Read (daily)
```

### Check off a habit

Example:

```text
Choose 1-6: 2
Habit to check off: Read
Habit checked off.
```

### List habits

Select option `3` to display all currently tracked habits.

### Delete a habit

Select option `5` to delete an existing habit. The application asks for confirmation before deleting the habit.



## Tests

The project uses `pytest` for unit testing.

To run the complete test suite:

```bash
python -m pytest -q
```

Alternatively:

```bash
python -m pytest
```



## Author

Kasbar Kasbarian

