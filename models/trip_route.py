from config.db import db, ma, app

# The data model for the 'tbltrip_route' table is defined.
class Trip_Route(db.Model):
    __tablename__ = "tbltrip_route"

    # The table columns are defined, each with its id."
    id = db.Column(db.Integer, primary_key = True)
    trip_id = db.Column(db.Integer, db.ForeignKey('tbltrip.id'))
    route_id = db.Column(db.Integer, db.ForeignKey('tblroute.id'))


    def __init__(self, trip_id, route_id):
        self.trip_id = trip_id
        self.route_id = route_id

# The 'tbltrip_route' table is created in the database within the app context."
with app.app_context():
    db.create_all()

# The serialization schema for Trip_Route is defined to convert objects into JSON."
class Trip_RouteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'trip_id', 'route_id')