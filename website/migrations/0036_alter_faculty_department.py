# Generated by Django 3.2.13 on 2022-12-12 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0035_alter_hero_image_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='department',
            field=models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('ME', 'ME'), ('CE', 'CE'), ('BSH', 'BSH'), ('None', 'None'), ('administrative_staff', 'Administrative Staff'), ('supporting_staff', 'Supporting Staff'), ('supporting_staff', 'Supporting Staff'), ('security_staff', 'Security Staff')], default='None', max_length=200),
        ),
    ]