from django.db import migrations


def migrate_audited_statements(apps, schema_editor):
    AuditedStatements = apps.get_model('aboutCCE', 'AuditedStatements')

    # Mapping of known statements to ensure both institutions have correct records and files
    cce_items = [
        {"name": "Audited Statement 2019-20", "file": "AuditedStatements/Christ_Educational__Charitable_Trust.pdf", "order": 1},
        {"name": "Audited Statement 2020-21", "file": "AuditedStatements/CECT_20-21_KByqZ9U.pdf", "order": 2},
        {"name": "Audited Statement 2021-22", "file": "AuditedStatements/CECT_21-22_Axmglxt.pdf", "order": 3},
        {"name": "Audited Statement 2022-23", "file": "AuditedStatements/Christ_Educational_and_Charitable_Trust.pdf", "order": 4},
        {"name": "Audited Statement 2023-24", "file": "AuditedStatements/Audited__2023-24.pdf", "order": 5},
        {"name": "Audited Statement 2024-25", "file": "AuditedStatements/Audited__2024-25.pdf", "order": 6},
        {"name": "Audited Statement 2025-26", "file": "AuditedStatements/Audited__2025-26.pdf", "order": 7},
    ]

    ccil_items = [
        {"name": "Audited FS 23-24", "file": "AuditedStatements/Audited_FS_23-24.pdf", "order": 1},
        {"name": "Audited FS 24-25", "file": "AuditedStatements/Audited_FS_24-25.pdf", "order": 2},
        {"name": "Audited FS 25-26", "file": "AuditedStatements/Audited_FS_25-26.pdf", "order": 3},
    ]

    # First, update existing records if they exist
    for item in AuditedStatements.objects.all():
        name_upper = item.name.upper()
        if "FS" in name_upper or "CHRIST CENTRE" in name_upper:
            item.institution = "Christ Centre for Innovation"
            if "23-24" in item.name:
                item.file = "AuditedStatements/Audited_FS_23-24.pdf"
                item.order = 1
            elif "24-25" in item.name:
                item.file = "AuditedStatements/Audited_FS_24-25.pdf"
                item.order = 2
            elif "25-26" in item.name:
                item.file = "AuditedStatements/Audited_FS_25-26.pdf"
                item.order = 3
            item.save()
        else:
            item.institution = "Christ College of Engineering"
            if "2019-20" in item.name:
                item.order = 1
            elif "2020-21" in item.name:
                item.order = 2
            elif "2021-22" in item.name:
                item.order = 3
            elif "2022-23" in item.name:
                item.order = 4
            elif "2023-24" in item.name:
                item.order = 5
            elif "2024-25" in item.name:
                item.order = 6
            elif "2025-26" in item.name:
                item.order = 7
            item.save()

    # If any records are missing (e.g. fresh environment or CCIL not yet added), create them
    for entry in cce_items:
        if not AuditedStatements.objects.filter(name=entry["name"], institution="Christ College of Engineering").exists():
            AuditedStatements.objects.create(
                name=entry["name"],
                file=entry["file"],
                institution="Christ College of Engineering",
                order=entry["order"]
            )

    for entry in ccil_items:
        if not AuditedStatements.objects.filter(name=entry["name"], institution="Christ Centre for Innovation").exists():
            AuditedStatements.objects.create(
                name=entry["name"],
                file=entry["file"],
                institution="Christ Centre for Innovation",
                order=entry["order"]
            )


def rollback(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('aboutCCE', '0020_auto_20261017_0406'),
    ]

    operations = [
        migrations.RunPython(migrate_audited_statements, rollback),
    ]
