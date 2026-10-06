# MorphUI Backend

MorphUI Agent 的 FastAPI 后端（MVP 阶段）。

## 接口一览

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| GET | `/api/health` | 健康检查（前端用它显示后端连接状态） |
| POST | `/api/chat` | 聊天占位接口（回显演示，后续接入 LLM / Agent） |
| GET | `/api/conversations` | 历史会话列表（演示数据） |
| GET | `/preview` | 实时预览演示页（供前端 iframe 加载） |
| GET | `/docs` | Swagger API 文档 |

## 本地运行

```bash
cd morphui-backend
python -m venv .venv
.venv\Scripts\activate          # Windows；macOS/Linux 为 source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

服务地址：http://127.0.0.1:8000 ，API 文档：http://127.0.0.1:8000/docs

## 与前端的连接方式

- 开发期前端（Vite, 端口 5273）通过代理把 `/api/*` 转发到本服务，见前端 `vite.config.ts`；
- 本服务同时开启了 CORS，允许 `http://localhost:5273` 直连。
