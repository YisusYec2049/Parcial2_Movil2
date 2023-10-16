from flask import Blueprint, request, json, jsonify
from config.db import db, ma, app
from models.trip import Trip, TripSchema

# Create a Blueprint to define routes related to trips.
route_trips = Blueprint('trip', __name__)

# Define a serialization schema for trips.
trip_schema = TripSchema
trips_schema = TripSchema(many=True)

# Create a route to get all trips.
@route_trips.route('/trips', methods = ['GET'])
def trip():
    resultall = Trip.query.all()
    result_trip = trips_schema.dump(resultall)
    return jsonify(result_trip)

# Create a route to save a new trip_vehicle.
@route_trips.route('/savetrip', methods = ['POST'])
def save():
    start_time = request.json['start_time']
    end_time = request.json['end_time']
    route_id = request.json['route_id']
    city_id = request.json['city_id']
    passenger_id = request.json['passenger_id']
    vehicle_id = request.json['vehicle_id']
    new_trip = Trip(start_time , end_time, route_id, city_id, passenger_id, vehicle_id)
    db.session.add(new_trip)
    db.session.commit()
    return 'Data saved successfully'

# Create a route to update an existing trip.
@route_trips.route('/updatetrip', methods = ['PUT'])
def update():
    id = request.json['id']
    start_time = request.json['start_time']
    end_time = request.json['end_time']
    route_id = request.json['route_id']
    city_id = request.json['city_id']
    passenger_id = request.json['passenger_id']
    vehicle_id = request.json['vehicle_id']
    trip = Trip.query.get(id)
    if trip:
        trip.start_time = start_time
        trip.end_time = end_time
        trip.route_id = route_id
        trip.city_id = city_id
        trip.passenger_id = passenger_id
        trip.vehicle_id = vehicle_id
        db.session.commit()
        return 'Data update successfully'
    else:
        return 'Error'
    
# Create a route to delete a trip by its ID.
@route_trips.route('/deletetrip<id>', methods = ['DELETE'])
def delete(id):
    trip = Trip.query.get(id)
    db.session.delete(trip)
    db.session.commit()
    return jsonify(trip_schema.dump(trip))