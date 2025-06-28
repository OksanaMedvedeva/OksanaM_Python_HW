import pytest  # noqa: F401
from yougile_api import YougileAPI

# Инициализация API клиента
api_key = ("EkfXF+DAa-zeJmU77qdxaK-6JvpyI4"
           "t3Xyzm87XMZ6vKBU2lmTYy7PoeP+MCkFxb")
base_url = "https://ru.yougile.com/api-v2"
yougile_api = YougileAPI(base_url, api_key)

# Тестовые данные
test_project_title = "Test Project"
test_project_users = {"f9407d0d-9242-482a-ad9"
                      "0-3e2a89a2ba3e": "admin"}


def test_create_project():
    # Проверяет успешное создание проекта
    response = yougile_api.create_project(
        test_project_title, test_project_users
    )
    assert response.status_code == 201
    # Получаем ID созданного проекта, оно не равно None
    project_id = response.json().get("id")
    assert project_id is not None
    # Удаляем проект после проверки
    yougile_api.update_project(project_id, deleted=True)


def test_create_project_negative():
    # Создание проекта с пустым названием завершается ошибкой
    response = yougile_api.create_project("", test_project_users)
    assert response.status_code != 201
    assert response.status_code == 400


def test_update_project():
    # Создаем проект
    create_response = yougile_api.create_project(
        test_project_title, test_project_users
    )
    assert create_response.status_code == 201
    # Получаем ID созданного проекта
    project_id = create_response.json().get("id")
    assert project_id is not None
    # Обновляем название проекта
    new_title = "Updated Test Project"
    response = yougile_api.update_project(
        project_id, title=new_title
    )
    assert response.status_code == 200
    project_id = response.json().get("id")
    assert project_id is not None
    # Удаляем проект после проверки
    yougile_api.update_project(project_id, deleted=True)


def test_update_project_negative():
    # Обновление несуществующего проекта завершается ошибкой
    response = yougile_api.update_project(
        "invalid_id", title="Updated Test Project"
    )
    assert response.status_code != 200
    assert response.status_code == 404


def test_get_project():
    # Создаем проект
    create_response = yougile_api.create_project(
        test_project_title, test_project_users
    )
    assert create_response.status_code == 201
    # Получаем ID созданного проекта
    project_id = create_response.json().get("id")
    assert project_id is not None
    # Получаем данные проекта по его ID
    response = yougile_api.get_project(project_id)
    assert response.status_code == 200
    assert response.json().get("id") == project_id
    assert response.json().get("title") == test_project_title
    # Удаляем проект после проверки
    yougile_api.update_project(project_id, deleted=True)


def test_get_project_negative():
    # Получение данных несуществующего проекта завершается ошибкой
    response = yougile_api.get_project("invalid_id")
    assert response.status_code != 200
    assert response.status_code == 404
