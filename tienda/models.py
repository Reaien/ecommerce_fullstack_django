from django.db import models

# Create your models here.

#tabla foranea categoria
class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombre_categoria)

#tabla tipo producto
class TipoProducto(models.Model):
    nombre_tipo_producto = models.CharField(max_length=100)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombre_tipo_producto)

#Tabla producto
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=200)
    precio = models.PositiveSmallIntegerField()
    descripcion_producto = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    tipo_producto = models.ForeignKey(TipoProducto,null=True, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="tienda/", null=True, blank=True)

