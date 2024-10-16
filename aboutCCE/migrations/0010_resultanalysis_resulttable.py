# Generated by Django 3.2.17 on 2023-09-26 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutCCE', '0009_aicteapprovals_kturegulations_mandatorydisclosure'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='results/')),
            ],
        ),
        migrations.CreateModel(
            name='ResultTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.IntegerField()),
                ('api', models.IntegerField()),
            ],
        ),
    ]
