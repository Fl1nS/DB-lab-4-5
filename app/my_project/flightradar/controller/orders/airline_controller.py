from .. import AirlineService
from ..general_controller import GeneralController


class AirlineController(GeneralController):
    def __init__(self):
        super().__init__(AirlineService())

    