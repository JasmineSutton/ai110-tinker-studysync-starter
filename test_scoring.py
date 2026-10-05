"""
Tinker 1B, Part 1: write an assert-based pytest test for session_rating()
BEFORE you touch anything else. One test is started for you -- add at least
one more.
"""

from datetime import date

from scoring import session_rating
from sessions import find_conflicts, next_occurrence


def test_session_rating_boundary_90_is_great():
    assert session_rating(90) == "Great"


def test_session_rating_boundary_80_is_good():
    assert session_rating(80) == "Good"


def test_next_occurrence_daily_and_weekly():
    assert next_occurrence(date(2026, 1, 1), "daily") == date(2026, 1, 2)
    assert next_occurrence(date(2026, 1, 1), "weekly") == date(2026, 1, 8)


def test_find_conflicts_detects_duplicates_and_handles_empty():
    assert find_conflicts([
        {"subject": "Calc II", "slot": "08:00"},
        {"subject": "Chem Lab", "slot": "08:00"},
        {"subject": "History", "slot": "09:00"},
    ]) == [
        ({"subject": "Calc II", "slot": "08:00"}, {"subject": "Chem Lab", "slot": "08:00"})
    ]
    assert find_conflicts([]) == []
