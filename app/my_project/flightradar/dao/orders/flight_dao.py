from my_project.flightradar.dao.general_dao import GeneralDAO


class FlightDAO(GeneralDAO):
    from my_project.flightradar.dao.__init__ import Flight
    def __init__(self):
        super().__init__(self.Flight)