from flask import Blueprint, request, json, jsonify
from config.db import db, ma, app
from models.request import Request, RequestSchema

# Create a Blueprint to define routes related to requests.
route_requests = Blueprint('route_request', __name__)

# Define a serialization schema for requests.
request_schema = RequestSchema
requests_schema = RequestSchema(many=True)

# Create a route to get all requests.
@route_requests.route('/requests', methods = ['GET'])
def requests():
    resultall = Request.query.all()
    result_requests = requests_schema.dump(resultall)
    return jsonify(result_requests)

# Create a route to save a new request.
@route_requests.route('/saverequest', methods = ['POST'])
def save():
    preferences = request.json['preferences']
    state = request.json['state']
    details = request.json['details']
    origin_city_id = request.json['origin_city_id']
    destination_city_id = request.json['destination_city_id']
    passenger_id = request.json['passenger_id']
    vehicle_id = request.json['vehicle_id']
    driver_id = request.json['driver_id']
    new_request = Request(preferences, state, details, origin_city_id, destination_city_id, passenger_id, vehicle_id, driver_id)
    db.session.add(new_request)
    db.session.commit()
    return 'Data saved successfully'

# Create a route to update an existing request.
@route_requests.route('/updaterequest_vehicle', methods = ['PUT'])
def update():
    id = request.json['id']
    preferences = request.json['preferences']
    state = request.json['state']
    details = request.json['details']
    origin_city_id = request.json['origin_city_id']
    destination_city_id = request.json['destination_city_id']
    passenger_id = request.json['passenger_id']
    vehicle_id = request.json['vehicle_id']
    driver_id = request.json['driver_id']
    request = Request.query.get(id)
    if request:
        request.preferences = preferences
        request.state = state
        request.details = details
        request.origin_city_id = origin_city_id
        request.destination_city_id = destination_city_id
        request.passenger_id = passenger_id
        request.vehicle_id = vehicle_id
        request.driver_id = driver_id
        db.session.commit()
        return 'Data update successfully'
    else:
        return 'Error'
    
# Create a route to delete a request by its ID.
@route_requests.route('/deleterequest<id>', methods = ['DELETE'])
def delete(id):
    request = Request.query.get(id)
    db.session.delete(request)
    db.session.commit()
    return jsonify(request_schema.dump(request))