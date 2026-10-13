from django.contrib import admin
from website.models import *

# Register your models here.
admin.site.register(Testimonials)
admin.site.register(HomeUpdates)
admin.site.register(HomeEvents)
admin.site.register(GalleryEventTypes)
admin.site.register(Gallery)
admin.site.register(Faculty)
admin.site.register(Role)
admin.site.register(UpcomingEvents)
admin.site.register(Alumni)
admin.site.register(AlumniCommittee)
admin.site.register(Recruiters)
admin.site.register(Hero_Image)
admin.site.register(Facilities)
admin.site.register(Achivements)
admin.site.register(FundedProjects)
admin.site.register(AcademicConsultancy)
admin.site.register(ResearchGuides)
admin.site.register(Conference)
admin.site.register(AcademicPartnerShip)
admin.site.register(FacultyStudentPublications)
admin.site.register(AdmissionGraph)
admin.site.register(AdmissionStatistics)
admin.site.register(WebsiteTeam)
admin.site.register(QualityPolicy)
admin.site.register(PHD_Faculty)
admin.site.register(ResearchScholar)
admin.site.register(AwardedPHD)
admin.site.register(NirfPDFs)
admin.site.register(Admission)


@admin.register(Patent)
class PatentAdmin(admin.ModelAdmin):
    list_display = (
        "title", "name_of_faculty", "department", "patent_type",
        "status", "academic_year", "date_of_filing",
    )
    list_filter = ("department", "academic_year", "patent_type", "status")
    search_fields = ("title", "name_of_faculty", "application_no")
    ordering = ("-academic_year", "-date_of_publishing")


class HomeAnnouncementLinkInline(admin.TabularInline):
    model = HomeAnnouncementLink
    extra = 1
    fields = ("name", "url","description")
    show_change_link = False

@admin.register(HomeAnouncement)
class HomeAnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    inlines = [HomeAnnouncementLinkInline]


#admin.site.register(HomeAnouncement)
# admin.site.register(Techletics24)






@admin.register(NBAComplianceLink)
class NBAComplianceLinkAdmin(admin.ModelAdmin):
    list_display = ("name", "department", "order", "url")
    list_editable = ("order",)
    list_filter = ("department",)
    search_fields = ("name",)
    ordering = ("department", "order", "name")


admin.site.site_header = 'CCE Web Administration'
