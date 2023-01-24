# Generated by Django 3.2.13 on 2023-01-03 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0017_newsletters_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletters',
            name='department',
            field=models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('ME', 'ME'), ('CE', 'CE'), ('BSH', 'BSH'), ('None', 'None')], default='None', max_length=200),
        ),
    ]