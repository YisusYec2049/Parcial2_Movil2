from flask import Blueprint, request, json, jsonify
from config.db import db, ma, app
from models.request_passenger import Request_Passenger, Request_PassengerSchema

# Create a Blueprint to define routes related to request_passengers.
route_request_passengers = Blueprint('route_request_passenger', __name__)

# Define a serialization schema for request_passengers.
request_passenger_schema = Request_PassengerSchema
request_passengers_schema = Request_PassengerSchema(many=True)

# Create a route to get all request_passengers.
@route_request_passengers.route('/request_passengers', methods = ['GET'])
def request_passenger():
    resultall = Request_Passenger.query.all()
    result_request_passengers = request_passengers_schema.dump(resultall)
    return jsonify(result_request_passengers)

# Create a route to save a new request_passenger.
@route_request_passengers.route('/saverequest_passenger', methods = ['POST'])
def save():
    request_id = request.json['request_id']
    passenger_id = request.json['passenger_id']
    new_request_passenger = Request_Passenger(type, request_id, passenger_id)
    db.session.add(new_request_passenger)
    db.session.commit()
    return 'Data saved successfully'

# Create a route to update an existing request_passenger.
@route_request_passengers.route('/updaterequest_passenger', methods = ['PUT'])
def update():
    id = request.json['id']
    request_id = request.json['request_id']
    passenger_id = request.json['passenger_id']
    request_passenger = Request_Passenger.query.get(id)
    if request_passenger:
        request_passenger.request_id = request_id
        request_passenger.passenger_id = passenger_id
        db.session.commit()
        return 'Data update successfully'
    else:
        return 'Error'
    
# Create a route to delete a request_passenger by its ID.
@route_request_passengers.route('/deleterequest_passenger<id>', methods = ['DELETE'])
def delete(id):
    request_passenger = Request_Passenger.query.get(id)
    db.session.delete(request_passenger)
    db.session.commit()
    return jsonify(request_passenger_schema.dump(request_passenger))