from config.db import db, ma, app

class Payment(db.Model):
    __tablename__ = "Payment"

    idPayment = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)

    def __init__(self, name):
        self.name = name

# Creación de la tabla en la base de datos dentro del contexto de la aplicación
with app.app_context():
    db.create_all()

# Definición del esquema de serialización
class PaymentSchema(ma.Schema):
    class Meta:
        fields = ("idPayment", "name")