# Generated manually

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0071_auto_20260910_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='autonomouscurriculum',
            name='ds_s1_syllabus',
            field=models.FileField(blank=True, upload_to='Autonomous/DS', verbose_name='B.Tech (DS) S1 Syllabus'),
        ),
        migrations.AddField(
            model_name='autonomouscurriculum',
            name='ds_s2_syllabus',
            field=models.FileField(blank=True, upload_to='Autonomous/DS', verbose_name='B.Tech (DS) S2 Syllabus'),
        ),
        migrations.AddField(
            model_name='autonomouscurriculum',
            name='bs_s1_syllabus',
            field=models.FileField(blank=True, upload_to='Autonomous/BS', verbose_name='B.Tech (CSBS) S1 Syllabus'),
        ),
        migrations.AddField(
            model_name='autonomouscurriculum',
            name='bs_s2_syllabus',
            field=models.FileField(blank=True, upload_to='Autonomous/BS', verbose_name='B.Tech (CSBS) S2 Syllabus'),
        ),
    ]
