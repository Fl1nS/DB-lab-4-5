from .. import PilotService
from ..general_controller import GeneralController


class PilotController(GeneralController):
    def __init__(self):
        super().__init__(PilotService())
