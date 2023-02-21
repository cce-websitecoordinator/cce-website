from django.db import models
import uuid
from website.models import Faculty

# Create your models here.
DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
class DepHero(models.Model):
    image = models.ImageField(upload_to="DEP_Heros_Images",blank=True)
    video = models.FileField(upload_to="DEP_Heros_Videos",blank=True)
    TYPE = (("img","IMAGE"),("vdo","VIDEO"))
    type = models.CharField(max_length=200, choices = TYPE, default="img")
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    def __str__(self):
        return self.department

class DepAbout(models.Model):
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    PAGES =(("about","About"),("faculty","Faculties"),("associations","Associations"),("professionalBodies","Professional Bodies"),("curriculum_and_syllabus","Sylabus"))
    page = models.CharField(max_length=200, choices = PAGES, default="About")
    about = models.TextField()

    def __str__(self):
        return self.department
class POES(models.Model):
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    data = models.CharField(max_length=300)
    class Meta:
        verbose_name_plural = "POE"

class POS(models.Model):
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    data = models.CharField(max_length=300)
    class Meta:
        verbose_name_plural = "PO"


class PSOS(models.Model):
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    data = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = "PSO"

class Vission(models.Model):
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    vission = models.CharField(max_length=300)
    class Meta:
        verbose_name = ("Vission")
        verbose_name_plural = (" Vission")

    def __str__(self):
        return self.department + " ( " + self.vission[:50] + " )"

 

class Mission(models.Model):
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    Mission = models.CharField(max_length=300)
    class Meta:
        verbose_name = ("Mission")
        verbose_name_plural = ("Missions")

    def __str__(self):
        return self.department + " ( " + self.Mission[:50] + " )"
 
class DepUpdates(models.Model):
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    title = models.CharField(max_length=100)
    data = models.CharField(max_length=300)
    date = models.DateField()

    def __str__(self):
        return self.title


class Associations(models.Model):
    title = models.CharField(max_length=150)
    short_description = models.CharField(max_length=500,default="None")
    data = models.TextField()
    image = models.ImageField(upload_to="AssociationsImages")
    hero_image = models.ImageField(upload_to="AssociationsImages/Hero_images",default="None")
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    linkname = models.CharField(max_length=100)
    def __str__(self):
        return self.title


class AssociationsEvents(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150)
    short_description = models.CharField(max_length=500,default="None")
    assosiation = models.ForeignKey(Associations, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="AssociationsImagesEvents")
    def __str__(self):
        return self.title
  
class AssociationTeamMembers(models.Model):
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    image = models.ImageField(upload_to="Association")
    assosiation = models.ForeignKey(Associations, on_delete=models.CASCADE)
    priority = models.IntegerField(default=0)
    def __str__(self):
        return self.name

   

class ProfessionalBodies(models.Model):
    title = models.CharField(max_length=150)
    short_description = models.CharField(max_length=500,default="None")
    image = models.ImageField(upload_to="ProfessionalBodiesImages",default="None")
    hero_image = models.ImageField(upload_to="ProfessionalBodiesImages/Hero_images",default="None")
    data = models.TextField()
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    linkname = models.CharField(max_length=100)
    def __str__(self):
        return self.title
class ProfessionalBodiesEvents(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150)
    short_description = models.CharField(max_length=500,default="None")
    ProfessionalBodies = models.ForeignKey(ProfessionalBodies, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="ProfessionalBodiesImagesEvents")
    def __str__(self):
        return self.title

class ProfessionalBodiesTeamMembers(models.Model):
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    image = models.ImageField(upload_to="ProfessionalBodies")
    ProfessionalBodies = models.ForeignKey(ProfessionalBodies, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class SyllabusPDFS(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="SyllabusPDFS")
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
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")


class Laboratories(models.Model):

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="LaboratoriesImages")
    data = models.CharField(max_length=500)
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    faculties = models.ManyToManyField(Faculty, blank=True)
    class Meta:
        verbose_name = "Labs"
        verbose_name_plural = "Laboratories"

    def __str__(self):
        return self.name


class Achivements(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="AchivementsImages")
    data = models.CharField(max_length=500)
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    link = models.URLField()
    class Meta:
        verbose_name = ("Achivement")
        verbose_name_plural = ("Achivements")

    def __str__(self):
        return self.name


class Events(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="EventsImages")
    poster = models.ImageField(upload_to="EventsImages",default="None")
    data = models.CharField(max_length=500)
    date = models.DateField()
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    TYPE = (("workshops_seminars","Workshops / Seminars"),("addons","Add-Ons"),("iv","Industrial Visits"))
    type  = models.CharField(choices=TYPE,max_length=100,default="iv")
    link = models.URLField()
    class Meta:
        verbose_name = ("Event")
        verbose_name_plural = ("Events")

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(("Email"), blank=False)
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return self.name


class NewsLetters(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="NewsLettersImages",default="None")
    file = models.FileField(upload_to="NewsLetters")
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    class Meta:
        verbose_name = ("NewsLetters")
        verbose_name_plural = ("NewsLetterss")

    def __str__(self):
        return self.title


class Objectives(models.Model):
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    data =  models.CharField(max_length=500);

    def __str__(self):
        return self.department


