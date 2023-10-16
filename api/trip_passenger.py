from flask import Blueprint, request, json, jsonify
from config.db import db, ma, app
from models.trip_passenger import Trip_Passenger, Trip_PassengerSchema

# Create a Blueprint to define routes related to trip_passengers.
route_trip_passengers = Blueprint('trip_passenger', __name__)

# Define a serialization schema for trip_passengers.
trip_passenger_schema = Trip_PassengerSchema
trip_passengers_schema = Trip_PassengerSchema(many=True)

# Create a route to get all trip_passengers.
@route_trip_passengers.route('/trip_passengers', methods = ['GET'])
def trip_passenger():
    resultall = Trip_Passenger.query.all()
    result_trip_passengers = trip_passengers_schema.dump(resultall)
    return jsonify(result_trip_passengers)

# Create a route to save a new trip_passenger.
@route_trip_passengers.route('/savetrip_passenger', methods = ['POST'])
def save():
    trip_id = request.json['trip_id']
    passenger_id = request.json['passenger_id']
    new_trip_passenger = Trip_Passenger(trip_id, passenger_id)
    db.session.add(new_trip_passenger)
    db.session.commit()
    return 'Data saved successfully'

# Create a route to update an existing trip_passenger.
@route_trip_passengers.route('/updatetrip_passenger', methods = ['PUT'])
def update():
    id = trip_passenger.json['id']
    trip_id = request.json['trip_id']
    passenger_id = request.json['passenger_id']
    trip_passenger = Trip_Passenger.query.get(id)
    if trip_passenger:
        trip_passenger.trip_id = trip_id
        trip_passenger.passenger_id = passenger_id
        db.session.commit()
        return 'Data update successfully'
    else:
        return 'Error'
    
# Create a route to delete a trip_passenger by its ID.
@route_trip_passengers.route('/deletetrip_passenger<id>', methods = ['DELETE'])
def delete(id):
    trip_passenger = Trip_Passenger.query.get(id)
    db.session.delete(trip_passenger)
    db.session.commit()
    return jsonify(trip_passenger_schema.dump(trip_passenger))