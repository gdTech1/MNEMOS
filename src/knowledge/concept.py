from __future__ import annotations
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Optional
from uuid import uuid4
from pydantic import BaseModel, ConfigDict, Field

class ConceptType(str, Enum):
    ENTITY = "entity"
    TOPIC = "topic"


class Concept(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, validate_assignment=True)

    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str = Field(..., min_length=1)
    type: ConceptType
    description: Optional[str] = Field(default=None, min_length=1)
    importance: int = Field(..., ge=1, le=10)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    def __setattr__(self, name: str, value: Any):
        super().__setattr__(name, value)
        if name != "updated_at":
            super().__setattr__("updated_at", datetime.now(timezone.utc))