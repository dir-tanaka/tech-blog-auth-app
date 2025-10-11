from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.domain.models.user_model import GetUser, User, CreateUser, RequestUser
from app.domain.services.auth.create_token import create_access_token
from app.domain.services.auth.password_hasher import PasswordHasher
from app.infrastructure.daos.user_dao import get_user_dao, create_user_dao

async def create_user_service(db_session: AsyncSession, requested_user: RequestUser) -> User:
  # passwordのハッシュ化
  password_hasher: PasswordHasher = await PasswordHasher.hash_password(requested_user.password)

  hashed_user = CreateUser(
    email=requested_user.email,
    password_hash=password_hasher.password_hash,
    salt=password_hasher.salt
  )

  # ユーザー登録Dao
  stored_user = await create_user_dao(db_session, hashed_user)

  return stored_user

async def login_user_service(db_session: AsyncSession, requested_user: RequestUser):
  # db登録のpassword hash, saltを取得
  db_user: GetUser = await get_user_dao(db_session, requested_user.email)
  # リクエストしてきたpasswordのハッシュ化
  request_password_hasher: PasswordHasher = await PasswordHasher.test_hash_password(
    db_user.salt,
    requested_user.password,
  )

  # ログイン検証
  if request_password_hasher != db_user.password_hash:
    raise HTTPException(status_code=400, detail="Inactive user")

  return create_access_token(db_user.__dict__)

