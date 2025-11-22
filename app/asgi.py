# app/asgi.py

from fastapi import FastAPI
from app.modules import user_module, healthcheck_module
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173", # Reactアプリのオリジン
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# prefixとtagsを指定してルーターを含める
app.include_router(user_module.router, prefix="/users", tags=["users"])
app.include_router(healthcheck_module.router, prefix="/health", tags=["healthcheck"])
