from django.urls import path
from website import views

urlpatterns = [
    path('', views.home_page, name='home'),

]
