from __future__ import annotations
from datetime import datetime, timedelta, timezone

class TemporalReview:

    def __init__(self, review_interval_days: int = 7):
        if review_interval_days <= 0:
            raise ValueError("Review interval must be greater than zero.")

        self.review_interval = timedelta(days=review_interval_days)

    def is_due(
        self,
        created_at: datetime,
        now: datetime | None = None,
    ):
        if created_at.tzinfo is None:
            raise ValueError("created_at must be timezone-aware.")

        now = now or datetime.now(timezone.utc)

        return now >= created_at + self.review_interval

    def next_review(
        self,
        created_at: datetime,
    ):
        if created_at.tzinfo is None:
            raise ValueError("created_at must be timezone-aware.")

        return created_at + self.review_interval