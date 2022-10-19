

from django.db import models

class Rubro(models.Model):
    nombre = models.CharField(max_length = 128)
    def __str__(self) -> str:
        return f"{self.nombre}"
    
class Gasto(models.Model):
    fecha = models.DateField()
    rubro  = models.ForeignKey(Rubro, on_delete=models.SET_NULL, null= True)
    descripcion = models.CharField(max_length = 128)
    importe = models.CharField(max_length = 10)
