from flask import Blueprint, request, json, jsonify
from config.db import db, ma, app
from models.vehicle import Vehicle, VehicleSchema

# Create a Blueprint to define routes related to vehicles.
vehicle_blueprint = Blueprint("vehicle", __name__)
vehicle_schema = VehicleSchema()
vehicles_schema = VehicleSchema(many=True)

# Ruta para crear un nuevo vehículo
@vehicle_blueprint.route("/vehicles/create", methods=["POST"])
def add_vehicle():
    Driver_idDriver = request.json["Driver_idDriver"]
    capacity = request.json["capacity"]
    make = request.json["make"]
    model = request.json["model"]

    new_vehicle = Vehicle(Driver_idDriver, capacity, make, model)

    db.session.add(new_vehicle)
    db.session.commit()

    return vehicle_schema.jsonify(new_vehicle), 201

# Ruta para obtener todos los vehículos
@vehicle_blueprint.route("/vehicles", methods=["GET"])
def get_vehicles():
    vehicles = Vehicle.query.all()
    return vehicles_schema.jsonify(vehicles), 200

# Ruta para obtener un vehículo por su ID
@vehicle_blueprint.route("/vehicles/<int:idVehicle>", methods=["GET"])
def get_vehicle(idVehicle):
    vehicle = Vehicle.query.get(idVehicle)
    if vehicle:
        return vehicle_schema.jsonify(vehicle), 200
    else:
        return jsonify({"message": "Vehicle not found"}), 404

# Ruta para actualizar un vehículo por su ID
@vehicle_blueprint.route("/vehicles/update/<int:idVehicle>", methods=["PUT"])
def update_vehicle(idVehicle):
    vehicle = Vehicle.query.get(idVehicle)

    if vehicle:
        Driver_idDriver = request.json.get("Driver_idDriver")
        capacity = request.json.get("capacity")
        make = request.json.get("make")
        model = request.json.get("model")

        if Driver_idDriver is not None:
            vehicle.Driver_idDriver = Driver_idDriver
        if capacity is not None:
            vehicle.capacity = capacity
        if make is not None:
            vehicle.make = make
        if model is not None:
            vehicle.model = model

        db.session.commit()
        return vehicle_schema.jsonify(vehicle), 200
    else:
        return jsonify({"message": "Vehicle not found"}), 404

# Ruta para eliminar un vehículo por su ID
@vehicle_blueprint.route("/vehicles/delete/<int:idVehicle>", methods=["DELETE"])
def delete_vehicle(idVehicle):
    vehicle = Vehicle.query.get(idVehicle)

    if vehicle:
        db.session.delete(vehicle)
        db.session.commit()
        return vehicle_schema.jsonify(vehicle), 200
    else:
        return jsonify({"message": "Vehicle not found"}), 404