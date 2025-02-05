from flask import Blueprint
from my_project.flightradar.controller.orders.pilot_controller import PilotController


pilot_bp = Blueprint("pilot", __name__)
pilot_controller = PilotController()

@pilot_bp.route("/pilot", methods=['GET'])
def get_pilot():
    return pilot_controller.get_all()

@pilot_bp.route("/pilot/<int:pilot_id>", methods=['GET'])
def get_pilot_by_id(pilot_id):
    return pilot_controller.get_by_id(pilot_id)

@pilot_bp.route("/pilot", methods=['POST'])
def add_pilot():
    return pilot_controller.create()

@pilot_bp.route("/pilot/<int:pilot_id>", methods=['PATCH'])
def update_pilot(pilot_id):
    return pilot_controller.update(pilot_id)

@pilot_bp.route("/pilot/<int:pilot_id>", methods=['DELETE'])
def delete_pilot(pilot_id):
    return pilot_controller.delete(pilot_id)