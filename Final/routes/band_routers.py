from flask import request, jsonify
from models import Band
from . import band_bp
from config import db


@band_bp.route('/bands', methods=['GET'])
def get_bands():
    bands = Band.query.all()
    return jsonify([band.to_dict() for band in bands])

@band_bp.route('/bands/<int:id>', methods=['GET'])
def get_band(id):
    band = Band.query.get_or_404(id)
    return jsonify(band.to_dict())

@band_bp.route('/bands', methods=['POST'])
def create_band():
    data = request.get_json()
    new_band = Band(
        name=data['name'],
        imageBand=data['imageBand']  # Sesuaikan dengan nama kolom yang ada di model Band
    )
    db.session.add(new_band)
    db.session.commit()
    return jsonify(new_band.to_dict()), 201

@band_bp.route('/bands/<int:id>', methods=['PUT'])
def update_band(id):
    data = request.get_json()
    band = Band.query.get_or_404(id)
    band.name = data['name']
    band.imageBand = data['imageBand']  # Sesuaikan dengan nama kolom yang ada di model Band
    db.session.commit()
    return jsonify(band.to_dict())

@band_bp.route('/bands/<int:id>', methods=['DELETE'])
def delete_band(id):
    band = Band.query.get_or_404(id)
    db.session.delete(band)
    db.session.commit()
    return '', 204
