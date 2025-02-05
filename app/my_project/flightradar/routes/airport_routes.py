from flask import Blueprint
from ..controller.orders.airport_controller import AirportController


airport_bp = Blueprint("airport", __name__)
airport_controller = AirportController()

@airport_bp.route("/airport", methods=['GET'])
def get_airport():
    return airport_controller.get_all()

@airport_bp.route("/airport/<int:airport_id>", methods=['GET'])
def get_airport_by_id(airport_id):
    return airport_controller.get_by_id(airport_id)

@airport_bp.route("/airport", methods=['POST'])
def add_airport():
    return airport_controller.create()

@airport_bp.route("/airport/<int:airport_id>", methods=['PATCH'])
def update_airport(airport_id):
    return airport_controller.update(airport_id)

@airport_bp.route("/airport/<int:airport_id>", methods=['DELETE'])
def delete_airport(airport_id):
    return airport_controller.delete(airport_id)