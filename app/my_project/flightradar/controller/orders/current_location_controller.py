from .. import CurrentLocationService
from ..general_controller import GeneralController


class CurrentLocationController(GeneralController):
    def __init__(self):
        super().__init__(CurrentLocationService())
