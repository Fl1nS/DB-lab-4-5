from my_project.flightradar.dao.general_dao import GeneralDAO


class PilotDAO(GeneralDAO):
    from my_project.flightradar.dao.__init__ import Pilot
    def __init__(self):
        super().__init__(self.Pilot)