from django import forms
from django.db import models

from website.models import Faculty

import datetime


grievance_type = (
    ("student", "Student"),
    ("faculty", "Faculty"),
    ("staff", "Staff"),
    ("parents", "Parents"),
    ("other", "Other"),
)

grievance_category = (
    ("academic", "Academic Grievances"),
    ("exam", "Exam Grievances"),
    ("administrative", "Administrative Grievances"),
    ("faculty_staff", "Faculty and Staff-related Issues"),
    ("infrastructure_facilities", "Infrastructure and Facilities"),
    ("health_safety", "Health and Safety"),
    ("financial", "Financial Matters"),
    ("discipline", "Code of Conduct and Discipline"),
    ("research", "Research and Project-related Grievances"),
    ("harrasement", "Harassment and Discrimination"),
    ("interpersonal", "Interpersonal and Social Concerns"),
    ("scst", "SC/ST Related Grievances"),
    ("other", "Other Grievances"),
)

DEPARTMENTS = (
    ("CSE", "CSE"),
    ("ECE", "ECE"),
    ("EEE", "EEE"),
    ("ME", "ME"),
    ("CE", "CE"),
    ("DS", "DS"),
    ("BSH", "BSH"),
    ("None", "None"),
)

ACADEMIC_YEARS = [
    (f"{r}-{r + 1}", f"{r}-{r + 1}")
    for r in range(2020, datetime.date.today().year + 1)
]


