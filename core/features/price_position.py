# core/features/price_position.py

import pandas as pd


def calculate_price_position(
    df: pd.DataFrame,
    price_col: str = "close"
) -> float:
    """
    Calculate normalized price position (0-10)
    based on historical min/max.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing historical prices
    price_col : str
        Column name for price (default: 'close')

    Returns
    -------
    float
        Price position between 0 and 10
    """

    if df.empty:
        raise ValueError("DataFrame is empty")

    min_price = df[price_col].min()
    max_price = df[price_col].max()
    current_price = df[price_col].iloc[-1]

    if max_price == min_price:
        return 5.0  # 異常ケース（値が動いていない）

    position = (current_price - min_price) / (max_price - min_price) * 10

    # 念のためクリップ
    position = max(0.0, min(10.0, position))

    return float(position)
