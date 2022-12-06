from django.db import models

from website.models import Faculty

# Create your models here.
class DepHero(models.Model):
    image = models.ImageField(upload_to="DepHeroImages")
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")

    def __str__(self):
        return self.department

class POES(models.Model):
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    data = models.CharField(max_length=300)


class POS(models.Model):
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    data = models.CharField(max_length=300)


class PSOS(models.Model):
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    data = models.CharField(max_length=300)

class Vission(models.Model):
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    vission = models.CharField(max_length=300)
 

class Mission(models.Model):
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    Mission = models.CharField(max_length=300)
    def __str__(self):
        return self.Mission
 
class DepUpdates(models.Model):
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    title = models.CharField(max_length=100)
    data = models.CharField(max_length=300)
    date = models.DateField()

    def __str__(self):
        return self.title


class Associations(models.Model):
    title = models.CharField(max_length=150)
    data = models.CharField(max_length=500)
    image = models.ImageField(upload_to="AssociationsImages")
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    linkname = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.title


class ProfessionalBodies(models.Model):
    title = models.CharField(max_length=150)
    data = models.CharField(max_length=500)
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    linkname = models.CharField(max_length=100)
    link = models.URLField()
    def __str__(self):
        return self.title


class SyllabusPDFS(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="SyllabusPDFS")
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    def __str__(self) -> str:
        return self.title


class Handouts(models.Model):
    course_name = models.CharField(max_length=200)
    course_code = models.IntegerField()
    course_credits = models.IntegerField()
    course_information_sheet = models.FileField(upload_to="Handouts/InformationSheets")
    course_notes = models.FileField(upload_to="Handouts/Notes")
    SEMESTERS = (("S1&S2","S1&S2"),("S3","S3"),("S4","S4"),("S5","S5"),("S6","S6"),("S7","S7"),("S8","S8"))
    semester = models.CharField(max_length=200, choices = SEMESTERS, default="S1&S2")
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")


class Laboratories(models.Model):

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="LaboratoriesImages")
    data = models.CharField(max_length=500)
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    faculties = models.ManyToManyField(Faculty, blank=True)

    

    class Meta:
        verbose_name = "Labs"
        verbose_name_plural = "Laboratories"

    def __str__(self):
        return self.name
