from django.urls import path
from . import views

urlpatterns=[
    path('index', views.index, name='index'),
    path('producto/<str:pk>', views.producto, name='producto'),
    path('manga', views.manga, name='manga'),
]
