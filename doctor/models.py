from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Specialization(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)

    def __str__(self):
        return self.name

class Designation(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)

    def __str__(self):
        return self.name

class AvailableTime(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    image = models.ImageField(upload_to='doctor/images/')
    designation = models.CharField(Designation)
    speacialization = models.ManyToManyField(Specialization)
    available_time = models.ManyToManyField(AvailableTime)
    fee = models.IntegerField()
    meet_link = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"