from .. import AircraftService
from ..general_controller import GeneralController


class AircraftController(GeneralController):
    def __init__(self):
        super().__init__(AircraftService())
