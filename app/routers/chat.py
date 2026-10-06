import itertools
import time

from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix="/api/chat", tags=["chat"])

_seq = itertools.count(1)


class ChatRequest(BaseModel):
    message: str = Field(min_length=1)
    conversation_id: str | None = None


class ChatResponse(BaseModel):
    reply: str
    conversation_id: str


@router.post("", response_model=ChatResponse)
async def send_message(payload: ChatRequest) -> ChatResponse:
    """占位聊天接口：目前为回显演示，后续在此接入 LLM / Agent 执行流程。"""
    n = next(_seq)
    reply = (
        f"【MorphUI 占位回复 #{n}】\n\n"
        f"已收到你的消息：\n\n“{payload.message}”\n\n"
        "FastAPI 后端已接通。下一步将在这里接入大模型与 Agent 流程，"
        "生成的页面会推送到右侧「实时预览」区域。"
    )
    return ChatResponse(
        reply=reply,
        conversation_id=payload.conversation_id or f"conv-{int(time.time() * 1000)}",
    )
