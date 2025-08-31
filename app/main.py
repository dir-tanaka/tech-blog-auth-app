from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from db.database import get_db
from db.schemas import GetAccount, CreateAccount
from models import models
from services.crud import get_user, create_user


from pydantic import BaseModel
from typing import List

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/account/{account_id}", response_model=GetAccount)
async def read_account(account_id: int, db: AsyncSession = Depends(get_db)):
    # crud.get_userの呼び出しにawaitを追加
    db_account = await get_user(db, account_id=account_id)
    if db_account is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_account

# シンプルなJSON Bodyの受け取り
# FastAPIのエンドポイント
@app.post("/user/")
async def create_account(account: CreateAccount, db: AsyncSession = Depends(get_db)):
    # ここでdbセッションをcreate_userに渡す
    db_account = await create_user(db, account)
    # レスポンスbody
    return {"res": "ok", "id": db_account.id, "名前": db_account.name}


# データベース接続確認エンドポイント
@app.get("/db_check")
async def db_check(db: AsyncSession = Depends(get_db)):
    try:
        # 簡単なクエリを実行して接続を確認
        await db.execute(select(1))
        return {"message": "Successfully connected to PostgreSQL via SQLAlchemy."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not connect to PostgreSQL via SQLAlchemy: {e}")
