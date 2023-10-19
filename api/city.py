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

# Ruta para agregar una o más ciudades
@city_blueprint.route("/cities/add", methods=["POST"])
def add_cities():
    cities_data = request.json  # Espera una lista de ciudades en el cuerpo de la solicitud

    added_cities = []
    for city_data in cities_data:
        if "name" in city_data:
            name = city_data["name"]
            new_city = City(name=name)
            db.session.add(new_city)
            added_cities.append(new_city)

    db.session.commit()

    return cities_schema.jsonify(added_cities), 201

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
@city_blueprint.route("/city/update", methods=["PUT"])
def update_city(idCity=None):
    if idCity is not None:
        city = City.query.get(idCity)
    else:
        # Si el parámetro idCity no se proporciona en la URL, intenta obtenerlo de la cadena de consulta
        idCity = request.args.get("idCity")
        if idCity is not None:
            city = City.query.get(idCity)

    if city:
        name = request.json.get("name")
        if name is not None:
            city.name = name
            db.session.commit()
            return city_schema.jsonify(city), 200
    return {"message": "Ciudad no encontrada"}, 404

# Ruta para eliminar una ciudad por su ID
@city_blueprint.route("/city/delete", methods=["DELETE"])
def delete_city_by_id():
    city_id = request.args.get("idCity")  # Obtén el parámetro idCity de la consulta

    if city_id is not None:
        city = City.query.get(city_id)
        if city:
            db.session.delete(city)
            db.session.commit()
            return city_schema.jsonify(city), 200

    return {"message": "Ciudad no encontrada"}, 404
