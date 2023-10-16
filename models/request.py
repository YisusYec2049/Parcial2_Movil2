from config.db import db, ma, app

# The data model for the 'tblrequest' table is defined.
class  Request(db.Model):
    __tablename__ = 'tblrequest'

    # The table columns are defined, each with its id."
    id = db.Column(db.Integer, primary_key = True)
    preferences = db.Column(db.String(50))
    state = db.Column(db.String(50))
    details = db.Column(db.String(50))
    origin_city_id = db.Column(db.String() ,db.ForeignKey('tblcity.id'))
    destination_city_id = db.Column(db.String(), db.ForeingKey('tblcity.id'))
    passenger_id = db.Column(db.Integer, db.ForeignKey('tblpassenger.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('tblvehicle.id'))
    driver_id = db.Column(db.Integer, db.ForeignKey('tbldriver.id'))

    def __init__(self, preferences, state, details, origin_city_id, destination_city_id, passenger_id, vehicle_id, driver_id):
        self.preferences = preferences
        self.state = state
        self.details = details
        self.origin_city_id = origin_city_id
        self.destination_city_id = destination_city_id
        self.passenger_id = passenger_id
        self.vehicle_id = vehicle_id
        self.driver_id = driver_id

# The 'tblrequest' table is created in the database within the app context."
with app.app_context():
    db.create_all()

# The serialization schema for Passenger is defined to convert objects into JSON."
class RequestSchema(ma.Schema):
    class Meta:
        fields = ('id', 'preferences', 'state', 'details', 'origin_city_id', 'destination_city_id', 'passenger_id', 'vehicle_id', 'drive_id')