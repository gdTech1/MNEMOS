from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from .association_generator import AssociationCandidate, AssociationGenerator
from .similarity import SimilarityCalculator
from .temporal_review import TemporalReview

@dataclass(frozen=True)
class DreamResult:
    associations: list[AssociationCandidate]
    review_due: bool

class DreamEngine:

    def __init__(
        self,
        similarity: SimilarityCalculator | None = None,
        temporal_review: TemporalReview | None = None,
        association_generator: AssociationGenerator | None = None,
    ):
        self.similarity = similarity or SimilarityCalculator()
        self.temporal_review = temporal_review or TemporalReview()
        self.association_generator = (
            association_generator or AssociationGenerator()
        )

    def process(
        self,
        source_id: str,
        source_embedding: list[float],
        matches: list[dict],
        created_at: datetime,
        now: datetime | None = None,
    ):
        review_due = self.temporal_review.is_due(
            created_at,
            now,
        )

        associations = self.association_generator.generate(
            source_id,
            matches,
        )

        return DreamResult(
            associations=associations,
            review_due=review_due,
        )