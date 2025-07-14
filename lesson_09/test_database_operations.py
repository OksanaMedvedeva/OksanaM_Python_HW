import pytest  # noqa: F401
from sqlalchemy import create_engine, text, inspect

# Строка подключения к базе данных
db_connection_string = "postgresql://postgres:John62rus@localhost:5432/QA"

# Создаем подключение к базе данных
engine = create_engine(db_connection_string)


def test_db_connection():
    # Используем инспектор для получения информации о таблицах
    inspector = inspect(engine)
    names = inspector.get_table_names()
    assert 'student' in names


def test_insert_student():
    # Создаем соединение
    with engine.connect() as connection:
        # SQL-запрос для добавления студента
        sql = text("INSERT INTO student ("
                   "user_id,"
                   " level, "
                   "education_form,"
                   " subject_id"
                   ") "
                   "VALUES (:user_id, :level, :education_form, :subject_id)")
        connection.execute(sql, {
            "user_id": 1, "level": "Beginner",
            "education_form": "group", "subject_id": 1
        })

        # Проверяем, что студент добавлен
        check_sql = text("SELECT level FROM student WHERE user_id = :user_id")
        result = connection.execute(check_sql, {"user_id": 1}).fetchone()
        assert result[0] == "Beginner"

        # Удаляем студента после теста
        delete_sql = text("DELETE FROM student WHERE user_id = :user_id")
        connection.execute(delete_sql, {"user_id": 1})


def test_update_student():
    # Создаем соединение
    with engine.connect() as connection:
        # Сначала добавляем студента
        insert_sql = text("INSERT INTO student ("
                          "user_id,"
                          " level,"
                          " education_form,"
                          " subject_id) "
                          "VALUES (:user_id, :level, "
                          ":education_form, :subject_id)"
                          )
        connection.execute(insert_sql, {
            "user_id": 2, "level": "Beginner",
            "education_form": "group", "subject_id": 1
        })

        # SQL-запрос для изменения данных студента
        update_sql = text("UPDATE student SET level = :level "
                          "WHERE user_id = :user_id")
        connection.execute(update_sql, {
            "level": "Intermediate", "user_id": 2
        })

        # Проверяем, что данные изменились
        check_sql = text("SELECT level FROM student "
                         "WHERE user_id = :user_id")
        result = connection.execute(check_sql,
                                    {"user_id": 2}).fetchone()
        assert result[0] == "Intermediate"

        # Удаляем студента после теста
        delete_sql = text("DELETE FROM student "
                          "WHERE user_id = :user_id")
        connection.execute(delete_sql, {"user_id": 2})


def test_delete_student():
    # Создаем соединение
    with engine.connect() as connection:
        # Сначала добавляем студента
        insert_sql = text("INSERT INTO student ("
                          "user_id,"
                          "level,"
                          "education_form,"
                          "subject_id) "
                          "VALUES (:user_id, :level, "
                          ":education_form, :subject_id)")
        connection.execute(insert_sql, {
            "user_id": 3, "level": "Beginner",
            "education_form": "group", "subject_id": 1
        })

        # SQL-запрос для удаления студента
        delete_sql = text("DELETE FROM student "
                          "WHERE user_id = :user_id")
        connection.execute(delete_sql, {"user_id": 3})

        # Проверяем, что студент удален
        check_sql = text("SELECT user_id FROM student "
                         "WHERE user_id = :user_id")
        connection.execute(check_sql, {"user_id": 3}).fetchone()
