from my_project.database import db

class Aircraft(db.Model):
    __tablename__ = "aircraft"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    registration_number = db.Column(db.String(20), nullable=False, unique=True)
    manufacturer = db.Column(db.String(50))
    model = db.Column(db.String(50))
    total_flight_hours = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "registration_number": self.registration_number,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "total_flight_hours": self.total_flight_hours,
        }
