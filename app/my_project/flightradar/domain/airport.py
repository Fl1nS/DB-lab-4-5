from my_project.database import db

class Airport(db.Model):
    __tablename__ = "airport"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    code = db.Column(db.String(10), nullable=False, unique=True)
    city = db.Column(db.String(50))
    country = db.Column(db.String(50))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "city": self.city,
            "country": self.country,
        }
