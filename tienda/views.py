from django.shortcuts import render
from .models import Producto

# Create your views here.
def index(request):
    return render(request,'tienda/index.html')

def producto(request):
    productosListado = Producto.objects.all()
    return render(request,'tienda/producto.html', {"Productos": productosListado})

def manga(request):
    return render(request,'tienda/manga.html')

def gamer(request):
    return render(request,'tienda/gamer.html')

