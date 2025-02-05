from my_project.flightradar.dao.general_dao import GeneralDAO


class AirportDAO(GeneralDAO):
    from my_project.flightradar.dao.__init__ import Airport
    def __init__(self):
        super().__init__(self.Airport)