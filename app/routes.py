from flask import Blueprint, render_template, request
from app.services.calculator import calculate_symmetric_allocation

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        try:
            # Get user inputs from form
            amount = float(request.form['amount'])
            price_hype_btc = float(request.form['price'])
            price_btc_usd = float(request.form['price_btc_usd'])

            # Compute symmetric allocation
            result = calculate_symmetric_allocation(
                amount_total_usd=amount,
                price_hype_btc=price_hype_btc,
                price_btc_usd=price_btc_usd
            )

        except Exception as e:
            result = {'error': str(e)}

    return render_template('index.html', result=result)
