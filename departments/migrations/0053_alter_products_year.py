# Generated by Django 3.2.17 on 2023-11-07 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0052_auto_20231107_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='year',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
