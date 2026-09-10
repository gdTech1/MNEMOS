from datetime import datetime, timedelta, timezone
from src.dreaming.dream_engine import DreamEngine

def test_process_generates_associations_and_review_status():
    engine = DreamEngine()

    created_at = datetime.now(timezone.utc) - timedelta(days=8)

    matches = [
        {
            "id": "memory-2",
            "distance": 0.10,
        },
        {
            "id": "memory-3",
            "distance": 0.50,
        },
    ]

    result = engine.process(
        source_id="memory-1",
        source_embedding=[1.0, 0.0],
        matches=matches,
        created_at=created_at,
    )

    assert result.review_due is True
    assert len(result.associations) == 1
    assert result.associations[0].source_id == "memory-1"
    assert result.associations[0].target_id == "memory-2"


def test_process_detects_memory_not_due_for_review():
    engine = DreamEngine()

    created_at = datetime.now(timezone.utc)

    result = engine.process(
        source_id="memory-1",
        source_embedding=[1.0, 0.0],
        matches=[],
        created_at=created_at,
    )

    assert result.review_due is False
    assert result.associations == []


def test_process_does_not_modify_input_matches():
    engine = DreamEngine()

    matches = [
        {
            "id": "memory-2",
            "distance": 0.10,
        }
    ]

    original = matches.copy()

    engine.process(
        source_id="memory-1",
        source_embedding=[1.0, 0.0],
        matches=matches,
        created_at=datetime.now(timezone.utc),
    )

    assert matches == original