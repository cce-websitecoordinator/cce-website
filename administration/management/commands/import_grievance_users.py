import csv
from django.core.management.base import BaseCommand
from administrator.models import GrivenceUser

class Command(BaseCommand):
    help = "Import grievance users from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        with open(options['csv_file'], newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            created = 0
            for row in reader:
                if not GrivenceUser.objects.filter(email=row['email']).exists():
                    GrivenceUser.objects.create(
                        name=row['name'],
                        email=row['email'],
                        password=row['password'],
                        type=row.get('type', 'student')
                    )
                    created += 1
        self.stdout.write(self.style.SUCCESS(f"{created} users imported"))
