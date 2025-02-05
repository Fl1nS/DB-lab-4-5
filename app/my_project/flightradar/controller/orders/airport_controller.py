from .. import AirportService
from ..general_controller import GeneralController


class AirportController(GeneralController):
    def __init__(self):
        super().__init__(AirportService())
