from flask import Blueprint, jsonify
from my_project.flightradar.controller.orders.flight_history_controller import FlightHistoryController

flight_history_bp = Blueprint("flight_history", __name__)
flight_history_controller = FlightHistoryController()

@flight_history_bp.route("/flight_history", methods=['GET'])
def get_flight_history():
    return flight_history_controller.get_all()

@flight_history_bp.route("/flight_history/<int:flight_history_id>", methods=['GET'])
def get_flight_history_by_id(flight_history_id):
    return flight_history_controller.get_by_id(flight_history_id)

@flight_history_bp.route("/flight_history", methods=['POST'])
def add_flight_history():
    return flight_history_controller.create()

@flight_history_bp.route("/flight_history/<int:flight_history_id>", methods=['PATCH'])
def update_flight_history(flight_history_id):
    return flight_history_controller.update(flight_history_id)

@flight_history_bp.route("/flight_history/<int:flight_history_id>", methods=['DELETE'])
def delete_flight_history(flight_history_id):
    return flight_history_controller.delete(flight_history_id)
