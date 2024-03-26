from django.db import models

# Create your models here.


class Location(models.Model):
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    # Other relevant location information

    def __str__(self):
        return self.city


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    mileage = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    photo1 = models.ImageField(upload_to='cars/images',default='')
    photo2 = models.ImageField(upload_to='cars/images', default='')
    photo3 = models.ImageField(upload_to='cars/images', default='')
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # Other relevant user information

    def __str__(self):
        return self.username


class RentalTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rental_start_date = models.DateField()
    rental_end_date = models.DateField()
    # Other relevant transaction information

    def __str__(self):
        return f"Rental transaction for {self.car} by {self.user}"
