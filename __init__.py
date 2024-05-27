from flask import Flask
from main import Main as Main_blueprint
 

def Run_app():
    app = Flask(__name__)
    app.secret_key = 'akr'
    app.register_blueprint(Main_blueprint)
    return app



if __name__ == "__main__":
    Run_app().run(debug=True)