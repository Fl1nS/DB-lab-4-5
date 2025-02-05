from flask import Blueprint
from my_project.flightradar.controller.orders.flight_controller import FlightController


flight_bp = Blueprint("flight", __name__)
flight_controller = FlightController()

@flight_bp.route("/flight", methods=['GET'])
def get_flight():
    return flight_controller.get_all()

@flight_bp.route("/flight/<int:flight_id>", methods=['GET'])
def get_flight_by_id(flight_id):
    return flight_controller.get_by_id(flight_id)

@flight_bp.route("/flight", methods=['POST'])
def add_flight():
    return flight_controller.create()

@flight_bp.route("/flight/<int:flight_id>", methods=['PATCH'])
def update_flight(flight_id):
    return flight_controller.update(flight_id)

@flight_bp.route("/flight/<int:flight_id>", methods=['DELETE'])
def delete_flight(flight_id):
    return flight_controller.delete(flight_id)