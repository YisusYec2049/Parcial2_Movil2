from config.db import db, ma, app

# The data model for the 'Passenger' table is defined.
class Passanger(db.Model):
    __tablename__ = "Passanger"

    idPassanger = db.Column(db.Integer, primary_key=True)
    User_idUser = db.Column(db.Integer, db.ForeignKey('User.idUser'), nullable=False)
    preferred_idPayment = db.Column(db.Integer, db.ForeignKey('Payment.idPayment'), nullable=False)

    user = db.relationship('User', backref='passangers')
    payment_method = db.relationship('Payment', backref='passangers')

    # Constructor
    def __init__(self, User_idUser, preferred_idPayment):
        self.User_idUser = User_idUser
        self.preferred_idPayment = preferred_idPayment

# Creación de la tabla en la base de datos dentro del contexto de la aplicación
with app.app_context():
    db.create_all()

# Definición del esquema de serialización
class PassangerSchema(ma.Schema):
    class Meta:
        fields = ("idPassanger", "User_idUser", "preferred_idPayment")