# ola_mundo/api_urls.py

from django.urls import path
from .api_views import ProdutoListCreate, ProdutoRetrieveUpdateDestroy

urlpatterns = [
    path('produtos/', ProdutoListCreate.as_view(), name='produto-list-create'),
    path('produtos/<int:pk>/', ProdutoRetrieveUpdateDestroy.as_view(), name='produto-detail'),
]