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
admin.site.register(NssAbout)
admin.site.register(NSSMembers)
admin.site.register(NssEvents)
admin.site.register(NssGallery)
admin.site.register(IICCertificate)
admin.site.register(IICCommitee)
admin.site.register(Clubs)
admin.site.register(ClubEvents)
admin.site.register(ClubMembers)

admin.site.register(WomenCellCommitee)
admin.site.register(Union)
admin.site.register(UnionCommitee)
admin.site.register(CentralLibrary)
admin.site.register(LibraryFaculty)
admin.site.register(DigitalLibrary)
admin.site.register(Mentoring)
admin.site.register(MentoringEvents)
admin.site.register(MentoringTeam)
admin.site.register(IEEEJournals)
admin.site.register(IEEEevents)
admin.site.register(IEEEmembers)
admin.site.register(IRCAbout)
admin.site.register(IRCEvents)
admin.site.register(IRCTeam)
admin.site.register(CCILAbout)
admin.site.register(CCILEvents)
admin.site.register(CCILTeam)




