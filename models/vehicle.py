from config.db import db, ma, app

class Vehicle(db.Model):
    __tablename__ = "tblvehicle"

    id = db.Column(db.Integer, primary_key = True)
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    plate = db.Column(db.String(50))
    capacity = db.Column(db.Integer)
    available = db.Column(db.String(50))
    driver = db.Column(db.String(50), db.ForeignKey('tbldriver.id'))

    def __init__(self, make, model, plate, capacity, available, driver):
        self. make = make
        self.model = model
        self.plate = plate
        self.capacity = capacity
        self.available = available
        self.driver = driver

with app.app_context():
    db.create_all()   

class VehicleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'make', 'model', 'plate', 'capacity', 'available', 'diver')
        