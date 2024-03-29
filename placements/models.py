from django.db import models
import datetime


from website.models import Faculty

ACADEMIC_YEARS = [
    ("{}-{}".format(r, r + 1), "{}-{}".format(r, r + 1))
    for r in range(2019, datetime.date.today().year + 1)
]

# Create your models here.
class  PVissionANDMission(models.Model):
    data = models.TextField(max_length=250)
    CHOICES = (("Vision", "Vision"), ("Mission", "Mission"),("objectives", "objectives"))
    name = models.CharField(max_length=10, choices=CHOICES)
    class Meta:
        verbose_name = ("Placement Vission and Mission")
        verbose_name_plural = ("Placement Vissions and Missions")

    def __str__(self):
        return self.name


class Testimonials(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='placement/testimonials/')
    def __str__(self):
        return self.title
class PlacementUpdates(models.Model):
    title = models.CharField(max_length=100)
    data = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.title

class PlacementTraning(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='placement/training/')
    data = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.title
class Achivements(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='placement/training/')
    data = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.image.name

class PlacementFaculty(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    role = models.CharField(max_length=70)
    order = models.IntegerField()
    def __str__(self):
        return self.faculty.full_name

class PlacementStatistics(models.Model):
    graph = models.ImageField(("Graph"), upload_to=None, height_field=None, width_field=None, max_length=None)

class PlacementStatsTable(models.Model):
    year = models.CharField(choices=ACADEMIC_YEARS,default="None",max_length=30)
    students = models.IntegerField()
    placement = models.IntegerField()
    higher_studies = models.IntegerField()
    total = models.IntegerField()
    highest = models.DecimalField(max_digits=5,decimal_places=2)
    avg = models.DecimalField(max_digits=5,decimal_places=2)
    def __str__(self):
        return self.year

    

class PlacementGallery(models.Model):
    image = models.ImageField(upload_to="gallery",blank=True)
    video = models.FileField(upload_to="PlacementGallery",blank=True)
    TYPE = (("img","IMAGE"),("vdo","VIDEO"))
    type = models.CharField(max_length=200, choices = TYPE, default="img")
    date = models.DateField(default=datetime.date.today)
