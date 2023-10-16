from flask import Blueprint, request, json, jsonify
from config.db import db, ma, app
from models.request_vehicle import Request_Vehicle, Request_VehicleSchema

# Create a Blueprint to define routes related to request_vehicles.
route_request_vehicles = Blueprint('route_request_vehicle', __name__)

# Define a serialization schema for request_vehicles.
request_vehicle_schema = Request_VehicleSchema
request_vehicles_schema = Request_VehicleSchema(many=True)

# Create a route to get all request_vehicles.
@route_request_vehicles.route('/request_vehicles', methods = ['GET'])
def request_vehicle():
    resultall = Request_Vehicle.query.all()
    result_request_vehicles = request_vehicles_schema.dump(resultall)
    return jsonify(result_request_vehicles)

# Create a route to save a new request_vehicle.
@route_request_vehicles.route('/saverequest_vehicle', methods = ['POST'])
def save():
    request_id = request.json['request_id']
    vehicle_id = request.json['vehicle_id']
    new_request_vehicle = Request_Vehicle(type, request_id, vehicle_id)
    db.session.add(new_request_vehicle)
    db.session.commit()
    return 'Data saved successfully'

# Create a route to update an existing request_vehicle.
@route_request_vehicles.route('/updaterequest_vehicle', methods = ['PUT'])
def update():
    id = request.json['id']
    request_id = request.json['request_id']
    vehicle_id = request.json['vehicle_id']
    request_vehicle = Request_Vehicle.query.get(id)
    if request_vehicle:
        request_vehicle.request_id = request_id
        request_vehicle.vehicle_id = vehicle_id
        db.session.commit()
        return 'Data update successfully'
    else:
        return 'Error'
    
# Create a route to delete a request_vehicle by its ID.
@route_request_vehicles.route('/deleterequest_vehicle<id>', methods = ['DELETE'])
def delete(id):
    request_vehicle = Request_Vehicle.query.get(id)
    db.session.delete(request_vehicle)
    db.session.commit()
    return jsonify(request_vehicle_schema.dump(request_vehicle))