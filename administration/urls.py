from django.urls import path
from administration import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("governing_body", views.governing_body, name="Governing_Body"),
    path("pta", views.pta_page, name="PTA"),
    path("office/<str:slug>", views.office_page, name="Office"),
    path('iqac', views.iqac_page, name='iqac'),
    path('anti_ragging_cell', views.anti_ragging_cell_page, name='anti_ragging_cell'),
    path('sc_st_committee_cell', views.sc_st_monitoring_cell_page, name='sc_st_committee_cell'),
    path('examination_cell', views.examination_cell_page, name='examination_cell'),
    path('organogram',views.organogram_page,name='organogram'),
    path('academic_administration',views.academic_administration_page,name='academic_administration'),
    path("grievance/", views.grivence_redressal_index_page, name="grivence_redressal_index"),
    path("grievance/<str:slug>/<str:page>", views.grivence_redressal_page, name="grivence_redressal"),
    path("test",views.test_fn,name="test"),
    path('disciplinary_committee', views.disciplinary_committee_page, name='disciplinary_committee'),
    path('internal_audit', views.internal_audit_page, name='internal_audit'),
    path('external_audit', views.external_audit_page, name='external_audit'),
    path('seed_users', views.seed_grievance_users, name='seed_users'),
    path('ugc-compliance/', views.ugc_compliance_page, name='ugc_compliance'),
    path("ugc-icc/", views.ugc_icc_page, name="UGC_ICC"),
    path('ugc_grievance/', views.ugc_grievance_page, name='ugc_grievance'),
     path('ugc_antiragging/', views.ugc_antiragging_page, name='ugc_antiragging'),
     path('ugc_eoc/', views.ugc_eoc_page, name='ugc_eoc'),
     path('sedg-cell/', views.ugc_sedg_page, name='ugc_sedg'),
     path('ugc-idp/', views.ugc_idp_page, name='ugc_idp'),
     path("ugc_fee/", views.ugc_fee_page, name="ugc_fee"),
     path('committee-accessibility/', views.committee_accessibility_page, name='committee_accessibility'),
     path('merit-admission/', views.merit_admission_page, name='merit_admission'),
     path('cpio/', views.cpio_page, name='cpio'),
     path('audited_statements/', views.audited_statements_page, name='audited_statements'),
     path('exam_circulars', views.exam_circulars_page, name='exam_circulars'),


]

if settings.DEBUG:     
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
