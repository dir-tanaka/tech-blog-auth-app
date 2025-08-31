import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLAlchemyのデータベースURLを構築
# PostgreSQL + asyncpg ドライバを使用
SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://postgres:password@postgresql:5432/example"

# 非同期エンジンを作成
# echo=True は、実行されるSQL文をログに出力します (開発時に便利)
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# セッションファクトリの作成
# expire_on_commit=False にすることで、コミット後にオブジェクトがデタッチされません
AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession  # 非同期セッションを指定
)

# データベースモデルの基底クラス
Base = declarative_base()

# 依存性注入のためのDBセッション取得関数
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()