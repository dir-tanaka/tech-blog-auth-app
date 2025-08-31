from sqlalchemy import Column, Integer, String
from db.database import Base

class Account(Base):
    __tablename__ = "account" # テーブル名

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
