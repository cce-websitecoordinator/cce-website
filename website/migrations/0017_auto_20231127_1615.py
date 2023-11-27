# Generated by Django 3.2.17 on 2023-11-27 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_websiteteam'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='websiteteam',
            options={'verbose_name_plural': 'Website Team'},
        ),
        migrations.AddField(
            model_name='websiteteam',
            name='batch',
            field=models.CharField(choices=[('2020-2021', '2020-2021'), ('2021-2022', '2021-2022'), ('2022-2023', '2022-2023'), ('2023-2024', '2023-2024')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='websiteteam',
            name='img',
            field=models.ImageField(blank=True, upload_to='websiteteam'),
        ),
        migrations.AddField(
            model_name='websiteteam',
            name='name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='websiteteam',
            name='role',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='hero_image',
            name='page',
            field=models.CharField(choices=[('management', 'Management'), ('directors_desk', 'Directors Desk'), ('facilities', 'Facilities'), ('principals_desk', "Principal's Desk"), ('cce_in_media', 'CCE In Media'), ('governing_body', 'Governing Body'), ('organogram', 'Organogram'), ('mandatory_disclosure', 'Mandatory Disclosure'), ('antiraging_cell', 'AntiRaging Cell'), ('grivence_redressal_sysytem', 'Grivence Redressal System'), ('sc_st_monitoring_commite', 'Sc/St Monitoring Commitee'), ('iqac', 'IQAC'), ('examination_cell', 'Examination Cell'), ('pta', 'PTA'), ('office', 'office'), ('nss', 'NSS'), ('college_union', 'College Union'), ('facilities', 'Facilities'), ('pta', 'PTA'), ('None', 'None'), ('research', 'Research'), ('arts', 'Arts'), ('sports', 'Sports'), ('placements', 'Placements'), ('admissions', 'Admissions'), ('academic_research', 'Academic Research'), ('womencell', 'Women Cell'), ('clubs', 'Clubs'), ('iic', 'IIC'), ('all_committees', 'All Committees'), ('programs_offered', 'Programs Offered'), ('hr_manual', 'HR Policy'), ('vision_2035', 'Vision 2035'), ('annual_report', 'Annual Report'), ('college_handbook', 'College Handbook'), ('college_calendar', 'College Calendar'), ('audited_statements', 'Audited Statements'), ('college_magazine', 'College Magazine'), ('ktu_aicte_regulations', 'KTU AICTE Regulations'), ('approvals', 'Approvals'), ('techies_park', 'Techies Park'), ('events', 'Events'), ('study_abroad', 'Study Abroad'), ('library', 'Library'), ('disciplinary_committee', 'Disciplinary Committee'), ('internal_audit_page', 'Internal Audit'), ('external_audit_page', 'External Audit'), ('ieee', 'IEEE'), ('website_team', 'Website Team')], default='None', max_length=200),
        ),
    ]
