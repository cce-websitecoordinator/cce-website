# Generated by Django 3.2.17 on 2023-12-08 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_auto_20231208_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteteam',
            name='batch',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
