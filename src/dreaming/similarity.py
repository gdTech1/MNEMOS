from __future__ import annotations
import math

class SimilarityCalculator:

    @staticmethod
    def cosine_similarity(
        embedding_a: list[float],
        embedding_b: list[float],
    ):
        if len(embedding_a) != len(embedding_b):
            raise ValueError("Embeddings must have the same dimensions.")

        if not embedding_a or not embedding_b:
            raise ValueError("Embeddings cannot be empty.")

        dot_product = sum(
            a * b
            for a, b in zip(embedding_a, embedding_b)
        )

        magnitude_a = math.sqrt(
            sum(a * a for a in embedding_a)
        )

        magnitude_b = math.sqrt(
            sum(b * b for b in embedding_b)
        )

        if magnitude_a == 0 or magnitude_b == 0:
            raise ValueError("Embeddings cannot have zero magnitude.")

        return dot_product / (magnitude_a * magnitude_b)