from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


# Create your views here.
class CarCRUD(RetrieveUpdateDestroyAPIView, CreateModelMixin, ListModelMixin):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            return self.retrieve(request, args, kwargs)
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CarSerializer(queryset, many=True)
        return Response(serializer.data)


class CarModelCRUD(RetrieveUpdateDestroyAPIView, CreateModelMixin, ListModelMixin):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            return self.retrieve(request, args, kwargs)
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CarModelSerializer(queryset, many=True)
        return Response(serializer.data)


class ServiceCRUD(RetrieveUpdateDestroyAPIView, CreateModelMixin, ListModelMixin):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            return self.retrieve(request, args, kwargs)
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ServiceSerializer(queryset, many=True)
        return Response(serializer.data)


class ReservationCRUD(RetrieveUpdateDestroyAPIView, CreateModelMixin, ListModelMixin):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            return self.retrieve(request, args, kwargs)
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ReservationSerializer(queryset, many=True)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, args, kwargs)


class MiniServiceCRUD(RetrieveUpdateDestroyAPIView, CreateModelMixin, ListModelMixin):
    queryset = MiniService.objects.all()
    serializer_class = MiniServiceSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            return self.retrieve(request, args, kwargs)
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(self, args, kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = MiniServiceSerializer(queryset, many=True)
        return Response(serializer.data)
