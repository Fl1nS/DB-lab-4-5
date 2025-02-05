from .. import FlightHistoryService
from ..general_controller import GeneralController


class FlightHistoryController(GeneralController):
    def __init__(self):
        super().__init__(FlightHistoryService())

    