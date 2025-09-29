from typing import List, Union
from pydantic import BaseModel

class User(BaseModel):
  id: int
  name: str
  description: str

class GetUser(BaseModel):
  id: int
  name: str

class CreateUser(BaseModel):
  name: str
  description: str

