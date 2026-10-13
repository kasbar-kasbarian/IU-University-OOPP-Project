from datetime import datetime

import pytest

from event import CompletionEvent


def test_event_round_trip():
    timestamp = datetime(2026, 8, 1, 12, 30)
    event = CompletionEvent(timestamp)
    assert CompletionEvent.from_dict(event.to_dict()) == event


def test_event_is_immutable():
    event = CompletionEvent(datetime(2026, 8, 1, 12, 30))
    with pytest.raises(AttributeError):
        event.timestamp = datetime(2026, 8, 2, 12, 30)
