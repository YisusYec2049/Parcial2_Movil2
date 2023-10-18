from config.db import db, ma, app

# The data model for the 'tbldriver' table is defined.
class Driver(db.Model):
    __tablename__ = "Driver"

    idDriver = db.Column(db.Integer, primary_key=True)
    User_idUser = db.Column(db.Integer, db.ForeignKey('User.idUser'), nullable=False)
    license = db.Column(db.String(45), nullable=False)

    user = db.relationship('User', backref=db.backref('drivers'))

    def __init__(self, user, license):
        self.user = user
        self.license = license

# Creación de la tabla en la base de datos dentro del contexto de la aplicación
with app.app_context():
    db.create_all()

# Definición del esquema de serialización
class DriverSchema(ma.Schema):
    class Meta:
        fields = ("idDriver", "User_idUser", "license")