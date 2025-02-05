from my_project.database import db
from sqlalchemy import ForeignKey



class Maintenance(db.Model):
    __tablename__ = "maintenance"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    aircraft_id = db.Column(db.Integer, ForeignKey('aircraft.id'), nullable=False)
    maintenance_date = db.Column(db.Date)
    details = db.Column(db.Text)

    aircraft = db.relationship('Aircraft', backref='maintenance_records')

    def to_dict(self):
        return {
            "id": self.id,
            "aircraft_id": self.aircraft_id,
            "maintenance_date": self.maintenance_date,
            "details": self.details,
        }