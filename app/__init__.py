from flask import Flask
from app.db import mongo  # from db.py

# with open("/media/goutam/projects/TechSite (1)/app/DB/my_credentials", "r") as file:
#     username = file.readline().strip()
#     password=file.readline().strip()

    # print(f"Username: {username}, Password: {password}")

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb+srv://Goutam:19221879@cluster0.byjpf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    mongo.init_app(app)

    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    return app

