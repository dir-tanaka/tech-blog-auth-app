from fastapi import APIRouter, Depends
from app.domain.models.healthcheck_model import DBConnectionStatus

from app.domain.services.healthcheck_service import verify_db_connection
from app.infrastructure.core import AsyncSessionLocal, get_db

router = APIRouter()

# データベース接続確認エンドポイント
@router.get("/readiness")
async def healthcheck_readiness():
  return {"status": "ok"}

# データベース接続確認エンドポイント
@router.get("/startup", response_model=DBConnectionStatus)
async def healthcheck_startup(db_session: AsyncSessionLocal = Depends(get_db)):
  return await verify_db_connection(db_session)
