from django.db import models

# Create your models here.
# hay que seguir unas pautas , crear una clase , que herede de la superclase models.Model


class Mi_blog(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField()
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now = True)

