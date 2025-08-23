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
            # Get user inputs from form
            amount = float(request.form['amount'])

            # Get BTC price (from form or cache/API)
            try:
                price_btc_usd = float(request.form['price_btc_usd'])
            except:
                # Use cache if available
                if 'price_btc_usd' in session and time.time() - session.get('btc_timestamp', 0) < 300:
                    price_btc_usd = session['price_btc_usd']
                else:
                    price_btc_usd = get_price_usd('bitcoin')
                    session['price_btc_usd'] = price_btc_usd
                    session['btc_timestamp'] = time.time()

            # Get HYPE/BTC price (from form or CoinGecko)
            try:
                price_hype_btc = float(request.form['price'])
            except:
                # Fallback to CoinGecko if price not provided
                price_hype_usd = get_price_usd('hyperliquid-hype')
                price_hype_btc = price_hype_usd / price_btc_usd

            # Get allocation splits
            allocation_btc_pct = float(request.form['allocation_btc'])
            allocation_hype_pct = float(request.form['allocation_hype'])

            # Compute custom allocation
            result = calculate_custom_allocation(
                amount_total_usd=amount,
                price_hype_btc=price_hype_btc,
                price_btc_usd=price_btc_usd,
                allocation_btc_pct=allocation_btc_pct,
                allocation_hype_pct=allocation_hype_pct
            )

        except Exception as e:
            result = {'error': str(e)}

    return render_template('index.html', result=result)
