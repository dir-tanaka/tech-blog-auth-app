from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.models import Account
from db.schemas import GetAccount, CreateAccount

async def get_user(db: AsyncSession, account_id: int):
  # selectステートメントを使用する
  stmt = select(Account).filter(Account.id == account_id)
  result = await db.execute(stmt)
  return result.scalars().first()

async def create_user(db: AsyncSession, account: CreateAccount):
  db_account = Account(name=account.name)
  # データベースにモデルのインスタンスを追加
  db.add(db_account)
  # 変更をコミットしてデータベースに永続化
  await db.commit()
  # データベースから更新されたインスタンスを再取得
  await db.refresh(db_account)
  return db_account
