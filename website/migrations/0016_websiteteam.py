# Generated by Django 3.2.17 on 2023-11-27 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_alter_hero_image_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]