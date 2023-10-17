from flask import Blueprint, request, json, jsonify
from config.db import db, ma, app
from models.passenger import Passenger, PassengerSchema

# Create a Blueprint to define routes related to passengers.
route_passengers = Blueprint('route_passenger', __name__)

# Define a serialization schema for passengers.
passenger_schema = PassengerSchema
passengers_schema = PassengerSchema(many=True)

# Create a route to get all passengers.
@route_passengers.route('/passengers', methods = ['GET'])
def passenger():
    resultall = Passenger.query.all()
    result_passenger = passengers_schema.dump(resultall)
    return jsonify(result_passenger)

# Create a route to save a new passsenger.
@route_passengers.route('/savepassenger', methods = ['POST'])
def save():
    name = request.json['name']
    lastname = request.json['lastname']
    email = request.json['email']
    phone = request.json['phone']
    user_id = request.json['user_id']
    new_passenger = Passenger(name, lastname, email, phone, user_id)
    db.session.add(new_passenger)
    db.session.commit()
    return 'Data saved successfully.'

# Create a route to update an existing passenger.
@route_passengers.route('/updatepassenger', methods=['PUT'])
def update():
    id  = request.json['id']
    name = request.json['name']
    lastname = request.json['lastname']
    email = request.json['email']
    phone = request.json['phone']
    user_id = request.json['user_id']
    passenger = Passenger.query.get(id)
    if passenger:
        passenger.name = name
        passenger.lastname = lastname
        passenger.email = email
        passenger.phone = phone
        passenger.user_id = user_id
        db.session.commit()
        return 'Data update successfully.'
    else:
        return 'Error'
    
# Create a route to delete a passenger by its ID.
@route_passengers.route('/deletepassenger/<id>', methods = ['DELETE'])
def delete(id):
    passenger = Passenger.query.get(id)
    db.session.delete(passenger)
    db.session.commit()
    return jsonify(passenger_schema.dump(passenger))

