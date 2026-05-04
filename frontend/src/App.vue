<!-- frontend/src/App.vue -->
<template>
  <div class="common-layout">
    <el-container class="app-container">
      <!-- 左侧边栏 -->
      <el-aside width="260px" class="sidebar">
        <h2 class="logo">🚀 RAG 知识库助手</h2>
        <div class="session-info">
          <p>当前会话 ID:</p>
          <el-tag size="small" type="info">{{ sessionId }}</el-tag>
        </div>
        <!-- 这里后续可以添加历史会话列表或文件上传组件 -->
      </el-aside>

      <!-- 右侧主聊天区 -->
      <el-container>
        <el-main class="chat-main" ref="chatMainRef">
          <div class="message-list">
            <div 
              v-for="(msg, index) in messages" 
              :key="index"
              :class="['message-item', msg.role === 'user' ? 'is-user' : 'is-ai']"
            >
              <div class="avatar">{{ msg.role === 'user' ? '🧑‍💻' : '🤖' }}</div>
              <!-- AI 消息使用 markdown 渲染，用户消息直接显示纯文本 -->
              <div 
                class="message-content" 
                v-if="msg.role === 'ai'" 
                v-html="renderMarkdown(msg.content)"
              ></div>
              <div class="message-content" v-else>{{ msg.content }}</div>
            </div>
          </div>
        </el-main>

        <!-- 底部输入区 -->
        <el-footer class="chat-footer" height="auto">
          <div class="input-wrapper">
            <el-input
              v-model="inputText"
              type="textarea"
              :rows="3"
              placeholder="问点关于我笔记里的问题吧..."
              resize="none"
              @keydown.enter.prevent="sendMessage"
            />
            <el-button 
              type="primary" 
              class="send-btn" 
              @click="sendMessage" 
              :loading="isGenerating"
            >
              发送
            </el-button>
          </div>
        </el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import { ref, nextTick } from 'vue'
import MarkdownIt from 'markdown-it'

// 初始化 Markdown 渲染器
const md = new MarkdownIt({ breaks: true })

// 状态定义
const inputText = ref('')
const messages = ref<{ role: 'user' | 'ai', content: string }[]>([])
const isGenerating = ref(false)
const chatMainRef = ref<any>(null)

// 生成一个简单的随机 Session ID
const sessionId = ref('sess_' + Math.random().toString(36).substring(2, 9))

// 渲染 Markdown 的工具函数
const renderMarkdown = (text: string) => {
  return md.render(text)
}

// 自动滚动到页面底部
const scrollToBottom = async () => {
  await nextTick()
  if (chatMainRef.value && chatMainRef.value.$el) {
    const el = chatMainRef.value.$el
    el.scrollTop = el.scrollHeight
  }
}

// 发送消息核心逻辑
const sendMessage = async () => {
  const text = inputText.value.trim()
  if (!text || isGenerating.value) return

  // 1. 把用户消息上屏
  messages.value.push({ role: 'user', content: text })
  inputText.value = ''
  isGenerating.value = true
  scrollToBottom()

  // 2. 预先推入一个空的 AI 消息对象，用于一会接收流式字符
  messages.value.push({ role: 'ai', content: '' })
  const aiMessageIndex = messages.value.length - 1

  try {
    // 3. 使用原生的 fetch 发送 POST 请求。
    // 流式响应 (SSE) 使用原生的 fetch 比 Axios 更容易处理字节流。
    const response = await fetch('http://localhost:8000/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        session_id: sessionId.value,
        query: text
      })
    })

    if (!response.ok) throw new Error('网络请求失败')
    if (!response.body) throw new Error('未获取到响应体')

    // 4. 读取流式数据
    const reader = response.body.getReader()
    const decoder = new TextDecoder('utf-8')

    while (true) {
      const { done, value } = await reader.read()
      if (done) break
      
      // 解码字节并拼接到当前的 AI 消息内容中
      const chunk = decoder.decode(value, { stream: true })
      messages.value[aiMessageIndex].content += chunk
      scrollToBottom() // 每次文字更新都滚动到底部
    }
  } catch (error) {
    console.error(error)
    messages.value[aiMessageIndex].content = '⚠️ 抱歉，请求后端失败，请检查服务是否正常启动。'
  } finally {
    isGenerating.value = false
  }
}
</script>

<style>
/* 重置默认边距 */
body { margin: 0; font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', Arial, sans-serif; }
</style>

<style scoped>
.app-container {
  height: 100vh;
  background-color: #f5f7fa;
}

.sidebar {
  background-color: #2c3e50;
  color: #fff;
  padding: 20px;
  display: flex;
  flex-direction: column;
}

.logo {
  margin-top: 0;
  font-size: 20px;
  border-bottom: 1px solid #4a5c6f;
  padding-bottom: 15px;
}

.session-info {
  margin-top: 20px;
  font-size: 14px;
}

.chat-main {
  padding: 20px;
  overflow-y: auto;
}

.message-list {
  max-width: 800px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.message-item {
  display: flex;
  gap: 15px;
}

.message-item.is-user {
  flex-direction: row-reverse;
}

.avatar {
  font-size: 24px;
  background: #fff;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  flex-shrink: 0;
}

.message-content {
  background-color: #fff;
  padding: 12px 16px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  max-width: 80%;
  line-height: 1.6;
  font-size: 15px;
  color: #333;
}

.is-user .message-content {
  background-color: #e1f3d8;
}

/* Markdown 内部样式覆盖 */
.message-content :deep(p) { margin: 0 0 10px 0; }
.message-content :deep(p:last-child) { margin: 0; }
.message-content :deep(pre) { background-color: #f8f9fa; padding: 10px; border-radius: 4px; overflow-x: auto; }
.message-content :deep(code) { font-family: monospace; background-color: #f0f2f5; padding: 2px 4px; border-radius: 3px; }

.chat-footer {
  background-color: #fff;
  border-top: 1px solid #ebeef5;
  padding: 20px;
}

.input-wrapper {
  max-width: 800px;
  margin: 0 auto;
  display: flex;
  align-items: flex-end;
  gap: 15px;
}

.send-btn {
  height: 74px; /* 匹配 textarea 3行的高度 */
  width: 100px;
}
</style>