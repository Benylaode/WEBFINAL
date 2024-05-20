from flask import request, jsonify
from models import Ticket
from . import ticket_bp
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

@ticket_bp.route('/ticket', methods=['GET'])
def get_tickets():
    ticket = Ticket.query.all()
    return jsonify([Ticket.to_dict() for tickets in ticket])

@ticket_bp.route('/ticket/<int:id>', methods=['GET'])
def get_ticket(id):
   ticket = Ticket.query.get_or_404(id)
   return jsonify(ticket.to_dict())

@ticket_bp.route('/ticket', methods=['POST'])
def create_ticket():
    data = request.get_json()
    new_ticket = Ticket(
        idConcert=data['IdConcert'],
        ticketType=data['TicketType'],
        status=data['Status'],
        price=data['Price'],
        idUser = data['IdUser'],
        payment = data['Payment']
    )
    db.session.add(new_ticket)
    db.session.commit()
    return jsonify(new_ticket.to_dict()), 201

@ticket_bp.route('/ticket/<int:id>', methods=['PUT'])
def update_ticket(id):
    data = request.get_json()
    ticket= Ticket.query.get_or_404(id)
    ticket.idConcert = data['IdConcert']
    ticket.ticket_type = data['TicketType']
    ticket.status = data['Status']
    ticket.price = data['Price']
    ticket.balance = data['balance']
    ticket.idUser = data['IdUser']
    ticket.payment = data['Payment']
    db.session.commit()
    return jsonify(ticket.to_dict())

@ticket_bp.route('/ticket/<int:id>', methods=['DELETE'])
def delete_ticket(id):
    ticket= Ticket.query.get_or_404(id)
    db.session.delete(ticket)
    db.session.commit()
    return '', 204
