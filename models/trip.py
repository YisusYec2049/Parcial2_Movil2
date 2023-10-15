from config.db import db, ma, app

class Trip(db.Model):
    __tablename__ = "tbltrip"

    id = db.Column(db.Integer, primary_key = True)
    stops = db.Column(db.String(50))
    driver = db.Column(db.Integer, db.ForeignKey('tbldriver.id'))
    traveler = db.Column(db.Integer, db.ForeignKey('tbltraveler.id'))
    vehicle = db.Column(db.Integer, db.ForeignKey('tblvehicle.id'))
    origin = db.Column(db.String(50), db.ForeignKey('tblcity.id'))
    destination = db.Column(db.String(50),  db.ForeignKey('tblcity.id'))

    def __init__(self, stops, driver, traveler, vehicle, origin, destiantion):
        self.stops = stops 
        self.driver = driver
        self.traveler = traveler
        self.vehicle = vehicle
        self.origin = origin
        self.destination = destiantion

with app.app_context():
    db.create_all()

class TripSchema(ma.Schema):
    class Meta:
        fields= ('id', 'stops', 'driver', 'traveler', 'vehicle', 'origin', 'destination')