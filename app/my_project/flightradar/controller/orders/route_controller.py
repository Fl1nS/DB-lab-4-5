from .. import RouteService
from ..general_controller import GeneralController


class RouteController(GeneralController):
    def __init__(self):
        super().__init__(RouteService())
