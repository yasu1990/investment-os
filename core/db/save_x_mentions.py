import sqlite3
import datetime
import pandas as pd

def save_x_mentions(rows: list[dict], db_path: str):
    """
    rows: [
      {
        "ticker": "7203",
        "source_account": "example_account",
        "post_id": "123456",
        "text": "トヨタが面白そう",
        "sentiment_score": 0.8
      },
      ...
    ]
    """
    if not rows:
        return

    conn = sqlite3.connect(db_path)

    now = datetime.datetime.utcnow().isoformat()
    df = pd.DataFrame(rows)
    df["detected_at"] = now

    df.to_sql(
        "x_mentions",
        conn,
        if_exists="append",
        index=False
    )

    conn.close()
