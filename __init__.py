from flask import Flask
from app import Main as main


def Run_app():
    app = Flask(__name__)
    app.secret_key = 'akr'
    app.register_blueprint(main)
    return app



if __name__ == "__main__":
    Run_app().run(debug=True)