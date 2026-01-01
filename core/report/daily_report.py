# core/report/daily_report.py

import pandas as pd

from core.fetch.prices import fetch_price_data
from core.features.price_position import calculate_price_position
from core.features.volume_anomaly import calculate_volume_ratio
from core.features.historical_spike import has_historical_spike
from core.scoring.ten_bagger import calculate_ten_bagger_score, load_weights


def generate_daily_report(
    tickers: list[str],
    top_n: int = 20
) -> pd.DataFrame:
    """
    Generate daily ten-bagger screening report.

    Parameters
    ----------
    tickers : list[str]
        List of stock tickers
    top_n : int
        Number of top candidates to return

    Returns
    -------
    pd.DataFrame
        Sorted report DataFrame
    """

    weights = load_weights()
    results = []

    for ticker in tickers:
        try:
            df = fetch_price_data(ticker)

            price_pos = calculate_price_position(df)
            volume_ratio = calculate_volume_ratio(df)
            spike = has_historical_spike(df)

            score = calculate_ten_bagger_score(
                price_position=price_pos,
                volume_ratio=volume_ratio,
                historical_spike=spike,
                weights=weights
            )

            results.append({
                "ticker": ticker,
                "price_position": round(price_pos, 2),
                "volume_ratio": round(volume_ratio, 2),
                "historical_spike": spike,
                "score": round(score, 2)
            })

        except Exception as e:
            # 1銘柄落ちても全体は止めない
            print(f"[SKIP] {ticker}: {e}")

    report_df = pd.DataFrame(results)

    if report_df.empty:
        return report_df

    report_df = report_df.sort_values(
        by="score",
        ascending=False
    ).reset_index(drop=True)

    return report_df.head(top_n)
