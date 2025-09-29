from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.domain.models.user_model import CreateUser, User
from app.infrastructure.schemas.user_schemas import Users

async def get_user_dao(db_session: AsyncSession, user_id: int) -> User:
  stmt = select(Users).filter(Users.id == user_id)
  result = await db_session.execute(stmt)
  db_user = result.scalars().first()

  # ユーザーが見つからない場合はNoneを返す
  if db_user is None:
    return None

  # SQLAlchemyのモデルインスタンスをPydanticモデルに変換
  return User(
    id=db_user.id,
    name=db_user.name,
    description=db_user.description
  )

async def create_user_dao(db_session: AsyncSession, user: CreateUser) -> User:
  db_user = Users(name=user.name, description=user.description)
  # データベースにモデルのインスタンスを追加
  db_session.add(db_user)
  # 変更をコミットしてデータベースに永続化
  await db_session.commit()
  # データベースから更新されたインスタンスを再取得
  await db_session.refresh(db_user)
  return User(
    id=db_user.id,
    name=db_user.name,
    description=db_user.description,
  )

