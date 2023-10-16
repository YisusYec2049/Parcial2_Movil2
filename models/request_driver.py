from config.db import db, ma, app

# The data model for the 'tblrequest_driver' table is defined.
class Request_Driver(db.Model):
    __tablename__ = "tblrequest_driver"

    # The table columns are defined, each with its id."
    id = db.Column(db.Integer, primary_key = True)
    request_id = db.Column(db.Integer, db.ForeignKey('tblrequest.id'))
    driver_id = db.Column(db.Integer, db.ForeignKey('tbldriver.id'))


    def __init__(self, request_id, driver_id):
        self.request_id = request_id
        self.driver_id = driver_id

# The 'tblrequest_driver' table is created in the database within the app context."
with app.app_context():
    db.create_all()

# The serialization schema for Request_Driver is defined to convert objects into JSON."
class Request_DriverSchema(ma.Schema):
    class Meta:
        fields = ('id', 'request_id', 'driver_id')