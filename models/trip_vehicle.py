from config.db import db, ma, app

# The data model for the 'tbltrip_vehicle' table is defined.
class Trip_Vehicle(db.Model):
    __tablename__ = "tbltrip_vehicle"

    # The table columns are defined, each with its id."
    id = db.Column(db.Integer, primary_key = True)
    trip_id = db.Column(db.Integer, db.ForeignKey('tbltrip.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('tblvehicle.id'))


    def __init__(self, trip_id, vehicle_id):
        self.trip_id = trip_id
        self.vehicle_id = vehicle_id

# The 'tbltrip_vehicle' table is created in the database within the app context."
with app.app_context():
    db.create_all()

# The serialization schema for Trip_Vehicle is defined to convert objects into JSON."
class Trip_VehicleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'trip_id', 'vehicle_id')