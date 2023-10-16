from config.db import db, ma, app

# The data model for the 'tbldriver' table is defined.
class Driver(db.Model):
    __tablename__ = "tbldriver"

    # The table columns are defined, each with its id."
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    license = db.Column(db.String(50))

    def __init__(self, name, lastname, license):
        self.name = name
        self.lastname = lastname
        self.license = license

# The 'tbldriver' table is created in the database within the app context."
with app.app_context():
    db.create_all()

# The serialization schema for Driver is defined to convert objects into JSON."
class DriverSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'lastname', 'license')