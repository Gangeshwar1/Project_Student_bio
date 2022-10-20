from django.db import models
from .models import*

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100,null=False)
    username = models.CharField(max_length=50,blank=True)
    password = models.CharField(max_length=50,blank=True)
    roll_no = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    standard = models.CharField(max_length=50,blank=True)
    image = models.ImageField(upload_to='images/',null=True, blank=True)
    gender = models.CharField(max_length=10,blank=True)

def __str__(self):
        return self.name