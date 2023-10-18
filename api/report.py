from flask import Blueprint, request, json, jsonify
from config.db import db, ma, app
from models.report import Report, ReportSchema

# Create a Blueprint to define routes related to reports.
report_blueprint = Blueprint("report", __name__)
report_schema = ReportSchema()
reports_schema = ReportSchema(many=True)

# Ruta para crear un nuevo informe
@report_blueprint.route("/report/create", methods=["POST"])
def add_report():
    date_issue = request.json["date_issue"]
    description = request.json["description"]
    new_report = Report(date_issue, description)

    db.session.add(new_report)
    db.session.commit()

    return report_schema.jsonify(new_report), 201

# Ruta para obtener todos los informes
@report_blueprint.route("/report/get", methods=["GET"])
def get_reports():
    reports = Report.query.all()
    return reports_schema.jsonify(reports), 200

# Ruta para obtener un informe por su ID
@report_blueprint.route("/report/get/<int:idReport>", methods=["GET"])
def get_report(idReport):
    report = Report.query.get(idReport)
    return report_schema.jsonify(report), 200

# Ruta para actualizar un informe por su ID
@report_blueprint.route("/report/update/<int:idReport>", methods=["PUT"])
def update_report(idReport):
    report = Report.query.get(idReport)
    date_issue = request.json["date_issue"]
    description = request.json["description"]

    report.date_issue = date_issue
    report.description = description

    db.session.commit()
    return report_schema.jsonify(report), 200

# Ruta para eliminar un informe por su ID
@report_blueprint.route("/report/delete/<int:idReport>", methods=["DELETE"])
def delete_report(idReport):
    report = Report.query.get(idReport)
    db.session.delete(report)
    db.session.commit()

    return report_schema.jsonify(report), 200