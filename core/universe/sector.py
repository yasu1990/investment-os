import yfinance as yf

def get_sector(ticker: str) -> str:
    """
    Get sector / industry information for a ticker.
    Used only as contextual label.
    """
    try:
        info = yf.Ticker(ticker).info
        return (
            info.get("industry")
            or info.get("sector")
            or "Unknown"
        )
    except Exception:
        return "Unknown"
