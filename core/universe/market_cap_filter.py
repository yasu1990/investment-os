# core/universe/market_cap_filter.py

import yfinance as yf


def get_market_cap_yen(ticker: str) -> float | None:
    """
    Get market capitalization in JPY.
    Returns None if data is unavailable.
    """
    try:
        t = yf.Ticker(ticker)
        info = t.info

        shares = info.get("sharesOutstanding")
        price = info.get("currentPrice")

        if shares is None or price is None:
            return None

        market_cap = shares * price
        return float(market_cap)

    except Exception:
        return None


def filter_small_caps(
    tickers: list[str],
    max_market_cap_yen: float = 150_000_000_000
) -> list[str]:
    """
    Filter tickers by market capitalization.
    """

    small_caps = []

    for ticker in tickers:
        mc = get_market_cap_yen(ticker)

        if mc is None:
            continue

        if mc <= max_market_cap_yen:
            small_caps.append(ticker)

    return small_caps
