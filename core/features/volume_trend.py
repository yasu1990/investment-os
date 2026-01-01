# core/features/volume_trend.py

import pandas as pd


def calculate_volume_trend(
    df: pd.DataFrame,
    lookback_days: int = 5
) -> bool:
    """
    Detect consecutive increase in trading volume.

    Returns True if volume has increased consecutively
    for lookback_days.
    """

    if len(df) < lookback_days + 1:
        return False

    volumes = df["volume"].tail(lookback_days + 1).values

    # Check strictly increasing sequence
    for i in range(1, len(volumes)):
        if volumes[i] <= volumes[i - 1]:
            return False

    return True
