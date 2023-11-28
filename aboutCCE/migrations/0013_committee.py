# Generated by Django 3.2.17 on 2023-11-27 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutCCE', '0012_ktuaffiliations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(choices=[('2020-2021', '2020-2021'), ('2021-2022', '2021-2022'), ('2022-2023', '2022-2023'), ('2023-2024', '2023-2024')], default=('2022-2023', '2022-2023'), max_length=200)),
                ('pdf', models.FileField(upload_to='Committee')),
            ],
            options={
                'verbose_name': 'Committee',
                'verbose_name_plural': 'Committees',
            },
        ),
    ]