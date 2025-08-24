# ola_mundo/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProdutoForm
from .forms import Produto
from django.http import JsonResponse

def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto_cadastrado_com_sucesso')
    else:
        form = ProdutoForm()

    return render(request, 'cadastrar_produto.html', {'form': form})

def produto_cadastrado_com_sucesso(request):
    return render(request, 'sucesso.html')

def listar_produtos(request):
    if request.method == 'GET':
        produtos = Produto.objects.all().values()  # pega todos os registros
        return JsonResponse(list(produtos), safe=False)
    
def alterar_produto(request, pk):
    #Esta linha tenta buscar um objeto Produto com o ID (pk) fornecido na URL
    produto = get_object_or_404(Produto, pk=pk)
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto_cadastrado_com_sucesso') # ou para uma página de sucesso
    else:
        form = ProdutoForm(instance=produto)
        
    return render(request, 'cadastrar_produto.html', {'form': form})

def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    
    if request.method == 'POST':
        produto.delete()
        # Redireciona para uma página de sucesso (ou de listagem) após a exclusão
        return redirect('produto_deletado_com_sucesso')
    
    # Se a requisição for GET, exibe a página de confirmação
    return render(request, 'confirmar_exclusao.html', {'produto': produto})

def produto_deletado_com_sucesso(request):
    return render(request, 'sucesso_exclusao.html')

def listar_produtos(request):
    produtos = Produto.objects.all() # Busca todos os produtos do banco de dados
    return render(request, 'listar_produtos.html', {'produtos': produtos})
def tela_inicial(request):
    return render(request, 'tela_inicial.html')