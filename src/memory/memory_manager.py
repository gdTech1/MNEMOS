from __future__ import annotations
from datetime import datetime, timezone
from typing import Any, Optional
from .memory import ConceptCollection, Memory, MemoryStatus

class MemoryNotFoundError(KeyError):
    """Raised when a memory with the specified ID is not found in the MemoryManager."""
    pass

class MemoryManager:

    def __init__(self) -> None:
        self._memories: dict[str, Memory] = {}

    def create_memory(
        self,
        content: str,
        importance: int,
        context: str,
        sentiment: str,
        interpretation: str,
        concepts: Optional[ConceptCollection] = None,
        relationships: Optional[list[str]] = None,
        status: MemoryStatus = MemoryStatus.TEMPORARY):
        memory = Memory(
            content=content,
            importance=importance,
            context=context,
            sentiment=sentiment,
            interpretation=interpretation,
            concepts=concepts if concepts is not None else ConceptCollection(),
            relationships=relationships if relationships is not None else [],
            status=status,
        )
        self._memories[memory.id] = memory
        return memory

    def get_memory(self, memory_id: str): 
        return self._memories.get(memory_id)

    def update_memory(self, memory_id: str, **fields: Any):
        memory = self._get_or_raise(memory_id)

        immutable_fields = {"id", "created_at"}
        valid_fields = set(Memory.model_fields.keys())

        for field_name in fields:
            if field_name in immutable_fields:
                raise ValueError(f"Field '{field_name}' cannot be modified.")
            if field_name not in valid_fields:
                raise ValueError(f"'{field_name}' is not a valid Memory field.")

        for field_name, value in fields.items():
            setattr(memory, field_name, value)

        return memory

    def review_memory(
        self,
        memory_id: str,
        new_status: MemoryStatus = MemoryStatus.CONSOLIDATED):
        memory = self._get_or_raise(memory_id)
        memory.reviewed_at = datetime.now(timezone.utc)
        memory.status = new_status
        return memory

    def archive_memory(self, memory_id: str):
        memory = self._get_or_raise(memory_id)
        memory.status = MemoryStatus.ARCHIVED
        return memory

    def list_memories(self, status: Optional[MemoryStatus] = None):
        memories = list(self._memories.values())
        if status is not None:
            memories = [memory for memory in memories if memory.status == status]
        return memories

    def _get_or_raise(self, memory_id: str):
        memory = self._memories.get(memory_id)
        if memory is None:
            raise MemoryNotFoundError(f"No memory found with id '{memory_id}'.")
        return memory

    def __len__(self):
        return len(self._memories)