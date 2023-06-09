from django.db import models

# Create your models here.
class Producto(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=6)
    nombre_producto = models.CharField(max_length=200)
    precio = models.PositiveSmallIntegerField()
    descripcion_producto = models.CharField(max_length=200)
    formato = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    editorial = models.CharField(max_length=80)
    idioma =  models.CharField(max_length=70)
    paginas = models.CharField(max_length=4)
    categoria = models.CharField(max_length=200)
    sinopsis = models.CharField(max_length=400)
    imagen = models.ImageField(upload_to="tienda/", null=True, blank=True)

    def __str__(self):
        texto = "({0}) {1}"
        return texto.format(self.id_producto, self.nombre_producto)
