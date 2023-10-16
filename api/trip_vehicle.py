from flask import Blueprint, request, json, jsonify
from config.db import db, ma, app
from models.trip_vehicle import Trip_Vehicle, Trip_VehicleSchema

# Create a Blueprint to define routes related to trip_vehicles.
route_trip_vehicles = Blueprint('trip_vehicle', __name__)

# Define a serialization schema for trip_vehicles.
trip_vehicle_schema = Trip_VehicleSchema
trip_vehicles_schema = Trip_VehicleSchema(many=True)

# Create a route to get all trip_vehicles.
@route_trip_vehicles.route('/trip_vehicles', methods = ['GET'])
def trip_vehicle():
    resultall = Trip_Vehicle.query.all()
    result_trip_vehicles = trip_vehicles_schema.dump(resultall)
    return jsonify(result_trip_vehicles)

# Create a route to save a new trip_vehicle.
@route_trip_vehicles.route('/savetrip_vehicle', methods = ['POST'])
def save():
    trip_id = request.json['trip_id']
    vehicle_id = request.json['vehicle_id']
    new_trip_vehicles = Trip_Vehicle(trip_id, vehicle_id)
    db.session.add(new_trip_vehicles)
    db.session.commit()
    return 'Data saved successfully'

# Create a route to update an existing trip_vehicle.
@route_trip_vehicles.route('/updatetrip_vehicle', methods = ['PUT'])
def update():
    id = request.json['id']
    trip_id = request.json['trip_id']
    vehicle_id = request.json['route_id']
    trip_vehicle = Trip_Vehicle.query.get(id)
    if trip_vehicle:
        trip_vehicle.trip_id = trip_id
        trip_vehicle.vehicle_id = vehicle_id
        db.session.commit()
        return 'Data update successfully'
    else:
        return 'Error'
    
# Create a route to delete a trip_vehicle by its ID.
@route_trip_vehicles.route('/deletetrip_vehicle<id>', methods = ['DELETE'])
def delete(id):
    trip_vehicle = Trip_Vehicle.query.get(id)
    db.session.delete(trip_vehicle)
    db.session.commit()
    return jsonify(trip_vehicle_schema.dump(trip_vehicle))