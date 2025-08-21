from EVapp import db


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
