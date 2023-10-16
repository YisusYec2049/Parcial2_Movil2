from flask import Blueprint, request, json, jsonify
from config.db import db, ma, app
from models.report_trip import Report_Trip, Report_TripSchema

# Create a Blueprint to define routes related to report_trips.
route_report_trips = Blueprint('route_report_trip', __name__)

# Define a serialization schema for report_trips.
report_trip_schema = Report_TripSchema
report_trips_schema = Report_TripSchema(many=True)

# Create a route to get all report_trips.
@route_report_trips.route('/report_trips', methods = ['GET'])
def report_trip():
    resultall = Report_Trip.query.all()
    result_report_trip = report_trips_schema.dump(resultall)
    return jsonify(result_report_trip)

# Create a route to save a new report_trip.
@route_report_trips.route('/savereport_trip', methods = ['POST'])
def save():
    report_id = request.json['report_id']
    trip_id = request.json['trip_id']
    new_report_trip = Report_Trip(report_id, trip_id)
    db.session.add(new_report_trip)
    db.session.commit()
    return 'Data saved successfully'

# Create a route to update an existing report_trip.
@route_report_trips.route('/updatereport_trip', methods = ['PUT'])
def update():
    id = request.json['id']
    report_id = request.json['report_id']
    trip_id = request.json['trip_id']
    report_trip = Report_Trip.query.get(id)
    if report_trip:
        report_trip.report_id = report_id
        report_trip.trip_id = trip_id
        db.session.commit()
        return 'Data update successfully'
    else:
        return 'Error'
    
# Create a route to delete a report_trip by its ID.
@route_report_trips.route('/deletereport_trip<id>', methods = ['DELETE'])
def delete(id):
    report_trip = Report_Trip.query.get(id)
    db.session.delete(report_trip)
    db.session.commit()
    return jsonify(report_trip_schema.dump(report_trip))