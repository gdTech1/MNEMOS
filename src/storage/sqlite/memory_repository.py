from __future__ import annotations
import json
import sqlite3
from datetime import datetime
from .database import Database
from ...memory.memory import ConceptCollection, Memory, MemoryStatus

class MemoryNotFoundError(Exception):
    def __init__(self, memory_id: str):
        super().__init__(f"Memory with ID '{memory_id}' not found.")
        self.memory_id = memory_id

class MemoryRepository:
    def __init__(self, database: Database) -> None:
        self._database = database
        self._database.initialize()

    def save_memory(self, memory: Memory):
        conn = self._database.connect()
        conn.execute(
            """
            INSERT INTO memories
                (id, content, concepts, relationships, importance, context,
                 sentiment, interpretation, created_at, reviewed_at, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            self._to_row(memory),
        )
        conn.commit()

    def get_memory(self, memory_id: str):
        conn = self._database.connect()
        row = conn.execute(
            "SELECT * FROM memories WHERE id = ?", (memory_id,)
        ).fetchone()
        return self._from_row(row) if row is not None else None

    def get_all_memories(self):
        conn = self._database.connect()
        rows = conn.execute("SELECT * FROM memories").fetchall()
        return [self._from_row(row) for row in rows]

    def update_memory(self, memory: Memory):
        conn = self._database.connect()
        cursor = conn.execute(
            """
            UPDATE memories
            SET content = ?, concepts = ?, relationships = ?, importance = ?,
                context = ?, sentiment = ?, interpretation = ?,
                created_at = ?, reviewed_at = ?, status = ?
            WHERE id = ?
            """,
            (*self._to_row(memory)[1:], memory.id),
        )
        conn.commit()
        if cursor.rowcount == 0:
            raise MemoryNotFoundError(memory.id)

    def delete_memory(self, memory_id: str):
        conn = self._database.connect()
        cursor = conn.execute("DELETE FROM memories WHERE id = ?", (memory_id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise MemoryNotFoundError(memory_id)

    @staticmethod
    def _to_row(memory: Memory):
        return (
            memory.id,
            memory.content,
            json.dumps(memory.concepts.model_dump()),
            json.dumps(memory.relationships),
            memory.importance,
            memory.context,
            memory.sentiment,
            memory.interpretation,
            memory.created_at.isoformat(),
            memory.reviewed_at.isoformat() if memory.reviewed_at else None,
            memory.status.value,
        )

    @staticmethod
    def _from_row(row: sqlite3.Row):
        return Memory(
            id=row["id"],
            content=row["content"],
            concepts=ConceptCollection(**json.loads(row["concepts"])),
            relationships=json.loads(row["relationships"]),
            importance=row["importance"],
            context=row["context"],
            sentiment=row["sentiment"],
            interpretation=row["interpretation"],
            created_at=datetime.fromisoformat(row["created_at"]),
            reviewed_at=(
                datetime.fromisoformat(row["reviewed_at"])
                if row["reviewed_at"] is not None
                else None
            ),
            status=MemoryStatus(row["status"]),
        )