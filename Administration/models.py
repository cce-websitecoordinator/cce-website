from django.db import models

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