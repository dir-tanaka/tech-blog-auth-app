from pydantic import BaseModel

class DBConnectionStatus(BaseModel):
    status_code: int
    message: str