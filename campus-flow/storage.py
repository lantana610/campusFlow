import sqlite3
from pathlib import Path

# Store the database alongside this file.
DATABASE_PATH = Path(__file__).resolve().parent / "campusflow.db"


def get_connection():
    """Create a connection to the CampusFlow database."""
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    """Create the tickets table if it does not already exist."""
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                category TEXT NOT NULL,
                priority TEXT NOT NULL DEFAULT 'medium',
                status TEXT NOT NULL DEFAULT 'open',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


def create_ticket(title, description, category,
                  priority="medium"):
    """Create a ticket and return its ID."""
    if not title or not title.strip():
        raise ValueError("Ticket title cannot be empty.")

    if not description or not description.strip():
        raise ValueError("Ticket description cannot be empty.")

    if not category or not category.strip():
        raise ValueError("Ticket category cannot be empty.")

    allowed_priorities = {"low", "medium", "high"}

    if priority not in allowed_priorities:
        raise ValueError(
            "Priority must be low, medium, or high."
        )

    with get_connection() as connection:
        cursor = connection.execute(
            """
            INSERT INTO tickets
                (title, description, category, priority)
            VALUES (?, ?, ?, ?)
            """,
            (
                title.strip(),
                description.strip(),
                category.strip(),
                priority,
            ),
        )

        return cursor.lastrowid


def get_ticket(ticket_id):
    """Retrieve a ticket by its ID."""
    with get_connection() as connection:
        row = connection.execute(
            "SELECT * FROM tickets WHERE id = ?",
            (ticket_id,),
        ).fetchone()

        return dict(row) if row else None


def get_all_tickets():
    """Retrieve all tickets, newest first."""
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT * FROM tickets ORDER BY created_at DESC, id DESC"
        ).fetchall()

        return [dict(row) for row in rows]


def update_ticket_status(ticket_id, status):
    """Update a ticket's status."""
    allowed_statuses = {
        "open",
        "in_progress",
        "resolved",
        "closed",
    }

    if status not in allowed_statuses:
        raise ValueError(
            "Status must be open, in_progress, resolved, or closed."
        )

    with get_connection() as connection:
        cursor = connection.execute(
            "UPDATE tickets SET status = ? WHERE id = ?",
            (status, ticket_id),
        )

        return cursor.rowcount > 0


# Initialize the database when this module is imported.
initialize_database()