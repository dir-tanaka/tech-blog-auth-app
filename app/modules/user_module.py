from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.services.user_service import create_user_service, login_user_service
from app.domain.models.user_model import RequestUser

from app.infrastructure.core import get_db

from typing import List

router = APIRouter()

# シンプルなJSON Bodyの受け取り
# FastAPIのエンドポイント
@router.post("/create")
async def create_user(user: RequestUser, db_session: AsyncSession = Depends(get_db)):
  # ここでdbセッションをcreate_userに渡す
  new_user = await create_user_service(db_session, user)
  # レスポンスbody
  return {"res": "ok", "id": new_user.id, "email": new_user.email}

@router.post("/login")
async def login_user(user: RequestUser, db_session: AsyncSession = Depends(get_db)):
  # ここでdbセッションをcreate_userに渡す
  token: dict = await login_user_service(db_session, user)
  # レスポンスbody
  return {"res": "ok", "token": token}
