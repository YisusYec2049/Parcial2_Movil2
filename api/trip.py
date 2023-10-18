from flask import Blueprint, request
from config.db import db
from models.trip import Trip, TripSchema

# Create a Blueprint to define routes related to trips.
trip_blueprint = Blueprint("trip", __name__)
trip_schema = TripSchema()
trips_schema = TripSchema(many=True)

# Ruta para crear un nuevo viaje
@trip_blueprint.route("/trip/create", methods=["POST"])
def add_trip():
    Vehicle_idVehicle = request.json["Vehicle_idVehicle"]
    Vehicle_Driver_idDriver = request.json["Vehicle_Driver_idDriver"]
    city_destination = request.json["city_destination"]
    city_origin = request.json["city_origin"]
    start_time = request.json["start_time"]
    departure_time = request.json["departure_time"]
    arrival_time = request.json["arrival_time"]
    price_per_seat = request.json["price_per_seat"]
    available_seats = request.json["available_seats"]
    route = request.json["route"]

    new_trip = Trip(Vehicle_idVehicle, Vehicle_Driver_idDriver, city_destination, city_origin, start_time, departure_time, arrival_time, price_per_seat, available_seats, route)

    db.session.add(new_trip)
    db.session.commit()

    return trip_schema.jsonify(new_trip), 201

# Ruta para obtener todos los viajes
@trip_blueprint.route("/trip/get", methods=["GET"])
def get_trips():
    trips = Trip.query.all()
    return trips_schema.jsonify(trips), 200

# Ruta para obtener un viaje por su ID
@trip_blueprint.route("/trip/get/<int:idTrip>", methods=["GET"])
def get_trip(idTrip):
    trip = Trip.query.get(idTrip)
    return trip_schema.jsonify(trip), 200

# Ruta para actualizar un viaje por su ID
@trip_blueprint.route("/trip/update/<int:idTrip>", methods=["PUT"])
def update_trip(idTrip):
    trip = Trip.query.get(idTrip)
    Vehicle_idVehicle = request.json["Vehicle_idVehicle"]
    Vehicle_Driver_idDriver = request.json["Vehicle_Driver_idDriver"]
    city_destination = request.json["city_destination"]
    city_origin = request.json["city_origin"]
    start_time = request.json["start_time"]
    departure_time = request.json["departure_time"]
    arrival_time = request.json["arrival_time"]
    price_per_seat = request.json["price_per_seat"]
    available_seats = request.json["available_seats"]
    route = request.json["route"]

    trip.Vehicle_idVehicle = Vehicle_idVehicle
    trip.Vehicle_Driver_idDriver = Vehicle_Driver_idDriver
    trip.city_destination = city_destination
    trip.city_origin = city_origin
    trip.start_time = start_time
    trip.departure_time = departure_time
    trip.arrival_time = arrival_time
    trip.price_per_seat = price_per_seat
    trip.available_seats = available_seats
    trip.route = route

    db.session.commit()
    return trip_schema.jsonify(trip), 200

# Ruta para eliminar un viaje por su ID
@trip_blueprint.route("/trip/delete/<int:idTrip>", methods=["DELETE"])
def delete_trip(idTrip):
    trip = Trip.query.get(idTrip)
    db.session.delete(trip)
    db.session.commit()

    return trip_schema.jsonify(trip), 200