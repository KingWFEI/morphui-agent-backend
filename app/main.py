from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from app.demo_page import PREVIEW_HTML
from app.routers import chat, conversations

app = FastAPI(title="MorphUI Agent API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5273",
        "http://127.0.0.1:5273",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router)
app.include_router(conversations.router)


@app.get("/", tags=["system"])
def root() -> dict:
    return {"service": "morphui-backend", "docs": "/docs", "preview": "/preview"}


@app.get("/api/health", tags=["system"])
def health() -> dict:
    """健康检查：前端轮询该接口判断后端连接状态。"""
    return {"status": "ok", "service": "morphui-backend", "version": "0.1.0"}


@app.get("/preview", response_class=HTMLResponse, tags=["preview"])
def preview_demo() -> str:
    """演示页面：供前端「实时预览」面板的 iframe 加载。"""
    return PREVIEW_HTML
