from config.db import db, ma, app

# The data model for the 'tbltrip_passenger' table is defined.
class Trip_Passenger(db.Model):
    __tablename__ = "tbltrip_passenger"

    # The table columns are defined, each with its id."
    id = db.Column(db.Integer, primary_key = True)
    trip_id = db.Column(db.Integer, db.ForeignKey('tbltrip.id'))
    passenger_id = db.Column(db.Integer, db.ForeignKey('tblpassenger.id'))


    def __init__(self, trip_id, passenger_id):
        self.trip_id = trip_id
        self.passenger_id = passenger_id

# The 'tbltrip_passenger' table is created in the database within the app context."
with app.app_context():
    db.create_all()

# The serialization schema for Trip_Passenger is defined to convert objects into JSON."
class Trip_PassengerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'trip_id', 'passenger_id')