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
    path("grivence/<str:slug>/<str:page>",views.grivence_redressal_page,name="grivence_redressal"),
]

if settings.DEBUG:     
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
