from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from . import views

urlpatterns = [
    path('professionalbodies/<str:slug>', views.ProfessionalBodie, name='dep_professionalbodies'),
    path('associations/<str:slug>', views.Association, name='dep_associations'),
    path('research/<str:department>/<str:slug>', views.research_page, name='dep_research'),
    path('<str:department>/<str:route>', views.Department, name='Department'),
]
if settings.DEBUG:     
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
