# ola_mundo/models.py

from django.db import models

class Produto(models.Model):
    codigo_barras = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=200)
    marca = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_disponivel = models.IntegerField()

    def __str__(self):
       return f"{self.nome} - {self.marca}"
  
  