from flask import request, jsonify
from models import Payment
from . import payment_bp 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app) 

@payment_bp.route('/payments', methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    return jsonify([payment.to_dict() for payment in payments])

@payment_bp.route('/payments/<int:id>', methods=['GET'])
def get_payment(id):
    payment = Payment.query.get_or_404(id)
    return jsonify(payment.to_dict())

@payment_bp.route('/payments', methods=['POST'])
def create_payment():
    data = request.get_json()
    new_payment = Payment(
        idUser=data['idUser'],
        idTicket=data['idTicket'],
        payment_date=data['payment_date'],
        amount=data['amount']
    )
    db.session.add(new_payment)
    db.session.commit()
    return jsonify(new_payment.to_dict()), 201

@payment_bp.route('/payments/<int:id>', methods=['PUT'])
def update_payment(id):
    data = request.get_json()
    payment = Payment.query.get_or_404(id)
    payment.idUser = data['idUser']
    payment.idTicket = data['idTicket']
    payment.payment_date = data['payment_date']
    payment.amount = data['amount']
    db.session.commit()
    return jsonify(payment.to_dict())

@payment_bp.route('/payments/<int:id>', methods=['DELETE'])
def delete_payment(id):
    payment = Payment.query.get_or_404(id)
    db.session.delete(payment)
    db.session.commit()
    return '', 204
