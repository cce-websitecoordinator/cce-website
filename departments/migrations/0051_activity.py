# Generated by Django 3.2.17 on 2023-11-07 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0050_dabtable_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_pdfs', models.FileField(default='None', upload_to='pdfs/mooc_course')),
            ],
            options={
                'verbose_name': 'Activity Point',
                'verbose_name_plural': 'Activity Points',
            },
        ),
    ]