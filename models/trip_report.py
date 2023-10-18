from config.db import db, ma, app

# The data model for the 'tblreport_trip' table is defined.
class TripHasReport(db.Model):
    __tablename__ = "Trip_has_Report"

    Trip_idTrip = db.Column(db.Integer, db.ForeignKey('Trip.idTrip'), primary_key=True)
    Trip_Vehicle_idVehicle = db.Column(db.Integer, db.ForeignKey('Trip.Vehicle_idVehicle'), primary_key=True)
    Trip_Vehicle_Driver_idDriver = db.Column(db.Integer, db.ForeignKey('Trip.Vehicle_Driver_idDriver'), primary_key=True)
    Trip_city_destination = db.Column(db.Integer, db.ForeignKey('Trip.city_destination'), primary_key=True)
    Trip_city_origin = db.Column(db.Integer, db.ForeignKey('Trip.city_origin'), primary_key=True)
    Report_idReport = db.Column(db.Integer, db.ForeignKey('Report.idReport'), primary_key=True)

    def __init__(self, Trip_idTrip, Trip_Vehicle_idVehicle, Trip_Vehicle_Driver_idDriver, Trip_city_destination,
                 Trip_city_origin, Report_idReport):
        self.Trip_idTrip = Trip_idTrip
        self.Trip_Vehicle_idVehicle = Trip_Vehicle_idVehicle
        self.Trip_Vehicle_Driver_idDriver = Trip_Vehicle_Driver_idDriver
        self.Trip_city_destination = Trip_city_destination
        self.Trip_city_origin = Trip_city_origin
        self.Report_idReport = Report_idReport

# Creación de la tabla en la base de datos dentro del contexto de la aplicación
with app.app_context():
    db.create_all()

class TripHasReportSchema(ma.Schema):
    class Meta:
        fields = ("Trip_idTrip", "Trip_Vehicle_idVehicle", "Trip_Vehicle_Driver_idDriver",
                  "Trip_city_destination", "Trip_city_origin", "Report_idReport")