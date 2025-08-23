import requests


def get_price_usd(token_id):
    """
    Fetch the current USD price of a given token from CoinGecko.

    Args:
        token_id (str): The CoinGecko token ID (e.g., 'bitcoin', 'ethereum', 'tether')

    Returns:
        float: Price in USD
    """
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": token_id,
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if token_id in data and "usd" in data[token_id]:
        return float(data[token_id]["usd"])
    else:
        raise ValueError(f"Price for {token_id} not found on CoinGecko.")
