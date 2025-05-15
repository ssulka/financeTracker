import sqlite3
from pathlib import Path

# Define the path to the database file
DB_PATH = Path(__file__).parent / "finance_tracker.db"

def initialize_database():
    """Initialize the database and create tables if they don't exist."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        # Create a table for transactions
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        )
        """)
        conn.commit()

def add_transaction(date, category, amount, description=None):
    """Add a new transaction to the database."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO transactions (date, category, amount, description)
        VALUES (?, ?, ?, ?)
        """, (date, category, amount, description))
        conn.commit()

def get_transactions():
    """Retrieve all transactions from the database."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transactions")
        return cursor.fetchall()

# Initialize the database when the script is run
if __name__ == "__main__":
    initialize_database()