from django.db import models

# Create your models here.
class DepHero(models.Model):
    image = models.ImageField(upload_to="DepHeroImages")
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")