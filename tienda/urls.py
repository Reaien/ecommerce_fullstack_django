from django.urls import path
from . import views

urlpatterns=[
    path('index', views.index, name='index'),
    path('producto/<str:pk>', views.producto, name='producto'),
    path('manga', views.manga, name='manga'),
    path('agregar-producto', views.agregarProducto, name='agregarProducto'),
    path('listar-producto', views.listarProducto, name='listarProducto'),
    path('modificar-producto/<str:pk>', views.modificarProducto, name='modificarProducto'),
    path('eliminar-producto/<str:pk>/', views.eliminarProducto, name='eliminarProducto'),
    path('control-panel', views.controlPanel, name='controlPanel'),
]
