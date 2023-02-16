# Description: This file contains the URL patterns for the CCE website.
from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('department/', include('departments.urls')),
    path('aboutCCE/', include('aboutCCE.urls')),
    path('administration/', include('administration.urls')),
    path('student_services/', include('studentservices.urls')),
    path('placements/', include('placements.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]

handler500 = "website.views.server_error_page"
handler404 = "website.views.not_found_error_page"

if settings.DEBUG:     
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

