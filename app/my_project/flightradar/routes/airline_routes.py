from flask import Blueprint
from ..controller.orders.airline_controller import AirlineController

airline_bp = Blueprint("airline", __name__)
airline_controller = AirlineController()

@airline_bp.route("/airline", methods=['GET'])
def get_airline():
    return airline_controller.get_all()

@airline_bp.route("/airline/<int:airline_id>", methods=['GET'])
def get_airline_by_id(airline_id):
    return airline_controller.get_by_id(airline_id)

@airline_bp.route("/airline", methods=['POST'])
def add_airline():
    return airline_controller.create()

@airline_bp.route("/airline/<int:airline_id>", methods=['PATCH'])
def update_airline(airline_id):
    return airline_controller.update(airline_id)

@airline_bp.route("/airline/<int:airline_id>", methods=['DELETE'])
def delete_airline(airline_id):
    return airline_controller.delete(airline_id)