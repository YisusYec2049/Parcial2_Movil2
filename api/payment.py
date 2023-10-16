from flask import Blueprint, request, json, jsonify
from config.db import db, ma, app
from models.payment import Payment, PaymentSchema

# Create a Blueprint to define routes related to payments.
route_payments = Blueprint('route_payment', __name__)

# Define a serialization schema for payments.
payment_schema = PaymentSchema
payments_schema = PaymentSchema(many=True)

# Create a route to get all payments.
@route_payments.route('/payments', methods = ['GET'])
def payment():
    resultall = Payment.query.all()
    result_payment = payments_schema.dump(resultall)
    return jsonify(result_payment)

# Create a route to save a new payment.
@route_payments.route('/savepayment', methods = ['POST'])
def save():
    amount = request.json['amount']
    pay_method = request.json['pay_method']
    state = request.json['state']
    trip_id = request.json['trip_id']
    user_id = request.json['user_id']
    vehicle_id = request.json['vehicle_id']
    new_payment = Payment(amount, pay_method, state, trip_id, user_id, vehicle_id)
    db.session.add(new_payment)
    db.session.commit()
    return 'Data saved successfully'

# Create a route to update an existing payment.
@route_payments.route('/updatepayment', methods = ['PUT'])
def update():
    id = request.json['id']
    amount = request.json['amount']
    pay_method = request.json['pay_method']
    state = request.json['state']
    trip_id = request.json['trip_id']
    user_id = request.json['user_id']
    vehicle_id = request.json['vehicle_id']
    payment = Payment.query.get(id)
    if payment:
        payment.amount = amount
        payment.pay_method = pay_method
        payment.state = state
        payment.trip_id = trip_id
        payment.user_id = user_id
        payment.vehicle_id = vehicle_id
        db.session.commit()
        return 'Data update successfully'
    else:
        return 'Error'
    
# Create a route to delete a payment by its ID.
@route_payments.route('/deletepayment<id>', methods = ['DELETE'])
def delete(id):
    payment = Payment.query.get(id)
    db.session.delete(payment)
    db.session.commit()
    return jsonify(payment_schema.dump(payment))