from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework import status

from .models import Car, CarModel, Service, Reservation, Price
from .serializers import (
    CarSerializer, CarModelSerializer,
    ServiceSerializer, ReservationSerializer,
    PriceSerializer
)


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
        service = Service.objects.filter(pk=request.data.get('reservation_service')).first()
        if not service:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'reservation service not found'})
        serializer = ReservationSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['reservation_service'] = service
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ReservationSerializer(queryset, many=True)
        return Response(serializer.data)


class PriceCRUD(RetrieveUpdateDestroyAPIView, CreateModelMixin, ListModelMixin):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            return self.retrieve(request, args, kwargs)
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        car_model = CarModel.objects.filter(pk=request.data.get('car_model')).first()
        if not car_model:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "car model not found"})
        service = Service.objects.filter(pk=request.data.get('service')).first()
        if not service:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "service not found"})
        serializer = PriceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['car_model'] = car_model
        serializer.validated_data['service'] = service
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PriceSerializer(queryset, many=True)
        return Response(serializer.data)
