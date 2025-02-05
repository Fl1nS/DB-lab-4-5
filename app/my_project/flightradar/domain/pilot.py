from my_project.database import db
from sqlalchemy import ForeignKey

class Pilot(db.Model):
    __tablename__ = "pilot"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    license_number = db.Column(db.String(20), nullable=False, unique=True)
    experience_years = db.Column(db.Integer)

    crew_assignments = db.relationship('CrewAssignment', back_populates='pilot')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "license_number": self.license_number,
            "experience_years": self.experience_years,
        }
