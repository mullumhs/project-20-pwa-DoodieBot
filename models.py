from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.Text)
    cc = db.Column(db.Date, nullable=False)
    fuel_capacity = db.Column(db.Integer, nullable=False)
    engine_type = db.Column(db.Boolean, default=False)
    seat_height = db.Column(db.intiger, default=datetime.utcnow)

    def __repr__(self):
        return f'<Task {self.title}>'