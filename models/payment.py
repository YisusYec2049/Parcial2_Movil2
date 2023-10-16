from config.db import db, ma, app

# The data model for the 'tblpayment' table is defined.
class Payment(db.Model):
    __tablename__ = "tblpayment"

    # The table columns are defined, each with its id."
    id = db.Column(db.Integer, primary_key = True)
    amount = db.Column(db.String(50))
    pay_method = db.Column(db.String(50))
    state = db.Column(db.String(50))
    trip_id = db.Column(db.Integer, db.Foreignkey('tbltrip.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('tbluser.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('tblvehicle.id'))
    
    def __init__(self, amount, pay_method, state, trip_id, user_id, vehicle_id):
        self.amount = amount
        self.pay_method = pay_method
        self.state = state
        self.trip_id = trip_id
        self.user_id = user_id
        self.vehicle_id = vehicle_id

# The 'tblpayment' table is created in the database within the app context."
with app.app_context():
    db.create_all()

# The serialization schema for Payment is defined to convert objects into JSON."
class PaymentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'amount', 'pay_method', 'state', 'trip_id', 'user_id', 'vehicle_id')