from flask import Blueprint
from ..controller.orders.crew_assignment_controller import CrewAssignmentController


crew_assignment_bp = Blueprint("crew_assignment", __name__)
crew_assignment_controller = CrewAssignmentController()

@crew_assignment_bp.route("/crew_assignment", methods=['GET'])
def get_crew_assignment():
    return crew_assignment_controller.get_all()

@crew_assignment_bp.route("/crew_assignment/<int:crew_assignment_id>", methods=['GET'])
def get_crew_assignment_by_id(crew_assignment_id):
    return crew_assignment_controller.get_by_id(crew_assignment_id)

@crew_assignment_bp.route("/crew_assignment", methods=['POST'])
def add_crew_assignment():
    return crew_assignment_controller.create()

@crew_assignment_bp.route("/crew_assignment/<int:crew_assignment_id>", methods=['PATCH'])
def update_crew_assignment(crew_assignment_id):
    return crew_assignment_controller.update(crew_assignment_id)

@crew_assignment_bp.route("/crew_assignment/<int:crew_assignment_id>", methods=['DELETE'])
def delete_crew_assignment(crew_assignment_id):
    return crew_assignment_controller.delete(crew_assignment_id)