from datetime import datetime
from typing import List, Union
from pydantic import BaseModel

class User(BaseModel):
  id: int
  email: str
  password_hash: str
  salt: str
  created_at: datetime
  updated_at: datetime

class GetUser(BaseModel):
  email: str
  password_hash: str
  salt: str

class RequestUser(BaseModel):
  email: str
  password: str

class CreateUser(BaseModel):
  email: str
  password_hash: str
  salt: str
