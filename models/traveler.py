from config.db import db, ma, app

class Traveler(db.Model):
    __tablename__ = "tbltraveler"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(50))
    city = db.Column(db.String(50), db.ForeignKey('tbllocate.id'))

    def __init__(self, name, lastname, age, gender, city):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.city = city

with app.app_context():
    db.create_all()

class TravelerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'lastname', 'gender', 'city')