from app.domain.models.healthcheck_model import DBConnectionStatus
from app.infrastructure.core import AsyncSessionLocal
from sqlalchemy.future import select

async def verify_db_connection(db_session: AsyncSessionLocal) -> DBConnectionStatus: # type: ignore
  try:
    # type: ignore
    await db_session.execute(select(1))
    return DBConnectionStatus(status_code=200, message="Successfully connected to PostgreSQL via SQLAlchemy.")
  except Exception as e:
      # 例外を発生させる代わりに、失敗した旨を伝えるモデルを返す
      return DBConnectionStatus(
          status_code=500,
          message=f"Could not connect to PostgreSQL via SQLAlchemy: {e}"
      )

