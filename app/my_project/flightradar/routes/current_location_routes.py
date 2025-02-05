from flask import Blueprint
from ..controller.orders.current_location_controller import CurrentLocationController

current_location_bp = Blueprint("current_location", __name__)
current_location_controller = CurrentLocationController()

@current_location_bp.route("/current_location", methods=['GET'])
def get_current_location():
    return current_location_controller.get_all()

@current_location_bp.route("/current_location/<int:current_location_id>", methods=['GET'])
def get_current_location_by_id(current_location_id):
    return current_location_controller.get_by_id(current_location_id)

@current_location_bp.route("/current_location", methods=['POST'])
def add_current_location():
    return current_location_controller.create()

@current_location_bp.route("/current_location/<int:current_location_id>", methods=['PATCH'])
def update_current_location(current_location_id):
    return current_location_controller.update(current_location_id)

@current_location_bp.route("/current_location/<int:current_location_id>", methods=['DELETE'])
def delete_current_location(current_location_id):
    return current_location_controller.delete(current_location_id)