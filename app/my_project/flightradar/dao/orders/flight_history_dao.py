from my_project.flightradar.dao.general_dao import GeneralDAO


class FlightHistoryDAO(GeneralDAO):
    from my_project.flightradar.dao.__init__ import FlightHistory
    def __init__(self):
        super().__init__(self.FlightHistory)
