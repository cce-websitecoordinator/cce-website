# Generated by Django 4.0.4 on 2022-11-09 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_alter_testimonials_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memorandum', models.FileField(upload_to='AlumniMemorandum')),
                ('by_laws', models.FileField(upload_to='AlumniByLaws')),
            ],
        ),
        migrations.CreateModel(
            name='AlumniCommittee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GoverningBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('role', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UpcomingEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='UpcomingEvents/1.jpg', upload_to='UpcomingEvents')),
                ('title', models.CharField(max_length=30)),
                ('sub_title', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='image',
            field=models.ImageField(upload_to='testimonials'),
        ),
    ]