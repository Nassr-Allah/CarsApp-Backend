from django.contrib import admin
from .models import CarModel, Car, Service, Reservation, Price

# Register your models here.
admin.site.register(CarModel, admin.ModelAdmin)
admin.site.register(Car, admin.ModelAdmin)
admin.site.register(Service, admin.ModelAdmin)
admin.site.register(Reservation, admin.ModelAdmin)
admin.site.register(Price, admin.ModelAdmin)
