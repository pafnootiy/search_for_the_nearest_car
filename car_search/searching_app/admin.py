from django.contrib import admin
from .models import Location, Machine, Cargo

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('city', 'state', 'zip_code', 'latitude', 'longitude')

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('get_machine_number', 'get_location')

    def get_machine_number(self, obj):
        return obj.machine_number

    get_machine_number.short_description = 'Machine Number'

    def get_location(self, obj):
        return obj.location

    get_location.short_description = 'Location'

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('pickup_location', 'delivery_location', 'weight', 'description')
