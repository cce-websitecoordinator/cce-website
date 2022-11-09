# Generated by Django 3.2.13 on 2022-11-09 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0022_gallery_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='CCEinMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='CCEinMedia')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('short_description', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CCEManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='CCEManagement')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]