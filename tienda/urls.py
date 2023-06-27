from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('producto/<id>', views.producto, name='producto'),
    path('manga', views.manga, name='manga'),
    path('agregar-producto', views.agregarProducto, name='agregarProducto'),
    path('listar-producto', views.listarProducto, name='listarProducto'),
    path('modificar-producto/<id>', views.modificarProducto, name='modificarProducto'),
    path('eliminar-producto/<id>', views.eliminarProducto, name='eliminarProducto'),
    path('control-panel', views.controlPanel, name='controlPanel'),
    path('registro', views.registro, name='registro'),
    path('carrito', views.carrito, name='carrito'),
    path('agregar-producto-carrito/<int:id>', views.agregar_producto, name='agregarProductoCarrito'),
    path('eliminar-producto-carrito/<int:id>', views.eliminar_producto, name='eliminarProductoCarrito'),
    path('restar-producto-carrito/<int:id>', views.restar_producto, name='restarProductoCarrito'),
    path('limpiar-producto-carrito', views.limpiar_carrito, name='limpiarProductoCarrito'),
]
