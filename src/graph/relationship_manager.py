from __future__ import annotations
from ..knowledge.relationship import EntityType, Relationship

class RelationshipNotFoundError(KeyError):
    pass

class RelationshipManager:

    def __init__(self):
        self._relationships: dict[str, Relationship] = {}

    def create_relationship(
        self,
        source_id: str,
        source_type: EntityType,
        target_id: str,
        target_type: EntityType,
        relationship_type: str,
    ):
        relationship = Relationship(
            source_id=source_id,
            source_type=source_type,
            target_id=target_id,
            target_type=target_type,
            relationship_type=relationship_type,
        )

        self._relationships[relationship.id] = relationship

        return relationship

    def get_relationship(self, relationship_id: str):
        return self._relationships.get(relationship_id)

    def get_relationships_for_entity(self, entity_id: str):
        return [
            relationship
            for relationship in self._relationships.values()
            if (
                relationship.source_id == entity_id
                or relationship.target_id == entity_id
            )
        ]

    def list_relationships(self):
        return list(self._relationships.values())

    def delete_relationship(self, relationship_id: str):
        if relationship_id not in self._relationships:
            raise RelationshipNotFoundError(
                f"Relationship with ID '{relationship_id}' not found."
            )

        del self._relationships[relationship_id]

    def __len__(self):
        return len(self._relationships)