from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from broadcast import create_app

app, db = create_app()

# Define the model for the table
class Port(db.Model):
    __tablename__ = 'port'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    power = db.Column('power (kW)', db.Integer,nullable=False)

    # Defining the constructor method
    def __init__(self, type, power):
        self.type = type
        self.power = power

# Function to add a new charging station
def addPort(type, power):
    port = Port(type, power)
    db.session.add(port)
    db.session.commit()
    print(f"Added port: {type}")


if __name__ == '__main__':
    with app.app_context():
        addPort("Type 1", 45 ) 
