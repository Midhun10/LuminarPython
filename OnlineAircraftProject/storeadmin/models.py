from django.db import models


# Create your models here.
class Manufacture(models.Model):
    Manufacture_name = models.CharField(unique=True, max_length=200)
    Manufacture_image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.Manufacture_name


class Aircraftmodels(models.Model):
    Aircraft_manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE)
    Aircraft_name = models.CharField(unique=True, max_length=200)
    Aircraft_model = models.CharField(unique=True, max_length=200)
    Aircraft_seats = models.IntegerField()
    Aircraft_length = models.CharField(max_length=200)
    Aircraft_wingspan = models.CharField(max_length=200)
    Aircraft_fuel = models.CharField(max_length=200)
    Aircraft_ceiling = models.CharField(max_length=200)
    Aircraft_range = models.CharField(max_length=200)
    choice = (
        ('PW4000', 'PW4000'),
        ('GE90', 'GE90'),
        ('RR Trent800', 'RR Trent800')
    )
    Aircraft_engine = models.CharField(max_length=200, choices=choice, default="GE90")
    Aircraft_price = models.CharField(max_length=200, default="150 Million")
    Aircraft_image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.Aircraft_name


class Service(models.Model):
    Service_type = models.CharField(max_length=200, unique=True)
    Service_price = models.CharField(max_length=25, default="0USD")

    def __str__(self):
        return self.Service_type
