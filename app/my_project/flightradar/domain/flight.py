from my_project.database import db
from sqlalchemy import ForeignKey

class Flight(db.Model):
    __tablename__ = "flight"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    aircraft_id = db.Column(db.Integer, ForeignKey('aircraft.id'), nullable=False)
    route_id = db.Column(db.Integer, ForeignKey('route.id'), nullable=False)
    airline_id = db.Column(db.Integer, ForeignKey('airline.id'), nullable=False)
    departure_time = db.Column(db.DateTime)
    arrival_time = db.Column(db.DateTime)

    aircraft = db.relationship('Aircraft', backref='flights')
    route = db.relationship('Route', backref='flights')
    airline = db.relationship('Airline', backref='flights')
    crew_assignments = db.relationship('CrewAssignment', back_populates='flight')

    def to_dict(self):
        return {
            "id": self.id,
            "aircraft_id": self.aircraft_id,
            "route_id": self.route_id,
            "airline_id": self.airline_id,
            "departure_time": self.departure_time,
            "arrival_time": self.arrival_time,
        }
