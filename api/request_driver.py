from flask import Blueprint, request, json, jsonify
from config.db import db, ma, app
from models.request_driver import Request_Driver, Request_DriverSchema

# Create a Blueprint to define routes related to request_drivers.
route_request_drivers = Blueprint('route_request_driver', __name__)

# Define a serialization schema for request_drivers.
request_driver_schema = Request_DriverSchema
request_drivers_schema = Request_DriverSchema(many=True)

# Create a route to get all request_drivers.
@route_request_drivers.route('/request_driver', methods = ['GET'])
def request_driver():
    resultall = Request_Driver.query.all()
    result_request_drivers = request_drivers_schema.dump(resultall)
    return jsonify(result_request_drivers)

# Create a route to save a new request_driver.
@route_request_drivers.route('/saverequest_driver', methods = ['POST'])
def save():
    request_id = request.json['request_id']
    driver_id = request.json['driver_id']
    new_request_driver = Request_Driver(type, request_id, driver_id)
    db.session.add(new_request_driver)
    db.session.commit()
    return 'Data saved successfully'

# Create a route to update an existing request_driver.
@route_request_drivers.route('/updaterequest_driver', methods = ['PUT'])
def update():
    id = request.json['id']
    request_id = request.json['request_id']
    driver_id = request.json['driver_id']
    request_driver = Request_Driver.query.get(id)
    if request_driver:
        request_driver.request_id = request_id
        request_driver.driver_id = driver_id
        db.session.commit()
        return 'Data update successfully'
    else:
        return 'Error'
    
# Create a route to delete a request_driver by its ID.
@route_request_drivers.route('/deleterequest_driver<id>', methods = ['DELETE'])
def delete(id):
    request_driver = Request_Driver.query.get(id)
    db.session.delete(request_driver)
    db.session.commit()
    return jsonify(request_driver_schema.dump(request_driver))