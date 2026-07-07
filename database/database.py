import sqlite3
import os

# Database path
DB_NAME = os.path.join(os.path.dirname(__file__), "vbcua.db")


def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS evaluations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        transcript TEXT,
        similarity REAL,
        score REAL,
        feedback TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_result(transcript, similarity, score, feedback):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO evaluations
    (transcript, similarity, score, feedback)
    VALUES (?, ?, ?, ?)
    """, (transcript, similarity, score, feedback))

    conn.commit()
    conn.close()


def get_all_results():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM evaluations
    ORDER BY created_at DESC
    """)

    results = cursor.fetchall()

    conn.close()

    return results