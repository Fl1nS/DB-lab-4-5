from my_project.flightradar.dao.general_dao import GeneralDAO


class AirlineDAO(GeneralDAO):
    from my_project.flightradar.dao.__init__ import Airline
    def __init__(self):
        super().__init__(self.Airline)