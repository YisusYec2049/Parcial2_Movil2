from config.db import db, ma, app

# The data model for the 'tblpassenger' table is defined.
class Passenger(db.Model):
    __tablename__ = 'tblpassenger'

    # The table columns are defined, each with its id."
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column()
    user_id = db.Column(db.Integer, db.ForeignKey('tbluser'))

    def __init__ (self, name, lastname, email, phone, user_id):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.user_id = user_id

# The 'tblpassenger' table is created in the database within the app context."
with app.app_context():
    db.create_all()

# The serialization schema for Passenger is defined to convert objects into JSON."
class PassengerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'lastname', 'email', 'phone', 'user_id')