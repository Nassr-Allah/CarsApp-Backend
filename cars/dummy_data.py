import itertools
import random

from .models import Car, CarModel, Service, Reservation

car_list = {
    "BMW":      ["12", "k7", "NV13", "Something else"],
    "Nissan":   ["err", "prrr", "trrr", "Something else khlaf"],
    "Ford":     ["dddderr", "d3", "whatever", "Something else khlaf khlaf"],
    "Toyota":   ["big one", "bigger one", "gd chkoupi"],
    "Mercedes": ["fancy one", "fancier one", "hedi for bzf"],
}

services = [
    "Service 1",
    "Serivce 2",
    "Serivce 3",
    "Serivce 4",
    "Serivce 5",
]


def create_dummy_cars() -> None:
    for k, v in car_list.items():
        if Car.objects.filter(car_brand=k).first():
            continue
        c = Car.objects.create(car_brand=k)
        for i in v:
            m = CarModel.objects.create(model_name=i, car_model=c)
            for s in services:
                price = random.uniform(10, 1_000_000)
                service = Service.objects.create(service_name=s, service_price=str(price), service_model=m)
                service.save()
            m.save()
        c.save()
