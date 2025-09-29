from sqlalchemy import Column, Integer, String
from app.infrastructure.core import Base

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
    name = Column(String, index=True)
    description = Column(String, index=True)
