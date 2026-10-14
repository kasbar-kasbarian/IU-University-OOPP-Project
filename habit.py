"""Domain model for the habit tracking application."""

from datetime import datetime

from event import CompletionEvent


class Habit:
    """Represent one habit and its completion event log."""

    VALID_PERIODICITIES = ("daily", "weekly")

    def __init__(self, name, periodicity, created_date=None, events=None, completions=None):
        """Create a habit with validation and an optional event history."""
        if not name or not name.strip():
            raise ValueError("Habit name cannot be empty.")

        periodicity = periodicity.lower().strip()
        if periodicity not in self.VALID_PERIODICITIES:
            raise ValueError("Periodicity must be 'daily' or 'weekly'.")

        self.name = name.strip()
        self.periodicity = periodicity
        self.created_date = created_date or datetime.now()
        if events is None and completions is not None:
            events = [CompletionEvent(timestamp=item) for item in completions]
        self.events = list(events or [])

    @property
    def completions(self):
        """Return completion timestamps for compatibility and convenience."""
        return [event.timestamp for event in self.events]

    def check_off(self, completed_at=None):
        """Append a check-off event to the habit's event log."""
        timestamp = completed_at or datetime.now()
        if not isinstance(timestamp, datetime):
            raise TypeError("completed_at must be a datetime.")
        self.events.append(CompletionEvent(timestamp=timestamp))

    def to_dict(self):
        """Convert the habit and event log into JSON-friendly data."""
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "created_date": self.created_date.isoformat(),
            "events": [event.to_dict() for event in self.events],
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Habit from the current event-log JSON schema.

        The loader also accepts the original ``completions`` list so older
        Phase-1 data can still be opened without manual conversion.
        """
        if "events" in data:
            events = [CompletionEvent.from_dict(item) for item in data["events"]]
        else:
            events = [
                CompletionEvent(timestamp=datetime.fromisoformat(item))
                for item in data.get("completions", [])
            ]
        return cls(
            name=data["name"],
            periodicity=data["periodicity"],
            created_date=datetime.fromisoformat(data["created_date"]),
            events=events,
        )

    def __str__(self):
        """Return a concise human-readable habit label."""
        return f"{self.name} ({self.periodicity})"
