from config.db import db, ma, app

# The data model for the 'tblvehicle' table is defined.
class Vehicle(db.Model):
    __tablename__ = "tblvehicle"

    # The table columns are defined, each with its id."
    id = db.Column(db.Integer, primary_key = True)
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    plate = db.Column(db.String(50))
    capacity = db.Column(db.Integer)
    state = db.Column(db.String(50))
    driver_id = db.Column(db.Integer, db.ForeignKey('tbldriver'))

    def __init__(self, make, model, plate, capacity, state, driver_id):
        self.make = make
        self.model = model
        self.plate = plate
        self.capacity = capacity
        self.state = state
        self.driver_id = driver_id

# The 'tblvehicle' table is created in the database within the app context."
with app.app_context():
    db.create_all()

# The serialization schema for Vehicle is defined to convert objects into JSON."
class VehicleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'make', 'model', 'plate', 'capacity', 'state', 'driver_id')