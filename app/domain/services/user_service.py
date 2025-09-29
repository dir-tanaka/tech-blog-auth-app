from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.domain.models.user_model import GetUser, User, CreateUser
from app.infrastructure.daos.user_dao import get_user_dao, create_user_dao

async def get_user_service(db_session: AsyncSession, user_id: int) -> User:
  # selectステートメントを使用する
  get_user_info = await get_user_dao(db_session, user_id)
  return get_user_info

async def create_user_service(db_session: AsyncSession, user: CreateUser) -> User:
  create_user_info = await create_user_dao(db_session, user)
  return create_user_info
  
