import datetime
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from utils.compressor import Compress

class Role(models.Model):
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.role

class Testimonials(models.Model):
    full_name = models.CharField(max_length=30)
    role = models.CharField(max_length=15)
    department = models.CharField(max_length=50)
    quote = models.CharField(max_length=200)
    image = models.ImageField(upload_to="testimonials")
    batch = models.CharField(max_length=10)


    def save(self, *args, **kwargs):
        new_image = Compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)

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
    def save(self, *args, **kwargs):
        compressed_image1 = Compress(self.img1)
        compressed_image2 = Compress(self.img2)
        compressed_image3 = Compress(self.img3)
        compressed_image4 = Compress(self.img4)
        self.img1 = compressed_image1
        self.img2 = compressed_image2
        self.img4 = compressed_image3
        self.img4 = compressed_image4
        super().save(*args, **kwargs)

class UpcomingEvents(models.Model):
    img = models.ImageField(upload_to="UpcomingEvents",null=False,blank=False,default="UpcomingEvents/1.jpg")
    title = models.CharField(max_length=80)
    sub_title = models.TextField(max_length=150)
    date = models.DateField()
    def save(self, *args, **kwargs):
        new_image = Compress(self.img)
        self.img = new_image
        super().save(*args, **kwargs)



    def __str__(self) -> str:
        return self.title


class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery",blank=True)
    video = models.FileField(upload_to="Heros_Videos",blank=True)
    TYPE = (("img","IMAGE"),("vdo","VIDEO"))
    type = models.CharField(max_length=200, choices = TYPE, default="img")
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("MECH","MECH"),("CIVIL","CIVIL"),("BSH","BSH"),("All","All"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")

    def __str__(self):
        return "("+self.department+')' +self.image.name 




class Faculty(models.Model):
    uuid = models.CharField(max_length=8)
    full_name = models.CharField(max_length=100)
    role = models.ManyToManyField(Role)
    email = models.EmailField(default="faculty@cce.edu.in")
    image = models.ImageField(upload_to="faculty", default = "faculty.jpeg")
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"),("administrative_staff","Administrative Staff"),("wardens","Wardens "),("supporting_staff","Supporting Staff"),("security_staff","Security Staff"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    priorities = models.IntegerField(default=10)
    doj = models.DateField(null = True)
    def save(self, *args, **kwargs):
        new_image = Compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name



class GoverningBody(models.Model):
    role =  models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Alumni(models.Model):
    memorandum = models.FileField(upload_to="AlumniMemorandum")
    by_laws = models.FileField(upload_to="AlumniByLaws")
    def __str__(self):
        return self.name


class AlumniCommittee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    def __str__(self):
        return self.name



class Facilities(models.Model):
    image = models.ImageField(upload_to="Facilities")
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100,default="star")
    link_name = models.CharField(max_length=100,default="")
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.title


class Recruiters(models.Model):
    image = models.ImageField(upload_to="Recruiters")
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Hero_Image(models.Model):
    image = models.ImageField(upload_to="Heros_Images",blank=True)
    video = models.FileField(upload_to="Heros_Videos",blank=True)
    TYPE = (("img","IMAGE"),("vdo","VIDEO"))
    type = models.CharField(max_length=200, choices = TYPE, default="img")
    PAGE = (("management","Management"),("directors_desk","Directors Desk"),("facilities","Facilities"),("principals_desk","Principal's Desk"),("cce_in_media","CCE In Media"),("governing_body","Governing Body"),("organogram","Organogram"),("mandatory_disclosure","Mandatory Disclosure"),("antiraging_cell","AntiRaging Cell"),("grivence_redressal_sysytem","Grivence Redressal System"),("sc_st_monitoring_commite","Sc/St Monitoring Commitee"),("iqac","IQAC"),("examination_cell","Examination Cell"),("PTA","PTA"),("office","office"),("nss","NSS"),("college_union","College Union"),("facilities","Facilities"),("pta","PTA"),("None","None"))
    page = models.CharField(max_length=200, choices = PAGE, default="None") 
    def __str__(self):
        return self.page+"---"+self.image.name + self.video.name
    class Meta:
        verbose_name_plural = "Hero Images"
class Achivements (models.Model):
    image = models.ImageField(upload_to='achivements')
    date = models.DateField(default=datetime.date.today)
    class Meta:
        verbose_name = "Achivement"
        verbose_name_plural = "Achivements"
    def __str__(self):
        return self.image.name

  