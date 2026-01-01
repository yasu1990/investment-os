# core/universe/company_name.py

import yfinance as yf


def get_company_name(ticker: str) -> str:
    """
    Get company name (Japanese if available).
    Fallback to ticker if unavailable.
    """
    try:
        info = yf.Ticker(ticker).info

        # 日本株は longName に日本語が入ることが多い
        name = info.get("longName")

        if name:
            return name

        return ticker

    except Exception:
        return ticker
