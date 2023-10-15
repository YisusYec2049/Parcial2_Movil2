from config.db import db, ma, app

class City(db.Model):
    __tablename__ = "tblcity"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    departament = db.Column(db.String(50))
    origin = db.Column(db.String(50))
    destination = db.Column(db.String(50))

    def __init__(self, name, departament, origin, destination):
        self.name = name
        self.departament = departament
        self.origin = origin
        self.destination = destination

with app.app_context():
    db.create_all()

class CitySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'departament', 'origin', 'destination')