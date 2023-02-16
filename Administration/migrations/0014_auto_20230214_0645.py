# Generated by Django 3.2.13 on 2023-02-14 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0059_auto_20230207_1331'),
        ('Administration', '0013_academicadministration'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='examinationcellfaculty',
            options={},
        ),
        migrations.RemoveField(
            model_name='examinationcellfaculty',
            name='faculties',
        ),
        migrations.AddField(
            model_name='examinationcellfaculty',
            name='designation',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='examinationcellfaculty',
            name='faculty',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='website.faculty'),
        ),
    ]