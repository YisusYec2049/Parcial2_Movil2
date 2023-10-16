from flask import Blueprint, request, json, jsonify
from config.db import db, ma, app
from models.user import User, UserSchema

# Create a Blueprint to define routes related to users.
route_users = Blueprint('user', __name__)

# Define a serialization schema for users.
user_schema = UserSchema
users_schema = UserSchema(many=True)

# Create a route to get all users.
@route_users.route('/users', methods = ['GET'])
def user():
    resultall = User.query.all()
    result_user = users_schema.dump(resultall)
    return jsonify(result_user)

# Create a route to save a new user.
@route_users.route('/saveuser', methods = ['POST'])
def save():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    phone = request.json['phone']
    gender = request.json['gender']
    new_user = User(name , email, password, phone, gender)
    db.session.add(new_user)
    db.session.commit()
    return 'Data saved successfully'

# Create a route to update an existing user.
@route_users.route('/updateuser', methods = ['PUT'])
def update():
    id = request.json['id']
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    phone = request.json['phone']
    gender = request.json['gender']
    user = User.query.get(id)
    if user:
        user.name = name
        user.email = email
        user.password = password
        user.phone = phone
        user.gender = gender
        db.session.commit()
        return 'Data update successfully'
    else:
        return 'Error'
    
# Create a route to delete a user by its ID.
@route_users.route('/deleteuser<id>', methods = ['DELETE'])
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(user_schema.dump(user))