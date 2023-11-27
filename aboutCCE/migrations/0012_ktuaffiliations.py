# Generated by Django 3.2.17 on 2023-11-27 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutCCE', '0011_auto_20231110_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='KtuAffiliations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='KtuAffiliations')),
            ],
            options={
                'verbose_name_plural': 'KTU Affiliations',
            },
        ),
    ]