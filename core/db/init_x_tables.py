import sqlite3

def init_x_tables(db_path: str):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS x_mentions (
        detected_at TEXT,
        ticker TEXT,
        source_account TEXT,
        post_id TEXT,
        text TEXT,
        sentiment_score REAL
    )
    """)

    conn.commit()
    conn.close()
