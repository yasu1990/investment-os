# core/universe/load_universe.py

import pandas as pd


def load_universe(path: str) -> list[str]:
    """
    Load ticker universe from CSV.

    CSV format:
    ticker
    1234.T
    5678.T
    """

    df = pd.read_csv(path)

    if "ticker" not in df.columns:
        raise ValueError("CSV must contain 'ticker' column")

    return df["ticker"].dropna().unique().tolist()
