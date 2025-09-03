# ola_mundo/forms.py

from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['codigo_barras', 'nome', 'marca', 'valor', 'quantidade_disponivel']
