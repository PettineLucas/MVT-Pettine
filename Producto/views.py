from django.shortcuts import render
from .models import Producto



# Create your views here.
def home(request):
    return render(request, 'home.html',context={})

def ver_producto(request):
    Producto = Producto.objects.create(name = "Agua",price=150, fecha="2022-8-23")  
    context = { 'producto': Producto}  
    return render(request, "home.html", context)

    
    