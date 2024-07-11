# Generated by Django 3.2.23 on 2023-11-30 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutCCE', '0015_auto_20231130_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstituteCalendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='InstituteCalendar')),
            ],
            options={
                'verbose_name_plural': 'Institute Calendars',
            },
        ),
        migrations.AlterModelOptions(
            name='academiccalendar',
            options={'verbose_name_plural': 'Academic Calendars'},
        ),
    ]