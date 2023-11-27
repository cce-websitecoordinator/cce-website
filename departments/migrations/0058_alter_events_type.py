# Generated by Django 3.2.17 on 2023-11-09 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0057_auto_20231109_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='type',
            field=models.CharField(choices=[('workshops_seminars', 'Workshops / Seminars'), ('value_added', 'Value Added'), ('iv', 'Industrial Visits'), ('competitions', 'Competetions')], default='iv', max_length=100),
        ),
    ]
