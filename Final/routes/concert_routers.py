from flask import request, jsonify
from models import Concert
from . import concert_bp
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

@concert_bp.route('/concerts', methods=['GET'])
def get_concerts():
    concerts = Concert.query.all()
    return jsonify([concert.to_dict() for concert in concerts])

@concert_bp.route('/concerts/<int:id>', methods=['GET'])
def get_concert(id):
    concert = Concert.query.get_or_404(id)
    return jsonify(concert.to_dict())

@concert_bp.route('/concerts', methods=['POST'])
def create_concert():
    data = request.get_json()
    new_concert = Concert(
        nama=data['nama'],
        lokasi=data['lokasi'],
        image_concert=data['image_concert'],
        start_date=data['start_date'],
        end_date=data['end_date'],
        deskripsi=data['deskripsi'],
        idBand=data['idBand']
    )
    db.session.add(new_concert)
    db.session.commit()
    return jsonify(new_concert.to_dict()), 201

@concert_bp.route('/concerts/<int:id>', methods=['PUT'])
def update_concert(id):
    data = request.get_json()
    concert = Concert.query.get_or_404(id)
    concert.nama = data['nama']
    concert.lokasi = data['lokasi']
    concert.image_concert = data['image_concert']
    concert.start_date = data['start_date']
    concert.end_date = data['end_date']
    concert.deskripsi = data['deskripsi']
    concert.idBand = data['idBand']
    db.session.commit()
    return jsonify(concert.to_dict())

@concert_bp.route('/concerts/<int:id>', methods=['DELETE'])
def delete_concert(id):
    concert = Concert.query.get_or_404(id)
    db.session.delete(concert)
    db.session.commit()
    return '', 204
