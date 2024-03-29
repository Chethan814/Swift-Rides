from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Location(models.Model):
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    # Other relevant location information

    def __str__(self):
        return self.city


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    mileage = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    car_images = models.ImageField(upload_to='cars/images', default='')
    locations = models.ManyToManyField(Location, related_name='cars')

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class RentalTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rental_start_date = models.DateField()
    rental_end_date = models.DateField()
    # Other relevant transaction information

    def __str__(self):
        return f"Rental transaction for {self.car} by {self.user}"
