from django.urls import path
from website import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('academics', views.academics_page, name='academics'),
    path('campuslife', views.campuslife_page, name='campuslife'),
    path('about', views.about_page, name='about'),
    path('nirf', views.nirf_page, name='nirf'),
    path('gallery', views.gallery_page, name='gallery'),
    path('departments/BSH', views.department_of_BSH_page, name='Department of BSH'),
    path('departments/CSE', views.department_of_CSE_page, name='Department of CSE'),
    path('departments/CE', views.department_of_CE_page, name='Department of CE'),
    path('departments/ME', views.department_of_ME_page, name='Department of ME'),
    path('departments/EEE', views.department_of_EEE_page, name='Department of EEE'),
    path('departments/ECE', views.department_of_ECE_page, name='Department of ECE'),
    path('test', views.test_page, name='Department of ECE'),

]
