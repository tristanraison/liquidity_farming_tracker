import time
from flask import session, Blueprint, render_template, request
from app.services.calculator import calculate_custom_allocation
from app.services.coingecko_api import get_price_usd

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        try:
            # Get user input amount
            amount = float(request.form['amount'])

            # --- BTC PRICE (manual input or fallback to API/cache) ---
            try:
                price_btc_usd = float(request.form['price_btc_usd'])
            except:
                if 'price_btc_usd' in session and time.time() - session.get('btc_timestamp', 0) < 300:
                    price_btc_usd = session['price_btc_usd']
                else:
                    price_btc_usd = get_price_usd('bitcoin')
                    session['price_btc_usd'] = price_btc_usd
                    session['btc_timestamp'] = time.time()

            # --- HYPE PRICE (manual input or fallback to API/cache) ---
            try:
                price_hype_usd = float(request.form['price_hype_usd'])
            except:
                if 'price_hype_usd' in session and time.time() - session.get('hype_timestamp', 0) < 300:
                    price_hype_usd = session['price_hype_usd']
                else:
                    # Nom du token selon CoinGecko
                    # ou 'hyperliquid-hype' si nécessaire
                    price_hype_usd = get_price_usd('hyperliquid')
                    session['price_hype_usd'] = price_hype_usd
                    session['hype_timestamp'] = time.time()

            # Compute HYPE/BTC price internally
            price_hype_btc = price_hype_usd / price_btc_usd

            # Allocation percentages
            allocation_btc_pct = float(request.form['allocation_btc'])
            allocation_hype_pct = float(request.form['allocation_hype'])

            # Perform allocation calculation
            result = calculate_custom_allocation(
                amount_total_usd=amount,
                price_hype_btc=price_hype_btc,
                price_btc_usd=price_btc_usd,
                allocation_btc_pct=allocation_btc_pct,
                allocation_hype_pct=allocation_hype_pct
            )

            # Add HYPE/USD price to result for display
            result["price_hype_usd"] = round(price_hype_usd, 6)

        except Exception as e:
            result = {'error': str(e)}

    return render_template('index.html', result=result)
