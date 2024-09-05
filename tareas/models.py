from django.db import models

# Create your models here.
class Tarea(models.Model):
    opcionesEstado = [
        ('completo','COMPLETO'),
        ('incompleto','INCOMPLETO')
        
    ]
    titulo = models.CharField(max_length=80)
    descripcion = models.TextField(max_length=600)
    estado = models.CharField(max_length=20, choices=opcionesEstado, default='incompleto')
    def __str__(self):
        return self.titulo

