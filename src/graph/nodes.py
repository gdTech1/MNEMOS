from __future__ import annotations
from datetime import datetime, timezone
from enum import Enum
from pydantic import BaseModel, ConfigDict, Field

class NodeType(str, Enum):
    MEMORY = "memory"
    NOTE = "note"
    CONCEPT = "concept"

class Node(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, validate_assignment=True)

    id: str = Field(..., min_length=1)
    entity_type: NodeType
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))