from config.db import db, ma, app

# The data model for the 'tblcity' table is defined.
class City(db.Model):
    __tablename__ = "tblcity"

    # The table columns are defined, each with its id."
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    departament = db.Column(db.String(50))
    origin = db.Column(db.String(50))
    destiantion = db.Column(db.String(50))

    def __init__(self, name, departament, origin, destination):
        self.name = name
        self.departament = departament
        self.origin = origin
        self.destiantion = destination

# The 'tblcity' table is created in the database within the app context."
with app.app_context():
    db.create_all()

# The serialization schema for City is defined to convert objects into JSON."
class CitySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'departament', 'origin', 'destination')