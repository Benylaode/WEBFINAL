from flask import request, jsonify
from models import Concert
from . import concert_bp
from config import db


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
        imageConcert=data['imageConcert'],
        startDate=data['startDate'],  # Sesuaikan dengan nama kolom yang ada di model Concert
        endDate=data['endDate'],  # Sesuaikan dengan nama kolom yang ada di model Concert
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
    concert.imageConcert = data['imageConcert']
    concert.startDate = data['startDate']  # Sesuaikan dengan nama kolom yang ada di model Concert
    concert.endDate = data['endDate']  # Sesuaikan dengan nama kolom yang ada di model Concert
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
