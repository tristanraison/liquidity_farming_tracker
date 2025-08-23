import math


def calculate_symmetric_allocation(amount_total_usd, price_hype_btc, price_btc_usd):
    """
    Allocate 50/50 in USD between BTC and HYPE, given their cross rate and BTC price in USD.

    Args:
        amount_total_usd (float): Total amount in USD to invest
        price_hype_btc (float): Price of 1 HYPE in BTC
        price_btc_usd (float): Price of 1 BTC in USD

    Returns:
        dict: Contains USD and quantity allocation for both BTC and HYPE
    """

    amount_per_token_usd = amount_total_usd / 2

    # Token prices in USD
    price_hype_usd = price_hype_btc * price_btc_usd

    # Quantities to buy
    btc_quantity = amount_per_token_usd / price_btc_usd
    hype_quantity = amount_per_token_usd / price_hype_usd

    return {
        "btc_usd": round(amount_per_token_usd, 2),
        "hype_usd": round(amount_per_token_usd, 2),
        "btc_qty": round(btc_quantity, 8),
        "hype_qty": round(hype_quantity, 4),
        "price_btc_usd": round(price_btc_usd, 2),
        "price_hype_usd": round(price_hype_usd, 6)
    }
