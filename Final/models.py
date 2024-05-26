from config import db

class User(db.Model):
    __tablename__ = 'User'
    idUser = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(50))
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    noTelp = db.Column(db.String(15))
    balance = db.Column(db.Integer, default=100000)
    payments = db.relationship('Payment', backref='user', lazy=True)  # Lowercase 'user'
    ticket = db.relationship('Ticket', backref='user', uselist=False)  # Lowercase 'user'
    
    def to_dict(self):
        return {
            'idUser': self.idUser,
            'role': self.role,
            'name': self.name,
            'email': self.email,
            'noTelp': self.noTelp,
            'balance': self.balance,
            'payments': [payment.to_dict() for payment in self.payments],
            'ticket': self.ticket.to_dict() if self.ticket else None
        }

class Concert(db.Model):
    __tablename__ = 'Concert'
    idConcert = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    lokasi = db.Column(db.String(100))
    imageConcert = db.Column(db.String(100))
    startDate = db.Column(db.DateTime)
    endDate = db.Column(db.DateTime)
    deskripsi = db.Column(db.Text)
    idBand = db.Column(db.Integer, db.ForeignKey('Band.idBand'))  # Correct table name 'Band'
    tickets = db.relationship('Ticket', backref='concert', lazy=True)  # Lowercase 'concert'
    
    def to_dict(self):
        return {
            'idConcert': self.idConcert,
            'nama': self.nama,
            'lokasi': self.lokasi,
            'imageConcert': self.imageConcert,
            'startDate': self.startDate.isoformat() if self.startDate else None,
            'endDate': self.endDate.isoformat() if self.endDate else None,
            'deskripsi': self.deskripsi,
            'idBand': self.idBand,
            'tickets': [ticket.to_dict() for ticket in self.tickets]
        }

class Band(db.Model):
    __tablename__ = 'Band'
    idBand = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    imageBand = db.Column(db.String(100))
    concerts = db.relationship('Concert', backref='band', lazy=True)
    
    def to_dict(self):
        return {
            'idBand': self.idBand,
            'name': self.name,
            'imageBand': self.imageBand,
            'concerts': [concert.to_dict() for concert in self.concerts]
        }

class Ticket(db.Model):
    __tablename__ = 'Ticket'
    idTicket = db.Column(db.Integer, primary_key=True)
    idConcert = db.Column(db.Integer, db.ForeignKey('Concert.idConcert'))  # Correct table name 'Concert'
    ticketType = db.Column(db.String(50))
    status = db.Column(db.String(50))
    price = db.Column(db.Integer)
    idUser = db.Column(db.Integer, db.ForeignKey('User.idUser'))  # Correct table name 'User'
    payment = db.relationship('Payment', backref='ticket', uselist=False)  # Lowercase 'ticket'
    
    def to_dict(self):
        return {
            'idTicket': self.idTicket,
            'idConcert': self.idConcert,
            'ticketType': self.ticketType,
            'status': self.status,
            'price': self.price,
            'idUser': self.idUser,
            'payment': self.payment.to_dict() if self.payment else None
        }

class Payment(db.Model):
    __tablename__ = 'Payment'
    idPayment = db.Column(db.Integer, primary_key=True)
    idUser = db.Column(db.Integer, db.ForeignKey('User.idUser'))  # Correct table name 'User'
    idTicket = db.Column(db.Integer, db.ForeignKey('Ticket.idTicket'))  # Correct table name 'Ticket'
    paymentDate = db.Column(db.DateTime)
    amount = db.Column(db.Integer)
    
    def to_dict(self):
        return {
            'idPayment': self.idPayment,
            'idUser': self.idUser,
            'idTicket': self.idTicket,
            'paymentDate': self.paymentDate.isoformat() if self.paymentDate else None,
            'amount': self.amount
        }
