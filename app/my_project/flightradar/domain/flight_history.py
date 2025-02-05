from my_project.database import db
from sqlalchemy import ForeignKey

class FlightHistory(db.Model):
    __tablename__ = "flight_history"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flight_id = db.Column(db.Integer, ForeignKey('flight.id'), nullable=False)
    status = db.Column(db.String(50))

    flight = db.relationship('Flight', backref='history')

    def to_dict(self):
        return {
            "id": self.id,
            "flight_id": self.flight_id,
            "status": self.status,
        }
