from my_project.flightradar.dao.general_dao import GeneralDAO


class CrewAssignmentDAO(GeneralDAO):
    from my_project.flightradar.dao.__init__ import CrewAssignment
    def __init__(self):
        super().__init__(self.CrewAssignment)