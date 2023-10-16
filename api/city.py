from flask import Blueprint, request, json, jsonify
from config.db import db, ma, app
from models.city import City, CitySchema

# Create a Blueprint to define routes related to cities.
route_cities = Blueprint('route_city', __name__)

# Define a serialization schema for cities.
city_schema = CitySchema
cities_schema = CitySchema(many=True)

# Create a route to get all cities.
@route_cities.route('/cities', methods=['GET'])
def city():
    resultall = City.query.all()
    result_city = cities_schema.dump(resultall)
    return jsonify(result_city)

# Create a route to save a new city.
@route_cities.route('/savecities', methods=['POST'])
def save():
    name = request.json['name']
    departament = request.json['departament']
    origin = request.json['origin']
    destination = request.json['destination']
    new_city = City(name, departament, origin, destination)
    db.session.add(new_city)
    db.session.commit()
    return 'Data saved successfully' 

# Create a route to update an existing city.
@route_cities.route('/updatecities', methods = ['PUT'])
def update():
    id = request.json['id']
    name = request.json['name']
    departament = request.json['departament']
    origin = request.json['origin']
    destination = request.json['destination']
    city = City.query.get(id)
    if city:
        city.name = name
        city.departament = departament
        city.origin = origin
        city.destination = destination
        db.session.commit()
        return 'Data update successfully'
    else:
        return 'Error'

# Create a route to delete a city by its ID.
@route_cities.route('/deletecities/<id>', methods = ['DELETE'])
def delete(id):
    city = City.query.get(id)
    db.session.delete(city)
    db.session.commit()
    return jsonify(city_schema.dump(city))