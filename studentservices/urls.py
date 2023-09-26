from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from . import views

urlpatterns = [
    path('arts', views.arts_page, name='arts'),
    path('sports', views.sports_page, name='sports'),
    path('nss', views.nss_page, name='nss'),
    path('clubs', views.clubs_page, name='clubs'),
    path('iic', views.iic_page, name='iic'),
    path('womencell', views.womencell_page, name='women_cell'),
    path('techies_park', views.techies_park_page, name='techies_park'),
    path('mentoring', views.mentoring_page, name='Mentoring'),
    path('irc', views.irc_page, name='international_relations_cell'),
    path('union', views.union_page, name='union'),
    path('ieee', views.ieee_page, name='ieee'),
    path('<str:slug>', views.central_library_page, name='Central_Library'),

    

    
]

 
if settings.DEBUG:     
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
