from models import User, Concert, Band, Ticket, Payment

def to_dict(model_instance):
    return {c.name: getattr(model_instance, c.name) for c in model_instance.__table__.columns}

# Add this method to each model class
User.to_dict = to_dict
Concert.to_dict = to_dict
Band.to_dict = to_dict
Ticket.to_dict = to_dict
Payment.to_dict = to_dict
