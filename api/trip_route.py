from flask import Blueprint, request, json, jsonify
from config.db import db, ma, app
from models.trip_route import Trip_Route, Trip_RouteSchema

# Create a Blueprint to define routes related to trip_routes.
route_trip_routes = Blueprint('trip_route', __name__)

# Define a serialization schema for trip_routes.
trip_route_schema = Trip_RouteSchema
trip_routes_schema = Trip_RouteSchema(many=True)

# Create a route to get all trip_routes.
@route_trip_routes.route('/trip_routes', methods = ['GET'])
def trip_route():
    resultall = Trip_Route.query.all()
    result_trip_routes = trip_routes_schema.dump(resultall)
    return jsonify(result_trip_routes)

# Create a route to save a new trip_route.
@route_trip_routes.route('/savetrip_route', methods = ['POST'])
def save():
    trip_id = request.json['trip_id']
    route_id = request.json['route_id']
    new_trip_route = Trip_Route(trip_id, route_id)
    db.session.add(new_trip_route)
    db.session.commit()
    return 'Data saved successfully'

# Create a route to update an existing trip_route.
@route_trip_routes.route('/updatetrip_route', methods = ['PUT'])
def update():
    id = request.json['id']
    trip_id = request.json['trip_id']
    route_id = request.json['route_id']
    trip_route = Trip_Route.query.get(id)
    if trip_route:
        trip_route.trip_id = trip_id
        trip_route.route_id = route_id
        db.session.commit()
        return 'Data update successfully'
    else:
        return 'Error'
    
# Create a route to delete a trip_route by its ID.
@route_trip_routes.route('/deletetrip_route<id>', methods = ['DELETE'])
def delete(id):
    trip_route = Trip_Route.query.get(id)
    db.session.delete(trip_route)
    db.session.commit()
    return jsonify(trip_route_schema.dump(trip_route))