
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "trustmesh.db"


def connect():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)


def initialize_database():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS audit_events (
                event_id TEXT PRIMARY KEY,
                timestamp TEXT NOT NULL,
                user_id TEXT NOT NULL,
                device_id TEXT NOT NULL,
                resource_id TEXT NOT NULL,
                decision TEXT NOT NULL,
                reason TEXT NOT NULL
            )
        """)


def save_event(event):
    with connect() as conn:
        conn.execute(
            """
            INSERT INTO audit_events
            (event_id, timestamp, user_id, device_id,
             resource_id, decision, reason)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                event["event_id"],
                event["timestamp"],
                event["user_id"],
                event["device_id"],
                event["resource_id"],
                event["decision"],
                event["reason"],
            ),
        )


def get_events():
    with connect() as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT * FROM audit_events ORDER BY timestamp ASC"
        ).fetchall()
        return [dict(row) for row in rows]


import json
from datetime import datetime, timezone


def initialize_incidents():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS incidents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                user_id TEXT NOT NULL,
                device_id TEXT NOT NULL,
                resource_id TEXT NOT NULL,
                decision TEXT NOT NULL,
                risk_score INTEGER NOT NULL,
                risk_level TEXT NOT NULL,
                reasons TEXT NOT NULL,
                agent_results TEXT NOT NULL
            )
        """)


def save_incident(request, security, agents):
    initialize_incidents()

    with connect() as conn:
        cursor = conn.execute("""
            INSERT INTO incidents (
                timestamp, user_id, device_id,
                resource_id, decision, risk_score,
                risk_level, reasons, agent_results
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            datetime.now(timezone.utc).isoformat(),
            request.user_id,
            request.device_id,
            request.resource_id,
            security["decision"],
            security["risk_score"],
            security["risk_level"],
            json.dumps(security["reasons"]),
            json.dumps(agents)
        ))

        return cursor.lastrowid


def get_incidents():
    initialize_incidents()

    with connect() as conn:
        conn.row_factory = sqlite3.Row

        rows = conn.execute("""
            SELECT * FROM incidents
            ORDER BY id DESC
            LIMIT 100
        """).fetchall()

    incidents = []

    for row in rows:
        incident = dict(row)
        incident["reasons"] = json.loads(
            incident["reasons"]
        )
        incident["agent_results"] = json.loads(
            incident["agent_results"]
        )
        incidents.append(incident)

    return incidents
