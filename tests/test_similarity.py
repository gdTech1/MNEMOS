from src.dreaming.similarity import SimilarityCalculator


def test_identical_embeddings():
    embedding = [1.0, 2.0, 3.0]

    result = SimilarityCalculator.cosine_similarity(
        embedding,
        embedding,
    )

    assert result == 1.0


def test_orthogonal_embeddings():
    result = SimilarityCalculator.cosine_similarity(
        [1.0, 0.0],
        [0.0, 1.0],
    )

    assert result == 0.0


def test_different_dimensions():
    try:
        SimilarityCalculator.cosine_similarity(
            [1.0, 2.0],
            [1.0, 2.0, 3.0],
        )
        assert False
    except ValueError:
        assert True


def test_empty_embeddings():
    try:
        SimilarityCalculator.cosine_similarity([], [])
        assert False
    except ValueError:
        assert True


def test_zero_magnitude():
    try:
        SimilarityCalculator.cosine_similarity(
            [0.0, 0.0],
            [1.0, 2.0],
        )
        assert False
    except ValueError:
        assert True