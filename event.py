"""Event model used by the habit completion event log."""

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class CompletionEvent:
    """Represent one immutable habit check-off event."""

    timestamp: datetime
    event_type: str = "check_off"

    def to_dict(self):
        """Return a JSON-serialisable representation of the event."""
        return {
            "timestamp": self.timestamp.isoformat(),
            "event_type": self.event_type,
        }

    @classmethod
    def from_dict(cls, data):
        """Recreate an event from a stored dictionary."""
        if data.get("event_type", "check_off") != "check_off":
            raise ValueError("Unsupported event type.")
        return cls(timestamp=datetime.fromisoformat(data["timestamp"]))