# Create your models here.
class GoverningBodyMembers(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Governing Body"


class GoverningBodyOrderFile(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="GoverningBodyOrderFile")

    class Meta:
        verbose_name = "GoverningBodyOrderFile"
        verbose_name_plural = "GoverningBodyOrderFiles"

    def __str__(self):
        return self.name


class IQACExecutiveCommitee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    priority = models.IntegerField()

    def __str__(self):
        return f"{self.priority} {self.name}"

    class Meta:
        verbose_name_plural = "IQAC Executive Commitees"


class IQACFormationNotice(models.Model):
    notice = models.FileField(upload_to="IQACFormationNotice")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.notice.name

    class Meta:
        verbose_name_plural = "IQAC Formation Notices"


class PTAExecutiveCommitee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    year = models.CharField(choices=ACADEMIC_YEARS, max_length=20, default="none")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "PTA Executive Commitee"


class PTAMembers(models.Model):
    name = models.CharField(max_length=100)
    tudent_name = models.CharField(max_length=100)
    year = models.CharField(choices=ACADEMIC_YEARS, max_length=20, default="none")
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "PTA  Members"


class ProfileHighlights(models.Model):
    qulaification = models.CharField(max_length=500)
    choices = (("principal", "Principal"), ("exedir", "Executive Director"))
    designation = models.CharField(max_length=100, choices=choices)

    def __str__(self):
        return self.choices[0]


class AntiRaggingCommittee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Anti Ragging Committee"


class SCSTMonitoringCommittee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Sc/St Monitoing  Committee"


class ExaminationCellFaculty(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=2)
    designation = models.CharField(max_length=200, default=None)

    def __str__(self) -> str:
        return f"{self.faculty.full_name}  {self.designation}"


class ExaminationCellRules(models.Model):
    file = models.FileField(upload_to="ExamRulesAndRegulations")

    def __str__(self) -> str:
        return self.file.name


class AcademicAdministrationDirector(models.Model):
    director_reserch_img = models.ImageField(
        upload_to="academicAdministraction/faculty"
    )
    director_reserch_name = models.CharField(max_length=200)
    choices = (
        ("principal", "Principal"),
        ("vice_principal", "Vice Principal"),
        ("aca_dir", "Academic Director"),
        ("res_dir", "Research Director"),
        ("out_dir", "OutReach Director"),
    )
    director_reserch_role = models.CharField(
        max_length=200, choices=choices, default="principal"
    )

    def __str__(self):
        return f"{self.director_reserch_name} {self.director_reserch_role}"


class AcademicAdministractors(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=2)
    order = models.IntegerField()

    def __str__(self) -> str:
        return self.faculty.full_name


class GrivenceCommitee(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class IQACMeetingMinutes(models.Model):
    name = models.CharField(max_length=10)
    file = models.FileField(upload_to="IQACMeetingMinutes")
    year = models.CharField(max_length=10, choices=ACADEMIC_YEARS, default="2020-21")

    def __str__(self) -> str:
        return f"{self.name} {self.year}"
    
    class Meta:
        verbose_name = 'IQAC Meeting Minute'
        verbose_name_plural = 'IQAC Meeting Minutes'


class GrivenceUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    type = models.CharField(choices=grievance_type, max_length=30, default="student")

    def __str__(self) -> str:
        return f"{self.name} {self.email} {self.type}"
    
    class Meta:
        verbose_name = 'Grievance User'
        verbose_name_plural = 'Grievance Users'
    

class GrievanceUserCSVUpload(models.Model):
    csv_file = models.FileField(upload_to="grievance_users_csv/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CSV Uploaded at {self.uploaded_at}"    


class GrievanceBody(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    category = models.CharField(choices=grievance_category, max_length=30, default=0)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}  ({self.type.capitalize()})"
    
class DisciplinaryCommittee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Disciplinary Committee Member"
        verbose_name_plural = "Disciplinary Committee Members"


class InternalAudit(models.Model):
    auditors_1 = models.CharField(max_length=200, default=None)
    designation_1 = models.CharField(max_length=200, default=None)
    auditors_2 = models.CharField(max_length=200, default=None)
    designation_2 = models.CharField(max_length=200, default=None)
    department = models.CharField(max_length=200, choices=DEPARTMENTS)

    def __str__(self):
        return self.department

    class Meta:
        verbose_name_plural = "Internal Audits"


class InternalAuditAbout(models.Model):
    data = models.TextField()

    def __str__(self):
        return self.data


class ExternalAudit(models.Model):
    data = models.TextField()

    def __str__(self):
        return self.data

    class Meta:
        verbose_name_plural = "External Audits"


class Policy(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="Policies")
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Policy"
        verbose_name_plural = "Policies"
        ordering = ["-date"]


class MeritAdmissionScheduleSlot(models.Model):
    date_label = models.CharField(max_length=100, help_text="e.g. July 21st")
    departments = models.CharField(max_length=300, help_text="e.g. CS-DS, CS-BS, EEE")
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.date_label} - {self.departments}"

    class Meta:
        verbose_name = "Merit Admission Schedule Slot"
        verbose_name_plural = "Merit Admission Schedule Slots"
        ordering = ["order"]


class MeritAdmissionDocument(models.Model):
    DOCUMENT_TYPE = (
        ("original", "Original"),
        ("copy", "Copy"),
    )
    type = models.CharField(max_length=10, choices=DOCUMENT_TYPE, default="original")
    name = models.CharField(max_length=300)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"[{self.get_type_display()}] {self.name}"

    class Meta:
        verbose_name = "Merit Admission Required Document"
        verbose_name_plural = "Merit Admission Required Documents"
        ordering = ["type", "order"]


class MeritAdmissionDocumentNote(models.Model):
    text = models.CharField(max_length=500)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Merit Admission Document Note"
        verbose_name_plural = "Merit Admission Document Notes"
        ordering = ["order"]


class MeritAdmissionBankDetail(models.Model):
    name = models.CharField(max_length=300)
    account_no = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=50)
    bank = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    note = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f"{self.bank} - {self.account_no}"

    class Meta:
        verbose_name = "Merit Admission Bank Detail"
        verbose_name_plural = "Merit Admission Bank Details"


class MeritAdmissionUniformFee(models.Model):
    boys_fee = models.CharField(max_length=50, help_text="e.g. ₹11,000")
    girls_fee = models.CharField(max_length=50, help_text="e.g. ₹12,000")
    note = models.CharField(max_length=300, blank=True, default="*Cash only*")

    def __str__(self):
        return f"Boys: {self.boys_fee}, Girls: {self.girls_fee}"

    class Meta:
        verbose_name = "Merit Admission Uniform Fee"
        verbose_name_plural = "Merit Admission Uniform Fees"


class MeritAdmissionFormLink(models.Model):
    warning_1 = models.TextField(blank=True)
    warning_2 = models.TextField(blank=True)
    form_url = models.URLField()

    def __str__(self):
        return self.form_url

    class Meta:
        verbose_name = "Merit Admission Form Link"
        verbose_name_plural = "Merit Admission Form Links"


class MeritAdmissionTutorial(models.Model):
    video_url = models.URLField()

    def __str__(self):
        return self.video_url

    class Meta:
        verbose_name = "Merit Admission Tutorial"
        verbose_name_plural = "Merit Admission Tutorials"


class MeritAdmissionContact(models.Model):
    CATEGORY = (
        ("general", "General Admission Queries"),
        ("form", "Data Entry Form Queries"),
    )
    category = models.CharField(max_length=20, choices=CATEGORY, default="general")
    label = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.label}: {self.phone}"

    class Meta:
        verbose_name = "Merit Admission Contact"
        verbose_name_plural = "Merit Admission Contacts"
        ordering = ["category", "order"]


class MeetingMinutes(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="MeetingMinutes")
    date = models.DateField(default=datetime.date.today)
    
    # Categories matched to your UGC Compliance Page tabs
    CATEGORY_CHOICES = (
        ("icc", "Internal Complaints Committee (ICC)"),
        ("grievance", "Student Grievance & Redressal"),
        ("anti_ragging", "Anti-Ragging Committee"),
        ("eoc", "Equal Opportunity Cell"),
        ("sedg", "SEDG Cell"),
        ("accessibility", "Accessibility Committee"),
        ("sc_st", "SC/ST Committee"),
        ("minority", "Minority Cell"),
        ("obc", "OBC Cell"),
        ("idp", "Institutional Development Plan"), 
        
        # === ADD THIS NEW LINE ===
        ("rnd", "Research & Development"), 
        # =========================
        
        ("other", "Other"),
    )
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default="other")

    def __str__(self):
        return f"{self.title} - {self.get_category_display()}"

    class Meta:
        verbose_name = "Meeting Minute / UGC Document"
        verbose_name_plural = "Meeting Minutes & UGC Documents"