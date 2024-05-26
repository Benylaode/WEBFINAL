from flask import request, jsonify
from models import User
from . import user_bp
from flask_sqlalchemy import SQLAlchemy
from config import db


@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@user_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(
        role=data['role'],
        name=data['name'],
        email=data['email'],
        noTelp=data['no_telp'],  # Sesuaikan dengan nama kolom yang ada di model User
        balance=data.get('balance', 100000)
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

@user_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.get_or_404(id)
    user.role = data['role']
    user.name = data['name']
    user.email = data['email']
    user.noTelp = data['no_telp']  # Sesuaikan dengan nama kolom yang ada di model User
    user.balance = data['balance']
    db.session.commit()
    return jsonify(user.to_dict())

@user_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return '', 204
