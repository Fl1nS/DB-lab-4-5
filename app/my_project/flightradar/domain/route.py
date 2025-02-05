from my_project.database import db
from sqlalchemy import ForeignKey

class Route(db.Model):
    __tablename__ = "route"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    origin_airport_id = db.Column(db.Integer, ForeignKey('airport.id'), nullable=False)
    destination_airport_id = db.Column(db.Integer, ForeignKey('airport.id'), nullable=False)
    distance = db.Column(db.Float)

    origin_airport = db.relationship('Airport', foreign_keys=[origin_airport_id], backref='routes_from')
    destination_airport = db.relationship('Airport', foreign_keys=[destination_airport_id], backref='routes_to')

    def to_dict(self):
        return {
            "id": self.id,
            "origin_airport_id": self.origin_airport_id,
            "destination_airport_id": self.destination_airport_id,
            "distance": self.distance,
        }
