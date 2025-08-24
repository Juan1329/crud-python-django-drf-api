# ola_mundo/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.tela_inicial, name='tela_inicial'),
    # Página para cadastrar um novo produto
    path('cadastrar-produto/', views.cadastrar_produto, name='cadastrar_produto'),
      # Página de sucesso após o cadastro
    path('cadastro-sucesso/', views.produto_cadastrado_com_sucesso, name='produto_cadastrado_com_sucesso'),
    #consulta de produtos via API
    path('produtos/', views.listar_produtos, name='listar_produtos'),
     # Nova URL para alterar o produto
     # <int:pk> é o ID do produto a ser alterado que será passado na URL 
     # quando for chamada para edição do produto está sendo capturado como 
     # parâmetro na view alterar_produto  
    path('alterar-produto/<int:pk>/', views.alterar_produto, name='alterar_produto'),

    # Nova URL para excluir o produto
     # <int:pk> é o ID do produto a ser excluído que será passado na URL
     #exmmpo: /excluir-produto/1/ para excluir o produto com ID 1
    path('excluir-produto/<int:pk>/', views.excluir_produto, name='excluir_produto'),
    path('exclusao-sucesso/', views.produto_deletado_com_sucesso, name='produto_deletado_com_sucesso'),
    path('lista-de-produtos/', views.listar_produtos, name='listar_produtos'),
]
