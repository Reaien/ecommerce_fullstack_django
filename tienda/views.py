from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm, CustomUserCreationForm
from django.contrib import messages
#IMPORTANTE AUTENTICAR
from django.contrib.auth import authenticate, login #estas 2 funciones permitiran autenticar al usuario

# Create your views here.


#mostrar productos en index
def index(request):
    productosListado = Producto.objects.all()
    return render(request,'tienda/index.html',{"Productos": productosListado})

#mostrar detalle de producto
def producto(request,pk):
    #select * from prudctos where id_producto = 1
    productosListado = Producto.objects.get(id_producto=pk)
    return render(request,'tienda/producto.html', {"Productos": productosListado})

#listar productos en manga
def manga(request):
    productosListado = Producto.objects.all()
    return render(request,'tienda/manga.html',{"Productos": productosListado})


#funcion para agregar producto
def agregarProducto(request):

    data = {"form" : ProductoForm()}

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Registrado")
        else:
            data["form"] = formulario
    return render(request, 'tienda/producto/agregar.html', data)



#listar productos para control panel
def listarProducto(request):
    productoListado = Producto.objects.all()
    data = {"Productos": productoListado}
    return render(request, 'tienda/producto/listar.html', data)

#modificar producto para control panel
def modificarProducto(request,pk):
    #select * from prudctos where id_producto = 1
    producto = get_object_or_404(Producto, id_producto = pk)
    data = {'form': ProductoForm(instance=producto)}

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto modificado correctamente")
            return redirect(to="listarProducto")
        data['form'] = formulario

    return render(request,'tienda/producto/modificar.html', data)


#eliminar para control panel
def eliminarProducto(request, pk):
    producto = get_object_or_404(Producto, id_producto = pk)
    producto.delete()
    messages.success(request, "Producto eliminado correctamente")
    return redirect(to="listarProducto")


def controlPanel(request):
    return render(request, 'tienda/producto/panel_control.html')


def registro(request):
    data = {'form': CustomUserCreationForm}

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #se recibe al usuario y la contraseña, con cleaned_data un diccionario que sirve para autenticar
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            #logear auto
            login(request,user)
            messages.success(request, "Te has registrado correctamente, redirigiendo al Home")
            return redirect(to='index')
        data["form"] = formulario
    return render(request,'registration/registro.html', data)
