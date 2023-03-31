from django.urls import path
from aboutCCE import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('management', views.management_page, name='Management'),
    path('directors_desk', views.directors_desk_page, name='Directors_Desk'),
    path('principals_desk', views.principals_desk_page, name='Principals_Desk'),
    path('cce_in_media', views.cce_in_media_page, name='CCE_in_Media'),
    path('committees', views.committees, name='Committees'),

]

if settings.DEBUG:     
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
