from config.db import app

from api.city import city_blueprint
from api.driver import driver_blueprint
from api.user import user_blueprint
from api.passenger import passenger_blueprint
from api.vehicle import vehicle_blueprint
from api.trip import trip_blueprint
from api.payment import payment_blueprint
from api.report import report_blueprint
from api.request_status import request_status_blueprint
from api.request_trip import request_trip_blueprint
from api.trip_report import trip_has_report_blueprint

# Registra los Blueprints
app.register_blueprint(city_blueprint)
app.register_blueprint(driver_blueprint)    
app.register_blueprint(user_blueprint, url_prefix = '/api')
app.register_blueprint(passenger_blueprint)
app.register_blueprint(vehicle_blueprint, url_prefix = '/api')
app.register_blueprint(trip_blueprint, url_prefix = '/api')
app.register_blueprint(payment_blueprint, url_prefix = '/api')
app.register_blueprint(report_blueprint, url_prefix = '/api')
app.register_blueprint(request_status_blueprint)
app.register_blueprint(request_trip_blueprint)
app.register_blueprint(trip_has_report_blueprint)


# Ruta principal
@app.route('/')
def hello_world():
    return 'Hola, mundo!'

# if __name__ == '__main__':
#     app.run(debug=True)
# Inicializa la extensión de la base de datos


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')