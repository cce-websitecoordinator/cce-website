# Generated by Django 3.2.17 on 2023-08-18 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_auto_20230503_0627'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrivenceUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='academicadministrationdirector',
            name='director_reserch_role',
            field=models.CharField(choices=[('principal', 'Principal'), ('vice_principal', 'Vice Principal'), ('aca_dir', 'Academic Director'), ('res_dir', 'Research Director')], default='principal', max_length=200),
        ),
    ]
