import sqlite3

def get_connection():
    return sqlite3.connect("demo.db")


def create_table():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            email TEXT
        )
    """)

    conn.execute("""
        INSERT OR IGNORE INTO users
        VALUES (1, 'alice', 'alice@example.com')
    """)

    conn.commit()
    conn.close()
