from __future__ import annotations
from datetime import datetime, timezone
from enum import Enum
from uuid import uuid4
from pydantic import BaseModel, ConfigDict, Field

class EntityType(str, Enum):
    MEMORY = "memory"
    NOTE = "note"
    CONCEPT = "concept"

class Relationship(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, validate_assignment=True)

    id: str = Field(default_factory=lambda: str(uuid4()))
    source_id: str = Field(..., min_length=1)
    source_type: EntityType
    target_id: str = Field(..., min_length=1)
    target_type: EntityType
    relationship_type: str = Field(..., min_length=1)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))