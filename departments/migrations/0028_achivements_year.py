# Generated by Django 3.2.17 on 2023-05-17 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0027_remove_professionalbodiesteammembers_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='achivements',
            name='year',
            field=models.CharField(choices=[('2021-22', '2021-22'), ('2022-23', '2022-23'), ('2023-24', '2023-24')], default='2023-24', max_length=200),
        ),
    ]