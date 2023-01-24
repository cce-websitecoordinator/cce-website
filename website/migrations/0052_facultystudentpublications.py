# Generated by Django 3.2.13 on 2023-01-14 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0051_auto_20230114_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyStudentPublications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=300, verbose_name='Name Of Author')),
                ('dep', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('ME', 'ME'), ('CE', 'CE'), ('BSH', 'BSH'), ('None', 'None')], max_length=100, verbose_name='Department of Faculty/student')),
                ('journal', models.CharField(max_length=500, verbose_name='Name Of Journal')),
                ('year', models.CharField(max_length=50, verbose_name='Year Of Publication')),
                ('details', models.FileField(upload_to='research/publications', verbose_name='Details of Publictaion')),
            ],
        ),
    ]