from django.db import models

# Create your models here.
class GoverningBody(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Governing Body"



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