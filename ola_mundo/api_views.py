# ola_mundo/api_views.py

from rest_framework import generics
from .models import Produto
from .serializers import ProdutoSerializer

class ProdutoListCreate(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ProdutoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer