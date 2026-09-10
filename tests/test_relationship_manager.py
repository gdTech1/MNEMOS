from src.graph.relationship_manager import (
    RelationshipManager,
    RelationshipNotFoundError,
)
from src.knowledge.relationship import EntityType


def test_create_relationship():
    manager = RelationshipManager()

    relationship = manager.create_relationship(
        source_id="memory-1",
        source_type=EntityType.MEMORY,
        target_id="concept-1",
        target_type=EntityType.CONCEPT,
        relationship_type="related_to",
    )

    assert relationship.source_id == "memory-1"
    assert relationship.source_type == EntityType.MEMORY
    assert relationship.target_id == "concept-1"
    assert relationship.target_type == EntityType.CONCEPT
    assert relationship.relationship_type == "related_to"
    assert len(manager) == 1


def test_get_relationship():
    manager = RelationshipManager()

    relationship = manager.create_relationship(
        source_id="memory-1",
        source_type=EntityType.MEMORY,
        target_id="concept-1",
        target_type=EntityType.CONCEPT,
        relationship_type="related_to",
    )

    result = manager.get_relationship(relationship.id)

    assert result == relationship


def test_get_relationship_returns_none_when_not_found():
    manager = RelationshipManager()

    result = manager.get_relationship("non-existent")

    assert result is None


def test_get_relationships_for_entity():
    manager = RelationshipManager()

    first = manager.create_relationship(
        source_id="memory-1",
        source_type=EntityType.MEMORY,
        target_id="concept-1",
        target_type=EntityType.CONCEPT,
        relationship_type="related_to",
    )

    second = manager.create_relationship(
        source_id="concept-2",
        source_type=EntityType.CONCEPT,
        target_id="memory-1",
        target_type=EntityType.MEMORY,
        relationship_type="explains",
    )

    manager.create_relationship(
        source_id="note-1",
        source_type=EntityType.NOTE,
        target_id="concept-3",
        target_type=EntityType.CONCEPT,
        relationship_type="contains",
    )

    relationships = manager.get_relationships_for_entity("memory-1")

    assert len(relationships) == 2
    assert first in relationships
    assert second in relationships


def test_list_relationships():
    manager = RelationshipManager()

    first = manager.create_relationship(
        source_id="memory-1",
        source_type=EntityType.MEMORY,
        target_id="concept-1",
        target_type=EntityType.CONCEPT,
        relationship_type="related_to",
    )

    second = manager.create_relationship(
        source_id="note-1",
        source_type=EntityType.NOTE,
        target_id="concept-1",
        target_type=EntityType.CONCEPT,
        relationship_type="contains",
    )

    relationships = manager.list_relationships()

    assert len(relationships) == 2
    assert first in relationships
    assert second in relationships


def test_delete_relationship():
    manager = RelationshipManager()

    relationship = manager.create_relationship(
        source_id="memory-1",
        source_type=EntityType.MEMORY,
        target_id="concept-1",
        target_type=EntityType.CONCEPT,
        relationship_type="related_to",
    )

    manager.delete_relationship(relationship.id)

    assert manager.get_relationship(relationship.id) is None
    assert len(manager) == 0


def test_delete_relationship_raises_when_not_found():
    manager = RelationshipManager()

    try:
        manager.delete_relationship("non-existent")
        assert False
    except RelationshipNotFoundError:
        assert True