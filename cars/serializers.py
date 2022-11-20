from rest_framework import serializers
from .models import Car, CarModel, Service, Reservation


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
        depth = 1


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = "__all__"
        depth = 1


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"
        depth = 1


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
        depth = 1
