# Generated by Django 3.2.23 on 2023-12-07 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0062_auto_20231129_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facultypdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(choices=[('2020-2021', '2020-2021'), ('2021-2022', '2021-2022'), ('2022-2023', '2022-2023'), ('2023-2024', '2023-2024')], default=('2022-2023', '2022-2023'), max_length=200)),
                ('pdf', models.FileField(upload_to='')),
                ('department', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('ME', 'ME'), ('CE', 'CE'), ('BSH', 'BSH'), ('None', 'None')], default='None', max_length=200)),
            ],
            options={
                'verbose_name': 'Faculty PDF',
                'verbose_name_plural': 'Faculty PDFs',
            },
        ),
    ]
