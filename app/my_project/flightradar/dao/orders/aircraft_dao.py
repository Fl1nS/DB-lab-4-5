from my_project.flightradar.dao.general_dao import GeneralDAO


class AircraftDAO(GeneralDAO):
    from my_project.flightradar.dao.__init__ import Aircraft
    def __init__(self):
        super().__init__(self.Aircraft)