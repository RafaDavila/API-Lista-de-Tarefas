def test_health_check(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_task(client):
    task_data = {
        "titulo": "Estudar Pytest",
        "descricao": "Criar testes automatizados para a API"
    }

    response = client.post("/tasks/", json=task_data)

    assert response.status_code == 201

    response_data = response.json()

    assert response_data["id"] == 1
    assert response_data["titulo"] == "Estudar Pytest"
    assert response_data["descricao"] == "Criar testes automatizados para a API"
    assert response_data["concluida"] is False


def test_get_tasks(client):
    task_data = {
        "titulo": "Estudar FastAPI",
        "descricao": "Continuar o projeto da API"
    }

    client.post("/tasks/", json=task_data)

    response = client.get("/tasks/")

    assert response.status_code == 200

    response_data = response.json()

    assert len(response_data) == 1
    assert response_data[0]["titulo"] == "Estudar FastAPI"
    assert response_data[0]["descricao"] == "Continuar o projeto da API"
    assert response_data[0]["concluida"] is False


def test_get_task_by_id(client):
    task_data = {
        "titulo": "Aprender testes",
        "descricao": "Testar uma tarefa pelo ID"
    }

    create_response = client.post("/tasks/", json=task_data)
    task_id = create_response.json()["id"]

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["id"] == task_id
    assert response_data["titulo"] == "Aprender testes"
    assert response_data["descricao"] == "Testar uma tarefa pelo ID"
    assert response_data["concluida"] is False

def test_update_task(client):
    task_data = {
        "titulo": "Estudar FastAPI",
        "descricao": "Revisar os endpoints"
    }

    create_response = client.post("/tasks/", json=task_data)
    task_id = create_response.json()["id"]

    updated_data = {
        "titulo": "Estudar Pytest",
        "descricao": "Criar testes para o CRUD",
        "concluida": True
    }

    response = client.put(
        f"/tasks/{task_id}",
        json=updated_data
    )

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["id"] == task_id
    assert response_data["titulo"] == "Estudar Pytest"
    assert response_data["descricao"] == "Criar testes para o CRUD"
    assert response_data["concluida"] is True

def test_delete_task(client):
    task_data = {
        "titulo": "Tarefa temporária",
        "descricao": "Esta tarefa será excluída"
    }

    create_response = client.post("/tasks/", json=task_data)
    task_id = create_response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200

    deleted_task = response.json()

    assert deleted_task["id"] == task_id
    assert deleted_task["titulo"] == "Tarefa temporária"

    get_response = client.get(f"/tasks/{task_id}")

    assert get_response.status_code == 404