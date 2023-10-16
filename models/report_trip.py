from config.db import db, ma, app

# The data model for the 'tblreport_trip' table is defined.
class Report_Trip(db.Model):
    __tablename__ = "tblreport_trip"

    # The table columns are defined, each with its id."
    id = db.Column(db.Integer, primary_key = True)
    report_id = db.Column(db.Integer, db.ForeignKey('tblreport.id'))
    trip_id = db.Column(db.Integer, db.ForeignKey('tbltrip.id'))


    def __init__(self, report_id, trip_id):
        self.report_id = report_id
        self.trip_id = trip_id

# The 'tblreport_trip' table is created in the database within the app context."
with app.app_context():
    db.create_all()

# The serialization schema for Report_Trip is defined to convert objects into JSON."
class Report_TripSchema(ma.Schema):
    class Meta:
        fields = ('id', 'report_id', 'trip_id')