from django.db import models


# Create your models here.
class Car(models.Model):
    car_brand = models.CharField(max_length=30, default="", unique=True)


class CarModel(models.Model):
    model_name = models.CharField(max_length=30, default="", unique=True)
    car_model = models.ForeignKey(Car, on_delete=models.CASCADE)


class Service(models.Model):
    service_name = models.CharField(max_length=60, default="")
    service_price = models.CharField(max_length=12, default="")
    service_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)


class Reservation(models.Model):
    client_full_name = models.CharField(max_length=255, default="")
    client_phone = models.CharField(max_length=20, default="")
    reservation_date = models.CharField(max_length=50, default="")
    reservation_service = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
