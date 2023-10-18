from flask import Blueprint, request
from config.db import db
from models.passenger import Passenger, PassengerSchema

passenger_blueprint = Blueprint("passenger", __name__)
passenger_schema = PassengerSchema()
passengers_schema = PassengerSchema(many=True)

# Ruta para crear un nuevo pasajero
@passenger_blueprint.route("/passenger/create", methods=["POST"])
def add_passenger():
    User_idUser = request.json["User_idUser"]
    preferred_idPayment = request.json["preferred_idPayment"]
    new_passenger = Passenger(User_idUser, preferred_idPayment)

    db.session.add(new_passenger)
    db.session.commit()

    return passenger_schema.jsonify(new_passenger), 201

# Ruta para obtener todos los pasajeros
@passenger_blueprint.route("/passenger/get", methods=["GET"])
def get_passengers():
    passengers = Passenger.query.all()
    return passengers_schema.jsonify(passengers), 200

# Ruta para obtener un pasajero por su ID
@passenger_blueprint.route("/passenger/get/<int:idPassenger>", methods=["GET"])
def get_passenger(idPassenger):
    passenger = Passenger.query.get(idPassenger)
    return passenger_schema.jsonify(passenger), 200

# Ruta para actualizar un pasajero por su ID
@passenger_blueprint.route("/passenger/update/<int:idPassenger>", methods=["PUT"])
def update_passenger(idPassenger):
    passenger = Passenger.query.get(idPassenger)
    User_idUser = request.json["User_idUser"]
    preferred_idPayment = request.json["preferred_idPayment"]

    passenger.User_idUser = User_idUser
    passenger.preferred_idPayment = preferred_idPayment

    db.session.commit()
    return passenger_schema.jsonify(passenger), 200

# Ruta para eliminar un pasajero por su ID
@passenger_blueprint.route("/passenger/delete/<int:idPassenger>", methods=["DELETE"])
def delete_passenger(idPassenger):
    passenger = Passenger.query.get(idPassenger)
    db.session.delete(passenger)
    db.session.commit()

    return passenger_schema.jsonify(passenger), 200
