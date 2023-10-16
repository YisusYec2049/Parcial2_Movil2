from config.db import db, ma, app

# The data model for the 'tbltrip' table is defined.
class Trip(db.Model):
    __tablename__ = "tbltrip"

    # The table columns are defined, each with its id."
    id = db.Column(db.Integer, primary_key = True)
    start_time = db.Column(db.String(50))
    end_time = db.Column(db.String(50))
    route_id = db.Column(db.Integer, db.ForeignKey('tblroute.id'))
    city_id = db.Column(db.Integer, db.ForeignKey('tblcity.id'))
    passenger_id = db.Column(db.Integer, db.ForeignKey('tblpassenger.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('tblvehicle.id'))

    def __init__(self, start_time, end_time, route_id, city_id, passenger_id, vehicle_id):
        self.start_time = start_time
        self.end_time = end_time
        self.route_id = route_id
        self.city_id = city_id
        self.passenger_id = passenger_id
        self.vehicle_id = vehicle_id    

# The 'tbltrip' table is created in the database within the app context."
with app.app_context():
    db.create_all()

# The serialization schema for Trip is defined to convert objects into JSON."
class TripSchema(ma.Schema):
    class Meta:
        fields = ('id', 'start_time', 'end_time', 'route_id', 'city_id', 'passenger_id', 'vehicle_id')