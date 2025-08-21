from EVapp import db
from Models.Port import Port
from Models.CS import ChargingStation


class structure(db.Model):
    __tablename__ = 'structure'

    id = db.Column(db.Integer, primary_key=True)
    CS_id = db.Column(db.Integer, db.ForeignKey(ChargingStation.id), nullable=False)
    port_id = db.Column(db.Integer, db.ForeignKey(Port.id), nullable=False)
    available = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)

    # # Define relationships (optional but useful)
    # charging_station = db.relationship('chargingStation', backref=db.backref('port_availabilities', lazy=True))
    # port = db.relationship('Port', backref=db.backref('port_availabilities', lazy=True))

    def __init__(self, CS_id, port_id, available, total):
        self.CS_id = CS_id
        self.port_id = port_id
        self.available = available
        self.total = total

# Function to add a new PortAvailability record
def addStructure(CS_id, port_id, available, total):
    port_av = structure(CS_id, port_id, available, total)
    db.session.add(port_av)
    db.session.commit()
    print(f"Added PortAvailability: CS={CS_id}, Port={port_id}")

