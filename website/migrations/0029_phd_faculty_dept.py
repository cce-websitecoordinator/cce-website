# Generated by Django 3.2.23 on 2023-12-09 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0028_researchscholar_dept'),
    ]

    operations = [
        migrations.AddField(
            model_name='phd_faculty',
            name='dept',
            field=models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('ME', 'ME'), ('CE', 'CE'), ('BSH', 'BSH'), ('None', 'None')], default='None', max_length=100),
            preserve_default=False,
        ),
    ]
