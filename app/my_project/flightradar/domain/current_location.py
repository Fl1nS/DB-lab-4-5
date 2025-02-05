from my_project.database import db
from sqlalchemy import ForeignKey

class CurrentLocation(db.Model):
    __tablename__ = "current_location"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    aircraft_id = db.Column(db.Integer, ForeignKey('aircraft.id'), nullable=False, unique=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    altitude = db.Column(db.Integer)
    speed = db.Column(db.Float)
    last_updated = db.Column(db.DateTime)

    aircraft = db.relationship('Aircraft', backref='current_location', uselist=False)

    def to_dict(self):
        return {
            "id": self.id,
            "aircraft_id": self.aircraft_id,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "altitude": self.altitude,
            "speed": self.speed,
            "last_updated": self.last_updated,
        }
