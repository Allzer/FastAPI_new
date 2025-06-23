import asyncio  # Добавлен импорт asyncio для асинхронных операций
from logging.config import fileConfig
import sys
from src.models.models_main_page.model import BookModel
from sqlalchemy import pool
from sqlalchemy.engine import Connection  # Добавлен импорт Connection
from sqlalchemy.ext.asyncio import (  # Добавлен импорт асинхронных компонентов
    AsyncEngine,
    create_async_engine,
)
from alembic import context

from database import Base
from database import DATABASE_URL  # Используем ваш готовый URL

# Конфигурация Alembic
config = context.config

# Настройка логгера
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Устанавливаем метаданные для миграций
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Запуск миграций в offline-режиме (например, для --autogenerate)."""
    # Используем ваш DATABASE_URL вместо URL из конфига
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,  # Включаем сравнение типов колонок
    )

    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection: Connection) -> None:
    """Фактическое выполнение миграций с использованием подключения."""
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,  # Включаем сравнение типов колонок
    )

    with context.begin_transaction():
        context.run_migrations()

async def run_async_migrations() -> None:
    """Асинхронный запуск миграций."""
    # Создаем асинхронный движок с вашим DATABASE_URL
    connectable: AsyncEngine = create_async_engine(
        DATABASE_URL,
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        # Запускаем миграции в синхронном режиме через асинхронное соединение
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()  # Корректно закрываем соединения

def run_migrations_online() -> None:
    """Запуск миграций в online-режиме (непосредственно к БД)."""
    # Для Windows необходимо установить специальную политику event loop
    if sys.platform.startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    # Запускаем асинхронные миграции
    asyncio.run(run_async_migrations())

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()