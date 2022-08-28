from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.
class Producto(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    fecha = models.DateField()

class Comida(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    fecha = models.DateField(auto_created=True, auto_now=True)


    