from flask import Blueprint, request
from config.db import db
from models.driver import Driver, DriverSchema

driver_blueprint = Blueprint("driver", __name__)
driver_schema = DriverSchema()
drivers_schema = DriverSchema(many=True)

# Ruta para crear un nuevo conductor
@driver_blueprint.route("/driver/create", methods=["POST"])
def add_driver():
    User_idUser = request.json["User_idUser"]
    license = request.json["license"]
    new_driver = Driver(User_idUser, license)

    db.session.add(new_driver)
    db.session.commit()

    return driver_schema.jsonify(new_driver), 201

# Ruta para obtener todos los conductores
@driver_blueprint.route("/driver/get", methods=["GET"])
def get_drivers():
    drivers = Driver.query.all()
    return drivers_schema.jsonify(drivers), 200

# Ruta para obtener un conductor por su ID
@driver_blueprint.route("/driver/get/<int:idDriver>", methods=["GET"])
def get_driver(idDriver):
    driver = Driver.query.get(idDriver)
    return driver_schema.jsonify(driver), 200

# Ruta para actualizar un conductor por su ID
@driver_blueprint.route("/driver/update/<int:idDriver>", methods=["PUT"])
def update_driver(idDriver):
    driver = Driver.query.get(idDriver)
    User_idUser = request.json["User_idUser"]
    license = request.json["license"]

    driver.User_idUser = User_idUser
    driver.license = license

    db.session.commit()
    return driver_schema.jsonify(driver), 200

# Ruta para eliminar un conductor por su ID
@driver_blueprint.route("/driver/delete/<int:idDriver>", methods=["DELETE"])
def delete_driver(idDriver):
    driver = Driver.query.get(idDriver)
    db.session.delete(driver)
    db.session.commit()

    return driver_schema.jsonify(driver), 200