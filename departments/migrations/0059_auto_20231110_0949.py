# Generated by Django 3.2.17 on 2023-11-10 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0058_alter_events_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Magazines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(default='None', upload_to='MagazineImages')),
                ('file', models.FileField(upload_to='Magazines')),
                ('department', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('ME', 'ME'), ('CE', 'CE'), ('BSH', 'BSH'), ('None', 'None')], default='None', max_length=200)),
            ],
            options={
                'verbose_name': 'Magazine',
                'verbose_name_plural': 'Magazines',
            },
        ),
        migrations.AlterModelOptions(
            name='newsletters',
            options={'verbose_name': 'NewsLetter', 'verbose_name_plural': 'NewsLetters'},
        ),
    ]
