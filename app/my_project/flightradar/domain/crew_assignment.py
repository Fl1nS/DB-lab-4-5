from my_project.database import db
from sqlalchemy import ForeignKey

class CrewAssignment(db.Model):
    __tablename__ = "crew_assignment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pilot_id = db.Column(db.Integer, ForeignKey('pilot.id'), nullable=False)
    flight_id = db.Column(db.Integer, ForeignKey('flight.id'), nullable=False)

    pilot = db.relationship('Pilot', back_populates='crew_assignments')
    flight = db.relationship('Flight', back_populates='crew_assignments')

    def to_dict(self):
        return {
            "id": self.id,
            "pilot_id": self.pilot_id,
            "flight_id": self.flight_id,
        }
