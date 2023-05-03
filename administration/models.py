from django.db import models

from website.models import Faculty

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
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "IQAC Executive Commitee"
    

class IQACFormationNotice(models.Model):

    notice = models.FileField(upload_to="IQACFormationNotice")
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.notice.name
    class Meta:
        verbose_name_plural = "IQAC Formation Notice"


class PTAExecutiveCommitee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "PTA Executive Commitee"

class PTAMembers(models.Model):
    name = models.CharField(max_length=100)
    tudent_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "PTA  Members"
class ProfileHighlights(models.Model):
    qulaification = models.CharField(max_length=500)
    choices = (("principal","Principal"),("exedir","Executive Director"))
    designation = models.CharField(max_length=100,choices=choices)
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
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE,default=2)
    designation = models.CharField(max_length=200,default=None)

    def __str__(self) -> str:
        return self.faculty.full_name + "  " + self.designation


class AcademicAdministrationDirector(models.Model):
    director_reserch_img = models.ImageField( upload_to='academicAdministraction/faculty')
    director_reserch_name = models.CharField(max_length=200)
    def __str__(self):
        return self.director_reserch_name
class AcademicAdministractors(models.Model):
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE,default=2)
    order = models.IntegerField()

    def __str__(self) -> str:
        return self.faculty.full_name


class GrivenceCommitee(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

