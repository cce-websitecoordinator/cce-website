# Generated by Django 3.2.13 on 2022-11-14 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_alumni_alumnicommittee_governingbody_upcomingevents_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruiters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='Recruiters')),
            ],
        ),
        migrations.RemoveField(
            model_name='governingbody',
            name='phone',
        ),
        migrations.AlterField(
            model_name='upcomingevents',
            name='sub_title',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='upcomingevents',
            name='title',
            field=models.CharField(max_length=80),
        ),
    ]