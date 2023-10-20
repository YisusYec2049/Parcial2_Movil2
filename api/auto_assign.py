from flask import Blueprint, request
from config.db import db
from models.auto_assign_request import auto_assign_requests

auto_assign_blueprint = Blueprint("/autoasign", __name__)


@auto_assign_blueprint.route('/auto_asign', methods=['GET'])
def asignar_olicitudes():
    auto_assign_requests()
    return 'Solicitudes asignadas correctamente'
