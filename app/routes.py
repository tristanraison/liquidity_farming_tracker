from flask import Blueprint, render_template, request
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
            price_hype_btc = float(request.form['price'])
            # If BTC price not provided or invalid, fetch from CoinGecko
            try:
                price_btc_usd = float(request.form['price_btc_usd'])
            except:
                price_btc_usd = get_price_usd('bitcoin')

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
