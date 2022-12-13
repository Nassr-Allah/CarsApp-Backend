"""CarProject DB_URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a DB_URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a DB_URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a DB_URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cars.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', CarCRUD.as_view(), name='cars'),
    path('cars/<int:pk>/', CarCRUD.as_view(), name='car'),
    path('cars/<str:name>/models/', CarModelCRUD.as_view(), name='models'),
    path('models/<int:pk>/', CarModelCRUD.as_view(), name='models'),
    path('models/', CarModelCRUD.as_view(), name='models'),
    path('services/', ServiceCRUD.as_view(), name='services'),
    path('reservations/', ReservationCRUD.as_view(), name='reservations'),
    path('reservations/<int:pk>/', ReservationCRUD.as_view(), name='reservations'),
    path('miniservices/', MiniServiceCRUD.as_view(), name='mini_services')
]
