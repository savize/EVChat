from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from broadcast import create_app

app, db = create_app()

# Define the model for the table
class ChargingStation(db.Model):
    __tablename__ = 'chargingStation'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    lat = db.Column(db.Numeric(6, 4), nullable=False)
    lng = db.Column(db.Numeric(6, 4), nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)

    # Defining the constructor method
    def __init__(self, name, location, lat, lng, status):
        self.name = name
        self.location = location
        self.lat = lat
        self.lng = lng
        self.status = status

    # Defining the __repr__ method
    def __repr__(self):
        return f'<Charging Station {self.title}>'


# Function to add a new charging station
def addCS(name, location, lat, lng, status):
    station = ChargingStation(name, location, lat, lng, status)
    db.session.add(station)
    db.session.commit()
    print(f"Added charging station: {name}")


if __name__ == '__main__':
            with app.app_context():
                 addCS("Shell", "Wivenhoe", 44.04, 0.73, 1) 
