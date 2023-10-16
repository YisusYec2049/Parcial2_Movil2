from config.db import db, ma, app

# The data model for the 'tbluser' table is defined.
class User(db.Model):
    __tablename__ = "tbluser"

    # The table columns are defined, each with its id."
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    gender = db.Column(db.String(50))

    def __init__(self, name, email, password, phone, gender):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.gender = gender

# The 'tbluser' table is created in the database within the app context."
with app.app_context():
    db.create_all()

# The serialization schema for User is defined to convert objects into JSON."
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'phone', 'gender')