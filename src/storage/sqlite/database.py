from __future__ import annotations
import sqlite3
from pathlib import Path

DEFAULT_DB_PATH = Path("data/mnemos.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS memories (
    id TEXT PRIMARY KEY,
    content TEXT NOT NULL,
    concepts TEXT NOT NULL,
    relationships TEXT NOT NULL,
    importance INTEGER NOT NULL,
    context TEXT NOT NULL,
    sentiment TEXT NOT NULL,
    interpretation TEXT NOT NULL,
    created_at TEXT NOT NULL,
    reviewed_at TEXT,
    status TEXT NOT NULL
)
"""


class Database:

    def __init__(self, db_path: str | Path = DEFAULT_DB_PATH):
        self.db_path = Path(db_path)
        if str(self.db_path) != ":memory:":
            self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._connection: sqlite3.Connection | None = None

    def connect(self):
        if self._connection is None:
            self._connection = sqlite3.connect(self.db_path)
            self._connection.row_factory = sqlite3.Row
            self._connection.execute("PRAGMA foreign_keys = ON")
        return self._connection

    def initialize(self):
        conn = self.connect()
        conn.execute(SCHEMA)
        conn.commit()

    def close(self):
        if self._connection is not None:
            self._connection.close()
            self._connection = None

    def __enter__(self):
        self.initialize()
        return self

    def __exit__(self, *exc_info: object):
        self.close()