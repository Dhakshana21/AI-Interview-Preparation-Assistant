import sqlite3


def create_tables():
    conn = sqlite3.connect("interview.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interviews(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        candidate_name TEXT,
        role TEXT,
        score REAL,
        feedback TEXT
    )
    """)

    conn.commit()
    conn.close()