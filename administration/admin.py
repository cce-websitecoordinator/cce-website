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
    # Enable delete action in list view
    actions = ['delete_csv_uploads']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        try:
            obj.csv_file.open(mode='rb')
            with obj.csv_file as f:
                text_file = io.TextIOWrapper(f, encoding='utf-8')
                reader = csv.DictReader(text_file)
                reader.fieldnames = [h.strip() for h in reader.fieldnames]

                count = 0
                for row in reader:
                    data = {k.strip(): (v or '').strip() for k, v in row.items()}
                    email = data.get("email") or data.get("Email")
                    name = data.get("name") or data.get("Name")
                    password = data.get("password") or data.get("Password")
                    user_type = data.get("type") or data.get("Type") or "student"

                    if email and not GrivenceUser.objects.filter(email=email).exists():
                        GrivenceUser.objects.create(
                            name=name or "",
                            email=email,
                            password=make_password(password or ""),
                            type=user_type or "student"
                        )
                        count += 1
            messages.success(request, f"{count} grievance users created.")
        except Exception as e:
            messages.error(request, f"CSV import failed: {str(e)}")

    def delete_csv_uploads(self, request, queryset):
        """
        Custom action to delete selected CSV upload records and their files.
        """
        deleted_count = 0
        for obj in queryset:
            # Delete file from storage
            obj.csv_file.delete(save=False)
            # Delete the record
            obj.delete()
            deleted_count += 1
        self.message_user(request, f"Successfully deleted {deleted_count} CSV upload(s).", messages.SUCCESS)
    delete_csv_uploads.short_description = "Delete selected CSV uploads and files"

    # Ensure the delete permission is active
    def has_delete_permission(self, request, obj=None):
        return True