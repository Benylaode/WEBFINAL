from flask import request, jsonify
from models import Band
from . import band_bp
from werkzeug.utils import quote as url_quote
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

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
        image_band=data['image_band']
    )
    db.session.add(new_band)
    db.session.commit()
    return jsonify(new_band.to_dict()), 201

@band_bp.route('/bands/<int:id>', methods=['PUT'])
def update_band(id):
    data = request.get_json()
    band = Band.query.get_or_404(id)
    band.name = data['name']
    band.image_band = data['image_band']
    db.session.commit()
    return jsonify(band.to_dict())

@band_bp.route('/bands/<int:id>', methods=['DELETE'])
def delete_band(id):
    band = Band.query.get_or_404(id)
    db.session.delete(band)
    db.session.commit()
    return '', 204
