from config.db import db, ma, app

# The data model for the 'tblrequest' table is defined.
class RequestTrip(db.Model):
    __tablename__ = "Request_Trip"

    idRequest_Trip = db.Column(db.Integer, primary_key=True)
    Passanger_idPassanger = db.Column(db.Integer, db.ForeignKey('Passanger.idPassanger'), nullable=False)
    method_idPayment = db.Column(db.Integer, db.ForeignKey('Payment.idPayment'), nullable=False)
    Trip_idTrip = db.Column(db.Integer)
    Trip_Vehicle_idVehicle = db.Column(db.Integer, unique=True)
    Trip_Vehicle_Driver_idDriver = db.Column(db.Integer, unique=True)
    city_destination = db.Column(db.Integer, db.ForeignKey('City.idCity'), nullable=False)
    city_origin = db.Column(db.Integer, db.ForeignKey('City.idCity'), nullable=False)
    idRequest_Status = db.Column(db.Integer, db.ForeignKey('Request_Status.idRequest_Status'), nullable=False)
    origin_address = db.Column(db.String(45), nullable=False)
    destination_address = db.Column(db.String(45), nullable=False)
    time_arrival = db.Column(db.Time, nullable=False)
    preferences = db.Column(db.String(100))

    def __init__(self, Passanger_idPassanger, method_idPayment, Trip_idTrip,
                 Trip_Vehicle_idVehicle, Trip_Vehicle_Driver_idDriver, city_destination,
                 city_origin, idRequest_Status, origin_address, destination_address,
                 time_arrival, preferences):
        self.Passanger_idPassanger = Passanger_idPassanger
        self.method_idPayment = method_idPayment
        self.Trip_idTrip = Trip_idTrip
        self.Trip_Vehicle_idVehicle = Trip_Vehicle_idVehicle
        self.Trip_Vehicle_Driver_idDriver = Trip_Vehicle_Driver_idDriver
        self.city_destination = city_destination
        self.city_origin = city_origin
        self.idRequest_Status = idRequest_Status
        self.origin_address = origin_address
        self.destination_address = destination_address
        self.time_arrival = time_arrival
        self.preferences = preferences

# Creación de la tabla en la base de datos dentro del contexto de la aplicación
with app.app_context():
    db.create_all()

# Definición del esquema de serialización
class RequestTripSchema(ma.Schema):
    class Meta:
        fields = ("idRequest_Trip", "Passanger_idPassanger", "method_idPayment", "Trip_idTrip",
                  "Trip_Vehicle_idVehicle", "Trip_Vehicle_Driver_idDriver", "city_destination", "city_origin",
                  "idRequest_Status", "origin_address", "destination_address", "time_arrival", "preferences")