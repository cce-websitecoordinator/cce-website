from django.contrib import admin
from administration.models import *
from django.contrib import admin, messages
from django.contrib.auth.hashers import make_password
from .models import GrivenceUser, GrievanceUserCSVUpload
import csv
import io

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
            # Open the uploaded file in binary mode and wrap for text reading
            obj.csv_file.open(mode='rb')
            with obj.csv_file as f:
                text_file = io.TextIOWrapper(f, encoding='utf-8')
                reader = csv.DictReader(text_file)
                count = 0
                for row in reader:
                    email = row.get("email", "").strip()
                    if email and not GrivenceUser.objects.filter(email=email).exists():
                        GrivenceUser.objects.create(
                            name=row.get("name", "").strip(),
                            email=email,
                            password=make_password(row.get("password", "")),
                            type=row.get("type", "student").strip() or "student"
                        )
                        count += 1
            messages.success(request, f"{count} grievance users created.")
        except Exception as e:
            messages.error(request, f"CSV import failed: {str(e)}")

    def delete_model(self, request, obj):
        # Remove the file from storage before deleting the record
        obj.csv_file.delete(save=False)
        super().delete_model(request, obj)