# Generated by Django 3.2.17 on 2023-11-27 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0013_disciplinarycommittee_internalaudit'),
    ]

    operations = [
        migrations.AddField(
            model_name='internalaudit',
            name='auditors_1',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='internalaudit',
            name='auditors_2',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='internalaudit',
            name='designation_1',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='internalaudit',
            name='designation_2',
            field=models.CharField(default=None, max_length=200),
        ),
    ]