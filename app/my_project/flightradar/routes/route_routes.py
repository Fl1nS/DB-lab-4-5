from flask import Blueprint
from ..controller.orders.route_controller import RouteController

route_bp = Blueprint("route", __name__)
route_controller = RouteController()

@route_bp.route("/route", methods=['GET'])
def get_route():
    return route_controller.get_all()

@route_bp.route("/route/<int:route_id>", methods=['GET'])
def get_route_by_id(route_id):
    return route_controller.get_by_id(route_id)

@route_bp.route("/route", methods=['POST'])
def add_route():
    return route_controller.create()

@route_bp.route("/route/<int:route_id>", methods=['PATCH'])
def update_route(route_id):
    return route_controller.update(route_id)

@route_bp.route("/route/<int:route_id>", methods=['DELETE'])
def delete_route(route_id):
    return route_controller.delete(route_id)