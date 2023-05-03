from django.urls import path
from aboutCCE import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('management', views.management_page, name='Management'),
    path('directors_desk', views.directors_desk_page, name='Directors_Desk'),
    path('principals_desk', views.principals_desk_page, name='Principals_Desk'),
    path('cce_in_media', views.cce_in_media_page, name='CCE_in_Media'),
    path('committees', views.committees_page, name='Committees'),
    path('programs', views.programs_page, name='Programs'),
    path('hr_manual', views.hr_manual_page, name='HR_Manual'),
    path('vision_2035', views.vision_2035_page, name='Vision_2035'),
    path('annual_report', views.annual_report_page, name='Annual_Report'),
    path('college_calendar', views.college_calendar_page, name='College_Calendar'),
    path('college_handbook', views.college_handbook_page, name='College_Handbook'),
    path('mandatory_disclosure',views.mandatory_disclosure_page,name='Mandatory_Disclosure'),
    path('ktu_aicte_regulations',views.ktu_regulations_page,name='Ktu_Regulations'),
    path('approvals',views.aicte_approvals_page,name='Aicte_Approvals'),
    path('audited_statements', views.audited_statements_page, name='Audited_Statements'),
    path('college_magazine', views.college_magazine_page, name='College_Magazine'),
]

if settings.DEBUG:     
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
