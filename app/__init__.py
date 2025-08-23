from flask import Flask

# Custom filter to format numbers with space as thousands separator


def format_number(value):
    try:
        return '{:,.2f}'.format(value).replace(',', ' ')
    except:
        return value  # fallback if non-numeric


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecretkey'

    from .routes import main
    app.register_blueprint(main)

    # Register the filter
    app.jinja_env.filters['format_number'] = format_number

    return app
