from django.urls import path
from Servicios import views

urlpatterns = [
    path('', views.Servicios, name="Servicios"),
]

