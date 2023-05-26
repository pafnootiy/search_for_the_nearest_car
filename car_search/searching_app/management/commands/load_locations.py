import csv
from django.core.management.base import BaseCommand
from searching_app.models import Location


class Command(BaseCommand):
    help = 'Loads locations from uszips.csv'

    def handle(self, *args, **options):
        with open('uszips.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row
            for row in reader:
                location = Location(
                    city=row[3],
                    state=row[5],
                    zip_code=row[0],
                    latitude=row[1],
                    longitude=row[2]
                )
                location.save()
