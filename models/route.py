from config.db import db, ma, app

class Route(db.Model):
    __tablename__ = "tblroute"

    id = db.Column(db.Integer, primary_key = True)
    origin = db.Column(db.String(50), db.ForeignKey('tbllocate.id'))
    destination = db.Column(db.String(50),  db.ForeignKey('tbllocate.id'))
    distance = db.Column(db.String(50))
   

    def __init__(self, origin, destination, distance):
        self.origin = origin
        self.destination = destination
        self.distance = distance

with app.app_context():
    db.create_all()

class RouteSchema(ma.Schema):
    class Meta:
        fields = ("id", "origin", "destination", "distance")