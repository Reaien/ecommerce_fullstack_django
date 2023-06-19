from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def index(request):
    productosListado = Producto.objects.all()
    return render(request,'tienda/index.html',{"Productos": productosListado})

def producto(request,pk):
    #select * from prudctos where id_producto = 1
    productosListado = Producto.objects.get(id_producto=pk)
    return render(request,'tienda/producto.html', {"Productos": productosListado})

def manga(request):
    productosListado = Producto.objects.all()
    return render(request,'tienda/manga.html',{"Productos": productosListado})

def agregarProducto(request):

    data = {"form" : ProductoForm()}

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Producto guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, 'tienda/producto/agregar.html', data)


def listarProducto(request):
    productoListado = Producto.objects.all()
    data = {"Productos": productoListado}
    return render(request, 'tienda/producto/listar.html', data)
