from django.urls import path
from . import views

urlpatterns=[
    path('index', views.index, name='index'),
    path('producto', views.producto, name='producto'),
    path('manga', views.manga, name='manga'),
    path('gamer', views.gamer, name='gamer')
]
