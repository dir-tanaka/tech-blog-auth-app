# app/asgi.py

from fastapi import FastAPI
from app.modules import user_module, healthcheck_module

app = FastAPI()

# prefixとtagsを指定してルーターを含める
app.include_router(user_module.router, prefix="/users", tags=["users"])
app.include_router(healthcheck_module.router, prefix="/health", tags=["healthcheck"])
