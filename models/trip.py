from config.db import db, ma, app

# The data model for the 'tbltrip' table is defined.
class Trip(db.Model):
    __tablename__ = "Trip"

    idTrip = db.Column(db.Integer, primary_key=True)
    Vehicle_idVehicle = db.Column(db.Integer, db.ForeignKey('Vehicle.idVehicle'), nullable=False)
    Vehicle_Driver_idDriver = db.Column(db.Integer, db.ForeignKey('Vehicle.Driver_idDriver'), nullable=False)
    city_destination = db.Column(db.Integer, db.ForeignKey('City.idCity'), nullable=False)
    city_origin = db.Column(db.Integer, db.ForeignKey('City.idCity'), nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    departure_time = db.Column(db.Time, nullable=False)
    arrival_time = db.Column(db.Time, nullable=False)
    price_per_seat = db.Column(db.Float, nullable=False)
    available_seats = db.Column(db.Integer, nullable=False)
    route = db.Column(db.String(100), nullable=False)
    total_value = db.Column(db.Numeric(precision=10, scale=2), server_default=db.text("(available_seats * price_per_seat)"), nullable=False)

    def __init__(self, Vehicle_idVehicle, Vehicle_Driver_idDriver, city_destination, city_origin,
                 start_time, departure_time, arrival_time, price_per_seat, available_seats, route):
        self.Vehicle_idVehicle = Vehicle_idVehicle
        self.Vehicle_Driver_idDriver = Vehicle_Driver_idDriver
        self.city_destination = city_destination
        self.city_origin = city_origin
        self.start_time = start_time
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price_per_seat = price_per_seat
        self.available_seats = available_seats
        self.route = route

# Creación de la tabla en la base de datos dentro del contexto de la aplicación
with app.app_context():
    db.create_all()

# Definición del esquema de serialización
class TripSchema(ma.Schema):
    class Meta:
        fields = ("idTrip", "Vehicle_idVehicle", "Vehicle_Driver_idDriver", "city_destination",
                  "city_origin", "start_time", "departure_time", "arrival_time", "price_per_seat",
                  "available_seats", "route", "total_value")