from config.db import db, ma, app

# The data model for the 'tblreport' table is defined.
class Report(db.Model):
    __tablename__ = "tblreport"

    # The table columns are defined, each with its id."
    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.String(50))
    content = db.Column(db.String(2000))
    creation_date = db.Column(db.String(50))
    trip_id = db.Column(db.Integer, db.ForeignKey('tbltrip.id'))
    

# The 'tblreport' table is created in the database within the app context."
with app.app_context():
    db.create_all()

# The serialization schema for Report is defined to convert objects into JSON."
class ReportSchema(ma.Schema):
    class Meta:
        fields = ('id', 'type', 'content', 'creation_date', 'trip_id')