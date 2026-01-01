# core/features/volume_anomaly.py

import pandas as pd


def calculate_volume_ratio(
    df: pd.DataFrame,
    volume_col: str = "volume",
    window: int = 20
) -> float:
    """
    Calculate volume anomaly ratio.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing volume data
    volume_col : str
        Column name for volume
    window : int
        Rolling window for average volume

    Returns
    -------
    float
        Volume ratio (current volume / average volume)
    """

    if df.empty:
        raise ValueError("DataFrame is empty")

    if len(df) < window + 1:
        return 1.0  # データ不足時は平常扱い

    current_volume = df[volume_col].iloc[-1]
    avg_volume = df[volume_col].iloc[-(window + 1):-1].mean()

    if avg_volume == 0:
        return 1.0

    ratio = current_volume / avg_volume

    return float(ratio)
