import datetime
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from utils.compressor import Compress

ACADEMIC_YEARS = [
    (f"{r}-{r + 1}", f"{r}-{r + 1}")
    for r in range(2020, datetime.date.today().year + 1)
]

DEPARTMENTS = (
    ("CSE", "CSE"),
    ("ECE", "ECE"),
    ("EEE", "EEE"),
    ("ME", "ME"),
    ("CE", "CE"),
    ("BSH", "BSH"),
    ("None", "None"),
)


class Role(models.Model):
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.role


class Testimonials(models.Model):
    full_name = models.CharField(max_length=50)
    role = models.CharField(max_length=150)
    department = models.CharField(max_length=150)
    quote = models.CharField(max_length=500)
    image = models.ImageField(upload_to="testimonials")

    def __str__(self):
        return self.full_name


class HomeUpdates(models.Model):
    data = models.CharField(max_length=300)

    def __str__(self):
        return self.data


class QualityPolicy(models.Model):
    data = models.TextField()

    def __str__(self):
        return self.data


class HomeEvents(models.Model):
    # has_video = models.BooleanField(default=False);
    # video = models.FileField(upload_to="Heros_Videos", blank=True, default="")
    img1 = models.ImageField(
        upload_to="HomeEvents", null=False, blank=False, default="HomeEvents/1.jpg"
    )
    img2 = models.ImageField(
        upload_to="HomeEvents", null=False, blank=False, default="HomeEvents/2.jpg"
    )
    img3 = models.ImageField(
        upload_to="HomeEvents", null=False, blank=False, default="HomeEvents/3.jpg"
    )
    img4 = models.ImageField(
        upload_to="HomeEvents", null=False, blank=False, default="HomeEvents/2.jpg"
    )
    heading = models.CharField(max_length=30)
    sub_heading = models.CharField(max_length=50)
    sub_text = models.TextField()

    def __str__(self):
        return self.heading


class UpcomingEvents(models.Model):
    img = models.ImageField(
        upload_to="UpcomingEvents",
        null=False,
        blank=False,
        default="UpcomingEvents/1.jpg",
    )
    title = models.CharField(max_length=80)
    sub_title = models.TextField()
    date = models.DateField()

    def __str__(self) -> str:
        return self.title


