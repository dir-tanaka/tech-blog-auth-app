from logging.config import fileConfig

import asyncio
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine # <-- 変更: AsyncEngine, create_async_engine をインポート

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

# ここをあなたのBaseオブジェクトのインポートと設定に置き換えてください
# 例: from app.database import Base
# target_metadata = Base.metadata
# 正しいパスと変数名に置き換えてください
from app.infrastructure.core import Base # 仮定: あなたのBaseオブジェクトが app/database.py にある場合
target_metadata = Base.metadata # <-- 修正: あなたのBase.metadata を設定


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    # connectable を AsyncEngine として作成
    connectable = create_async_engine(
        config.get_main_option("sqlalchemy.url"),
        poolclass=pool.NullPool,
        echo=True
    )

    # 非同期マイグレーションを実行するためのラッパー関数を呼び出す
    asyncio.run(run_async_migrations(connectable))


async def run_async_migrations(connectable: AsyncEngine):
    """Non-sync run migrations (for asyncio)."""
    async with connectable.connect() as connection:
        # connection.run_sync() を使って、同期的な do_run_migrations を非同期コンテキストで実行
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()


def do_run_migrations(connection):
    """Inner function to run migrations in the context."""
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,
        dialect_opts={"paramstyle": "named"}
    )

    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
