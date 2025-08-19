from flask import Flask 

from .events import socketio
from .routes import main 
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "secret"

    # Configuring the Flask app to connect to the MySQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://myuser:#edge_dev#@localhost/EV'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(main)

    socketio.init_app(app)

    db = SQLAlchemy(app)

    return app, db