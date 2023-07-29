from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'))
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    mobile = models.IntegerField()
    salary = models.IntegerField()
    date = models.DateField()
    
    
