from django.contrib import admin

# Register your models here.
from django.contrib import admin
from studentservices.models import *

# Register your models here.

# future update add a single model for events and updates and add option to select the page from there

admin.site.register(Artsupdates)
admin.site.register(ArtsEvents)
admin.site.register(artsTeamStatus)
admin.site.register(ArtsGallery)
admin.site.register(SportsUpdates)
admin.site.register(SportsEvents)
admin.site.register(SportsTeamStatus)
admin.site.register(SportsGallery)
admin.site.register(NssFaculty)
admin.site.register(NssStudents)
admin.site.register(NssEvents)
admin.site.register(NssGallery)
admin.site.register(IICCertificate)
admin.site.register(IICCommitee)
admin.site.register(Clubs)
admin.site.register(WomenCellCommitee)
admin.site.register(Union)
admin.site.register(UnionCommitee)



