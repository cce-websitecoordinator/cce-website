# Generated by Django 3.2.17 on 2023-12-07 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentservices', '0018_libraryimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='WomenEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sub_title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='women_cell/events')),
            ],
        ),
    ]