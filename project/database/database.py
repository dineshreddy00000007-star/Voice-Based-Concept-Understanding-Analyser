import sqlite3

DB_NAME = "database/vbcua.db"

def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic TEXT,
        transcript TEXT,
        similarity REAL,
        final_score REAL,
        feedback TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_result(topic, transcript, similarity, final_score, feedback):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO results(
        topic,
        transcript,
        similarity,
        final_score,
        feedback
    )
    VALUES(?,?,?,?,?)
    """, (
        topic,
        transcript,
        similarity,
        final_score,
        feedback
    ))

    conn.commit()
    conn.close()