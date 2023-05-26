from rest_framework import serializers
from .models import Location, Machine, Cargo


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['city', 'state', 'zip_code', 'latitude', 'longitude']


class MachineSerializer(serializers.ModelSerializer):
    current_location = LocationSerializer()

    class Meta:
        model = Machine
        fields = ['number', 'current_location', 'capacity']


class CargoSerializer(serializers.ModelSerializer):
    pickup_location = LocationSerializer()
    delivery_location = LocationSerializer()

    class Meta:
        model = Cargo
        fields = ['pickup_location', 'delivery_location', 'weight', 'description']
