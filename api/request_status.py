from flask import Blueprint, request, jsonify
from config.db import db
from models.request_status import RequestStatus, RequestStatusSchema

request_status_blueprint = Blueprint("request_status", __name__)
request_status_schema = RequestStatusSchema()
request_statuses_schema = RequestStatusSchema(many=True)

# Ruta para crear un nuevo estado de solicitud
@request_status_blueprint.route("/request_status/create", methods=["POST"])
def add_request_status():
    name = request.json["name"]
    new_request_status = RequestStatus(name)

    db.session.add(new_request_status)
    db.session.commit()

    return request_status_schema.jsonify(new_request_status), 201

# Ruta para obtener todos los estados de solicitud
@request_status_blueprint.route("/request_status/get", methods=["GET"])
def get_request_statuses():
    request_statuses = RequestStatus.query.all()
    return request_statuses_schema.jsonify(request_statuses), 200

# Ruta para obtener un estado de solicitud por su ID
@request_status_blueprint.route("/request_status/get/<int:idRequest_Status>", methods=["GET"])
def get_request_status(idRequest_Status):
    request_status = RequestStatus.query.get(idRequest_Status)
    return request_status_schema.jsonify(request_status), 200

# Ruta para actualizar un estado de solicitud por su ID
@request_status_blueprint.route("/request_status/update/<int:idRequest_Status>", methods=["PUT"])
def update_request_status(idRequest_Status):
    request_status = RequestStatus.query.get(idRequest_Status)
    name = request.json["name"]

    request_status.name = name

    db.session.commit()
    return request_status_schema.jsonify(request_status), 200

# Ruta para eliminar un estado de solicitud por su ID
@request_status_blueprint.route("/request_status/delete/<int:idRequest_Status>", methods=["DELETE"])
def delete_request_status(idRequest_Status):
    request_status = RequestStatus.query.get(idRequest_Status)
    db.session.delete(request_status)
    db.session.commit()

    return request_status_schema.jsonify(request_status), 200
