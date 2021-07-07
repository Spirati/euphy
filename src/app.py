from flask import Flask
from dotenv import load_dotenv

def create_app():
    load_dotenv()

    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello, world!"

    return app