# Generated by Django 3.2.17 on 2023-05-18 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0030_achivements_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achivements',
            name='year',
            field=models.CharField(choices=[('2021-2022', '2021-2022'), ('2022-2023', '2022-2023'), ('2023-2024', '2023-2024')], default=('2022-2023', '2022-2023'), max_length=200),
        ),
    ]
