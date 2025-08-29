# Ponto de Venda (PDV) API

Sistema básico de PDV (Ponto de Venda) que permita o cadastro e gerenciamento de produtos e a realização de vendas. Esse sistema expoe APIs REST para que um frontend ou aplicativo móvel possa consumir,também permitir que um administrador gerencie os dados pelo Django Admin.

---

## Funcionalidades

* **Gerenciamento de Produtos:** Cadastro, listagem, visualização, atualização e exclusão de produtos.
* **Controle de Estoque:** O estoque de um produto é automaticamente atualizado (diminuído) após a realização de uma venda.
* **Registro de Vendas:** Criação de vendas.
* **Arquitetura MVC:** O projeto segue uma arquitetura modular, separando as responsabilidades em **Model**, **Controller** e **View** (Serializers).
* **Documentação Interativa:** Endpoint disponível para visualização e teste da API via Django REST Framework.

---

## Tecnologias Utilizadas

* **Linguagem:** Python 
* **Framework:** Django 
* **API:** Django REST Framework
* **Banco de Dados:** PostgreSQL
* **Gerenciamento de Dependências:** pip

---

## Pré-requisitos

Certifique-se de que as seguintes ferramentas estão instaladas em sua máquina:
* Python
* pip
* PostgreSQL

---

## Instalação e Configuração

Siga os passos abaixo para ter uma cópia do projeto em execução em sua máquina local.

1.  **Clone o repositório:**
    --
2.  **Crie e ative o ambiente virtual:**
    ```bash
    python -m venv venv
    # No Windows:
    venv\Scripts\activate
    

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure o banco de dados:**
    * No arquivo `system/settings.py`, configure as informações do seu banco de dados PostgreSQL.

5.  **Execute as migrações:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```
    A API estará disponível em `http://127.0.0.1:8000/`.

---

## Endpoints da API

A API está acessível em `http://127.0.0.1:8000/api/v1/`.

#### Produtos

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| **GET** | `/products/` | Lista todos os produtos. |
| **POST** | `/products/` | Cria um ou mais produtos (aceita lista de JSON). |
| **GET** | `/products/<uuid:pk>/` | Retorna um produto específico. |
| **PUT** | `/products/<uuid:pk>/` | Atualiza um produto específico. |
| **DELETE**| `/products/<uuid:pk>/` | Exclui um produto específico. |

#### Vendas

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| **GET** | `/sales/` | Lista todas as vendas. |
| **POST**| `/sales/` | Registra uma nova venda. |
| **GET** | `/sales/<uuid:pk>/` | Retorna uma venda específica. |

---

## AUTOR:  JUAN ALMEIDA

## Executando os testes

Para rodar os testes unitários do projeto, execute o seguinte comando:
```bash
python manage.py test