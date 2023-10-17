from config.db import db, ma, app

# The data model for the 'tblroute' table is defined.
class Route(db.Model):
    __tablename__ = "tblroute"

    # The table columns are defined, each with its id."
    id = db.Column(db.Integer, primary_key = True)
    distance = db.Column(db.String(50))
    origin_city_id = db.Column(db.Integer, db.ForeignKey('tblcity.id'))
    destination_city_id = db.Column(db.Integer, db.ForeignKey('tblcity.id'))

    def __init__(self, distance, origin_city_id, destination_city_id):
        self.distance = distance
        self.origin_city_id = origin_city_id
        self.destination_city_id = destination_city_id

# The 'tblroute' table is created in the database within the app context."
with app.app_context():
    db.create_all()

# The serialization schema for Route is defined to convert objects into JSON."
class RouteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'distance', 'origin_city_id', 'destination_city_id')