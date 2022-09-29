
from distutils.command.upload import upload
from turtle import title
from django.db import models


class Testimonials(models.Model):
    full_name = models.CharField(max_length=30)
    role = models.CharField(max_length=15)
    department = models.CharField(max_length=50)
    quote = models.CharField(max_length=200)
    image = models.ImageField(upload_to="testimonials")
    batch = models.CharField(max_length=10)

    def __str__(self):
        return self.full_name

class HomeUpdates(models.Model):
    data= models.CharField(max_length=300)

    def __str__(self):
        return self.data
   
class HomeEvents(models.Model):
    img1 = models.ImageField(upload_to="HomeEvents",null=False,blank=False,default="HomeEvents/1.jpg")
    img2 = models.ImageField(upload_to="HomeEvents",null=False,blank=False,default="HomeEvents/2.jpg")
    img3 = models.ImageField(upload_to="HomeEvents",null=False,blank=False,default="HomeEvents/3.jpg")
    img4 = models.ImageField(upload_to="HomeEvents",null=False,blank=False,default="HomeEvents/2.jpg")
    heading = models.CharField(max_length=30)
    sub_heading = models.CharField(max_length=50)
    sub_text = models.TextField()


class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery")


class UpcomingEvent(models.Model):
    date= models.DateField() 
    image = models.ImageField(upload_to="upcomingEvents")
    title = models.CharField(max_length=30)
    sub_title  = models.CharField(max_length=100)


