from django.shortcuts import render, redirect
from .forms import formulario_contacto

# Create your views here.

def Contacto(request):
    mi_formulario=formulario_contacto()

    if request.method=="POST":
        mi_formulario=formulario_contacto(data=request.POST)
        if mi_formulario.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            return redirect("/contacto/?valido")

    return render(request, "contacto/contacto.html", {"miFormulario": mi_formulario})