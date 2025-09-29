from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from app.domain.services.user_service import get_user_service, create_user_service
from app.domain.models.user_model import User, GetUser, CreateUser

from app.infrastructure.core import get_db


from pydantic import BaseModel
from typing import List

router = APIRouter()

@router.get("/{user_id}", response_model=GetUser)
async def get_user(user_id: int, db_session: AsyncSession = Depends(get_db)):
  user = await get_user_service(db_session, user_id)
  return GetUser(id=user.id, name=user.name)

# シンプルなJSON Bodyの受け取り
# FastAPIのエンドポイント
@router.post("/create")
async def create_user(user: CreateUser, db_session: AsyncSession = Depends(get_db)):
  # ここでdbセッションをcreate_userに渡す
  new_user = await create_user_service(db_session, user)
  # レスポンスbody
  return {"res": "ok", "id": new_user.id, "name": new_user.name}
