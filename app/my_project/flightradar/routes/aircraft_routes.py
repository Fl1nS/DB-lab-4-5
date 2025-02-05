from flask import Blueprint
from ..controller.orders.aircraft_controller import AircraftController

aircraft_bp = Blueprint("aircraft", __name__)
aircraft_controller = AircraftController()

@aircraft_bp.route("/aircraft", methods=['GET'])
def get_aircraft():
    return aircraft_controller.get_all()

@aircraft_bp.route("/aircraft/<int:aircraft_id>", methods=['GET'])
def get_aircraft_by_id(aircraft_id):
    return aircraft_controller.get_by_id(aircraft_id)

@aircraft_bp.route("/aircraft", methods=['POST'])
def add_aircraft():
    return aircraft_controller.create()

@aircraft_bp.route("/aircraft/<int:aircraft_id>", methods=['PATCH'])
def update_aircraft(aircraft_id):
    return aircraft_controller.update(aircraft_id)

@aircraft_bp.route("/aircraft/<int:aircraft_id>", methods=['DELETE'])
def delete_aircraft(aircraft_id):
    return aircraft_controller.delete(aircraft_id)