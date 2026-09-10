from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class AssociationCandidate:
    source_id: str
    target_id: str
    similarity: float

class AssociationGenerator:

    def __init__(self, similarity_threshold: float = 0.75):
        if not 0.0 <= similarity_threshold <= 1.0:
            raise ValueError("Similarity threshold must be between 0.0 and 1.0.")

        self.similarity_threshold = similarity_threshold

    def generate(
        self,
        source_id: str,
        matches: list[dict],
    ):
        associations = []

        for match in matches:
            target_id = match.get("id")
            similarity = match.get("distance")

            if target_id is None or similarity is None:
                continue

            similarity_score = 1.0 - similarity

            if target_id == source_id:
                continue

            if similarity_score < self.similarity_threshold:
                continue

            associations.append(
                AssociationCandidate(
                    source_id=source_id,
                    target_id=target_id,
                    similarity=similarity_score,
                )
            )
        return associations