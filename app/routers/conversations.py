from datetime import datetime, timedelta

from fastapi import APIRouter

router = APIRouter(prefix="/api/conversations", tags=["conversations"])


def _days_ago(days: int, hour: int, minute: int = 24) -> str:
    t = datetime.now() - timedelta(days=days)
    return t.replace(hour=hour, minute=minute, second=0, microsecond=0).isoformat()


# 演示数据：后续替换为数据库 / 文件存储
_DEMO_CONVERSATIONS = [
    {"id": "conv-demo-1", "title": "MorphUI 整体布局与主题设计", "updated_at": _days_ago(0, 9, 41)},
    {"id": "conv-demo-2", "title": "实时预览面板的 iframe 方案调研", "updated_at": _days_ago(0, 8, 12)},
    {"id": "conv-demo-3", "title": "FastAPI 接入大模型的接口设计", "updated_at": _days_ago(1, 21, 5)},
    {"id": "conv-demo-4", "title": "React 组件拆分与状态管理", "updated_at": _days_ago(2, 15, 30)},
    {"id": "conv-demo-5", "title": "Agent 任务编排思路整理", "updated_at": _days_ago(5, 11, 2)},
    {"id": "conv-demo-6", "title": "仓库拆分：前端 / 后端各自独立", "updated_at": _days_ago(13, 20, 47)},
]


@router.get("")
def list_conversations() -> list[dict]:
    return _DEMO_CONVERSATIONS
