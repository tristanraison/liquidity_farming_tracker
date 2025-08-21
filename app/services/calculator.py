import math


def calculate_token_proportions(price_current, price_min, price_max):
    """
    Calculate the proportion of token0 and token1 required in a concentrated liquidity pool
    based on Uniswap V3 formulas.

    Args:
        price_current (float): Current price of token1 in terms of token0 (e.g., HYPE/BTC)
        price_min (float): Lower bound of the tick range
        price_max (float): Upper bound of the tick range

    Returns:
        tuple: (token0_ratio, token1_ratio) as floats summing to 1
    """

    sqrtP = math.sqrt(price_current)
    sqrtA = math.sqrt(price_min)
    sqrtB = math.sqrt(price_max)

    if price_current <= price_min:
        # Only token0 is required (price is below the active range)
        return (1.0, 0.0)
    elif price_current >= price_max:
        # Only token1 is required (price is above the active range)
        return (0.0, 1.0)
    else:
        # Both tokens are required (price is within range)
        # We calculate relative liquidity contributions
        amount0 = (sqrtB - sqrtP) / (sqrtP * sqrtB)
        amount1 = sqrtP - sqrtA

        total = amount0 + amount1
        token0_ratio = amount0 / total
        token1_ratio = amount1 / total

        return (token0_ratio, token1_ratio)
