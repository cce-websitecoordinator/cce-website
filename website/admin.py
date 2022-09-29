from django.contrib import admin
from website.models import *

# Register your models here.
admin.site.register(Testimonials)
admin.site.register(HomeUpdates)
admin.site.register(HomeEvents)
admin.site.register(Gallery)
admin.site.register(UpcomingEvent)

ADMIN_REORDER = (
# 'webapp',

#### First group
{
    'app': 'website', 
    'label': 'group1',
    'models': (
        'website.models.Testimonials', 
        # 'webapp.ProductModelName_2', 
        # 'webapp.ProductModelName_3',

    )
},
)
admin.site.site_header = 'CCE Web Administration '