from django.db import models

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
        return self.title
