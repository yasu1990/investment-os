import sqlite3
from datetime import datetime

def write_x_mention(
    db_path: str,
    ticker: str | None,
    company_name: str | None,
    source_account: str,
    post_id: str,
    text: str,
    sentiment_score: float,
):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO x_mentions (
            detected_at,
            ticker,
            company_name,
            source_account,
            post_id,
            text,
            sentiment_score
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            datetime.utcnow().isoformat(),
            ticker,
            company_name,
            source_account,
            post_id,
            text,
            sentiment_score,
        ),
    )

    conn.commit()
    conn.close()
