from .. import CrewAssignmentService
from ..general_controller import GeneralController


class CrewAssignmentController(GeneralController):
    def __init__(self):
        super().__init__(CrewAssignmentService())
