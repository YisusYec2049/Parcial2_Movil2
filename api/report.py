from flask import Blueprint, request, json, jsonify
from config.db import db, ma, app
from models.report import Report, ReportSchema

# Create a Blueprint to define routes related to reports.
route_reports = Blueprint('route_report', __name__)

# Define a serialization schema for reports.
report_schema = ReportSchema
reports_schema = ReportSchema(many=True)

# Create a route to get all reports.
@route_reports.route('/reports', methods = ['GET'])
def report():
    resultall = Report.query.all()
    result_report = reports_schema.dump(resultall)
    return jsonify(result_report)

# Create a route to save a new report.
@route_reports.route('/savereport', methods = ['POST'])
def save():
    type = request.json['type']
    content =request.json['content']
    creation_date = request.json['creation_date']
    trip_id = request.json['trip_id']
    new_report = Report(type, content, creation_date, trip_id)
    db.session.add(new_report)
    db.session.commit()
    return 'Data saved successfully'

# Create a route to update an existing report.
@route_reports.route('/updatereport', methods = ['PUT'])
def update():
    id = request.json['id']
    type = request.json['type']
    content =request.json['content']
    creation_date = request.json['creation_date']
    trip_id = request.json['trip_id']
    report = Report.query.get(id)
    if report:
        report.type = type
        report.content = content
        report.creation_date = creation_date
        report.trip_id = trip_id
        db.session.commit()
        return 'Data update successfully'
    else:
        return 'Error'
    
# Create a route to delete a report by its ID.
@route_reports.route('/deletereport<id>', methods = ['DELETE'])
def delete(id):
    report = Report.query.get(id)
    db.session.delete(report)
    db.session.commit()
    return jsonify(report_schema.dump(report))