# Generated by Django 3.2.23 on 2023-11-30 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0016_auto_20231130_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternalAuditAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
            ],
        ),
    ]