class GalleryEventTypes(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery", blank=True)
    video = models.FileField(upload_to="Heros_Videos", blank=True)
    TYPE = (("img", "IMAGE"), ("vdo", "VIDEO"))
    type = models.CharField(max_length=200, choices=TYPE, default="img")
    date = models.DateField(default=datetime.date.today)
    event_type = models.ManyToManyField(GalleryEventTypes, default="None")
    DEPARTMENTS = (
        ("CSE", "CSE"),
        ("ECE", "ECE"),
        ("EEE", "EEE"),
        ("MECH", "ME"),
        ("CIVIL", "CE"),
        ("BSH", "BSH"),
        ("All", "All"),
    )
    department = models.CharField(max_length=200, choices=DEPARTMENTS, default="None")

    def __str__(self):
        return f"({self.department}) {self.image.name}"


class Faculty(models.Model):
    uuid = models.CharField(max_length=8)
    full_name = models.CharField(max_length=100)
    role = models.ManyToManyField(Role)
    email = models.EmailField(default="faculty@cce.edu.in")
    image = models.ImageField(upload_to="faculty", default="faculty.jpeg")
    DEPARTMENTS = (
        ("CSE", "CSE"),
        ("ECE", "ECE"),
        ("EEE", "EEE"),
        ("ME", "ME"),
        ("CE", "CE"),
        ("BSH", "BSH"),
        ("None", "None"),
        ("administrative_staff", "Administrative Staff"),
        ("wardens", "Wardens "),
        ("supporting_staff", "Supporting Staff"),
        ("security_staff", "Security Staff"),
    )
    department = models.CharField(max_length=200, choices=DEPARTMENTS, default="None")
    profile = models.FileField(
        upload_to="faculty_profile", default="faculty_profile.pdf"
    )
    priorities = models.IntegerField(default=10)
    doj = models.DateField(null=True)

    def __str__(self):
        return self.full_name


class GoverningBody(models.Model):
    role = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Alumni(models.Model):
    memorandum = models.FileField(upload_to="AlumniMemorandum")
    by_laws = models.FileField(upload_to="AlumniByLaws")

    def __str__(self):
        return self.name


class AlumniCommittee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Facilities(models.Model):
    image = models.ImageField(upload_to="Facilities")
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, default="star")
    link_name = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Recruiters(models.Model):
    image = models.ImageField(upload_to="Recruiters")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Hero_Image(models.Model):
    image = models.ImageField(upload_to="Heros_Images", blank=True)
    video = models.FileField(upload_to="Heros_Videos", blank=True)
    TYPE = (("img", "IMAGE"), ("vdo", "VIDEO"))
    type = models.CharField(max_length=200, choices=TYPE, default="img")
    PAGE = (
        ("management", "Management"),
        ("directors_desk", "Directors Desk"),
        ("facilities", "Facilities"),
        ("principals_desk", "Principal's Desk"),
        ("cce_in_media", "CCE In Media"),
        ("governing_body", "Governing Body"),
        ("organogram", "Organogram"),
        ("mandatory_disclosure", "Mandatory Disclosure"),
        ("antiraging_cell", "AntiRaging Cell"),
        ("grivence_redressal_sysytem", "Grivence Redressal System"),
        ("sc_st_monitoring_commite", "Sc/St Monitoring Commitee"),
        ("iqac", "IQAC"),
        ("examination_cell", "Examination Cell"),
        ("pta", "PTA"),
        ("office", "office"),
        ("nss", "NSS"),
        ("college_union", "College Union"),
        ("facilities", "Facilities"),
        ("pta", "PTA"),
        ("None", "None"),
        ("research", "Research"),
        ("arts", "Arts"),
        ("sports", "Sports"),
        ("placements", "Placements"),
        ("admissions", "Admissions"),
        ("academic_research", "Academic Research"),
        ("womencell", "Women Cell"),
        ("clubs", "Clubs"),
        ("iic", "IIC"),
        ("all_committees", "All Committees"),
        ("programs_offered", "Programs Offered"),
        ("hr_manual", "HR Policy"),
        ("vision_2035", "Vision 2035"),
        ("annual_report", "Annual Report"),
        ("college_handbook", "College Handbook"),
        ("academic_calendar", "academic Calendar"),
        ("audited_statements", "Audited Statements"),
        ("college_magazine", "College Magazine"),
        ("ktu_aicte_regulations", "KTU AICTE Regulations"),
        ("approvals", "Approvals"),
        ("techies_park", "Techies Park"),
        ("events", "Events"),
        ("study_abroad", "Study Abroad"),
        ("library", "Library"),
        ("disciplinary_committee", "Disciplinary Committee"),
        ("internal_audit_page", "Internal Audit"),
        ("external_audit_page", "External Audit"),
        ("ieee", "IEEE"),
        ("quality_policy", "Quality Policy"),
        ("mentoring", "Mentoring"),
        ("ccil", "CCIL"),
        ("international_relations", "International Relations Cell"),
        ("webteam", "webteam"),
        ("ccevr", "ccevr"),
        ("result_analysis", "Result Analysis"),
    )
    page = models.CharField(max_length=200, choices=PAGE, default="None")

    def __str__(self):
        return f"{self.page}---{self.image.name}{self.video.name}"

    class Meta:
        verbose_name_plural = "Hero Images"


class Achivements(models.Model):
    image = models.ImageField(upload_to="achivements")
    date = models.DateField(default=datetime.date.today)

    class Meta:
        verbose_name = "Achivement"
        verbose_name_plural = "Achivements"

    def __str__(self):
        return self.image.name


