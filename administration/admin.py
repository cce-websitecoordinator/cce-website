from django.contrib import admin
from administration.models import *
from django.contrib import admin, messages
from django.contrib.auth.hashers import make_password
from .models import GrivenceUser, GrievanceUserCSVUpload
import csv

# Register your models here.
admin.site.register(GoverningBodyMembers)
admin.site.register(GoverningBodyOrderFile)
admin.site.register(IQACExecutiveCommitee)
admin.site.register(IQACFormationNotice)
admin.site.register(PTAExecutiveCommitee)
admin.site.register(PTAMembers)
admin.site.register(AntiRaggingCommittee)
admin.site.register(SCSTMonitoringCommittee)
admin.site.register(ExaminationCellFaculty)
admin.site.register(ExaminationCellRules)
admin.site.register(AcademicAdministrationDirector)
admin.site.register(AcademicAdministractors)
admin.site.register(GrivenceCommitee)
admin.site.register(IQACMeetingMinutes)
admin.site.register(GrievanceBody)
admin.site.register(GrivenceUser)
admin.site.register(DisciplinaryCommittee)
admin.site.register(InternalAudit)
admin.site.register(InternalAuditAbout)
admin.site.register(ExternalAudit)

@admin.register(GrievanceUserCSVUpload)
class GrievanceUserCSVUploadAdmin(admin.ModelAdmin):
    list_display = ("csv_file", "uploaded_at")

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        try:
            # Use storage backend's file handle instead of absolute path
            obj.csv_file.open(mode='r', encoding='utf-8')
            reader = csv.DictReader(obj.csv_file)
            count = 0
            for row in reader:
                if not GrivenceUser.objects.filter(email=row.get("email")).exists():
                    GrivenceUser.objects.create(
                        name=row.get("name", "").strip(),
                        email=row.get("email", "").strip(),
                        password=make_password(row.get("password", "")),
                        type=row.get("type", "student").strip() or "student"
                    )
                    count += 1
            messages.success(request, f"{count} grievance users created.")
        except Exception as e:
            messages.error(request, f"CSV import failed: {str(e)}")
        finally:
            obj.csv_file.close()
