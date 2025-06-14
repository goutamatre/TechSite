from flask import Flask
from .db import mongo  # from db.py

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "----------------------"
    mongo.init_app(app)

    from .routes.main import main_bp
    app.register_blueprint(main_bp)

    return app

