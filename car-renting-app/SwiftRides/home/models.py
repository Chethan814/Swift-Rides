from django.db import models

# Create your models here.


class homes(models.Model):
    FirstName = models.CharField(max_length=255)
    secondName = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    dateOfBirth = models.DateField(null=True)

    # to see values in admin panel
    def __str__(self):
        return self.FirstName


class User_Information(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=13)
    address = models.TextField(max_length=255)
    postcode = models.CharField(max_length=10)
    state = models.CharField(max_length=255)
    area = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state_region = models.CharField(max_length=100)


class cars(models.Model):
    phots = 
    name = models.CharField(max_length=255)
    price = models.FloatField(null=False)
