from flask import Blueprint, request, json, jsonify
from config.db import db, ma, app
from models.user import User, UserSchema

# Create a Blueprint to define routes related to users.
user_blueprint = Blueprint("user", __name__)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Ruta para crear un nuevo usuario
@user_blueprint.route("/user/create", methods=["POST"])
def add_user():
    name = request.json["name"]
    lastname = request.json.get("lastname")
    number = request.json["number"]
    email = request.json.get("email")
    password = request.json["password"]

    new_user = User(name, lastname, number, email, password)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user), 201

# Ruta para obtener todos los usuarios
@user_blueprint.route("/user/get", methods=["GET"])
def get_users():
    users = User.query.all()
    return users_schema.jsonify(users), 200

# Ruta para obtener un usuario por su ID
@user_blueprint.route("/user/get/<int:idUser>", methods=["GET"])
def get_user(idUser):
    user = User.query.get(idUser)
    return user_schema.jsonify(user), 200

# Ruta para actualizar un usuario por su ID
@user_blueprint.route("/user/update/<int:idUser>", methods=["PUT"])
def update_user(idUser):
    user = User.query.get(idUser)
    name = request.json["name"]
    lastname = request.json.get("lastname")
    number = request.json["number"]
    email = request.json.get("email")
    password = request.json["password"]

    user.name = name
    user.lastname = lastname
    user.number = number
    user.email = email
    user.password = password

    db.session.commit()
    return user_schema.jsonify(user), 200

# Ruta para eliminar un usuario por su ID
@user_blueprint.route("/user/delete/<int:idUser>", methods=["DELETE"])
def delete_user(idUser):
    user = User.query.get(idUser)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user), 200