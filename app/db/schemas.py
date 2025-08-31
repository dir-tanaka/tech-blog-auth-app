from typing import List, Union
from pydantic import BaseModel

class GetAccount(BaseModel):
  id: int
  name: str
  description: str

class CreateAccount(BaseModel):
  name: str
