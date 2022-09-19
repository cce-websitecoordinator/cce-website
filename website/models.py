
from django.db import models


class Testimonials(models.Model):
    full_name = models.CharField(max_length=30)
    role = models.CharField(max_length=15)
    department = models.CharField(max_length=50)
    quote = models.CharField(max_length=100)
    image = models.CharField(max_length=50)
    batch = models.CharField(max_length=10)

    def __str__(self):
        return self.full_name

class HomeUpdates(models.Model):
    data= models.CharField(max_length=300)

    def __str__(self):
        return self.data
   
class HomeEvents(models.Model):
    heading = models.CharField(max_length=30)
    sub_heading = models.CharField(max_length=50)
    sub_text = models.TextField()