from django.shortcuts import render, redirect, get_object_or_404
from tienda.carrito import Carrito
from .models import Producto
from .forms import ProductoForm, CustomUserCreationForm, UserModForm
from django.contrib.auth.models import User
from django.contrib import messages
#IMPORTANTE AUTENTICAR
from django.contrib.auth import authenticate, login #estas 2 funciones permitiran autenticar al usuario
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.


#mostrar productos en index
def index(request):
    productosListado = Producto.objects.all()
    return render(request,'tienda/index.html',{"Productos": productosListado})

#mostrar detalle de producto
def producto(request,id):
    #select * from prudctos where id_producto = 1
    productosListado = Producto.objects.get(id = id)
    return render(request,'tienda/producto.html', {"Productos": productosListado})

#listar productos en manga
def manga(request):
    productosListado = Producto.objects.filter(tipo_producto=1)
    return render(request,'tienda/manga.html',{"Productos": productosListado})

#listar productos en ropa
def ropa(request):
    productosListado = Producto.objects.filter(tipo_producto=2)
    return render(request,'tienda/ropa.html',{"Productos": productosListado})

#listar productos en figura
def figura(request):
    productosListado = Producto.objects.filter(tipo_producto=3)
    return render(request,'tienda/figura.html',{"Productos": productosListado})

#listar productos en anime
def anime(request):
    productosListado = Producto.objects.filter(tipo_producto=4)
    return render(request,'tienda/anime.html',{"Productos": productosListado})



#seccion CRUD con permisos de autorizacion
@permission_required('tienda.add_producto')
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


@permission_required('tienda.view_producto')
#listar productos para control panel
def listarProducto(request):
    productoListado = Producto.objects.all()
    data = {"Productos": productoListado}
    return render(request, 'tienda/producto/listar.html', data)


@permission_required('tienda.change_producto')
#modificar producto para control panel
def modificarProducto(request,id):
    #select * from prudctos where id_producto = 1
    producto = get_object_or_404(Producto, id = id)
    data = {'form': ProductoForm(instance=producto)}

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto modificado correctamente")
            return redirect(to="listarProducto")
        data['form'] = formulario

    return render(request,'tienda/producto/modificar.html', data)

@permission_required('tienda.delete_producto')
#eliminar para control panel
def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Producto eliminado correctamente")
    return redirect(to="listarProducto")

@permission_required('tienda.delete_producto')
def controlPanel(request):
    return render(request, 'tienda/producto/panel_control.html')

@permission_required('tienda.delete_producto')
def listar_usuarios(request):
    listadoUsuarios = User.objects.all()
    data = {'usuarios': listadoUsuarios}
    return render(request, 'tienda/producto/listar_usuarios.html', data)

@permission_required('tienda.change_producto')
#modificar producto para control panel
def modificarUsuario(request,id):
    #select * from prudctos where id_producto = 1
    usuario = get_object_or_404(User, id = id)
    data = {'form': UserModForm(instance=usuario)}

    if request.method == 'POST':
        formulario = UserModForm(data=request.POST, instance=usuario, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Usuario modificado correctamente")
            return redirect(to="listarUsuarios")
        data['form'] = formulario

    return render(request,'tienda/producto/modificar_usuario.html', data)
#FIN seccion CRUD con permisos de autorizacion


#registro de usuario
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




#seccion carrito
def carrito(request):
    productosListado = Producto.objects.all()
    data = {"productos": productosListado}
    return render(request,'tienda/carrito.html',data)    

def agregar_producto(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito.agregar(producto)
    return redirect(to='carrito')

def eliminar_producto(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito.eliminar(producto)
    return redirect('carrito')

def restar_producto(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito.restar(producto)
    return redirect('carrito')

def limpiar_carrito(request):
    carrito= Carrito(request)
    carrito.limpiar()
    return redirect('carrito')
