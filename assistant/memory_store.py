"""SQLite persistence for explicitly approved Aroha memories."""

from datetime import datetime, timezone
import os
import sqlite3


class MemoryStore:
    """Small, local, parameterized SQLite store for user preferences."""

    def __init__(self, database_path, max_memories=100, max_value_length=240):
        self.database_path = database_path
        self.max_memories = max(1, int(max_memories))
        self.max_value_length = max(1, int(max_value_length))
        self._initialize()

    def save(self, key, value, category="preference"):
        key = self._clean(key, 120)
        value = self._clean(value, self.max_value_length)
        if not key or not value:
            raise ValueError("Memory key and value are required")

        now = datetime.now(timezone.utc).isoformat()
        with self._connect() as connection:
            connection.execute(
                """
                INSERT INTO memories (memory_key, memory_value, category, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(memory_key) DO UPDATE SET
                    memory_value = excluded.memory_value,
                    category = excluded.category,
                    updated_at = excluded.updated_at
                """,
                (key, value, category, now, now),
            )
            connection.execute(
                """
                DELETE FROM memories
                WHERE id NOT IN (
                    SELECT id FROM memories ORDER BY updated_at DESC, id DESC LIMIT ?
                )
                """,
                (self.max_memories,),
            )

    def list(self, query=""):
        query = self._clean(query, 120)
        with self._connect() as connection:
            if query:
                pattern = f"%{query}%"
                rows = connection.execute(
                    """
                    SELECT memory_key, memory_value, category, updated_at
                    FROM memories
                    WHERE memory_key LIKE ? OR memory_value LIKE ?
                    ORDER BY updated_at DESC, id DESC
                    LIMIT ?
                    """,
                    (pattern, pattern, self.max_memories),
                ).fetchall()
            else:
                rows = connection.execute(
                    """
                    SELECT memory_key, memory_value, category, updated_at
                    FROM memories
                    ORDER BY updated_at DESC, id DESC
                    LIMIT ?
                    """,
                    (self.max_memories,),
                ).fetchall()
        return [dict(row) for row in rows]

    def delete(self, query):
        query = self._clean(query, 120)
        if not query:
            return 0
        with self._connect() as connection:
            cursor = connection.execute(
                "DELETE FROM memories WHERE memory_key LIKE ? OR memory_value LIKE ?",
                (f"%{query}%", f"%{query}%"),
            )
            return cursor.rowcount

    def _connect(self):
        directory = os.path.dirname(self.database_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialize(self):
        with self._connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS memories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    memory_key TEXT NOT NULL UNIQUE,
                    memory_value TEXT NOT NULL,
                    category TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
                """
            )
            connection.execute(
                "CREATE INDEX IF NOT EXISTS idx_memories_search ON memories(memory_key, memory_value)"
            )

    @staticmethod
    def _clean(value, limit):
        return " ".join(str(value or "").split())[:limit].strip()