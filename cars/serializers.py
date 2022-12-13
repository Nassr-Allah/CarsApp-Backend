from rest_framework import serializers
from .models import *


class MiniServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = MiniService
        fields = "__all__"
        depth = 1


class ServiceSerializer(serializers.ModelSerializer):
    miniservice_set = MiniServiceSerializer(many=True)

    class Meta:
        model = Service
        fields = "__all__"
        depth = 3


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = "__all__"
        depth = 0


class CarSerializer(serializers.ModelSerializer):
    carmodel_set = CarModelSerializer(many=True)

    class Meta:
        model = Car
        fields = "__all__"
        depth = 1


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
        depth = 1

