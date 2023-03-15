from django.db import models

# Create your models here.

class Persona:
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=20)
    mail = models.EmailField()

class Profes(models.Model, Persona):
    pass