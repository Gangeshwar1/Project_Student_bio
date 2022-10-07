from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100,null=False)
    roll_no = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    standard = models.IntegerField(blank=True)
    image = models.ImageField(upload_to='images/',null=True, blank=True)
    

def __str__(self):
        return self.name