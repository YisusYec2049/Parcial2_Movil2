from config.db import db  # Reemplaza 'your_flask_app' con el nombre de tu aplicación Flask
from models.request_trip import RequestTrip  # Reemplaza 'your_models_module' con el módulo donde están tus modelos
from models.vehicle import Vehicle
def auto_assign_requests():
    # Paso 1: Obtener las solicitudes en espera
    pending_requests = RequestTrip.query.filter_by(status='en espera').all()

    for request in pending_requests:
        # Paso 2: Evaluar las características de la solicitud
        origin = request.city_origin
        destination = request.city_destination

        # Paso 3: Buscar viajes existentes que coincidan
        matching_trips = Vehicle.query.filter_by(city_origin=origin, city_destination=destination).filter(Vehicle.available_seats > 0).all()

        if matching_trips:
            # Paso 4: Asignar la solicitud a un viaje existente
            trip = matching_trips[0]  # Aquí puedes aplicar lógica para elegir el viaje más eficiente si hay múltiples coincidencias
            trip.add_request(request)  # Agregar la solicitud al viaje
            request.status = 'asignada'
            db.session.commit()
        else:
            # Paso 5: Crear un nuevo viaje si no hay coincidencias
            new_trip = Vehicle(city_origin=origin, city_destination=destination, available_seats=trip.capacity)
            new_trip.add_request(request)  # Agregar la solicitud al nuevo viaje
            request.status = 'asignada'
            db.session.add(new_trip)
            db.session.commit()

        # Puedes aplicar lógica adicional para la eficiencia logística aquí

    # Paso 6: Guardar los cambios en la base de datos
