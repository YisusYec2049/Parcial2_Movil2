from config.db import db, ma, app

# The data model for the 'tblrequest_passenger' table is defined.
class Request_Passenger(db.Model):
    __tablename__ = "tblrequest_passenger"

    # The table columns are defined, each with its id."
    id = db.Column(db.Integer, primary_key = True)
    request_id = db.Column(db.Integer, db.ForeignKey('tblrequest.id'))
    passenger_id = db.Column(db.Integer, db.ForeignKey('tblpassenger.id'))


    def __init__(self, request_id, passenger_id):
        self.request_id = request_id
        self.passenger_id = passenger_id

# The 'tblrequest_passenger' table is created in the database within the app context."
with app.app_context():
    db.create_all()

# The serialization schema for Request_Passenger is defined to convert objects into JSON."
class Request_PassengerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'request_id', 'passenger_id')