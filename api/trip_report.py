from flask import Blueprint, request, json, jsonify
from config.db import db, ma, app
from models.trip_report import TripHasReport, TripHasReportSchema

# Create a Blueprint to define routes related to requests.
trip_has_report_blueprint = Blueprint("trip_has_report", __name__)
trip_has_report_schema = TripHasReportSchema()
trip_has_reports_schema = TripHasReportSchema(many=True)

# Ruta para crear un nuevo TripHasReport
@trip_has_report_blueprint.route("/trip_has_reports/create", methods=["POST"])
def add_trip_has_report():
    Trip_idTrip = request.json["Trip_idTrip"]
    Trip_Vehicle_idVehicle = request.json["Trip_Vehicle_idVehicle"]
    Trip_Vehicle_Driver_idDriver = request.json["Trip_Vehicle_Driver_idDriver"]
    Trip_city_destination = request.json["Trip_city_destination"]
    Trip_city_origin = request.json["Trip_city_origin"]
    Report_idReport = request.json["Report_idReport"]

    new_trip_has_report = TripHasReport(
        Trip_idTrip,
        Trip_Vehicle_idVehicle,
        Trip_Vehicle_Driver_idDriver,
        Trip_city_destination,
        Trip_city_origin,
        Report_idReport
    )

    db.session.add(new_trip_has_report)
    db.session.commit()

    return trip_has_report_schema.jsonify(new_trip_has_report), 201

# Ruta para obtener todos los TripHasReports
@trip_has_report_blueprint.route("/trip_has_reports", methods=["GET"])
def get_trip_has_reports():
    trip_has_reports = TripHasReport.query.all()
    return trip_has_reports_schema.jsonify(trip_has_reports), 200

# Ruta para obtener un TripHasReport por su clave primaria
@trip_has_report_blueprint.route("/trip_has_reports/<int:Trip_idTrip>/<int:Trip_Vehicle_idVehicle>/<int:Trip_Vehicle_Driver_idDriver>/<int:Trip_city_destination>/<int:Trip_city_origin>/<int:Report_idReport>", methods=["GET"])
def get_trip_has_report(Trip_idTrip, Trip_Vehicle_idVehicle, Trip_Vehicle_Driver_idDriver, Trip_city_destination, Trip_city_origin, Report_idReport):
    trip_has_report = TripHasReport.query.get((Trip_idTrip, Trip_Vehicle_idVehicle, Trip_Vehicle_Driver_idDriver, Trip_city_destination, Trip_city_origin, Report_idReport))
    if trip_has_report:
        return trip_has_report_schema.jsonify(trip_has_report), 200
    else:
        return jsonify({"message": "TripHasReport not found"}), 404

# Ruta para actualizar un TripHasReport por su clave primaria
@trip_has_report_blueprint.route("/trip_has_reports/update/<int:Trip_idTrip>/<int:Trip_Vehicle_idVehicle>/<int:Trip_Vehicle_Driver_idDriver>/<int:Trip_city_destination>/<int:Trip_city_origin>/<int:Report_idReport>", methods=["PUT"])
def update_trip_has_report(Trip_idTrip, Trip_Vehicle_idVehicle, Trip_Vehicle_Driver_idDriver, Trip_city_destination, Trip_city_origin, Report_idReport):
    trip_has_report = TripHasReport.query.get((Trip_idTrip, Trip_Vehicle_idVehicle, Trip_Vehicle_Driver_idDriver, Trip_city_destination, Trip_city_origin, Report_idReport))

    if trip_has_report:
        # Actualiza los campos necesarios
        # E.g., trip_has_report.campo = request.json["campo"]
        db.session.commit()
        return trip_has_report_schema.jsonify(trip_has_report), 200
    else:
        return jsonify({"message": "TripHasReport not found"}), 404

# Ruta para eliminar un TripHasReport por su clave primaria
@trip_has_report_blueprint.route("/trip_has_reports/delete/<int:Trip_idTrip>/<int:Trip_Vehicle_idVehicle>/<int:Trip_Vehicle_Driver_idDriver>/<int:Trip_city_destination>/<int:Trip_city_origin>/<int:Report_idReport>", methods=["DELETE"])
def delete_trip_has_report(Trip_idTrip, Trip_Vehicle_idVehicle, Trip_Vehicle_Driver_idDriver, Trip_city_destination, Trip_city_origin, Report_idReport):
    trip_has_report = TripHasReport.query.get((Trip_idTrip, Trip_Vehicle_idVehicle, Trip_Vehicle_Driver_idDriver, Trip_city_destination, Trip_city_origin, Report_idReport))

    if trip_has_report:
        db.session.delete(trip_has_report)
        db.session.commit()
        return trip_has_report_schema.jsonify(trip_has_report), 200
    else:
        return jsonify({"message": "TripHasReport not found"}), 404