# Generated by Django 3.2.17 on 2023-11-09 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentservices', '0012_ccilabout_ccilevents_ccilteam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libraryfaculty',
            name='role',
            field=models.CharField(max_length=100),
        ),
    ]
