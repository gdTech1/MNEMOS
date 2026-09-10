import pytest
from src.dreaming.association_generator import (
    AssociationCandidate,
    AssociationGenerator,
)

def test_generates_association_above_threshold():
    generator = AssociationGenerator(0.75)

    matches = [
        {"id": "memory-2", "distance": 0.10},
    ]

    result = generator.generate("memory-1", matches)

    assert len(result) == 1
    assert result[0] == AssociationCandidate(
        source_id="memory-1",
        target_id="memory-2",
        similarity=0.90,
    )

def test_ignores_match_below_threshold():
    generator = AssociationGenerator(0.75)

    matches = [
        {"id": "memory-2", "distance": 0.40},
    ]

    result = generator.generate("memory-1", matches)

    assert result == []


def test_ignores_source_itself():
    generator = AssociationGenerator(0.75)

    matches = [
        {"id": "memory-1", "distance": 0.05},
    ]

    result = generator.generate("memory-1", matches)

    assert result == []


def test_ignores_incomplete_matches():
    generator = AssociationGenerator(0.75)

    matches = [
        {"id": "memory-2"},
        {"distance": 0.10},
        {},
    ]

    result = generator.generate("memory-1", matches)

    assert result == []


def test_multiple_associations_are_generated():
    generator = AssociationGenerator(0.75)

    matches = [
        {"id": "memory-2", "distance": 0.10},
        {"id": "memory-3", "distance": 0.20},
        {"id": "memory-4", "distance": 0.50},
    ]

    result = generator.generate("memory-1", matches)

    assert len(result) == 2
    assert result[0].target_id == "memory-2"
    assert result[1].target_id == "memory-3"


def test_invalid_threshold_is_rejected():
    with pytest.raises(ValueError):
        AssociationGenerator(1.5)