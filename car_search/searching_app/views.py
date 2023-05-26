from django.shortcuts import get_object_or_404
from geopy.distance import geodesic
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Machine, Cargo, Location
from .serializers import CargoSerializer, MachineSerializer, LocationSerializer
from geopy.distance import geodesic
from geopy.point import Point
from django.shortcuts import get_object_or_404
from geopy.geocoders import Nominatim
from .models import Location
from django.shortcuts import get_object_or_404
from geopy.distance import geodesic
from searching_app.management.commands.load_locations import Command as LoadLocationsCommand

 
geolocator = Nominatim(user_agent='your_app_name')

@api_view(['POST'])
def create_cargo(request):
    serializer = CargoSerializer(data=request.data)
    if serializer.is_valid():
        pickup_zip = serializer.validated_data['pickup_location']['zip_code']
        delivery_zip = serializer.validated_data['delivery_location']['zip_code']
        pickup_location = get_or_create_location_by_zip(pickup_zip)
        delivery_location = get_or_create_location_by_zip(delivery_zip)
        serializer.validated_data['pickup_location'] = pickup_location
        serializer.validated_data['delivery_location'] = delivery_location
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_or_create_location_by_zip(zip_code):
    try:
        location = Location.objects.get(zip_code=zip_code)
    except Location.DoesNotExist:
        # Загрузить данные о местоположении из файла uszips.csv
        load_command = LoadLocationsCommand()
        load_command.handle()

        try:
            location = Location.objects.get(zip_code=zip_code)
        except Location.DoesNotExist:
            raise ValueError(
                f"Location data for ZIP code {zip_code} not found.")

    return location


@api_view(['GET'])
def get_cargo_list(request):
    cargos = Cargo.objects.all()
    cargo_data = []
    for cargo in cargos:
        pickup_location = cargo.pickup_location
        delivery_location = cargo.delivery_location
        machine_count = get_nearby_machine_count(
            pickup_location, delivery_location)
        cargo_data.append({
            'pickup_location': get_location_data(pickup_location),
            'delivery_location': get_location_data(delivery_location),
            'machine_count': machine_count
        })
    return Response(cargo_data)


@api_view(['GET'])
def get_cargo(request, cargo_id):
    cargo = get_object_or_404(Cargo, pk=cargo_id)
    pickup_location = cargo.pickup_location
    delivery_location = cargo.delivery_location
    machine_distances = get_machine_distances(
        pickup_location, delivery_location)
    cargo_data = {
        'pickup_location': get_location_data(pickup_location),
        'delivery_location': get_location_data(delivery_location),
        'weight': cargo.weight,
        'description': cargo.description,
        'machine_distances': machine_distances
    }
    return Response(cargo_data)


@api_view(['PUT'])
def update_machine(request, machine_id):
    machine = get_object_or_404(Machine, pk=machine_id)
    serializer = MachineSerializer(machine, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_cargo(request, cargo_id):
    cargo = get_object_or_404(Cargo, pk=cargo_id)
    serializer = CargoSerializer(cargo, data=request.data)
    if serializer.is_valid():
        pickup_zip = serializer.validated_data['pickup_location']['zip_code']
        delivery_zip = serializer.validated_data['delivery_location']['zip_code']
        pickup_location = get_or_create_location_by_zip(pickup_zip)
        delivery_location = get_or_create_location_by_zip(delivery_zip)
        serializer.validated_data['pickup_location'] = pickup_location.id
        serializer.validated_data['delivery_location'] = delivery_location.id
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_cargo(request, cargo_id):
    cargo = get_object_or_404(Cargo, pk=cargo_id)
    cargo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


def get_nearby_machine_count(pickup_location, delivery_location):
    pickup_point = Point(pickup_location.latitude, pickup_location.longitude)
    delivery_point = Point(delivery_location.latitude,
                           delivery_location.longitude)

    # Найти все машины в радиусе 450 миль от точки pick-up или delivery
    machines = Machine.objects.all()
    nearby_machine_count = 0
    for machine in machines:
        machine_point = Point(machine.location.latitude,
                              machine.location.longitude)
        if geodesic(pickup_point, machine_point).miles <= 450 or geodesic(delivery_point, machine_point).miles <= 450:
            nearby_machine_count += 1

    return nearby_machine_count


def get_location_data(location):
    return {
        'city': location.city,
        'state': location.state,
        'zip': location.zip,
        'latitude': location.latitude,
        'longitude': location.longitude
    }


def get_machine_distances(pickup_location, delivery_location):
    pickup_point = Point(pickup_location.latitude, pickup_location.longitude)
    delivery_point = Point(delivery_location.latitude,
                           delivery_location.longitude)

    # Получить расстояния от точки pick-up и delivery до каждой машины
    machines = Machine.objects.all()
    machine_distances = []
    for machine in machines:
        machine_point = Point(machine.location.latitude,
                              machine.location.longitude)
        pickup_distance = geodesic(pickup_point, machine_point).miles
        delivery_distance = geodesic(delivery_point, machine_point).miles
        machine_distances.append({
            'machine_number': machine.machine_number,
            'pickup_distance': pickup_distance,
            'delivery_distance': delivery_distance
        })

    return machine_distances


def get_or_create_location_by_zip(zip_code):
    try:
        location = Location.objects.get(zip_code=zip_code)
    except Location.DoesNotExist:
        # Загрузить данные о местоположении из файла uszips.csv
        load_command = LoadLocationsCommand()
        load_command.handle()

        try:
            location = Location.objects.get(zip_code=zip_code)
        except Location.DoesNotExist:
            raise ValueError(
                f"Location data for ZIP code {zip_code} not found.")

    return location
