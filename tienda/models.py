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
    formato = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    editorial = models.CharField(max_length=80)
    idioma =  models.CharField(max_length=70)
    paginas = models.CharField(max_length=4)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    sinopsis = models.CharField(max_length=400)
    tipo_producto = models.ForeignKey(TipoProducto,null=True, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="tienda/", null=True, blank=True)

