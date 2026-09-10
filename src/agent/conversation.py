from __future__ import annotations
from datetime import datetime, timezone
from enum import Enum
from uuid import uuid4
from pydantic import BaseModel, ConfigDict, Field

class MessageRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"

class Message(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    id: str = Field(default_factory=lambda: str(uuid4()))
    role: MessageRole
    content: str = Field(min_length=1)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

class Conversation(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
    )

    id: str = Field(default_factory=lambda: str(uuid4()))
    messages: list[Message] = Field(default_factory=list)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def add_message(
        self,
        role: MessageRole,
        content: str,
    ):
        message = Message(
            role=role,
            content=content,
        )

        self.messages.append(message)

        return message

    def get_messages(self):
        return list(self.messages)

    def get_last_message(self):
        if not self.messages:
            return None

        return self.messages[-1]

    def __len__(self):
        return len(self.messages)