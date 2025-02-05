from my_project.flightradar.dao.general_dao import GeneralDAO


class RouteDAO(GeneralDAO):
    from my_project.flightradar.dao.__init__ import Route
    def __init__(self):
        super().__init__(self.Route)
