import math


def calculate_custom_allocation(amount_total_usd, price_hype_btc, price_btc_usd, allocation_btc_pct, allocation_hype_pct):
    """
    Allocate custom proportions in USD between BTC and HYPE, given their prices and user-defined split.

    Args:
        amount_total_usd (float): Total USD to invest
        price_hype_btc (float): Price of 1 HYPE in BTC
        price_btc_usd (float): Price of 1 BTC in USD
        allocation_btc_pct (float): Percentage of capital to allocate to BTC (0–100)
        allocation_hype_pct (float): Percentage of capital to allocate to HYPE (0–100)

    Returns:
        dict: Contains USD and quantity allocation for both BTC and HYPE
    """

    # Check total percentage = 100
    total_pct = allocation_btc_pct + allocation_hype_pct
    if round(total_pct, 5) != 100:
        raise ValueError("The sum of BTC and HYPE allocation must equal 100%.")

    # Convert to decimals
    btc_weight = allocation_btc_pct / 100
    hype_weight = allocation_hype_pct / 100

    # Token prices in USD
    price_hype_usd = price_hype_btc * price_btc_usd

    # Amounts in USD
    btc_usd = amount_total_usd * btc_weight
    hype_usd = amount_total_usd * hype_weight

    # Quantities
    btc_qty = btc_usd / price_btc_usd
    hype_qty = hype_usd / price_hype_usd

    return {
        "btc_usd": round(btc_usd, 2),
        "hype_usd": round(hype_usd, 2),
        "btc_qty": round(btc_qty, 8),
        "hype_qty": round(hype_qty, 4),
        "price_btc_usd": round(price_btc_usd, 2),
        "price_hype_usd": round(price_hype_usd, 6),
        "btc_pct": allocation_btc_pct,
        "hype_pct": allocation_hype_pct
    }
