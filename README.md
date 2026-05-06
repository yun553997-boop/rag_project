# 📚 个人知识库助手 (RAG Fullstack Assistant)

一个基于大语言模型（LLM）的检索增强生成（RAG）全栈应用。旨在帮助用户沉淀个人知识（Markdown/PDF/TXT），并提供带有“打字机”流式响应效果的智能问答体验。

## 🛠️ 技术栈 (Tech Stack)

- **前端 (Frontend)**：Vue 3 (Composition API) + TypeScript + Vite + Element Plus
- **后端 (Backend)**：FastAPI + Python 3.11 + Uvicorn
- **AI 框架**：LangChain + 通义千问 API (DashScope)
- **向量存储**：ChromaDB (本地轻量级向量库)
- **部署与工程化**：Docker + Docker Compose

## ✨ 核心特性 (Features)

- **全栈分离架构**：标准的 B/S 架构，前后端通过 RESTful API 进行通信。
- **动态知识注入**：支持通过 Web 界面拖拽上传私有文档，后端自动完成文本解析、Chunk 分割、向量化并更新至 Chroma 数据库。
- **极致的交互体验**：利用 Server-Sent Events (SSE) 技术，配合浏览器的原生 Fetch API，实现零延迟的大模型流式输出（打字机效果）。
- **多轮会话记忆**：基于 LangChain 的 History 模块与本地 JSON 存储，实现带上下文记忆的连贯问答。
- **一键容器化部署**：提供完整的 Dockerfile 与 docker-compose 编排脚本，极速拉起整套服务。

## 🚀 快速启动 (Quick Start)

1. 克隆本项目到本地
2. 在 `backend` 目录下创建 `.env` 文件，填入你的 API Key：
   ```env
   DASHSCOPE_API_KEY="你的通义千问API密钥"
3. 在项目根目录执行一键启动命令：

```Bash
docker-compose up -d --build
```
访问前端页面：http://localhost

访问后端接口文档：http://localhost:8000/docs
