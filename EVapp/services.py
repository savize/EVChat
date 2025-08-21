from .Models.CS import ChargingStation
from .Models.Port import Port
from .Models.Structure import structure

from .extensions import db


# Add charging station
def addCS(name, location, lat, lng, status):
    station = ChargingStation(name, location, lat, lng, status)
    db.session.add(station)
    db.session.commit()
    print(f"Added charging station: {name}")

# Read charging station
def readCS():
    strct = structure.query.all()  
    return ChargingStation.query.filter_by(status=True).all()
