from django.db import migrations


def migrate_data_forward(apps, schema_editor):
    """
    Migrate existing SyllabusPDFS and AutonomousCurriculum data
    into the new unified CurriculumDocument model.
    """
    SyllabusPDFS = apps.get_model('departments', 'SyllabusPDFS')
    AutonomousCurriculum = apps.get_model('departments', 'AutonomousCurriculum')
    CurriculumDocument = apps.get_model('departments', 'CurriculumDocument')

    # 1. Migrate SyllabusPDFS → CurriculumDocument (type = 'ktu')
    for sp in SyllabusPDFS.objects.all():
        if sp.file:
            CurriculumDocument.objects.create(
                department=sp.department,
                syllabus_type='ktu',
                program='',
                semester='',
                title=sp.title,
                file=sp.file,
                order=0,
            )

    # 2. Migrate AutonomousCurriculum → CurriculumDocument (type = 'autonomous')
    # Map of (field_name, program, semester) for each file field
    DEPARTMENT_PROGRAM_MAP = {
        'CSE': 'B.Tech (CSE)',
        'ECE': 'B.Tech (ECE)',
        'EEE': 'B.Tech (EEE)',
        'ME': 'B.Tech (ME)',
        'CE': 'B.Tech (CE)',
        'BSH': 'B.Tech',
        'MCA': 'MCA',
        'MBA': 'MBA',
    }

    FIELD_MAP = [
        ('btech_s1_syllabus', 'B.Tech', 'S1'),
        ('btech_s2_syllabus', 'B.Tech', 'S2'),
        ('btech_ec_s1_syllabus', 'B.Tech (EC)', 'S1'),
        ('btech_ec_s2_syllabus', 'B.Tech (EC)', 'S2'),
        ('btech_vlsi_s1_syllabus', 'B.Tech (VLSI)', 'S1'),
        ('btech_vlsi_s2_syllabus', 'B.Tech (VLSI)', 'S2'),
        ('ds_s1_syllabus', 'B.Tech (Data Science)', 'S1'),
        ('ds_s2_syllabus', 'B.Tech (Data Science)', 'S2'),
        ('bs_s1_syllabus', 'B.Tech (CSBS)', 'S1'),
        ('bs_s2_syllabus', 'B.Tech (CSBS)', 'S2'),
        ('mtech_s1_syllabus', 'M.Tech', 'S1'),
        ('mtech_s2_syllabus', 'M.Tech', 'S2'),
    ]

    for ac in AutonomousCurriculum.objects.all():
        for field_name, program, semester in FIELD_MAP:
            file_field = getattr(ac, field_name)
            if file_field and str(file_field):
                CurriculumDocument.objects.create(
                    department=ac.department,
                    syllabus_type='autonomous',
                    program=program,
                    semester=semester,
                    title=f"{program} {semester} Curriculum",
                    file=file_field,
                    order=0,
                )


def migrate_data_backward(apps, schema_editor):
    """
    Reverse: delete all CurriculumDocument rows (the old tables still exist).
    """
    CurriculumDocument = apps.get_model('departments', 'CurriculumDocument')
    CurriculumDocument.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0074_add_curriculum_document_model'),
    ]

    operations = [
        migrations.RunPython(migrate_data_forward, migrate_data_backward),
    ]
