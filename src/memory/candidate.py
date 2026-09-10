from __future__ import annotations
from datetime import datetime, timezone
from uuid import uuid4
from pydantic import BaseModel, ConfigDict, Field

class MemoryCandidate(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
    )

    id: str = Field(default_factory=lambda: str(uuid4()))
    content: str = Field(min_length=1)
    importance: int = Field(ge=1, le=10)
    context: str = Field(min_length=1)
    sentiment: str | None = None
    interpretation: str = Field(min_length=1)
    confidence: float = Field(ge=0.0, le=1.0)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )