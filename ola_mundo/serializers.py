# ola_mundo/serializers.py

from rest_framework import serializers
from .models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'codigo_barras', 'nome', 'marca', 'valor', 'quantidade_disponivel']