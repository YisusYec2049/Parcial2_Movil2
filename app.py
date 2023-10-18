from flask import Flask
from config.db import db, ma, app

from api.city import city_blueprint
from api.driver import driver_blueprint
from api.user import route_users
from api.route import route_routes
from api.passenger import passenger_blueprint
from api.vehicle import route_vehicles
from api.trip import route_trips
from api.payment import payment_blueprint
from api.report import report_blueprint
from api.request import route_requests
from api.request_status import request_status_blueprint
from api.request_vehicle import route_request_vehicles
from api.trip_passenger import route_trip_passengers
from api.trip_route import route_trip_routes
from api.request_trip import request_trip_blueprint

# Registra los Blueprints
app.register_blueprint(city_blueprint)
app.register_blueprint(driver_blueprint)
app.register_blueprint(route_users, url_prefix = '/api')
app.register_blueprint(passenger_blueprint)
app.register_blueprint(route_routes, url_prefix = '/api')
app.register_blueprint(route_vehicles, url_prefix = '/api')
app.register_blueprint(route_trips, url_prefix = '/api')
app.register_blueprint(payment_blueprint, url_prefix = '/api')
app.register_blueprint(report_blueprint, url_prefix = '/api')
app.register_blueprint(request_status_blueprint)
app.register_blueprint(request_trip_blueprint)

app.register_blueprint(route_request_vehicles, url_prefix = '/api')
app.register_blueprint(route_requests, url_prefix = '/api')
app.register_blueprint(route_trip_passengers, url_prefix = '/api')
app.register_blueprint(route_trip_routes, url_prefix = '/api')


# Ruta principal
@app.route('/')
def hello_world():
    return 'Hola, mundo!'

# if __name__ == '__main__':
#     app.run(debug=True)
# Inicializa la extensión de la base de datos


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')