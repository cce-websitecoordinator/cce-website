from django.db import models


class Testimonials(models.Model):
    full_name = models.CharField(max_length=30)
    role = models.CharField(max_length=15)
    department = models.CharField(max_length=15)
    quote = models.CharField()
    image = models.CharField()
    batch = models.CharField(max_length=10)

    def __str__(self):
        return self.full_name