class HomeAnouncement(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(
        ("image"),
        upload_to="HomeAnouncements",
        height_field=None,
        width_field=None,
        max_length=None,
        default="HomeAnouncements/announcement.png",
    )
    description = models.TextField()
    date = models.DateField(default=datetime.date.today)
    link_name = models.CharField(max_length=100, default="")
    link = models.URLField(max_length=100, default="")

    def __str__(self):
        return self.title


class FundedProjects(models.Model):
    name = models.CharField(max_length=100)
    principal_investigator = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    STATUS = (("ongoing", "ONGOING"), ("completed", "COMPLETED"))
    status = models.CharField(choices=STATUS, max_length=100)
    department = models.CharField(max_length=200, choices=DEPARTMENTS, default="None")
    funding_agency = models.CharField(max_length=100)
    grand_sanctioned = models.IntegerField()
    grand_recived = models.IntegerField()
    publictaion_details = models.FileField(upload_to="research/FundedProjects")

    def __str__(self):
        return self.name


class AcademicConsultancy(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    name_of_client = models.CharField(max_length=100)
    department = models.CharField(max_length=200, choices=DEPARTMENTS, default="None")
    STATUS = (("ongoing", "ONGOING"), ("completed", "COMPLETED"))
    status = models.CharField(max_length=100, choices=STATUS)
    amount_recived = models.IntegerField()

    def __str__(self):
        return self.name


class ResearchGuides(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=1)
    year = models.IntegerField()

    def __str__(self):
        return self.faculty.full_name


class Conference(models.Model):
    name = models.CharField(max_length=100)
    investor = models.CharField(("Name of Investor"), max_length=500, default="")
    STATUS = (("ongoing", "ONGOING"), ("completed", "COMPLETED"))
    status = models.CharField(max_length=100, choices=STATUS)
    department = models.CharField(max_length=200, choices=DEPARTMENTS, default="None")
    duration = models.CharField(max_length=100)
    year = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class AcademicPartnerShip(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    name_of_client = models.CharField(max_length=100)
    STATUS = (("ongoing", "ONGOING"), ("completed", "COMPLETED"))
    status = models.CharField(max_length=100, choices=STATUS)
    department = models.CharField(max_length=200, choices=DEPARTMENTS, default="None")
    amount = models.IntegerField()

    def __str__(self):
        return self.name


class FacultyStudentPublications(models.Model):
    title = models.CharField(max_length=500)
    name = models.CharField(("Name Of Author"), max_length=300)
    dep = models.CharField(
        ("Department of Faculty/student"), max_length=100, choices=DEPARTMENTS
    )
    journal = models.CharField(("Name Of Journal"), max_length=500)
    year = models.CharField(("Year Of Publication"), max_length=50)
    details = models.FileField(
        ("Details of Publictaion"), upload_to="research/publications", max_length=100
    )


class AdmissionStatistics(models.Model):
    dept = models.CharField(max_length=100, choices=DEPARTMENTS)
    seats = models.IntegerField()
    admitted = models.IntegerField()
    year = models.CharField(choices=ACADEMIC_YEARS, max_length=20, default="none")

    def __str__(self):
        return f"{self.dept} {self.year}"


class AdmissionGraph(models.Model):
    graph = models.ImageField(upload_to="admission/")
    year = models.CharField(choices=ACADEMIC_YEARS, max_length=20, default="none")


class Nptel(models.Model):
    title_year = models.CharField(max_length=100)
    file = models.FileField(upload_to="nptel")

    def __str__(self):
        return self.title_year


class WebsiteTeam(models.Model):
    name = models.CharField(max_length=100, default=None)
    img = models.ImageField(upload_to="websiteteam", blank=True)
    role = models.CharField(max_length=100, default=None)
    batch = models.CharField(max_length=100, default=None)

    class Meta:
        verbose_name_plural = "Website Team"

    def __str__(self):
        return self.name


class PHD_Faculty(models.Model):
    name = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    dept = models.CharField(max_length=100, choices=DEPARTMENTS)
    year = models.CharField(max_length=20)
    researchArea = models.CharField(max_length=100)
    options = (
        ("pursuing", "Pursuing"),
        ("awarded", "Awarded"),
    )
    status = models.CharField(choices=options, default=None, max_length=100)

    def __str__(self):
        return f"{self.name}-{self.dept}"

    class Meta:
        verbose_name = "PHD Faculty"
        verbose_name_plural = "PHD Facultys"


class ResearchScholar(models.Model):
    name = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    researchArea = models.CharField(max_length=100)
    guideName = models.CharField(max_length=100)
    dept = models.CharField(max_length=100, choices=DEPARTMENTS)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Research Scholar"
        verbose_name_plural = "Research Scholars"


class AwardedPHD(models.Model):
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=100, choices=DEPARTMENTS)
    designation = models.CharField(max_length=100)
    researchArea = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "AwardedPHD"
        verbose_name_plural = "AwardedPHDs"


class Techletics24(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="techletics24", blank=False)
    dept = models.CharField(max_length=100, choices=DEPARTMENTS)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Techletics 24 Image"
        verbose_name_plural = "Tecletics Images"
