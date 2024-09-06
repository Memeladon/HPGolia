from sqlalchemy import text
from sqlalchemy.exc import OperationalError

from .models import db_connect


def init_db():
    try:
        with db_connect.engine.connect() as connection:
            # Проверка на наличие таблиц 'public'
            result = connection.execute(
                text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
            )
            tables = result.fetchall()

            # Если таблиц нет, инициализируем бд
            if not tables:
                print("Tables are missing, create them...")
                db_connect.Base.metadata.create_all(bind=db_connect.engine)
                print("All tables have been successfully created!")
            else:
                print(f"Existing tables: {tables}")

    except OperationalError as e:
        print(f"Database connection error: {e}")
        raise


def clear_database():
    # Получаем список всех таблиц
    tables = db_connect.engine.execute(
        text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")).fetchall()

    # Удаляем все таблицы
    for table in tables:
        table_name = table[0]
        print(f"Удаляю таблицу: {table_name}")
        db_connect.Base.metadata.tables[table_name].drop(db_connect.engine)

    # Обновляем метаданные SQLAlchemy
    db_connect.Base.metadata.drop_all(db_connect.engine)
    db_connect.Base.metadata.create_all(db_connect.engine)

    print("Все таблицы успешно удалены.")
