from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class User(db.Model):
    idUser = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(50))
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    no_telp = db.Column(db.String(15))
    balance = db.Column(db.Integer, default=100000)
    payments = db.relationship('Payment', backref='user', lazy=True)
    ticket = db.relationship('Ticket', backref='user', uselist=False)

class Concert(db.Model):
    idConcert = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    lokasi = db.Column(db.String(100))
    image_concert = db.Column(db.String(100))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    deskripsi = db.Column(db.Text)
    idBand = db.Column(db.Integer, db.ForeignKey('band.idBand'))
    tickets = db.relationship('Ticket', backref='concert', lazy=True)

class Band(db.Model):
    idBand = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    image_band = db.Column(db.String(100))
    concerts = db.relationship('Concert', backref='band', lazy=True)

class Ticket(db.Model):
    idTicket = db.Column(db.Integer, primary_key=True)
    idConcert = db.Column(db.Integer, db.ForeignKey('concert.idConcert'))
    ticket_type = db.Column(db.String(50))
    status = db.Column(db.String(50))
    price = db.Column(db.Integer)
    idUser = db.Column(db.Integer, db.ForeignKey('user.idUser'))
    payment = db.relationship('Payment', backref='ticket', uselist=False)

class Payment(db.Model):
    idPayment = db.Column(db.Integer, primary_key=True)
    idUser = db.Column(db.Integer, db.ForeignKey('user.idUser'))
    idTicket = db.Column(db.Integer, db.ForeignKey('ticket.idTicket'))
    payment_date = db.Column(db.DateTime)
    amount = db.Column(db.Integer)
