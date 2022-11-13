from django.contrib import admin
from website.models import *

# Register your models here.
admin.site.register(Testimonials)
admin.site.register(HomeUpdates)
admin.site.register(HomeEvents)
admin.site.register(Gallery)
admin.site.register(Faculty)
admin.site.register(Role)
admin.site.register(UpcomingEvents)
admin.site.register(CCEinMedia)
admin.site.register(CCEManagement)
admin.site.register(Alumni)
admin.site.register(AlumniCommittee)





admin.site.site_header = 'CCE Web Administration'