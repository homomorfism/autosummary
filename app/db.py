"""SQLite storage for quiz attempts and question psychometrics (experiment E3).

One database (``QUIZ_DB_PATH``, default ``data/quiz_results.db``) holds:

* ``attempts`` — one row per submitted quiz (course, lecture, score);
* ``answers`` — one row per answered question inside an attempt. Questions are
  identified by a stable content hash (``question_id``) so statistics survive
  reordering of ``quiz.json``;
* ``retired_questions`` — the archive of questions removed by the rejection
  rule (``app.quality``), together with the statistics that condemned them.

All functions take an explicit ``db_path`` (defaulting to config) so tests and
one-off experiments can run against a scratch database.
"""

from __future__ import annotations

import hashlib
import json
import sqlite3
from pathlib import Path

from app import config

_SCHEMA = """\
CREATE TABLE IF NOT EXISTS attempts (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    course      TEXT NOT NULL,
    lecture     TEXT NOT NULL,
    created_at  TEXT NOT NULL DEFAULT (datetime('now')),
    score       INTEGER NOT NULL,
    total       INTEGER NOT NULL,
    client_id   TEXT,
    ip          TEXT,
    deleted_at  TEXT
);

CREATE TABLE IF NOT EXISTS answers (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    attempt_id   INTEGER NOT NULL REFERENCES attempts(id) ON DELETE CASCADE,
    question_id  TEXT NOT NULL,
    question     TEXT NOT NULL,
    chosen_index INTEGER NOT NULL,
    is_correct   INTEGER NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_answers_question ON answers(question_id);
CREATE INDEX IF NOT EXISTS idx_attempts_lecture ON attempts(course, lecture);

CREATE TABLE IF NOT EXISTS retired_questions (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    course         TEXT NOT NULL,
    lecture        TEXT NOT NULL,
    question_id    TEXT NOT NULL,
    question_json  TEXT NOT NULL,
    reason         TEXT NOT NULL,
    n_attempts     INTEGER,
    p_value        REAL,
    point_biserial REAL,
    retired_at     TEXT NOT NULL DEFAULT (datetime('now'))
);
"""


def question_id(course: str, lecture: str, question_text: str) -> str:
    """Stable identifier of a question: hash of (lecture, question text)."""
    raw = f"{course}/{lecture}//{question_text.strip()}"
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:16]


def _migrate(conn: sqlite3.Connection) -> None:
    """Add columns introduced after the initial release (CREATE TABLE IF NOT
    EXISTS never alters an existing table)."""
    existing = {row["name"] for row in conn.execute("PRAGMA table_info(attempts)")}
    for name in ("client_id", "ip", "deleted_at"):
        if name not in existing:
            conn.execute(f"ALTER TABLE attempts ADD COLUMN {name} TEXT")


def connect(db_path: Path | None = None) -> sqlite3.Connection:
    """Open the results DB, creating the schema on first use."""
    path = Path(db_path or config.QUIZ_DB_PATH)
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(_SCHEMA)
    _migrate(conn)
    return conn


def record_attempt(
    course: str,
    lecture: str,
    answers: list[dict],
    *,
    db_path: Path | None = None,
) -> int:
    """Save a submitted quiz. Each answer dict: question, chosen_index, is_correct.

    Returns the attempt id.
    """
    score = sum(1 for a in answers if a["is_correct"])
    with connect(db_path) as conn:
        cur = conn.execute(
            "INSERT INTO attempts (course, lecture, score, total) VALUES (?, ?, ?, ?)",
            (course, lecture, score, len(answers)),
        )
        attempt_id = cur.lastrowid
        conn.executemany(
            "INSERT INTO answers (attempt_id, question_id, question, chosen_index, is_correct) VALUES (?, ?, ?, ?, ?)",
            [
                (
                    attempt_id,
                    question_id(course, lecture, a["question"]),
                    a["question"],
                    a["chosen_index"],
                    int(a["is_correct"]),
                )
                for a in answers
            ],
        )
    return attempt_id


def get_attempt(attempt_id: int, *, db_path: Path | None = None) -> tuple[dict, list[dict]] | None:
    """Return (attempt row, its answers) or None if the attempt does not exist."""
    with connect(db_path) as conn:
        attempt = conn.execute("SELECT * FROM attempts WHERE id = ?", (attempt_id,)).fetchone()
        if attempt is None:
            return None
        answers = conn.execute("SELECT * FROM answers WHERE attempt_id = ? ORDER BY id", (attempt_id,)).fetchall()
    return dict(attempt), [dict(a) for a in answers]


def load_responses(course: str, lecture: str, *, db_path: Path | None = None) -> list[dict]:
    """All answers for a lecture joined with their attempt (input for item stats).

    Soft-deleted attempts (replaced by a retake in the web app) are excluded.
    """
    with connect(db_path) as conn:
        rows = conn.execute(
            """
            SELECT a.attempt_id, a.question_id, a.question, a.is_correct, t.score, t.total
            FROM answers a JOIN attempts t ON t.id = a.attempt_id
            WHERE t.course = ? AND t.lecture = ? AND t.deleted_at IS NULL
            ORDER BY a.attempt_id, a.id
            """,
            (course, lecture),
        ).fetchall()
    return [dict(r) for r in rows]


def attempt_count(course: str, lecture: str, *, db_path: Path | None = None) -> int:
    with connect(db_path) as conn:
        row = conn.execute(
            "SELECT COUNT(*) AS n FROM attempts WHERE course = ? AND lecture = ? AND deleted_at IS NULL",
            (course, lecture),
        ).fetchone()
    return int(row["n"])


def retire_question(
    course: str,
    lecture: str,
    question: dict,
    *,
    reason: str,
    n_attempts: int | None,
    p_value: float | None,
    point_biserial: float | None,
    db_path: Path | None = None,
) -> None:
    """Archive a question removed from quiz.json by the rejection rule."""
    with connect(db_path) as conn:
        conn.execute(
            "INSERT INTO retired_questions"
            " (course, lecture, question_id, question_json, reason, n_attempts, p_value, point_biserial)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (
                course,
                lecture,
                question_id(course, lecture, question["question"]),
                json.dumps(question, ensure_ascii=False),
                reason,
                n_attempts,
                p_value,
                point_biserial,
            ),
        )


def load_retired(course: str, lecture: str, *, db_path: Path | None = None) -> list[dict]:
    with connect(db_path) as conn:
        rows = conn.execute(
            "SELECT * FROM retired_questions WHERE course = ? AND lecture = ? ORDER BY retired_at DESC",
            (course, lecture),
        ).fetchall()
    return [dict(r) for r in rows]
