from django.db import models

# Create your models here.

class homes(models.Model):
    FirstName = models.CharField(max_length=255)
    secondName = models.CharField(max_length=255)
    phone = models.IntegerField(null = True)
    dateOfBirth = models.DateField(null = True)

