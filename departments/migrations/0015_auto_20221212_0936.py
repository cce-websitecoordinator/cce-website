# Generated by Django 3.2.13 on 2022-12-12 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0014_events_poster'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poes',
            options={'verbose_name_plural': 'POE'},
        ),
        migrations.AlterModelOptions(
            name='pos',
            options={'verbose_name_plural': 'PO'},
        ),
        migrations.AlterModelOptions(
            name='psos',
            options={'verbose_name_plural': 'PSO'},
        ),
        migrations.AddField(
            model_name='dephero',
            name='type',
            field=models.CharField(choices=[('img', 'IMAGE'), ('vdo', 'VIDEO')], default='img', max_length=200),
        ),
        migrations.AddField(
            model_name='dephero',
            name='video',
            field=models.FileField(blank=True, upload_to='DEP_Heros_Videos'),
        ),
        migrations.AlterField(
            model_name='dephero',
            name='image',
            field=models.ImageField(blank=True, upload_to='DEP_Heros_Images'),
        ),
    ]