from flask import Blueprint
from my_project.flightradar.controller.orders.maintenance_controller import MaintenanceController


maintenance_bp = Blueprint("maintenance", __name__)
maintenance_controller = MaintenanceController()

@maintenance_bp.route("/maintenance", methods=['GET'])
def get_maintenance():
    return maintenance_controller.get_all()

@maintenance_bp.route("/maintenance/<int:maintenance_id>", methods=['GET'])
def get_maintenance_by_id(maintenance_id):
    return maintenance_controller.get_by_id(maintenance_id)

@maintenance_bp.route("/maintenance", methods=['POST'])
def add_maintenance():
    return maintenance_controller.create()

@maintenance_bp.route("/maintenance/<int:maintenance_id>", methods=['PATCH'])
def update_maintenance(maintenance_id):
    return maintenance_controller.update(maintenance_id)

@maintenance_bp.route("/maintenance/<int:maintenance_id>", methods=['DELETE'])
def delete_maintenance(maintenance_id):
    return maintenance_controller.delete(maintenance_id)