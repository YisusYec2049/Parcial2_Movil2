from flask import Blueprint, request, jsonify
from config.db import db
from models.trip_report import TripHasReport, TripHasReportSchema

trip_has_report_blueprint = Blueprint("trip_has_report", __name__)
trip_has_report_schema = TripHasReportSchema()
trip_has_reports_schema = TripHasReportSchema(many=True)

# Ruta para crear una nueva relación entre viaje e informe
@trip_has_report_blueprint.route("/trip_has_report/create", methods=["POST"])
def add_trip_has_report():
    Trip_idTrip = request.json["Trip_idTrip"]
    Trip_Vehicle_idVehicle = request.json["Trip_Vehicle_idVehicle"]
    Trip_Vehicle_Driver_idDriver = request.json["Trip_Vehicle_Driver_idDriver"]
    Trip_city_destination = request.json["Trip_city_destination"]
    Trip_city_origin = request.json["Trip_city_origin"]
    Report_idReport = request.json["Report_idReport"]

    new_trip_has_report = TripHasReport(Trip_idTrip, Trip_Vehicle_idVehicle, Trip_Vehicle_Driver_idDriver, Trip_city_destination, Trip_city_origin, Report_idReport)

    db.session.add(new_trip_has_report)
    db.session.commit()

    return trip_has_report_schema.jsonify(new_trip_has_report), 201

# Ruta para obtener todas las relaciones entre viaje e informe
@trip_has_report_blueprint.route("/trip_has_report/get", methods=["GET"])
def get_trip_has_reports():
    trip_has_reports = TripHasReport.query.all()
    return trip_has_reports_schema.jsonify(trip_has_reports), 200

# Ruta para obtener una relación entre viaje e informe por su clave primaria
@trip_has_report_blueprint.route("/trip_has_report/get/<int:Trip_idTrip>/<int:Trip_Vehicle_idVehicle>/<int:Trip_Vehicle_Driver_idDriver>/<int:Trip_city_destination>/<int:Trip_city_origin>/<int:Report_idReport>", methods=["GET"])
def get_trip_has_report(Trip_idTrip, Trip_Vehicle_idVehicle, Trip_Vehicle_Driver_idDriver, Trip_city_destination, Trip_city_origin, Report_idReport):
    trip_has_report = TripHasReport.query.get((Trip_idTrip, Trip_Vehicle_idVehicle, Trip_Vehicle_Driver_idDriver, Trip_city_destination, Trip_city_origin, Report_idReport))
    return trip_has_report_schema.jsonify(trip_has_report), 200

# Ruta para eliminar una relación entre viaje e informe por su clave primaria
@trip_has_report_blueprint.route("/trip_has_report/delete/<int:Trip_idTrip>/<int:Trip_Vehicle_idVehicle>/<int:Trip_Vehicle_Driver_idDriver>/<int:Trip_city_destination>/<int:Trip_city_origin>/<int:Report_idReport>", methods=["DELETE"])
def delete_trip_has_report(Trip_idTrip, Trip_Vehicle_idVehicle, Trip_Vehicle_Driver_idDriver, Trip_city_destination, Trip_city_origin, Report_idReport):
    trip_has_report = TripHasReport.query.get((Trip_idTrip, Trip_Vehicle_idVehicle, Trip_Vehicle_Driver_idDriver, Trip_city_destination, Trip_city_origin, Report_idReport))
    db.session.delete(trip_has_report)
    db.session.commit()

    return trip_has_report_schema.jsonify(trip_has_report), 200
