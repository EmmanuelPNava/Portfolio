from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        EMAIL_PASSWORD=os.environ.get('EMAIL_PASSWORD')
    )

    from . import portfolio 

    app.register_blueprint(portfolio.bp)

    return app

