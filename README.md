# API-Lista-de-Tarefas

# ✅ ToDo API

Uma API REST para gerenciamento de tarefas desenvolvida em **Python** utilizando **FastAPI** e **SQLAlchemy**.

Este projeto faz parte do meu portfólio e tem como objetivo praticar o desenvolvimento de APIs REST seguindo boas práticas de arquitetura, organização de código e persistência de dados.

---

## 🚀 Tecnologias

- Python 3.14
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

---

## 📂 Estrutura do Projeto

```
todo-api/
│
├── app/
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── todo.db
├── venv/
└── README.md
```

---

## 📚 O que foi desenvolvido até agora

### ✅ Estrutura inicial do projeto

- Ambiente virtual (`venv`)
- Organização dos arquivos
- Configuração do FastAPI
- Servidor Uvicorn

---

### ✅ Banco de Dados

Foi configurado o SQLite utilizando SQLAlchemy.

Arquivo responsável:

```
app/database.py
```

Funções implementadas:

- Criação da conexão com o banco
- Criação da Session
- Classe Base dos Models
- Função `get_db()` para gerenciamento automático das conexões

---

### ✅ Modelagem da tabela

Criado o Model:

```python
Task
```

Tabela:

```
tasks
```

Campos:

| Campo | Tipo |
|--------|------|
| id | Integer |
| titulo | String |
| descricao | String |
| concluida | Boolean |

---

### ✅ Schemas (Pydantic)

Criados os Schemas:

- TaskBase
- TaskCreate
- TaskResponse

Objetivo:

- validar dados recebidos
- definir formato das respostas
- separar entrada e saída da API

---

### ✅ CRUD

Implementado:

- ✔ Criar tarefa

Função:

```python
create_task()
```

---

### ✅ Endpoint criado

```
POST /tasks
```

Responsável por cadastrar novas tarefas.

Exemplo:

```json
{
    "titulo": "Estudar FastAPI",
    "descricao": "Criar minha primeira API"
}
```

Resposta:

```json
{
    "id": 1,
    "titulo": "Estudar FastAPI",
    "descricao": "Criar minha primeira API",
    "concluida": false
}
```

---

## 📌 Próximas etapas

- [ ] Listar tarefas
- [ ] Buscar tarefa por ID
- [ ] Atualizar tarefa
- [ ] Excluir tarefa
- [ ] Tratamento de erros
- [ ] Validações
- [ ] PostgreSQL
- [ ] Docker
- [ ] Testes automatizados
- [ ] Front-end
- [ ] Deploy

---

## 🎯 Objetivo

Construir uma API REST completa utilizando boas práticas de desenvolvimento para compor meu portfólio como desenvolvedor Back-end Python.

Cada etapa do projeto está sendo documentada e desenvolvida de forma incremental, permitindo acompanhar a evolução da aplicação desde sua criação até uma versão pronta para produção.

---
