from flask import Blueprint, request, json, jsonify
from config.db import db, ma, app
from models.driver import Driver, DriverSchema

# Create a Blueprint to define routes related to drivers.
route_drivers = Blueprint('route_driver', __name__)

# Define a serialization schema for drivers.
driver_schema = DriverSchema
drivers_schema = DriverSchema(many=True)

# Create a route to get all drivers.
@route_drivers.route('/drivers', methods = ['GET'])
def driver():
    resultall = Driver.query.all()
    result_driver = drivers_schema.dump(resultall)
    return jsonify(result_driver)

# Create a route to save a new driver.
@route_drivers.route('/savedrivers', methods = ['POST'])
def save():
    name = request.json['name']
    lastname = request.json['lastname']
    license = request.json['license']
    new_driver = Driver(name, lastname, license)
    db.session.add(new_driver)
    db.session.commit()
    return 'Data saved successfully'

# Create a route to update an existing driver.
@route_drivers.route('/updatedrivers', methods = ['PUT'])
def update():
    id = request.json['id']
    name = request.json['name']
    lastname = request.json['lastname']
    license = request.json['license']
    driver = Driver.query.get(id)
    if driver:
        driver.name = name
        driver.lastname = name
        driver.license = license
        db.session.commit()
        return 'Data update successfully'
    else:
        return 'Error'
    
# Create a route to delete a driver by its ID.
@route_drivers.route('/deletedrivers/<id>', methods =['DELETE'])
def delete(id):
    driver = Driver.query.get(id)
    db.session.delete(driver)
    db.session.commit()
    return jsonify(driver_schema.dump(driver))