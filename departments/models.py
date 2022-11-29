from django.db import models

# Create your models here.
class DepHero(models.Model):
    image = models.ImageField(upload_to="DepHeroImages")
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")

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
 
class DepUpdates(models.Model):
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    title = models.CharField(max_length=100)
    data = models.CharField(max_length=300)
    date = models.DateField(auto_now_add=True)