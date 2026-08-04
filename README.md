# ✅ ToDo API

API REST para gerenciamento de tarefas desenvolvida com **Python**, **FastAPI**, **SQLAlchemy** e **PostgreSQL**.

O projeto faz parte do meu portfólio e foi criado com o objetivo de praticar desenvolvimento back-end, organização de código, persistência de dados, testes automatizados e conteinerização com Docker.

---
Front-end deste projeto:
https://github.com/RafaDavila/API-Lista-de-Tarefas-FrontEnd

## 🌐 API publicada

A aplicação está disponível publicamente no Render:

- Front-end publicado: https://todo-app-frontend-e35w.onrender.com

- Documentação Swagger: https://api-lista-de-tarefas-zjn5.onrender.com/docs
- Health check: https://api-lista-de-tarefas-zjn5.onrender.com/health
- Rota inicial: https://api-lista-de-tarefas-zjn5.onrender.com/

## 🚀 Tecnologias utilizadas

- Python 3.14
- FastAPI
- SQLAlchemy
- PostgreSQL
- Psycopg
- Pydantic
- Uvicorn
- Pytest
- Docker
- Docker Compose
- Git e GitHub
- Alembic
- Render
- CORS Middleware

---

## 📂 Estrutura do projeto

```text
todo-api/
│
├── app/
│   ├── routers/
│   │   ├── __init__.py
│   │   └── tasks.py
│   │
│   ├── __init__.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── tests/
│   ├── conftest.py
│   └── test_main.py
│
├── .dockerignore
├── .env
|── .env.example
|── alembic/
|── alembic.ini
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt

```
 
## 📌 Funcionalidades

A API permite:

- Criação de tarefas
- Listagem de tarefas
- Busca de tarefa por ID
- Atualização de tarefas
- Exclusão de tarefas
- Registro da data de criação
- Validação de dados com Pydantic
- Tratamento de erros 404
- Integração com front-end React por CORS


## 🔗 Endpoints

| Método   | Endpoint           | Descrição                          |
| -------- | ------------------ | ---------------------------------- |
| `POST`   | `/tasks/`          | Cria uma nova tarefa               |
| `GET`    | `/tasks/`          | Lista todas as tarefas             |
| `GET`    | `/tasks/{task_id}` | Busca uma tarefa pelo ID           |
| `PUT`    | `/tasks/{task_id}` | Atualiza uma tarefa                |
| `DELETE` | `/tasks/{task_id}` | Exclui uma tarefa                  |
| `GET`    | `/health`          | Verifica se a API está funcionando |
| `GET`    | `/`                | Exibe informações básicas da API   |


## 📝 Exemplo de criação de tarefa
```
{
  "titulo": "Estudar FastAPI",
  "descricao": "Continuar o desenvolvimento da API"
}
```
Resposta
```
{
  "id": 1,
  "titulo": "Estudar FastAPI",
  "descricao": "Continuar o desenvolvimento da API",
  "concluida": false,
  "data_criacao": "2026-07-31T20:41:53.340247Z"
}

```
A criação retorna o código HTTP: ``` 201 created ```

## 🔄 Migrações com Alembic

O projeto utiliza Alembic para versionar alterações na estrutura do banco de dados.

As migrações permitem:

- adicionar ou remover colunas;
- criar ou alterar tabelas;
- manter diferentes ambientes com a mesma estrutura;
- aplicar mudanças sem recriar o banco manualmente.

Para aplicar todas as migrações pendentes:

```bash
alembic upgrade head

```



## ✅ Validações

Os dados recebidos pela API são validados com Pydantic.

- Título
- Obrigatório
- Mínimo de 3 caracteres
- Máximo de 100 caracteres
- Descrição
- Opcional
- Máximo de 500 caracteres

Quando os dados enviados são inválidos, a API retorna: ``` 422 Unprocessable Entity ```

Quando uma tarefa não é encontrada, a API retorna: ``` 404 Not Found ```

Exemplo:
```
{
  "detail": "Tarefa não encontrada"
}
```
Banco de dados

