from config.db import db, ma, app

class User(db.Model):
    __tablename__ = "User"

    idUser = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    lastname = db.Column(db.String(45))
    number = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(200))
    password = db.Column(db.String(45), nullable=False)

    def __init__(self, name, lastname, number, email, password):
        self.name = name
        self.lastname = lastname
        self.number = number
        self.email = email
        self.password = password

# Creación de la tabla en la base de datos dentro del contexto de la aplicación
with app.app_context():
    db.create_all()

# Definición del esquema de serialización
class UserSchema(ma.Schema):
    class Meta:
        fields = ("idUser", "name", "lastname", "number", "email", "password")
