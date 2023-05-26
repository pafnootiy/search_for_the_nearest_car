from django.db import models
from geopy.geocoders import Nominatim
from geopy.distance import distance


class Location(models.Model):
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def get_coordinates(self):
        return self.latitude, self.longitude


class Machine(models.Model):
    number = models.CharField(max_length=5, unique=True)
    current_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    capacity = models.IntegerField()


class Cargo(models.Model):
    pickup_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='pickups')
    delivery_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='deliveries')
    weight = models.IntegerField()
    description = models.TextField()

    def get_distance_to_nearest_machines(self):
        pickup_coordinates = self.pickup_location.get_coordinates()
        delivery_coordinates = self.delivery_location.get_coordinates()
        distance_miles = calculate_distance(pickup_coordinates, delivery_coordinates)
        return distance_miles

    def get_all_machine_distances(self):
        machines = Machine.objects.all()
        distances = []
        for machine in machines:
            machine_coordinates = machine.current_location.get_coordinates()
            distance_miles = calculate_distance(machine_coordinates, self.pickup_location.get_coordinates())
            distances.append((machine.number, distance_miles))
        return distances


def calculate_distance(point1, point2):
    return distance(point1, point2).miles
