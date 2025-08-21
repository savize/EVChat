from flask import Flask 
from .extensions import db, socketio
from .routes import main 


def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "secret"

    # Configuring the Flask app to connect to the MySQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://myuser:#edge_dev#@localhost/EV'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(main)

    socketio.init_app(app)
    db.init_app(app)

    return app