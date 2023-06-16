from django.shortcuts import render
from .models import Producto

# Create your views here.
def index(request):
    productosListado = Producto.objects.all()
    return render(request,'tienda/index.html',{"Productos": productosListado})

def producto(request,pk):
    productosListado = Producto.objects.get(id_producto=pk)
    return render(request,'tienda/producto.html', {"Productos": productosListado})

def manga(request):
    productosListado = Producto.objects.all()
    return render(request,'tienda/manga.html',{"Productos": productosListado})


