from .maintenance_routes import maintenance_bp
from .current_location_routes import current_location_bp
from .flight_routes import flight_bp
from .flight_history_routes import flight_history_bp
from .route_routes import route_bp
from .airline_routes import airline_bp
from .aircraft_routes import aircraft_bp
from .airport_routes import airport_bp
from .pilot_routes import pilot_bp
from .crew_assignment_routes import crew_assignment_bp


def register_routes(app):
    app.register_blueprint(airline_bp, url_prefix="/api")
    app.register_blueprint(aircraft_bp, url_prefix="/api")
    app.register_blueprint(airport_bp, url_prefix="/api")
    app.register_blueprint(maintenance_bp, url_prefix="/api")
    app.register_blueprint(flight_bp, url_prefix="/api")
    app.register_blueprint(flight_history_bp, url_prefix="/api")
    app.register_blueprint(crew_assignment_bp, url_prefix="/api")
    app.register_blueprint(current_location_bp, url_prefix="/api")
    app.register_blueprint(pilot_bp, url_prefix="/api")
    app.register_blueprint(route_bp, url_prefix="/api")
    