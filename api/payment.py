from flask import Blueprint, request
from config.db import db
from models.payment import Payment, PaymentSchema

payment_blueprint = Blueprint("payment", __name__)
payment_schema = PaymentSchema()
payments_schema = PaymentSchema(many=True)

# Ruta para crear un nuevo método de pago
@payment_blueprint.route("/payment/create", methods=["POST"])
def add_payment():
    name = request.json["name"]
    new_payment = Payment(name)

    db.session.add(new_payment)
    db.session.commit()

    return payment_schema.jsonify(new_payment), 201

# Ruta para crear múltiples métodos de pago
@payment_blueprint.route("/payment/create_multiple", methods=["POST"])
def add_multiple_payments():
    data = request.get_json()  # Obtener la lista de métodos de pago desde la solicitud JSON

    # Crear una lista para almacenar los nuevos métodos de pago
    new_payments = []

    for item in data:
        name = item["name"]
        new_payment = Payment(name)
        db.session.add(new_payment)
        new_payments.append(new_payment)

    db.session.commit()

    return payments_schema.jsonify(new_payments), 201

# Ruta para obtener todos los métodos de pago
@payment_blueprint.route("/payment/get", methods=["GET"])
def get_payments():
    payments = Payment.query.all()
    return payments_schema.jsonify(payments), 200

# Ruta para obtener un método de pago por su ID
@payment_blueprint.route("/payment/get/<int:idPayment>", methods=["GET"])
def get_payment(idPayment):
    payment = Payment.query.get(idPayment)
    return payment_schema.jsonify(payment), 200

# Ruta para actualizar un método de pago por su ID
@payment_blueprint.route("/payment/update/<int:idPayment>", methods=["PUT"])
def update_payment(idPayment):
    payment = Payment.query.get(idPayment)
    name = request.json["name"]

    payment.name = name

    db.session.commit()
    return payment_schema.jsonify(payment), 200

# Ruta para eliminar un método de pago por su ID
@payment_blueprint.route("/payment/delete/<int:idPayment>", methods=["DELETE"])
def delete_payment(idPayment):
    payment = Payment.query.get(idPayment)
    db.session.delete(payment)
    db.session.commit()

    return payment_schema.jsonify(payment), 200