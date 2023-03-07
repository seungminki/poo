from pybo import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input = db.Column(db.String(200), nullable=False)
    station = db.Column(db.String(200), nullable=True)
    direction = db.Column(db.String(200), nullable=True)
    create_date = db.Column(db.DateTime(), nullable=True)
    success = db.Column(db.Integer, nullable=True)
