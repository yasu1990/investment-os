# core/fetch/prices.py

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


def fetch_price_data(
    ticker: str,
    years: int = 3
) -> pd.DataFrame:
    """
    Fetch daily price and volume data for a given ticker.

    Parameters
    ----------
    ticker : str
        Stock ticker (e.g. '7203.T')
    years : int
        Lookback period in years

    Returns
    -------
    pd.DataFrame
        DataFrame with columns:
        ['date', 'open', 'high', 'low', 'close', 'volume']
    """

    end_date = datetime.today()
    start_date = end_date - timedelta(days=365 * years)

    df = yf.download(
        ticker,
        start=start_date.strftime("%Y-%m-%d"),
        end=end_date.strftime("%Y-%m-%d"),
        progress=False
    )

    if df.empty:
        raise ValueError(f"No price data fetched for ticker: {ticker}")

    df = df.reset_index()

    df = df.rename(columns={
        "Date": "date",
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Volume": "volume"
    })

    df = df[[
        "date",
        "open",
        "high",
        "low",
        "close",
        "volume"
    ]]

    return df
