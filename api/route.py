from flask import Blueprint, request, json, jsonify
from config.db import db, ma, app
from models.route import Route, RouteSchema

# Create a Blueprint to define routes related to routes.
route_routes = Blueprint('route_route', __name__)

# Define a serialization schema for routes.
route_schema = RouteSchema
routes_schema = RouteSchema(many=True)

# Create a route to get all routes.
@route_routes.route('/routes', methods = ['GET'])
def route():
    resultall = Route.query.all()
    result_routes = routes_schema.dump(resultall)
    return jsonify(result_routes)

# Create a route to save a new route.
@route_routes.route('/saveroute', methods = ['POST'])
def save():
    distance = request.json['distance']
    origin_city_id = request.json['origin_city_id']
    destination_city_id = request.json['destination_city_id']
    new_route = Route(distance, origin_city_id, destination_city_id)
    db.session.add(new_route)
    db.session.commit()
    return 'Data saved successfully'

# Create a route to update an existing route.
@route_routes.route('/updateroute', methods = ['PUT'])
def update():
    id = route.json['id']
    distance = route.json['distance']
    origin_city_id = route.json['origin_city_id']
    destination_city_id = route.json['destination_city_id']
    route = Route.query.get(id)
    if route:
        route.distance = distance
        route.origin_city_id = origin_city_id
        route.destination_city_id = destination_city_id
        db.session.commit()
        return 'Data update successfully'
    else:
        return 'Error'
    
# Create a route to delete a route by its ID.
@route_routes.route('/deleteroute<id>', methods = ['DELETE'])
def delete(id):
    route = Route.query.get(id)
    db.session.delete(route)
    db.session.commit()
    return jsonify(route_schema.dump(route))