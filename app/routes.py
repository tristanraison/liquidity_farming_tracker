from flask import Blueprint, render_template, request
from app.services.calculator import calculate_token_proportions

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        try:
            # Get user inputs from form
            amount = float(request.form['amount'])
            price = float(request.form['price'])
            tick_min = float(request.form['tick_min'])
            tick_max = float(request.form['tick_max'])

            # Calculate proportions
            token0_ratio, token1_ratio = calculate_token_proportions(
                price, tick_min, tick_max)

            # Compute how much to allocate in USD
            token0_amount = amount * token0_ratio
            token1_amount = amount * token1_ratio

            # Package the result as a dict to pass to template
            result = {
                'token0_ratio': round(token0_ratio * 100, 2),
                'token1_ratio': round(token1_ratio * 100, 2),
                'token0_amount': round(token0_amount, 2),
                'token1_amount': round(token1_amount, 2)
            }

        except Exception as e:
            result = {'error': str(e)}

    return render_template('index.html', result=result)
