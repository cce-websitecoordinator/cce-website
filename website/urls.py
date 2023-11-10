from django.urls import path
from website import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page, name='home'),
    path('admission', views.admission_page, name='admission'),
    path('admission_stats', views.admission_stat_page, name='admission_statistics'),
    path('nirf', views.nirf_page, name='nirf'),
    path('nba', views.nba_page, name='nba'),
    path('alumini', views.alumini_page, name='alumini'),
    path('facilities', views.facilities_page, name='facilities'),
    path('gallery', views.gallery_page, name='gallery'),
    path('research/<str:slug>', views.research_page, name='home_research'),
    path('test', views.test_page, name='test'),
    path('events', views.events_page, name='events'),
    path('library/<str:slug>', views.library, name='library'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
