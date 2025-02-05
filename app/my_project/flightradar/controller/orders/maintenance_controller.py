from .. import MaintenanceService
from ..general_controller import GeneralController


class MaintenanceController(GeneralController):
    def __init__(self):
        super().__init__(MaintenanceService())
