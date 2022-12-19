from django.urls import path
from Administration import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("governing_body", views.governing_body, name="Governing_Body"),
    path('iqac', views.iqac_page, name='iqac'),
]

if settings.DEBUG:     
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
