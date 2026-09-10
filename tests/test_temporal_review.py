from datetime import datetime, timedelta, timezone
import pytest
from src.dreaming.temporal_review import TemporalReview

def test_memory_is_not_due_before_interval():
    review = TemporalReview(7)

    created_at = datetime.now(timezone.utc)

    assert review.is_due(created_at) is False


def test_memory_is_due_after_interval():
    review = TemporalReview(7)

    created_at = datetime.now(timezone.utc) - timedelta(days=8)

    assert review.is_due(created_at) is True


def test_memory_is_due_exactly_at_interval():
    review = TemporalReview(7)

    created_at = datetime(2026, 1, 1, tzinfo=timezone.utc)
    now = created_at + timedelta(days=7)

    assert review.is_due(created_at, now) is True


def test_next_review_returns_correct_date():
    review = TemporalReview(7)

    created_at = datetime(2026, 1, 1, tzinfo=timezone.utc)

    expected = datetime(2026, 1, 8, tzinfo=timezone.utc)

    assert review.next_review(created_at) == expected


def test_invalid_interval_is_rejected():
    with pytest.raises(ValueError):
        TemporalReview(0)


def test_naive_datetime_is_rejected():
    review = TemporalReview(7)

    created_at = datetime(2026, 1, 1)

    with pytest.raises(ValueError):
        review.is_due(created_at)