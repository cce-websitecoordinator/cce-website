# Generated by Django 3.2.17 on 2023-11-28 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_qualitypolicy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualitypolicy',
            name='data',
            field=models.TextField(),
        ),
    ]
