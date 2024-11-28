from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    cc = db.Column(db.Integer)
    fuel_capacity = db.Column(db.Integer)
    engine_type = db.Column(db.String(100))
    seat_height = db.Column(db.Integer)

    def __repr__(self):
        return f'<Task {self.brand}>'