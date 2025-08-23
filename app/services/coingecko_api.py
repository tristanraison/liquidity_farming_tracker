
import requests


def get_price_usd(token_id):
    """
    Fetch the current USD price of a given token from CoinGecko.
    Falls back gracefully if price is not available.

    Args:
        token_id (str): The CoinGecko token ID (e.g., 'bitcoin', 'hyperliquid-hype')

    Returns:
        float: Price in USD

    Raises:
        ValueError: If the price is not available in the response
    """
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": token_id,
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise ValueError(
            f"CoinGecko API error (status {response.status_code})")

    data = response.json()
    if token_id in data and "usd" in data[token_id]:
        return float(data[token_id]["usd"])

    # Optional debug: print(data)
    raise ValueError(f"Price not available in USD for token: {token_id}")
