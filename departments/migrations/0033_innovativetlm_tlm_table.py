# Generated by Django 3.2.17 on 2023-05-18 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0032_alter_achivements_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='InnovativeTLM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField()),
                ('tlm_methods', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('department', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('ME', 'ME'), ('CE', 'CE'), ('BSH', 'BSH'), ('None', 'None')], default='None', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TLM_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.TextField()),
                ('activity', models.TextField()),
                ('tlm_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.innovativetlm')),
            ],
        ),
    ]