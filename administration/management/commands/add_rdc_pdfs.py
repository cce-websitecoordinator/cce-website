"""
Management command to add RDC Constitution and RDC Minutes PDFs
as MeetingMinutes entries with category 'rnd' (Research & Development).
"""
import datetime
from pathlib import Path

from django.core.files import File
from django.core.management.base import BaseCommand

from administration.models import MeetingMinutes


class Command(BaseCommand):
    help = "Add RDC Constitution and RDC Minutes PDFs to the Research & Development page"

    def handle(self, *args, **options):
        pdfs = [
            {
                "title": "RDC Constitution",
                "path": Path("/home/abhin-krishna-m-p/Downloads/RDC Constitution .pdf"),
            },
            {
                "title": "RDC Minutes",
                "path": Path("/home/abhin-krishna-m-p/Downloads/RDC Minutes .pdf"),
            },
        ]

        for pdf_info in pdfs:
            path = pdf_info["path"]
            title = pdf_info["title"]

            if not path.exists():
                self.stderr.write(self.style.ERROR(f"File not found: {path}"))
                continue

            # Check if a record with this title and category already exists
            if MeetingMinutes.objects.filter(title=title, category="rnd").exists():
                self.stdout.write(self.style.WARNING(f"Already exists: {title} — skipping."))
                continue

            with open(path, "rb") as f:
                django_file = File(f, name=path.name)
                entry = MeetingMinutes.objects.create(
                    title=title,
                    file=django_file,
                    date=datetime.date.today(),
                    category="rnd",
                )

            self.stdout.write(self.style.SUCCESS(f"Created: {entry} (file URL: {entry.file.url})"))

        self.stdout.write(self.style.SUCCESS("Done."))
