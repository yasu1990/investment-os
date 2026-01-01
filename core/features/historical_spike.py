# core/features/historical_spike.py

import pandas as pd


def has_historical_spike(
    df: pd.DataFrame,
    price_col: str = "close",
    lookback_days: int = 120,
    spike_ratio: float = 2.0
) -> bool:
    """
    Check if the stock had a historical spike within a given window.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing historical prices
    price_col : str
        Column name for price
    lookback_days : int
        Lookback window in days
    spike_ratio : float
        Spike definition (e.g. 2.0 = 2x)

    Returns
    -------
    bool
        True if a spike occurred, False otherwise
    """

    if df.empty:
        return False

    if len(df) < lookback_days:
        return False

    prices = df[price_col].iloc[-lookback_days:]

    min_price = prices.min()
    max_price = prices.max()

    if min_price <= 0:
        return False

    return (max_price / min_price) >= spike_ratio
