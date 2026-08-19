from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, model_validator


class MemoryStatus(str, Enum):

    TEMPORARY = "temporary"
    REVIEW_PENDING = "review_pending"
    CONSOLIDATED = "consolidated"
    ARCHIVED = "archived"


class ConceptCollection(BaseModel):

    model_config = ConfigDict(str_strip_whitespace=True)

    entities: list[str] = Field(
        default_factory=list,
        description=(
            "Concrete, named entities associated with the memory "
            "(e.g. people, places, organizations, objects, systems)."
        ),
    )
    topics: list[str] = Field(
        default_factory=list,
        description=(
            "Abstract topics, themes, or domains associated with the "
            "memory (e.g. 'career planning', 'trust', 'machine learning')."
        ),
    )


class Memory(BaseModel):

    model_config = ConfigDict(str_strip_whitespace=True, validate_assignment=True)

    id: str = Field(
        default_factory=lambda: str(uuid4()),
        description="Unique identifier for the memory.",
    )
    content: str = Field(
        ...,
        min_length=1,
        description="The meaningful experience stored by the system.",
    )
    concepts: ConceptCollection = Field(
        default_factory=ConceptCollection,
        description=(
            "Structured concepts associated with the memory, divided into "
            "entities and topics."
        ),
    )
    relationships: list[str] = Field(
        default_factory=list,
        description="Identifiers of other memories this memory is connected to.",
    )
    importance: int = Field(
        ...,
        ge=1,
        le=10,
        description="Importance score of the memory, from 1 (trivial) to 10 (critical).",
    )
    context: str = Field(
        ...,
        min_length=1,
        description="Explanation of why the memory is important.",
    )
    sentiment: str = Field(
        ...,
        min_length=1,
        description="The emotional context associated with the memory.",
    )
    interpretation: str = Field(
        ...,
        min_length=1,
        description="The meaning assigned to the experience.",
    )
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Timestamp indicating when the memory was created.",
    )
    reviewed_at: Optional[datetime] = Field(
        default=None,
        description="Timestamp indicating the last time the memory was reviewed.",
    )
    status: MemoryStatus = Field(
        default=MemoryStatus.TEMPORARY,
        description="Current lifecycle status of the memory.",
    )

    @model_validator(mode="after")
    def _validate_reviewed_at_not_before_created_at(self) -> "Memory":
        """
        Ensure temporal consistency between creation and review timestamps.

        Raises:
            ValueError: If `reviewed_at` is set and occurs before
                `created_at`.
        """
        if self.reviewed_at is not None and self.reviewed_at < self.created_at:
            raise ValueError("reviewed_at cannot be earlier than created_at.")
        return self