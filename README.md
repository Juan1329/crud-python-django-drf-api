Objetivo: Ler, Alterar, Enviar e Deletar, consumir também via API
Linguagem: Python, HTML, Boostrap 
Framework: DJANGO DRF
Banco: Postgresql

Tela inicial: http://127.0.0.1:8000/orm/
Cadastro de produto: /orm/cadastrar-produto/ 
Lista de produto: /orm/lista-de-produto/ 
Editar produto: /orm/alterar-produto/3/
Excluir produto: /orm/excluir-produto/3/


Para Rodar o código voce precisa instalar o Python, pip e o postgre
Dentro de Settings coloca as informações do banco de dados criado no postgree: 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'casaracaodb',  #nome do banco criado
        'USER': 'petlar',       #usuário criado
        'PASSWORD': 'juan3030', #senha do usuário
        'HOST': 'localhost',    #se estiver rodando local
        'PORT': '5432',         #porta padrão do PostgreSQL
    }
Rode as migrações dentro do Terminal
python manage.py makemigrations ola_mundo
    python manage.py migrate

    Para executar o sistema é:
 python manage.py runserver

processo debug:
1- voce preenche informações no formulário:
http://127.0.0.1:8000/orm/cadastrar-produto/

2- Requisição chega no include:
meuprimeiroprojeto.urls  path('orm/', include('ola_mundo.urls')) 
Direcionado para ola_mundo.urls

3-Dentro de ola_mundo.URLS ele procura o caminho que foi passado na URL, no caso cadastro de produto
path('cadastrar-produto/', views.cadastrar_produto, name='cadastrar_produto')
Direcionado para Views cadastrar_produto

4- Na pasta de views, ele identifica a def ser executada:
def cadastrar_produto(request): 
Dentro de form ele identifica a class produto com os designados campos.
Realiza o insert into na tabela do banco de dados ola_mundo_produto
Direciona para o Template em HTML produto_cadastrado_com_sucesso

5-save feito no banco form.save()


===============API ============= 

1- Cliente enviar a solicitação pela url: http://127.0.0.1:8000/api/produtos/
com json {
    "codigo_barras": "01020",
    "nome": "Petisco",
    "marca": "melhor marca",
    "valor": "50",
    "quantidade_disponivel": 12
}
2- a requisição chega no meuprimeiroprojeto.url e identifica o PATH:
path('api/', include('ola_mundo.api_urls'))
Direcionado para o arquivo api_urls

3- no arquivo ele encontra a rota mencionada na URL /produtos/
path('produtos/', ProdutoListCreate.as_view(), name='produto-list-create'),
A classe ProdutoListCreate é uma view do Django Rest Framework recebe a requisição.
A view usa o serializer_class definido (ProdutoSerializer) para lidar com esses dados
Neste caso entra o DRF que cria uma instância e passa para ele 

4-Se os dados forem válidos, ele chama o método save() para criar uma nova instância do modelo Produto

5-ola_mundo/models.py e Banco de Dados:
save() do serializador interage com o Django ORM, ele pega a instância Python do modelo Produto e a transforma em um comando SQL INSERT

6- uma vez que desceu pro banco, o serializador pega o objeto Produto que acabou de ser salvo (agora com um ID) e o converte de volta para o formato JSON














