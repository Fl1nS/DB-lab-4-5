from .. import FlightService
from ..general_controller import GeneralController


class FlightController(GeneralController):
    def __init__(self):
        super().__init__(FlightService())
