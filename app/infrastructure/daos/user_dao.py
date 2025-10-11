from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.domain.models.user_model import CreateUser, GetUser, User
from app.infrastructure.schemas.user_schemas import Users

async def get_user_dao(db_session: AsyncSession, email: str) -> GetUser:
  stmt = select(Users).filter(Users.email == email)
  result = await db_session.execute(stmt)
  db_user = result.scalars().first()

  # ユーザーが見つからない場合はNoneを返す
  if db_user is None:
    return None

  # SQLAlchemyのモデルインスタンスをPydanticモデルに変換
  return GetUser(
    email=db_user.email,
    password_hash=db_user.password_hash,
    salt=db_user.salt
  )

async def create_user_dao(db_session: AsyncSession, user: CreateUser) -> User:
  db_user = Users(email=user.email, password_hash=user.password_hash, salt=user.salt)
  # データベースにモデルのインスタンスを追加
  db_session.add(db_user)
  # 変更をコミットしてデータベースに永続化
  await db_session.commit()
  # データベースから更新されたインスタンスを再取得
  await db_session.refresh(db_user)
  return User(
    id=db_user.id,
    email=db_user.email,
    salt=db_user.salt,
    password_hash=db_user.password_hash,
    created_at=db_user.created_at,
    updated_at=db_user.updated_at,
  )

