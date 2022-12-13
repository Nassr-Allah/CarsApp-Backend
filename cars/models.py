from django.db import models


# Create your models here.
class Car(models.Model):
    car_brand = models.CharField(max_length=30, default="", unique=True)
    image_url = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.car_brand


class CarModel(models.Model):
    model_name = models.CharField(max_length=30, default="", unique=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=300, default="", blank=True)

    def __str__(self):
        return self.model_name


class Service(models.Model):
    service_name = models.CharField(max_length=60, default="")

    def __str__(self):
        return f"{self.service_name}"


class Reservation(models.Model):
    client_full_name = models.CharField(max_length=255, default="")
    client_phone = models.CharField(max_length=20, default="")
    reservation_date = models.CharField(max_length=50, default="")
    reservation_time = models.CharField(max_length=30, default="")
    reservation_services = models.CharField(max_length=1024, default="")
    car_year = models.CharField(max_length=30, default="")
    car_engine = models.CharField(max_length=30, default="")
    car_brand = models.CharField(max_length=30, default="")
    car_model = models.CharField(max_length=30, default="")
    engine_type = models.CharField(max_length=30, default="")

    def __str__(self):
        return f"{self.client_full_name}/{self.reservation_date}/{self.reservation_services}"


class MiniService(models.Model):
    name = models.CharField(max_length=256, default="")
    service = models.ForeignKey(Service, on_delete=models.CASCADE)