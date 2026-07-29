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

def test_get_nonexistent_task(client):
        response = client.get("/tasks/999")

        assert response.status_code == 404
        assert response.json() == {"detail": "Tarefa não encontrada"}

def test_update_nonexistent_task(client):
    updated_data = {
        "titulo": "Tarefa inexistente",
        "descricao": "Tentativa de atualização",
        "concluida": True
    }

    response = client.put(
        "/tasks/999",
        json=updated_data
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Tarefa não encontrada"}

def test_delete_nonexistent_task(client):
    response = client.delete("/tasks/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Tarefa não encontrada"}


def test_create_task_with_short_title(client):
    task_data = {
        "titulo": "Oi",
        "descricao": "Título com menos de três caracteres"
    }

    response = client.post("/tasks/", json=task_data)

    assert response.status_code == 422

def test_create_task_without_title(client):
    task_data = {
        "descricao": "Tarefa sem título"
    }

    response = client.post("/tasks/", json=task_data)

    assert response.status_code == 422

def test_create_task_with_long_title(client):
    task_data = {
        "titulo": "A" * 101,
        "descricao": "Título acima do limite permitido"
    }

    response = client.post("/tasks/", json=task_data)

    assert response.status_code == 422

def test_create_task_with_long_description(client):
    task_data = {
        "titulo": "Descrição longa",
        "descricao": "A" * 501
    }

    response = client.post("/tasks/", json=task_data)

    assert response.status_code == 422