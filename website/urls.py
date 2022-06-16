from django.urls import path
from website import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('academics', views.academics_page, name='academics'),
    path('departments', views.departments_page, name='departments'),
    path('campuslife', views.campuslife_page, name='campuslife'),
    path('about', views.about_page, name='about'),
    path('nirf', views.nirf_page, name='nirf'),
    path('gallery', views.gallery_page, name='gallery'),

]
