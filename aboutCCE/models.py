from django.db import models

from utils.compressor import Compress

# Create your models here.
class Management(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    img = models.ImageField(upload_to="Management",default="img.png")
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Management"


class CCEinMedia(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="CCEinMedia")
    date = models.DateField()
    link = models.URLField()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "CCE in Media"
class MoreAboutCCE(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="MoreAboutCCE")
    link = models.URLField()
    date = models.DateField()
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "More About CCE"

class CollegeCalendar(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="CollegeCalendar")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "College Calendar"


class AnnualReport(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="AnnualReport")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Annual Report"


class MandatoryDisclosure(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="MandatoryDisclosure")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Mandatory Disclosure"

class KtuRegulations(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="KtuRegulations")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "KTU Regulations"

class AicteApprovals(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="AicteApprovals")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "AICTE Approvals"

class AuditedStatements(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="AuditedStatements")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Audited Statements"

class CollegeMagazine(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="CollegeMagazine")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "College Magazine"


