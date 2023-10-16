from flask import Blueprint, request, json, jsonify
from config.db import db, ma, app
from models.vehicle import Vehicle, VehicleSchema

# Create a Blueprint to define routes related to vehicles.
route_vehicles = Blueprint('vehicle', __name__)

# Define a serialization schema for vehicles.
vehicle_schema = VehicleSchema
vehicles_schema = VehicleSchema(many=True)

# Create a route to get all vehicles.
@route_vehicles.route('/vehicles', methods = ['GET'])
def vehicle():
    resultall = Vehicle.query.all()
    result_vehicle = vehicles_schema.dump(resultall)
    return jsonify(result_vehicle)

# Create a route to save a new vehicle.
@route_vehicles.route('/savevehicle', methods = ['POST'])
def save():
    make = request.json['make']
    model = request.json['model']
    plate = request.json['plate']
    capacity = request.json['capacity']
    state = request.json['state']
    driver_id = request.json['driver_id']
    new_vehicle = Vehicle(make , model, plate, capacity, state, driver_id)
    db.session.add(new_vehicle)
    db.session.commit()
    return 'Data saved successfully'

# Create a route to update an existing vehicle.
@route_vehicles.route('/updatevehicle', methods = ['PUT'])
def update():
    id = request.json['id']
    make = request.json['make']
    model = request.json['model']
    plate = request.json['plate']
    capacity = request.json['capacity']
    state = request.json['state']
    driver_id = request.json['driver_id']
    vehicle = Vehicle.query.get(id)
    if vehicle:
        vehicle.make = make
        vehicle.model = model
        vehicle.plate = plate
        vehicle.capacity = capacity
        vehicle.state = state
        vehicle.driver_id = driver_id
        db.session.commit()
        return 'Data update successfully'
    else:
        return 'Error'
    
# Create a route to delete a vehicle by its ID.
@route_vehicles.route('/deletevehicle<id>', methods = ['DELETE'])
def delete(id):
    vehicle = Vehicle.query.get(id)
    db.session.delete(vehicle)
    db.session.commit()
    return jsonify(vehicle_schema.dump(vehicle))