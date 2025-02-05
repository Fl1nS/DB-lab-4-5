from my_project.flightradar.dao.general_dao import GeneralDAO


class CurrentLocationDAO(GeneralDAO):
    from my_project.flightradar.dao.__init__ import CurrentLocation
    def __init__(self):
        super().__init__(self.CurrentLocation)