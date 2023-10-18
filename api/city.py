from flask import Blueprint, request
from config.db import db
from models.city import City, CitySchema

# Create a Blueprint to define routes related to cities.
city_blueprint = Blueprint("city", __name__)

# Define a serialization schema for cities.
city_schema = CitySchema()
cities_schema = CitySchema(many=True)

# Ruta para crear una nueva ciudad
@city_blueprint.route("/city/create", methods=["POST"])
def add_city():
    name = request.json["name"]
    new_city = City(name)

    db.session.add(new_city)
    db.session.commit()

    return city_schema.jsonify(new_city), 201

# Ruta para obtener todas las ciudades
@city_blueprint.route("/city/get", methods=["GET"])
def get_cities():
    cities = City.query.all()
    return cities_schema.jsonify(cities), 200

# Ruta para obtener una ciudad por su ID
@city_blueprint.route("/city/get/<int:idCity>", methods=["GET"])
def get_city(idCity):
    city = City.query.get(idCity)
    return city_schema.jsonify(city), 200

# Ruta para actualizar una ciudad por su ID
@city_blueprint.route("/city/update/<int:idCity>", methods=["PUT"])
def update_city(idCity):
    city = City.query.get(idCity)
    name = request.json["name"]

    city.name = name

    db.session.commit()
    return city_schema.jsonify(city), 200

# Ruta para eliminar una ciudad por su ID
@city_blueprint.route("/city/delete/<int:idCity>", methods=["DELETE"])
def delete_city(idCity):
    city = City.query.get(idCity)
    db.session.delete(city)
    db.session.commit()

    return city_schema.jsonify(city), 200