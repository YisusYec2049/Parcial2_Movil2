from config.db import db, ma, app

# The data model for the 'tblrequest_vehicle' table is defined.
class Request_Vehicle(db.Model):
    __tablename__ = "tblrequest_vehicle"

    # The table columns are defined, each with its id."
    id = db.Column(db.Integer, primary_key = True)
    request_id = db.Column(db.Integer, db.ForeignKey('tblrequest.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('tblvehicle.id'))


    def __init__(self, request_id, vehicle_id):
        self.request_id = request_id
        self.vehicle_id = vehicle_id

# The 'tblrequest_vehicle' table is created in the database within the app context."
with app.app_context():
    db.create_all()

# The serialization schema for Request_Vehicle is defined to convert objects into JSON."
class Request_VehicleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'request_id', 'vehicle_id')