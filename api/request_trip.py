from flask import Blueprint, request, jsonify
from config.db import db
from models.request_trip import RequestTrip, RequestTripSchema

request_trip_blueprint = Blueprint("request_trip", __name__)
request_trip_schema = RequestTripSchema()
request_trips_schema = RequestTripSchema(many=True)

# Ruta para crear una nueva solicitud de viaje
@request_trip_blueprint.route("/request_trip/create", methods=["POST"])
def add_request_trip():
    Passanger_idPassanger = request.json["Passanger_idPassanger"]
    method_idPayment = request.json["method_idPayment"]
    Trip_idTrip = request.json["Trip_idTrip"]
    Trip_Vehicle_idVehicle = request.json["Trip_Vehicle_idVehicle"]
    Trip_Vehicle_Driver_idDriver = request.json["Trip_Vehicle_Driver_idDriver"]
    city_destination = request.json["city_destination"]
    city_origin = request.json["city_origin"]
    idRequest_Status = request.json["idRequest_Status"]
    origin_address = request.json["origin_address"]
    destination_address = request.json["destination_address"]
    time_arrival = request.json["time_arrival"]
    preferences = request.json.get("preferences")

    new_request_trip = RequestTrip(Passanger_idPassanger, method_idPayment, Trip_idTrip, Trip_Vehicle_idVehicle, Trip_Vehicle_Driver_idDriver, city_destination, city_origin, idRequest_Status, origin_address, destination_address, time_arrival, preferences)

    db.session.add(new_request_trip)
    db.session.commit()

    return request_trip_schema.jsonify(new_request_trip), 201

# Ruta para obtener todas las solicitudes de viaje
@request_trip_blueprint.route("/request_trip/get", methods=["GET"])
def get_request_trips():
    request_trips = RequestTrip.query.all()
    return request_trips_schema.jsonify(request_trips), 200

# Ruta para obtener una solicitud de viaje por su ID
@request_trip_blueprint.route("/request_trip/get/<int:idRequest_Trip>", methods=["GET"])
def get_request_trip(idRequest_Trip):
    request_trip = RequestTrip.query.get(idRequest_Trip)
    return request_trip_schema.jsonify(request_trip), 200

# Ruta para actualizar una solicitud de viaje por su ID
@request_trip_blueprint.route("/request_trip/update/<int:idRequest_Trip>", methods=["PUT"])
def update_request_trip(idRequest_Trip):
    request_trip = RequestTrip.query.get(idRequest_Trip)
    Passanger_idPassanger = request.json["Passanger_idPassanger"]
    method_idPayment = request.json["method_idPayment"]
    Trip_idTrip = request.json["Trip_idTrip"]
    Trip_Vehicle_idVehicle = request.json["Trip_Vehicle_idVehicle"]
    Trip_Vehicle_Driver_idDriver = request.json["Trip_Vehicle_Driver_idDriver"]
    city_destination = request.json["city_destination"]
    city_origin = request.json["city_origin"]
    idRequest_Status = request.json["idRequest_Status"]
    origin_address = request.json["origin_address"]
    destination_address = request.json["destination_address"]
    time_arrival = request.json["time_arrival"]
    preferences = request.json.get("preferences")

    request_trip.Passanger_idPassanger = Passanger_idPassanger
    request_trip.method_idPayment = method_idPayment
    request_trip.Trip_idTrip = Trip_idTrip
    request_trip.Trip_Vehicle_idVehicle = Trip_Vehicle_idVehicle
    request_trip.Trip_Vehicle_Driver_idDriver = Trip_Vehicle_Driver_idDriver
    request_trip.city_destination = city_destination
    request_trip.city_origin = city_origin
    request_trip.idRequest_Status = idRequest_Status
    request_trip.origin_address = origin_address
    request_trip.destination_address = destination_address
    request_trip.time_arrival = time_arrival
    request_trip.preferences = preferences

    db.session.commit()
    return request_trip_schema.jsonify(request_trip), 200

# Ruta para eliminar una solicitud de viaje por su ID
@request_trip_blueprint.route("/request_trip/delete/<int:idRequest_Trip>", methods=["DELETE"])
def delete_request_trip(idRequest_Trip):
    request_trip = RequestTrip.query.get(idRequest_Trip)
    db.session.delete(request_trip)
    db.session.commit()

    return request_trip_schema.jsonify(request_trip), 200