A aplicação utiliza PostgreSQL para persistência dos dados.

A conexão é configurada por meio da variável de ambiente:
```
DATABASE_URL=postgresql+psycopg://usuario:senha@localhost:5432/todo_db
```
O SQLAlchemy é responsável por:

- Criar a conexão com o banco
- Gerenciar as sessões
- Mapear a tabela tasks
- Executar as operações de criação, consulta, atualização e exclusão

## 🧪 Testes automatizados

O projeto possui testes automatizados desenvolvidos com Pytest e o TestClient do FastAPI.

Os testes utilizam um banco SQLite em memória, separado do PostgreSQL principal. Dessa forma, os testes podem criar, atualizar e excluir dados sem alterar o banco real da aplicação.

Atualmente, o projeto possui 13 testes cobrindo:

- Health check
- Criação de tarefas
- Listagem de tarefas
- Busca de tarefa pelo ID
- Atualização de tarefas
- Exclusão de tarefas
- Busca de tarefa inexistente
- Atualização de tarefa inexistente
- Exclusão de tarefa inexistente
- Título com menos de 3 caracteres
- Requisição sem título
- Título com mais de 100 caracteres
- Descrição com mais de 500 caracteres

Para executar os testes:
```
python -m pytest -v
```
Resultado esperado: 14 passed 1 warning

## 🐳 Executando com Docker

O projeto utiliza Docker Compose para executar a API e o PostgreSQL em containers separados.

### Serviços
 - todo_api
 Container responsável pela aplicação FastAPI.
 - todo_db
 Container responsável pelo PostgreSQL.

O Docker Compose também cria:

- Uma rede interna entre a API e o banco
- Um volume para persistência dos dados
- Um healthcheck para verificar se o PostgreSQL está pronto

## Iniciar a aplicação

- Na raiz do projeto, execute:
 ``` docker compose up --build ```
- Para executar em segundo plano:
 ``` docker compose up --build -d ```
- Depois, acesse: 
 http://localhost:8000/docs
- A rota de verificação está disponível em:
 http://localhost:8000/health

### Verificar os containers
```
docker compose ps
```
### Parar os containers
```
docker compose down 
```
## Executando sem Docker

Crie e ative um ambiente virtual:

### Windows 
```
python -m venv venv
venv\Scripts\Activate.ps1
```
Instale as dependências: ``` pip install -r requirements.txt ```

Configure a variável DATABASE_URL em um arquivo .env.
Depois execute em: ``` uvicorn app.main:app --reload ```

A documentação estará disponível em: http://127.0.0.1:8000/docs

## CORS

A API permite requisições dos ambientes utilizados pelo front-end:

```text
http://localhost:5173
http://localhost:4173
https://todo-app-frontend-e35w.onrender.com
```



## Etapas concluídas
 - Estrutura inicial do projeto
 - Configuração do FastAPI
 - CRUD completo
 - Organização das rotas com APIRouter
 - Validações com Pydantic
 - Tratamento de erros
 - Migração de SQLite para PostgreSQL
 - Variáveis de ambiente
 - Testes automatizados
 - Dockerfile
 - Docker Compose
 - PostgreSQL em container
 - Persistência com volume
 - Healthcheck do banco
 - Migrações com Alembic
 - Coluna de data de criação
 - Aplicação automática das migrações no Docker

 ## Próximas etapas
- Autenticação de usuários com JWT
- Tarefas individuais por usuário
- Edição de título e descrição
- Filtros por tarefas pendentes e concluídas
- Testes automatizados do front-end
- Paginação da lista
- Melhorias de acessibilidade

 ## Observação 
 Atualmente, a aplicação utiliza uma lista pública e compartilhada.

Como ainda não existe autenticação, todos os visitantes acessam as mesmas tarefas e podem criar, atualizar ou excluir itens.

Uma futura evolução do projeto será adicionar autenticação com JWT e associar cada tarefa ao seu respectivo usuário.

## Autor

Desenvolvido por Rafael Davila.

GitHub: https://github.com/RafaDavila