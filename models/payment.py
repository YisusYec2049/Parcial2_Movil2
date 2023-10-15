from config.db import db, ma, app

class Payment(db.Model):
    __tablename__ = 'tblpayment'

    id = db.Column(db.Integer, primary_key= True)
    tipe = db.Column(db.String(50))
    amount = db.Column(db.Integer)
    
    def __init__(self, tipe, amount):
        self.tipe = tipe
        self.amount = amount
    
with app.app_context():
    db.create_all()

class PaymenySchema(ma.Schema):
    class Meta:
        fields = ('id', 'tipe', 'amount')
        