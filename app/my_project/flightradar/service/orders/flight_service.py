from .. import Flight, FlightDAO
from ..genral_service import GeneralService
from my_project.database import db


class FlightService(GeneralService):
    def __init__(self):
        super().__init__(FlightDAO(), Flight)
        self.model = Flight
    
    def delete(self, entity_id):
        entity = db.session.query(self.model).get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return True
        return False
        