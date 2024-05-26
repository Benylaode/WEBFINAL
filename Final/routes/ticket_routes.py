from flask import request, jsonify
from models import Ticket
from . import ticket_bp
from config import db


@ticket_bp.route('/tickets', methods=['GET'])
def get_tickets():
    tickets = Ticket.query.all()
    return jsonify([ticket.to_dict() for ticket in tickets])

@ticket_bp.route('/tickets/<int:id>', methods=['GET'])
def get_ticket(id):
    ticket = Ticket.query.get_or_404(id)
    return jsonify(ticket.to_dict())

@ticket_bp.route('/tickets', methods=['POST'])
def create_ticket():
    data = request.get_json()
    new_ticket = Ticket(
        idConcert=data['idConcert'],  
        ticketType=data['ticketType'],  
        status=data['status'],  
        price=data['price'],  
        idUser=data['idUser'],  
        payment=data['payment']  
    )
    db.session.add(new_ticket)
    db.session.commit()
    return jsonify(new_ticket.to_dict()), 201

@ticket_bp.route('/tickets/<int:id>', methods=['PUT'])
def update_ticket(id):
    data = request.get_json()
    ticket = Ticket.query.get_or_404(id)
    ticket.idConcert = data['idConcert']  
    ticket.ticketType = data['ticketType']  
    ticket.status = data['status']  
    ticket.price = data['price']  
    ticket.idUser = data['idUser']  
    ticket.payment = data['payment']  
    db.session.commit()
    return jsonify(ticket.to_dict())

@ticket_bp.route('/tickets/<int:id>', methods=['DELETE'])
def delete_ticket(id):
    ticket = Ticket.query.get_or_404(id)
    db.session.delete(ticket)
    db.session.commit()
    return '', 204
