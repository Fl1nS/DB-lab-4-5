from .. import Route, RouteDAO
from ..genral_service import GeneralService
from my_project.database import db


class RouteService(GeneralService):
    def __init__(self):
        super().__init__(RouteDAO(), Route)
        self.model = Route
    
    def delete(self, entity_id):
        entity = db.session.query(self.model).get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return True
        return False
        