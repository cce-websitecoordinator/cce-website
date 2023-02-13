from django.contrib import admin

from placements.models import PVissionANDMission, PlacementUpdates, Testimonials

# Register your models here.
admin.site.register(PVissionANDMission)
admin.site.register(Testimonials)
admin.site.register(PlacementUpdates)