# Generated by Django 3.2.17 on 2023-09-29 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0007_grievancebody'),
    ]

    operations = [
        migrations.AddField(
            model_name='grievancebody',
            name='classs',
            field=models.CharField(choices=[('women_harrasement', 'Womwn Harrasement')], default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='grievancebody',
            name='type',
            field=models.CharField(choices=[('student', 'Student'), ('faculty', 'Faculty'), ('staff', 'Staff'), ('other', 'Other')], default=0, max_length=30),
        ),
    ]
