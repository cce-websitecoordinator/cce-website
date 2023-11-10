# Generated by Django 3.2.17 on 2023-11-07 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0047_auto_20231106_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fdps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200)),
                ('year', models.TextField(max_length=30)),
                ('duration', models.TextField(max_length=30)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'FDP',
                'verbose_name_plural': 'FDPs',
            },
        ),
        migrations.CreateModel(
            name='Mooc_courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_pdf', models.FileField(default='None', upload_to='pdfs/mooc_course')),
                ('title', models.TextField(max_length=30)),
                ('year', models.TextField(choices=[('2020-2021', '2020-2021'), ('2021-2022', '2021-2022'), ('2022-2023', '2022-2023'), ('2023-2024', '2023-2024')], max_length=30)),
                ('type', models.CharField(choices=[('student', 'student'), ('faculty', 'faculty')], default='student', max_length=200)),
                ('department', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('ME', 'ME'), ('CE', 'CE'), ('BSH', 'BSH'), ('None', 'None')], default='None', max_length=200)),
            ],
            options={
                'verbose_name': 'Mooc Course',
                'verbose_name_plural': 'Mooc Courses',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('department', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('ME', 'ME'), ('CE', 'CE'), ('BSH', 'BSH'), ('None', 'None')], default='None', max_length=200)),
                ('name_of_developers', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('ongoing', 'Ongoing'), ('completed', 'Completed')], default='None', max_length=200)),
                ('reference', models.URLField()),
            ],
            options={
                'verbose_name': 'Product developed',
                'verbose_name_plural': 'Products developed',
            },
        ),
    ]