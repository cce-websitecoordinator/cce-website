# Generated by Django 3.2.17 on 2023-04-11 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('placements', '0005_achivements'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlacementFaculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=10)),
                ('order', models.IntegerField()),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.faculty')),
            ],
        ),
    ]
