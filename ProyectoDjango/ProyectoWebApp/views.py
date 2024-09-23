from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, "Home.html")

def Tienda(request):
    return render(request, "Tienda.html")

def Contacto(request):
    return render(request, "Contacto.html")