from flask import Flask
from config.db import db, ma, app

from api.city import route_cities
from api.driver import route_drivers
from api.user import route_users
from api.route import route_routes
from api.passenger import route_passengers
from api.vehicle import route_vehicles
from api.trip import route_trips
from api.payment import route_payments
from api.report import route_reports
from api.request import route_requests
from api.request_driver import route_request_drivers
from api.request_passenger import route_request_passengers
from api.request_vehicle import route_request_vehicles
from api.trip_passenger import route_trip_passengers
from api.trip_route import route_trip_routes
from api.trip_vehicle import route_trip_vehicles

app = Flask(__name__)


# Registra los Blueprints
app.register_blueprint(route_cities, url_prefix = '/api')
app.register_blueprint(route_drivers, url_prefix = '/api')
app.register_blueprint(route_users, url_prefix = '/api')
app.register_blueprint(route_passengers, url_prefix='/api')
app.register_blueprint(route_routes, url_prefix = '/api')
app.register_blueprint(route_vehicles, url_prefix = '/api')
app.register_blueprint(route_trips, url_prefix = '/api')
app.register_blueprint(route_payments, url_prefix = '/api')
app.register_blueprint(route_reports, url_prefix = '/api')
app.register_blueprint(route_request_drivers, url_prefix = '/api')
app.register_blueprint(route_request_passengers, url_prefix = '/api')
app.register_blueprint(route_request_vehicles, url_prefix = '/api')
app.register_blueprint(route_requests, url_prefix = '/api')
app.register_blueprint(route_trip_passengers, url_prefix = '/api')
app.register_blueprint(route_trip_routes, url_prefix = '/api')
app.register_blueprint(route_trip_vehicles, url_prefix = '/api')


# Ruta principal
@app.route('/')
def hello_world():
    return 'Hola, mundo!'

# if __name__ == '__main__':
#     app.run(debug=True)
# Inicializa la extensión de la base de datos


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')