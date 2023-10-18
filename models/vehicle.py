from config.db import db, ma, app

# The data model for the 'tblvehicle' table is defined.
class Vehicle(db.Model):
    __tablename__ = "Vehicle"

    idVehicle = db.Column(db.Integer, primary_key=True)
    Driver_idDriver = db.Column(db.Integer, db.ForeignKey('Driver.idDriver'), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    make = db.Column(db.String(45), nullable=False)
    model = db.Column(db.String(45), nullable=False)

    def __init__(self, Driver_idDriver, capacity, make, model):
        self.Driver_idDriver = Driver_idDriver
        self.capacity = capacity
        self.make = make
        self.model = model

# Creación de la tabla en la base de datos dentro del contexto de la aplicación
with app.app_context():
    db.create_all()

# Definición del esquema de serialización
class VehicleSchema(ma.Schema):
    class Meta:
        fields = ("idVehicle", "Driver_idDriver", "capacity", "make", "model")