from flask import Flask, request, abort
from dotenv import load_dotenv

from context import DatabaseConnection

def create_app():
    load_dotenv()

    app = Flask(__name__)

    @app.route("/sentence")
    def get_sentence():
        with DatabaseConnection() as conn:
            conn.execute("select * from sentences limit 1;")
            result = conn.fetchone()
            if result is None:
                abort(404)
            return result[1]

    return app