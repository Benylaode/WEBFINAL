from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from werkzeug.utils import quote as url_quote


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Import and register blueprints
from routes.user_routes import user_bp
from routes.concert_routers import concert_bp
from routes.band_routers import band_bp
from routes.ticket_routes import ticket_bp
from routes.payment_routes import payment_bp

app.register_blueprint(user_bp)
app.register_blueprint(concert_bp)
app.register_blueprint(band_bp)
app.register_blueprint(ticket_bp)
app.register_blueprint(payment_bp)

if __name__ == '__main__':
    app.run(debug=True)