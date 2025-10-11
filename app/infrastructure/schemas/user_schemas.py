from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timedelta, timezone
from app.infrastructure.core import Base

# 日本時間 (JST) のタイムゾーンオフセットを設定
# JSTはUTC+9時間です。
JST = timezone(timedelta(hours=+9))

# JSTの現在時刻を取得する関数
def jst_now():
    return datetime.now(JST)

# class Users(Base):
#     __tablename__ = "User" # テーブル名

#     user_id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     password_hash = Column(String, index=True)
#     created_at = Column(String, index=True)
#     updated_at = Column(String, index=True)

class Users(Base):
    __tablename__ = "user" # テーブル名

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    password_hash = Column(String, index=True)
    salt = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), default=jst_now) 
    updated_at = Column(DateTime(timezone=True), default=jst_now, onupdate=jst_now)