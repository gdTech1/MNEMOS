from __future__ import annotations
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4
from pydantic import BaseModel, ConfigDict, Field

class Note(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, validate_assignment=True)

    id: str = Field(default_factory=lambda: str(uuid4()))
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    importance: int = Field(..., ge=1, le=10)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    def __setattr__(self, name: str, value: Any):
        super().__setattr__(name, value)
        if name != "updated_at":
            super().__setattr__("updated_at", datetime.now(timezone.utc))