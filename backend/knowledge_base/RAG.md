# 第一章 大语言模型介绍

##1.1 大型语言模型（LLM）简介

大语言模型（LLM），也称大型语言模型，是一种旨在理解和生成人类语言的人工智能模型。

> 通常大模型由三个阶段构成：预训练、后训练和在线推理。
>

常用的LLM模型：

- 国外：ChatGPT、Claude（闭源，由OpenAI前成员创立）、Gemini、LLaMA（开源社区标杆）
- 国内：文心一言（百度，多样单模态）、星火（科大讯飞）、DeepSeek（推理性大模型，24年10月发布DeepSeek-V3及R2）、通义千问（26年发布多模态）、ChatGLM（由清华和智普AI研发）、Baichuan（百川智能，开源商用）




## 1.2 LLM的基本使用

- 可以在本地使用LLM API，也可以在云上使用
- 市面上有很多的LLM API，如ChatGPT、文心一言、讯飞星火、智谱 GLM，本章以ChatGDT为例

### 1.2.1 本地部署

概述：

​	为满足在低配设备（GPU）运行，使用蒸馏后的模型，因为模型本身仅仅是一个文件，所以使用Ollama托管模型，但只能进行命令行操作及RestfulAPI接口访问。想要使用网页访问，可以使用ChatboxAI或strmlit提供前端页面，快速实现交互页面。但需要提前安装Python环境。



### 1.2.2 云上---原生部署

概述：

​	前端部署与本地操作相同，后端使用LangChain托管，且使用的模型是完整的模型，没有经过蒸馏。

1. 配置client

   > 首先，当然是安装openAI库`pip install openai --upgrade`

   访问云平台，拿到秘钥（配置环境变量，或者直接写一个环境变量文件）

   > ```.env
   > OPENAI_API_KEY="你的API密钥"
   > ```

   ```python
   import os
   from openai import OpenAI
   from dotenv import load_dotenv

   # 加载 .env 文件中的环境变量
   load_dotenv()
   # 获取API Key (从环境变量中读取，更安全)
   api_key = os.getenv("DASHSCOPE_API_KEY")
   # 初始化客户端，它会自动从环境变量中读取 OPENAI_API_KEY
   client = OpenAI()
   ```

2. 调用模型（核心功能）

   ```python
   # 在配置好 client 后，直接调用
   response = client.chat.completions.create(
       model="gpt-3.5-turbo",  # 选择模型，如 gpt-3.5-turbo 或 gpt-4
       messages=[
           {"role": "system", "content": "你是一个乐于助人的助手。"},
           {"role": "assistant", "content": "好的，我是一个乐于助人的助手，请提问"}
           {"role": "user", "content": "什么是Python装饰器？"}
       ]
   )
   ```

   > 为了实现多轮对话，你需要在每次请求时，将**整个对话历史**（包括之前的user问题、assistant回答等）都放入 `messages` 数组中发送。

3. 处理结果

   ```python
   # 提取并打印回复内容
   print(response.choices[0].message.content)
   ```

- 流式响应

  ```python
  # 调用模型
  stream = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user", "content": "讲一个关于程序员的笑话"}],
      stream=True,  # 开启流式响应
  )

  # 使用迭代器输出
  for chunk in stream:
      print(
          chunkchoices[0].message.content, 
          end="",       #结束的回车去除
          flush=True    #立刻刷新缓冲区
      )  
  ```



## 1.3 RAG简介

为解决大型语言模型在生成文本时面临的一系列挑战，提高模型的性能和输出质量，提出了一种新的模型架构：**检索增强生成（RAG）**。该架构**整合了从庞大知识库中检索到的相关信息，并以此为基础，指导大型语言模型生成更为精准的答案**。

目前 LLM 面临的主要问题：

- 信息偏差/幻觉 
- 知识更新滞后性 
- 内容不可追溯
- 领域专业知识能力欠缺
- 长文本处理能力较弱

### 1.3.1 工作流程

RAG 是一个完整的系统，其工作流程简单分为：

1. 数据处理阶段
   1. 对原始数据进行清洗和处理。
   2. 将处理后的数据转化为检索模型可以使用的格式。
   3. 将处理后的数据存储在对应的数据库中。
2. 检索阶段
   1. 将用户的问题输入到检索系统中，从数据库中检索相关信息。
3. 增强阶段
   1. 对检索到的信息进行处理和增强，以便生成模型可以更好地理解和使用。
4. 生成阶段
   1. 将增强后的信息输入到生成模型中，生成模型根据这些信息生成答案。

### 1.3.2 RAG VS 微调

> 在提升大语言模型效果中，RAG 和 微调（Finetune）是两种主流的方法。
>
> **微调**: 通过在特定数据集上进一步训练大语言模型，来提升模型在特定任务上的表现。

相比于微调，RAG只需更新知识库



## 1.4 LangChain简介

> 为解决利用 OpenAI 提供的 API时，仍然需要大量的定制开发工作（API 集成、互动逻辑、数据存储等等），推出了多个开源项目。其中一个备受关注的项目就是 LangChain 框架。

LangChain 目标：为各种大型语言模型应用提供**通用接口**。

- LangChain 6个核心组件:
- - **模型输入/输出（Model I/O）**：与语言模型交互的接口
  - **数据连接（Data connection）**：与特定应用程序的数据进行交互的接口
  - **链（Chains）**：将组件组合实现端到端应用。比如后续我们会将搭建`检索问答链`来完成检索问答。
  - **记忆（Memory）**：用于链的多次运行之间持久化应用程序状态；
  - **智能体（Agents）**：扩展模型的推理能力。用于复杂的应用的调用序列；
  - **回调（Callbacks）**：扩展模型的推理能力。用于复杂的应用的调用序列；

  ​

# 第二章 基于LangChain框架

使用Langchain框架之前：

1. 确保安装LangChain的一系列第三方库

   ```bash
   pip install langchain langchain-community dashscope chromadb
   ```

   > - langchain :核心包
   > - langchain-community：社区支持包，提供更多第三方调用（阿里云千问等等）比如各种向量库、加载器、模型适配器等（会用到的“可插拔组件”）
   > - dashscope：阿里云通义千问的Python SDK
   > - chromadb：轻量级向量数据库

2. 确保获取到密钥，并使用环境变量储存

   ```.env
   DASHSCOPE_API_KEY = "密钥"
   ```

## 2.1 使用LLM API

LangChain目前支持三种类型的模型：LLMs（大语言模型）、Chat Models（聊天模型）、Embeddings Models（嵌入模型）

- LLMs：大范畴
- 聊天模型：专为对话场景优化的MMLs
- 嵌入模型：接受文本输入，得到文本向量

### 2.1.1 LLMs

```python
from langchain_community.llms.tongyi import Tongyi
model = Tongyi(model="qwen-max")
res = model.invoke(input="请给我讲一个笑话")
print(res)
```

> - invoke方法：一次性返回完整结果
> - stream方法：逐段返回结果（流式输出）

流式输出：

```python
from langchain_community.llms.tongyi import Tongyi
model = Tongyi(model="qwen-max")
res = model.stream(input="请给我讲一个笑话")
for chunk in res:
    print(chunk, end="", flush=True)
```

### 2.1.2 聊天模型

```python
from LangChain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage, SystemMessage, AiMessage

model = ChatTongyi("qwen3-max")

message = [
    SystemMessage(content="你是一名漫画家"),
    HumanMessage(content="给我讲一个笑话"),
    AiMessage("我给你讲个蛋")
]

for chunk in model.stream(input=message):
    print(chunk.content, end="", flush=True)
```

简写聊天模式：

```python
#...(一样的)
message = [
    ("system", "你是一名漫画家"),
    ("human", "给我讲一个笑话"),
    ("ai", "我给你讲个蛋")
]
#...
```

### 2.1.3 文本嵌入模式

Embeddings Models的特点：将字符串作为输入，返回一个浮点数列表（向量）

```python
from langchain_community.embeddings import DashScopeEmbeddings
#初始化嵌入模型，默认为text-embedding-v1(千问)
embed = DashScopeEmbeddings()

print(embed.mebed_query(''))             #单次转换
print(embed.mebed_documents(['','',''])) #批量转换
```

> 这里不使用invoke和stream，而使用embed.mebed_query和embed.mebed_documents



## 2.2 Prompt Engineering

设计高效 Prompt 的两个关键原则：**编写清晰、具体的指令**和**给予模型充足思考时间**。

### 2.2.1 设计prompt技巧

1. 使用分隔符清晰地表示输入的不同部分

   可以选择用 ```，"""，< >， ，: 等做分隔符，只要能明确起到隔断作用即可。

2. 寻求结构化的输出

   结构化输出就是**按照某种格式组织的内容，例如 JSON、HTML 等**。

   > 字典与JSON之间相互转换：
   >
   > - 字典转化JSON
   >
   >   ```python
   >   d = {
   >       "name" : "周杰伦",
   >       "age" : 18,
   >       "gender" : "男"
   >   }
   >   s = json.dumps(d, ensure_ascii=False)   #ensure_ascii确保中文正常显示
   >   ```
   >
   > - JSON转化字典
   >
   >   ```
   >   r = json.loads(s)
   >   ```

3. 要求模型检查是否满足条件

   如果任务有不能满足的假设，我们可以告诉模型先检查这些假设，如果不满足，则会指出并停止执行后续的完整流程。

4. 提供少量示例

   问AI的时候举出一两个例子，然他按照此例子依壶画瓢

   > 零样本学习（Zero-shot）：
   >
   > - 模型没有见过新类别的具体样本，但它可以借助**类别之间的语义描述**（如属性、词向量、文本描述）来推理出新类别。
   >
   > 少样本学习（Few-shot）：
   >
   > - 仅凭**极少数**的标注样本（通常每个新类别只有1~5个样本）就能快速学习并识别新类别。它模拟了人类“举一反三”的能力。

5. 给模型思考时间，指定完成任务所需的步骤




### 2.2.2 通用提示词模版

- 基于zero-shot思想，使用PromptTemplate完成
- 基于few-shot思想，使用FewShotPromptTemplate完成



#### 1.PromptTemplate

LangChain提供了PromptTemplate类，用来协助优化提示词，它表示提示词模版，可以自定义，支持变量注入，最终生所需提示词

- 基础用法：

  ```python
  from langchain_core.prompts import PromptTemplate
  from langchain_community.llms.tongyi import Tongyi

  prompt_template = PromptTemplate.from_template("你是一名优秀的{a}，请完成{b}工作")
  prompt_text = prompt_tempelate.format(a="建筑工人", b="砌墙")

  model = Tongyi(model="qwen-max")
  res = model.invoke(input=Prompt_text)
  print(res)
  ```

  invoke：最基础的调用方法，传入参数，获取最终输出。

  prompt_template：一个Runnable对象，负责接收输入字典，并格式化生成提示词。

  llm：一个Runnable对象，接收提示词，返回模型生成的响应。

  output_parser：一个Runnable对象，接收模型的响应，将其解析为你需要的格式（如JSON）

  ​

  > 当然，上述写法等同于：
  >
  > ```python
  > Prompt_tmplate = f"你是一名优秀的{a}，请完成{b}工作"
  > ```
  >
  > 但是，该写法不支持LangChain框架的链式调用

- 使用链：

  ```python
  prompt_template = promptTemplate.from_template("你是一名优秀的{a}，请完成{b}工作")

  model = Tongyi(model="qwen-max")
  chain = prompt_template|model  #现有提示词，再放入模版中
  res = chain.invoke(input={"a": "建筑工人"， "b": "砌墙"})
  ```

  ​

#### 2.FewShotPromptTemplate

在提示词中给模型提供**几个输入-输出的范例**，让模型学会你期望的回答风格、格式或推理逻辑。

- 基础用法：

  ```python
  from langchain.prompts import FewShotPromptTemplate, PromptTemplate

  example_template = PromptTemplate.from_template("你是一名优秀的{a}，请完成{b}工作")
  example_data = [
      {"a": "环卫工人", "b": "清洁马路"},
      {"a": "外卖骑手", "b": "配送外卖"}
  ]

  few_shot_prompt = FewShotPromptTemplate(
  	examples = example_data,
  	examples_prompt = example_template,
      prefix = "你是一个专业的知识问答助手。以下是一些高质量的回答范例：\n",
      suffix = "问题：现在请告诉我，如果学习{input_word}，他的提示词应该怎么写？\n答案：",
      input_variables = ["input_word"]
  )                                                                   #转为字符串
  prompt_text = few_shou_prompt.invoke(input={"input_word": "配送外卖"}).to_string()
  print(prompt_text)
  ```

  > - examples：示例数据（List，内套字典）
  > - examples_prompt：提示词模版
  > - prefix：示例数据前内容
  > - suffix：示例数据后的内容
  > - input_variables：列表，注入变量列表

  ```
  D:\...>
  你是一个专业的知识问答助手。以下是一些高质量的回答范例：	
  你是一名优秀的环卫工人，请完成清洁马路工作
  你是一名优秀的外卖骑手，请完成配送外卖工作
  问题：现在请告诉我，如果学习种地，他的提示词应该怎么写？
  答案：
  ```



#### 3.ChatPromtTemplate

支持注入任意数量的历史会话

PromptTemplate类的from_template只能接受一条消息，from_messages可以接受一个List消息

- 基础用法：

  ```python
  from langchain_core.prompts import ChatPromptTemplate, MessagePlaceholder

  chat_template = ChatPromptTemplate.from_messages([  
      ("system", "你是一个严谨的翻译助手，只返回译文，不解释任何内容。"),
      ("ai", "")
      MessagePlaceholder("history")
      ("human", "请翻译：{input_text}")   
  ])
  #历史对话
  history_data = [
      (),
      (),
      (),
  ]
  						#这里只能使用invoke					
  prompt_text = prompt_tempelate.invoke({"history": history_data}).to_string() 
  print(prompt_text)
  ```

  ​

  ​


#### 4.关于format和invoke方法

在上述模版中，我们使用到

- `prompt_text = prompt_tempelate.format(a="建筑工人", b="砌墙")`

- `prompt_text = few_shou_prompt.invoke(input={"input_word": "配送外卖"}).to_string()`

- format vs invoke：

  | 特性     | `.format()` 方法                           | `.invoke()` 方法                                 |
  | -------- | ------------------------------------------ | ------------------------------------------------ |
  | 定位     | 传统字符串工具方法（为了兼容 Python 习惯） | Runnable 标准接口（LangChain 推荐）              |
  | 传参方式 | 关键字参数：`prompt.format(k="v")`         | 字典输入：`prompt.invoke({"k": "v"})`            |
  | 返回值   | `str` (纯文本字符串)                       | `PromptValue` 对象（可转换为需要的格式，如JSON） |
  | 链式调用 | 不支持                                     | 支持                                             |
  | 适用场景 | 快速调试、打印查看提示词内容               | 构建生产级应用、RAG 链、多轮对话                 |




## 2.3 Chain的基础使用

**链（Chain）** 就是将多个独立的AI组件（如提示词模板、语言模型、输出解析器等）连接起来，形成一个多步骤、可复用的自动化处理流水线。有了它，你可以告别繁琐的手动调用，让数据在组件间自动流转。

对比：

| 特性         | 传统方式：Legacy Chain | 新方式：LCEL            |
| ------------ | ---------------------- | ----------------------- |
| **核心理念** | **命令式封装**         | **声明式组合**          |
| **核心语法** | 创建特定类的实例       | 使用管道符 `|` 连接组件 |
| **灵活性**   | **较低**               | **极高**                |

### 2.3.1 LCEL 基础用法

- 原理：

  上个组件输出作为下个组件的输入

- 前提：

  `Runnable`子类对象才能入链

- 用法：

  LCEL 的核心范式：Prompt | Model | Parser

  ```python
  from langchain_core.output_parsers import StrOutputParser
  from langchain_core.prompts import ChatPromptTemplate
  from langchain_openai import ChatOpenAI

  # 1. 定义组件
  prompt = ChatPromptTemplate.from_template("将以下文本翻译成英文：{text}")
  model = ChatOpenAI(model="gpt-4o-mini")
  parser = StrOutputParser()  # 用于提取字符串内容

  # 2. 构建链（提示词模版|大语言模型|输出解析器）
  translate_chain = prompt | model | parser

  # 3. 运行链
  result = translate_chain.invoke({"text": "我喜欢用 LangChain 构建应用。"})
  print(result)  # 输出翻译后的英文
  ```

  > 说明：在这个链条中，`prompt` 会自动调用 `invoke` 接收字典，生成 `PromptValue`，然后传给 `model`。`PromptValue` 对象内部封装了结构化信息，可以自动转换成模型需要的格式（比如  `messages` 列表）



### 2.3.2 输出解析器

LLM（大语言模型）的本质是**文本生成器**，它返回的是自然语言字符串。但在实际应用中，我们经常需要**结构化的数据**

```python
# 没有输出解析器：你得到的是字符串
result = llm.invoke("告诉我今天天气怎么样？")
# 输出："今天是2024年5月20日，北京天气晴朗，温度25度..."

# 有输出解析器：你得到的是结构化数据
result = chain.invoke({"question": "今天天气怎么样？"})
# 输出：{"date": "2024-05-20", "city": "北京", "weather": "晴朗", "temperature": 25}
```

在实际开发过程中，可能需要将模型返回的结果，在输入给模型，单模型只能接受PromptValue/string/Sequence

#### 1.内置解析器

LangChain 提供了多种输出解析器：

1. StrOutputParser：最简单的字符串解析器

   **用途**：当你只需要 LLM 返回的原始文本时使用（其实什么都没解析，只是提取了 LLM 返回的字符串内容）

   ```python
   from langchain_core.output_parsers import StrOutputParser
   from langchain_core.prompts import ChatPromptTemplate
   from langchain_openai import ChatOpenAI

   parser = StrOutputParser()
   chain = ChatPromptTemplate.from_template("讲一个关于{topic}的笑话") | ChatOpenAI() | parser

   result = chain.invoke({"topic": "程序员"})
   print(type(result))  # <class 'str'>
   print(result)        # 直接输出笑话文本
   ```

2. JsonOutputParser：结构化数据首选

   **用途**：让 LLM 返回 JSON 格式的数据，并自动解析为 Python 字典

   ```python
   from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
   from langchain_core.prompts import PromptTemplate
   from langchain_community.chat_models.tongyi import ChatTongyi

   str_parser = StrOutputParser()
   js_parser = JsonOutputParser() # 在此之前 ，可以定义期望的JSON结构（指定类型）

   firsr_prompt = PromptTemplate.from_template("""
   我邻居生孩子了，他爹姓{lastname}，是个{gender}孩，请起名，并封装到JSON格式返回给我。
   要求：key是name，Value是你起得名字。请严格按照格式。
   """)
   serond_prompt = PromptTemplate.from_template("姓名{name}，请分析含义")

   model = ChatTongyi(model="qwen3-max")
   chain = firsr_prompt | model | js_parser | serond_prompt | model | str_parser

   result: str = chain.invoke({"lastname": "张"， "gender": "女"})
   print(type(result))  # <class 'string'>
   print(result)        # {"张若琪",寓意：……}
   ```

3. PydanticOutputParser：强类型数据解析器

   **用途**：直接返回 Pydantic 对象，享受类型提示和数据验证的好处

4. CommaSeparatedListOutputParser：列表数据解析

   **用途**：当需要 LLM 返回一个列表时非常方便

5. EnumOutputParser：枚举值解析

   **用途**：限制 LLM 的输出只能是预定义的几个选项

#### 2.自定义解析器

这里使用类方法进行定义。当然如果足够简单，可以直接将函数写入链，实现这个功能需要基于`RunnableLambda`类实现。

- 例如，上述例子中（将str ---> JSON）：

  ```python
  from langchain_core.output_parsers import StrOutputParser
  ...
  from langchain_core.runables import RunnableLambda

  str_parser = StrOutputParser()
  my_func = RunnableLambda(lambda ai_msg: {"name" :ai_msg.content})

  ...
  chain = firsr_prompt | model | my_func | serond_prompt | model | str_parser
  ...#其余都一样（见上文）
  ```

  > 当然，普通的函数可以直接加入链：
  >
  > ```python
  > ...
  > chain = firsr_prompt | model | (lambda ai_msg: {"name" :ai_msg.content}) | serond_prompt | model | str_parser
  > ```



## 2.4 会话记录

###2.4.1 Memory临时会话记忆

在 LangChain 中，短期记忆主要依靠`RunnableWithMessageHistory`和 `InMemoryChatMessageHistory`来实现。它们共同构成了一个轻量级、会话隔离的对话记忆方案。

实现对话记忆步骤：

1. 创建一个基础对话链

   ```python
   from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
   model = Tongyi(model="qwen-plus")
   prompt = ChatPromptTemplate.from_messages([
       ("system", "你是一个乐于助人的助手。"),
       MessagesPlaceholder(variable_name="history"),  # 历史消息会放在这里
       ("human", "{input}")                           # 用户最新的输入
   ])

   chain = prompt | model
   ```

2. 添加记忆

   `InMemoryChatMessageHistory`负责：

   - 存储消息列表的对象，支持添加用户消息、AI 消息，以及获取所有消息。

   `RunnableWithMessageHistory` 负责：

   - 根据 `session_id` 找到对应的 `InMemoryChatMessageHistory` 对象。
   - 自动将历史消息填充到链的 `history` 参数中。
   - 在模型调用完成后，自动把用户输入和模型输出追加到历史中。

   另外，需要提供一个**工厂函数**（store），用于为每个 `session_id` 创建或返回一个 `ChatMessageHistory` 实例。这里使用最简单的内存存储（字典）

   ```python
   from langchain_core.runnables.history import RunnableWithMessageHistory
   from langchain_core.chat_history import InMemoryChatMessageHistory

   #获取指定会话ID的历史记录的函数（我给你ID，你给我会话记录）
   store = {}
   def get_session_history(session_id: str):
       if session_id not in store:
           store[session_id] = InMemoryChatMessageHistory() #添加消息
       return store[session_id]    #返回该对话的所有消息

   # 用 RunnableWithMessageHistory 包装上面的 chain
   chain_with_history = RunnableWithMessageHistory(
       runnable=chain,                    # 基础链
       get_session_history=get_session_history,  # 获取历史的函数
       input_messages_key="input",        # 声明当前消息的占位符
       history_messages_key="history"     # 声明历史记录的占位符
   )
   ```

3. 使用带记忆的链

   调用时，需要传入 `config` 参数，其中包含 `session_id`，用来区分不同会话

   ```python
   # 第一次对话
   response1 = chain_with_history.invoke(
       {"input": "我叫张三，我喜欢编程。"},
       config={"configurable": {"session_id": "user_123"}}
   )
   print(response1.content)  # 模型应该会记住你的名字

   # 第二次对话（同一会话）
   response2 = chain_with_history.invoke(
       {"input": "我叫什么名字？"},
       config={"configurable": {"session_id": "user_123"}}
   )
   print(response2.content)  # 模型应该能回答“张三”
   ```

   如果换一个 `session_id`，记忆就是独立的

   ```python
   response3 = chain_with_history.invoke(
       {"input": "我叫什么名字？"},
       config={"configurable": {"session_id": "user_456"}}
   )
   print(response3.content)  # 模型不知道，因为没有该会话的历史
   ```

   ​

### 2.4.1 Memory长期会话记忆

使用`InMemoryChatMessageHistory`仅能在内存中临时记忆，一旦退出程序，则记忆丢失。

 LangChain支持多种开箱即用的持久化方案：

| 类名                           | 存储介质     | 持久化 | 并发性能 | 部署复杂度 | 适用场景         |
| ------------------------------ | ------------ | ------ | -------- | ---------- | ---------------- |
| **FileChatMessageHistory**     | 本地JSON文件 | ✅      | ❌ 低     | 0          | 本地单用户程序   |
| **SQLChatMessageHistory**      | 本地SQLite   | ✅      | ⚠️ 中     | 0          | 本地多会话程序   |
| **RedisChatMessageHistory**    | Redis        | ✅      | ✅ 极高   | 低         | 线上高并发服务   |
| **PostgresChatMessageHistory** | PostgreSQL   | ✅      | ✅ 高     | 中         | 企业级、海量数据 |
| **MySQLChatMessageHistory**    | MySQL        | ✅      | ✅ 高     | 中         | 国内企业级应用   |

所有这些类的核心API都是一致的，这意味着更换存储介质非常方便，无需修改业务逻辑。

#### 1.本地JSON文件

**方法一：使用内置 `FileChatMessageHistory`** 

 `FileChatMessageHistory` 类会将消息追加到指定文件中（每行一个 JSON 对象）。

实现步骤：

1. 创建基础对话链（与短期相同）

2. 构建记忆包装器

   ```python
   from langchain_community.chat_message_histories import FileChatMessageHistory
   from langchain_core.runnables.history import RunnableWithMessageHistory

   # 关键：定义根据 session_id 返回 FileChatMessageHistory 的工厂函数
   def get_session_history(session_id: str):
       # 每个会话对应一个独立的文件，文件名包含 session_id
       file_path = f"./chat_histories/{session_id}.json"
       return FileChatMessageHistory(file_path)

   # 包装链
   chain_with_history = RunnableWithMessageHistory(...)#与短期一样
   ```

3. 使用带记忆的链（与短期一样）

   ```python
   config = {"configurable": {"session_id": "alice"}}
   # 第一轮
   response1 = chain_with_history.invoke({"input": "我叫爱丽丝，我喜欢音乐。"}, config=config)
   print(response1.content)
   ```

**方法二：自定义JSON文件存储**

如果你想完全控制存储格式，可以自己实现一个继承自 `BaseChatMessageHistory` 的类。

步骤：

1. 自定义类`JSONChatMessageHistory`

   ```python
   import json
   import os
   from typing import List
   from langchain_core.chat_history import BaseChatMessageHistory
   from langchain_core.messages import BaseMessage, message_to_dict, messages_from_dict

   class JSONChatMessageHistory(BaseChatMessageHistory):
       """将聊天历史存储在 JSON 文件中，每条会话一个文件。"""
       
       def __init__(self, file_path: str):
           self.file_path = file_path
           self._load_messages()
       
       def _load_messages(self):
           """从 JSON 文件加载消息列表"""
           if os.path.exists(self.file_path):
               with open(self.file_path, 'r', encoding='utf-8') as f:
                   data = json.load(f)
                   # messages_from_dict 将字典列表转回 Message 对象列表
                   self._messages = messages_from_dict(data)
           else:
               self._messages = []
       
       def _save_messages(self):
           """将当前消息列表保存到 JSON 文件"""
           # message_to_dict 将每个 Message 对象转为字典
           with open(self.file_path, 'w', encoding='utf-8') as f:
               json.dump([message_to_dict(msg) for msg in self._messages], f, ensure_ascii=False, indent=2)
       #获取消息
       @property
       def messages(self) -> List[BaseMessage]:
           return self._messages
       #添加消息
       def add_message(self, message: BaseMessage) -> None:
           self._messages.append(message)
           self._save_messages()   # 每次添加后立即持久化
       #清除消息
       def clear(self) -> None:
           self._messages = []
           if os.path.exists(self.file_path):
               os.remove(self.file_path)
   ```

2. 集成到 `RunnableWithMessageHistory`

   ```python
   def get_session_history(session_id: str):
       file_path = f"./custom_histories/{session_id}.json"
       # 确保目录存在
       os.makedirs(os.path.dirname(file_path), exist_ok=True)
       return JSONChatMessageHistory(file_path)

   chain_with_history = RunnableWithMessageHistory(
       runnable=chain,
       get_session_history=get_session_history,
       input_messages_key="input",
       history_messages_key="history"
   )
   ```

3. 使用带记忆的链

   ​

## 2.5 数据处理

为构建我们的本地知识库，我们需要对以多种类型存储的本地文档进行处理，读取本地文档并通过前文描述的 Embedding 方法将本地文档的内容转化为词向量来构建向量数据库。

### 2.5.1 源文档选取

选取步骤：

1. 选取PDF、Markdown、txt 等格式文档
2. 将其放到本地（最好是项目文件中）

### 2.5.2 数据读取

文档加载器将数据源（文件、网页等）转换为由两部分组成的 `Document` 对象

- page_content：提取出的文本内容。
- metadata：描述数据的额外信息，比如文件名、页码、作者等。这些元数据在后续检索和溯源时非常有用。

在LangChain中，其核心的 `BaseLoader` 提供了两种通用的加载方式

- load()：一次加载全部文档
- lazy_load()：返回一个迭代器，逐条处理数据

#### 1. 文本与Markdown

- 纯文本（`.txt`）

  ```python
  from langchain_community.document_loaders import TextLoader

  # 加载TXT文件，务必指定编码，特别是处理中文文档
  text_loader = TextLoader("./my_notes.txt", encoding="utf-8")
  text_documents = text_loader.load()
  print(f"文本文件加载为 {len(text_documents)} 个文档")
  ```

- Markdown（`.md`）

  ```python
  from langchain_community.document_loaders import UnstructuredMarkdownLoader

  # 加载Markdown文件
  md_loader = UnstructuredMarkdownLoader("./readme.md")
  md_documents = md_loader.load()
  print(f"Markdown加载为 {len(md_documents)} 个文档")
  print(f"内容预览: {md_documents[0].page_content[:100]}...")
  print(f"元数据: {md_documents[0].metadata}")
  ```

  ​

#### 2.PDF文件

PDF是RAG应用中最常见的格式。LangChain提供多种加载器，各有侧重。

| 加载器              | 特点                                                         | 适用场景                                        |
| ------------------- | ------------------------------------------------------------ | ----------------------------------------------- |
| **PyPDFLoader**     | 轻量、基础，会将每一页PDF内容单独拆分出来，并自动在`metadata`中记录页码。 | 处理以纯文本为主的PDF文件，如论文、报告。       |
| **PyMuPDFLoader**   | 解析速度更快、精度更高，对PDF布局的识别能力更强。            | 对速度和精度要求较高，处理稍微复杂的PDF布局时。 |
| **OnlinePDFLoader** | 专门用于加载互联网上的PDF文件。                              | 需要直接抓取并处理网络PDF资源时。               |

几种加载器用法都是一样的，这里以PyPDFLoader为例：

```python
from langchain_community.document_loaders import PyPDFLoader, PyMuPDFLoader

# 使用PyPDFLoader
pdf_loader = PyPDFLoader("./financial_report.pdf")
pdf_pages = pdf_loader.load()
print(f"PDF共 {len(pdf_pages)} 页")
print(f"第一页内容: {pdf_pages[0].page_content[:200]}...")
print(f"第一页元数据: {pdf_pages[0].metadata}")  # 包含page页码
```



#### 3.结构化数据（CSV/JSON）

对于结构化的CSV和JSON文件，LangChain有专门的加载器。

```python
from langchain_community.document_loaders import CSVLoader, JSONLoader
import json

# 加载CSV文件
# source_column参数可以指定一列作为每个Document的来源标识，方便追踪[reference:15]
csv_loader = CSVLoader(file_path="./employees.csv", source_column="name")
csv_documents = csv_loader.load()

# 加载JSON文件
# jq_schema用于精确提取JSON中的特定数据
loader = JSONLoader(
    file_path='./data.json',
    jq_schema='.messages[].content',  # 提取messages数组中所有对象的content字段
    text_content=False
)
json_documents = loader.load()
```



### 2.5.3 数据清洗

期望知识库的数据是有序的、优质的、精简的，因此要删除低质量的、甚至影响理解的文本数据。

这里主要使用正则表达式，具体操作：去除特殊字符、统一大小写、去除停用词（可选）、处理表格/图片（需 OCR 或多模态模型）



### 2.5.4 文档分割

- 分割原因：文档加载器将数据源转换为一个 `Document` 对象，若文档过长，就会超过模型支持的上下文，需要对文档进行分割。

- 分割规则：按固定规则分割成若干个 chunk（后续检索以它为单位）。

- LangChain提供的文本分割器：

  |         分割器 (Splitter)          |                           核心原理                           |                     适用场景                     |
  | :--------------------------------: | :----------------------------------------------------------: | :----------------------------------------------: |
  |     **CharacterTextSplitter**      |                         按字符数划分                         |               非结构化文本日志文件               |
  | **RecursiveCharacterTextSplitter** | 递归地按分隔符（`["\n\n", "\n", " ", ""]`），保持段落、语义完整 |       绝大多数通用文本，如文章、报告、书籍       |
  |       **TokenTextSplitter**        |    基于**Token**计数分割，确保每块大小符合LLM的Token限制     |          对成本敏感，或Token限制的模型           |
  |        **SemanticChunker**         | 利用**嵌入模型**计算文本语义相似度，智能识别语义边界进行分割 | 对语义连贯性要求极高的场景，如长篇小说、法律文书 |


- 分割器参数：

  |           参数            |            说明             |                             原因                             |
  | :-----------------------: | :-------------------------: | :----------------------------------------------------------: |
  |      **chunk_size**       | 每个块的最大字符数或Token数 | 需根据模型上下文窗口和文档特性调整，常见值为256、512、1024等 |
  |     **chunk_overlap**     |   相邻块之间的重叠字符数    |                        避免上下文断裂                        |
  | **separators (递归分割)** | 指定分割优先级的分隔符列表  |    处理**中文**时，推荐添加句号、逗号等中文标点作为分隔符    |


- 这里以RecursiveCharacterTextSplitter为例：

  ```python
  from langchain_text_splitters import RecursiveCharacterTextSplitter

  # 使用递归字符文本分割器
  text_splitter = RecursiveCharacterTextSplitter(
      chunk_size=500,
      chunk_overlap=50,
      separators=["\n\n", "\n", " ", ""],
      length_function=len  #统计字符数（这是python自带的统计函数len）
  )
  chunks = text_splitter.split_documents(text_documents)#text_documents已读取的文档
  ```

  > 分割完，就会产生多个document





## 2.6 搭建向量数据库

**词向量**（word embedding）将单词转化为固定的静态的向量，忽略了单词在不同语境中的意思。因此在RAG应用中使用的向量技术一般为**通用文本向量**，该技术向量化的单位不再是单词，而是输入的文本。

在RAG中，向量的优势主要有两点：

- 向量比文字更适合检索。
- 向量综合信息能力更强，可以查询文字、声音、图像、视频等多种媒介，通过多种向量模型将多种数据映射成统一的向量形式。

**向量数据库**是用于存储和检索向量数据的数据库系统。主要关注的是向量数据的特性和相似性。



### 2.6.1 VectorStore（向量存储）

​向量存储存放文本块（Chunk）和向量（Embedding），并在检索时进行高效的语义搜索。

- 原理：

  将分割后的文档块转换成向量，存储起来。当用户提问时，系统会将问题也转换成向量，然后在存储库中快速找到“意思最像”的那些文档块，并返回给大模型作为参考

- 向量存储主要分为：

- - 轻量级内置存储：`Chroma` (持久化), `FAISS` (高性能)
  - 生产级外部数据库：`Pinecone`, `Milvus`, `Weaviate`, `Qdrant`, `pgvector`

1. 初始化Chrome

   > 也可以使用LangChain内置的`InMemoryChatMessageHistory`,但是外部向量存储更好

   ```python
   from langchain_chroma import Chroma
   from langchain_community.embeddings import DashScopeEmbeddings

   #初始化Chrome实例
   # 注意：这里使用了 from_documents 这个类方法，直接创建并填充了向量库
   vector_store = Chroma.from_documents(
       documents=chunks,   #chunks刚分割好的Document列表
       embedding=DashScopeEmbeddings(),
       collection_name="my_knowledge_base",  #集合名称，相当于数据库的“表名”
       persist_directory="./chroma_db"    #指定数据保存的目录
   )
   ```

   > 不设persist_directory，数据只会存储在内存，程序重启即消失，用于代码调试

   ​

### 2.6.2 管理向量库

- **存入向量**

  ```python
  vector_store.add_documents(
      documents=documents,   #被添加的文档，type=List[Document]
      ids=["id"+str(i) for i in range(1,len(document)+1)]    #给文档添加ID，type=List[str]
  )
  ```

- **删除文档**：可以通过文档ID来删除。

  ```python
  # 删除ID为 "doc_4" 的文档
  vector_store.delete(ids=["doc_4"])
  ```

- **检索文档**

  1. **基础相似度搜索**

     根据问题，查找最相似的k个文档块。这是最常用的方法

     ```python
     # 查询问题
     query = "什么是 LangChain？"

     # 执行相似度搜索，k=2 表示返回最相似的2个结果
     results = vector_store.similarity_search(query, k=2)

     for doc in results:
         print(f"内容: {doc.page_content}")
         print(f"元数据: {doc.metadata}")
     ```

  2. **带分数阈值的相似度搜索**

     这个方法会同时返回文档内容和相似度分数，并可以设置一个分数阈值来过滤掉不相关的结果

     ```python
     results_with_score = vector_store.similarity_search_with_relevance_scores(query, k=2)

     for doc, score in results_with_score:
         # 只接受相似度分数高于某个阈值的结果，例如 0.7
         if score > 0.7:
             print(f"分数: {score}, 内容: {doc.page_content}")
     ```

  3. **元数据过滤检索**

     检索时加上过滤条件，只查找符合特定元数据的文档块。用于按来源、时间等筛选信息

     ```python
     # 过滤条件：只查找 metadata 中 "source" 字段值为 "chroma_intro" 的文档
     filter_criteria = {"source": "chroma_intro"}

     filtered_results = vector_store.similarity_search(
         query="什么是向量数据库？",
         k=1,
         filter=filter_criteria
     )
     ```

- **获取集合信息**：可以查看当前Chroma集合的统计信息，比如文档总数。

  ```python
  collection_info = vector_store._collection.count()
  print(f"当前集合中的文档数量: {collection_info}")
  ```



### 2.6.3 检索器

将检索器集成到RAG流程中，就像把向量库无缝接入一个完整的问答系统

```python
#将向量库转换为检索器
retriever = vector_database.as_retriever(
    search_type="similarity",  # 搜索类型，可选 "similarity" 或 "mmr"
    search_kwargs={"k": 4}  # 设置返回最相关的4个文档片段
)
```

> 通过`as_retriever()`将向量库包装为检索器，并通过`search_kwargs`控制检索行为。`k=4`表示每次检索返回最相似的4个文本块



# 第三章 构建完整RAG应用

RAG工作流程：添加原始文档 -> 数据处理阶段 -> 检索阶段  -> 增强阶段 -> 生成阶段。

RAG即检索、增强和生成，主要分为两条线：

- 离线处理：向私有知识库源源不断添加私有知识文档
  - 添加未来知识文档（模型训练完成时间是2023年，可以添加2026年的文档）
  - 添加私有知识文档（模型是基于公开知识的，可以添加公司内部知识）
  - 添加参考文档（在正常情况下，可能检索不到/检索错误，可以添加参考资料，规避幻觉）
- 在线处理：向用户提问会先基于私有知识库做检索，获取参考资料，同步组装新提示词询问大模型获取结果



## 3.1 全栈Streamlit

- **优点**：纯Python，无需前后端分离，代码量少，专注RAG逻辑。
- **缺点**：前端能力用不上，但可快速出效果。


### 3.1.1 项目起步

- **目标**：构建一个带 Web 界面的 RAG 应用，用户可上传私有文档（TXT、PDF、MD），系统自动构建向量知识库，后续提问时基于检索到的相关文档片段生成准确答案。

1. 创建python虚拟环境

2. 创建 `requirements.txt`：

   ```text
   langchain
   langchain-community
   langchain-chroma
   dashscope    #通义千问 SDK
   streamlit
   python-dotenv #管理环境变量
   pypdf       #PDF 解析
   unstructured #处理 MD 等
   ```

   安装命令：

   ```bash
   pip install -r requirements.txt
   ```

3. 配置API密钥：在项目根目录创建 `.env` 文件

   ```.env
   DASHSCOPE_API_KEY="sk-7b2fbd6af6eb45e8a52d53470dd322fa"
   ```

### 3.1.2 构建知识库

目的：将用户上传的文档转换为向量并存入 Chroma 数据库

步骤：

#### 1.加载文档、清洗

1. 主流程

   ```python
   raw_documents = load_all_documents(docs_dir)  #docs_dir原始文件夹目录
   if not raw_documents:
       print("警告：未找到任何支持的文档文件。")
       return
   print(f"共加载 {len(raw_documents)} 个原始文档对象。")
   ```

   > 得到all_docs = [[文件1Document对象],[文件2],[文件3]...] 

2. 加载所有支持文档

   ```python
   def load_all_documents(directory: str) -> List[Document]:
       all_docs = []   # 准备一个空列表，用来装所有加载成功的文档对象

       # os.walk 会递归遍历 directory 下的所有子文件夹
       for root, _, files in os.walk(directory):
           for file in files:
               # 只看后缀名是 .txt、.pdf、.md 的文件
               if file.endswith(('.txt', '.pdf', '.md')):
                   file_path = os.path.join(root, file)   # 拼接出完整路径
                   print(f"正在加载: {file_path}")
                   try:
                       docs = load_single_file(file_path)  # 调用单文件加载器
                       all_docs.extend(docs)               # 把加载好的文档对象追加到总列表
                   except Exception as e:
                       print(f"加载文件失败 {file_path}: {e}")#某个文件坏了或格式不支持，跳过并提示

       return all_docs   # 返回收集到的所有文档对象
   ```

   > 遍历筛选出的文件，调用加载器变成documents对象，并将这个对象添加到all_docs列表中

3. 单文件加载器

   ```python
   def load_single_file(file_path: str) -> List[Document]:
       """根据文件扩展名选择对应的加载器"""
       ext = os.path.splitext(file_path)[1].lower() #file_path文件路径
       if ext == '.txt':
           loader = TextLoader(file_path, encoding='utf-8')
       elif ext == '.pdf':
           loader = PyPDFLoader(file_path)
       elif ext == '.md':
           loader = UnstructuredMarkdownLoader(file_path)
       else:
           raise ValueError(f"不支持的文件格式: {ext}")
       
       documents = loader.load()
       # 为每个文档添加来源文件名到元数据中（有些加载器可能已包含，保险起见）
       for doc in documents:
           doc.metadata["source"] = os.path.basename(file_path)
           doc.metadata["file_hash"] = calculate_file_hash(file_path)
           # 清洗内容
           doc.page_content = clean_text(doc.page_content)
       return documents
   ```

4. 调用每个文件计算哈希值

5. 调用清洗文档内容

   ```python
   def clean_text(text: str) -> str:
       """
       清理文本中的多余空白、断行等问题。
       重点：合并被硬换行拆散的句子（中文环境下常见于PDF复制文本）。
       """
       # 将多个连续换行符替换为两个换行（保留段落分隔）
       text = re.sub(r'\n{3,}', '\n\n', text)
       # 去除行尾多余空格
       text = re.sub(r' +', ' ', text)
       # 处理 PDF 中常见的单字换行问题：不是标点符号结尾的换行，替换为空格
       # 简单策略：如果一行以非标点结束，且下一行以非大写字母/数字开头（适应中文）
       # 这里使用更通用的方法：将孤立的 '\n' 前后连接起来（保留 '\n\n' 作为段落标记）
       pattern = re.compile(r'(?<![。！？；：”’"\?\!\.\:\;])\n(?!\n)')
       text = pattern.sub('', text)
       return text.strip()
   ```

#### 2.分割文档

1. 主程序

   ```python
   split_docs = split_documents(raw_documents)
   print(f"分割后得到 {len(split_docs)} 个文本块。")
   ```

2. 分割文档

   ```python
   def split_documents(documents: List[Document]) -> List[Document]:
       """将文档切分为适合嵌入的块"""
       text_splitter = RecursiveCharacterTextSplitter(
           chunk_size=CHUNK_SIZE,
           chunk_overlap=CHUNK_OVERLAP,
           separators=["\n\n", "\n", "。", "！", "？", "；", "，", " ", ""],
           length_function=len,
       )
       return text_splitter.split_documents(documents)
   ```

   > 得到分割好的列表

#### 3.去重、存入Chrome

- 主程序概要

  ```python
  #原始文档所有的文件（夹）名的列表 and 路径是否存在，返回布尔值
  if os.path.exists(persist_dir) and os.listdir(persist_dir): 
  	#1. 加载现有向量库
  	#2. 获取所有文件的哈希值添加到集合（自动去重）
  	#3. 过滤掉已存在的文档块
  else:   
      #创建向量库并填充
  ```

- 创建向量库（见前面向量存储）

  ```python
  vectorstore = Chroma.from_documents(
      documents=split_docs,
      embedding=embedding_model,
      collection_name=collection_name,
      persist_directory=persist_dir
  )
  print(f"向量库创建成功，已存入 {len(split_docs)} 个文本块。")
  ```

- 1.加载现有向量库

  ```python
  vectorstore = Chroma(
      persist_directory=persist_dir,      #持久化地址
      embedding_function=embedding_model, #
      collection_name=collection_name     #集合名称
  )
  ```

- 2.从已有向量库中提取所有已入库文件的哈希值

  说明：得到已有向量库中的哈希值集合

  ```python
  existing_data = vectorstore.get(include=["metadatas"]) #返回库中所有已存储向量的元数据列表
  existing_hashes = set()
  if existing_data and existing_data["metadatas"]:
      for meta in existing_data["metadatas"]:      #收集所有出现过的 file_hash，存入一个集合 
          if meta and "file_hash" in meta:
              existing_hashes.add(meta["file_hash"])
  print(f"现有向量库中已包含 {len(existing_hashes)} 个唯一文件。")
  ```

  补充：

  在前面调用单文件加载器时，遍历documents数组，为每个文件的metadata中添加哈希值

  ```python
  def load_single_file(file_path: str) -> List[Document]:
      documents = loader.load()
      ...
      for doc in documents:
          doc.metadata["file_hash"] = calculate_file_hash(file_path) #添加哈希值
      return documents
  ```

  调用计算哈希值函数

  ```python
  import hashlib
  def calculate_file_hash(file_path: str) -> str:
      """计算文件的 MD5 哈希值"""
      hash_md5 = hashlib.md5()          #生成 MD5 哈希
      with open(file_path, "rb") as f:  #打开读取文件
          # 分块读取，避免大文件一次性占满内存
          for chunk in iter(lambda: f.read(4096), b""):#每次返回4096字节（4KB）
              hash_md5.update(chunk)
      return hash_md5.hexdigest()  # 返回 32 位的十六进制字符串
  ```

  > 哈希算法---MD5：文件内容用32位十六进制字符表示，例如：
  >
  > ```text
  > 5d41402abc4b2a76b9719d911017c592   
  > ```
  >
  > 特点：
  >
  > 1. 同一文件无论计算多少次，得到的MD5值都不变（文件名不同，内容相同也算）
  > 2. 不同文件MD5值都不同（哪怕只有一个逗号之差）


- 3.过滤掉已存在的文档块

  ```python
  # 过滤掉已存在的文档块
  new_docs_to_add = filter_duplicate_documents(split_docs, existing_hashes)
  print(f"去重后剩余 {len(new_docs_to_add)} 个新的文本块。")
  if new_docs_to_add:        #列表有内容，说明需要添加到已有向量库中
      vectorstore.add_documents(new_docs_to_add)
      print(f"已成功添加 {len(new_docs_to_add)} 个新文本块到向量库。")    
  else:
  	print("没有新的文档需要添加。")
  ```

  调用去重逻辑

  > 说明：将切割后的Document列表遍历，对比**每个**哈希值是否已经在哈希值**集合**中
  >
  > 即，筛选出（大）文件中可能存在的（小）文件相同内容

  ```python
  #去重逻辑：避免重复添加相同文件
  def filter_duplicate_documents(
          new_docs: List[Document],  #切割后的Document列表
          existing_hashes: List[str] #哈希值集合
  ) -> List[Document]:
      filtered = []
      for doc in new_docs:
          file_hash = doc.metadata.get("file_hash")
          if file_hash not in existing_hashes:
              filtered.append(doc)
      return filtered
  ```

#### 4.调用主程序

```python
if __name__ == "__main__":
    # 确保文档目录存在
    os.makedirs(DOCUMENTS_DIR, exist_ok=True)   #触发异常：（原始文档）目录存在不触发
    print(f"请将要处理的文档放入 '{DOCUMENTS_DIR}' 目录下，然后按回车继续...")
    input()
    build_or_update_vectorstore()   #调用主程序，主程序再调用其他程序
    print("知识库构建流程结束。")
```

> `if __name__ == "__main__":`当该脚本（.py）作为主程序时，执行下面代码；当它作为模块被调用在其他脚本时，执行else



### 3.1.3 封装RAG问答链

目的：接收用户问题，检索相关文档，调用大模型生成答案。

步骤：

####1.加载向量库

- 加载向量库函数（语法与构建知识库一样）

  ```python
  @st.cache_resource  #缓存向量库
  def load_vector_store():
      """加载或返回 None（如果向量库不存在）"""
      ## 会话历史 JSON 文件存储目录 and # 离线知识库构建（已完成）
      if os.path.exists(CHROMA_PERSIST_DIR) and os.listdir(CHROMA_PERSIST_DIR):
          return Chroma(
              persist_directory=CHROMA_PERSIST_DIR,
              embedding_function=embedding_model,
              collection_name=COLLECTION_NAME
          )
      return None
  ```

- 主流程（调用函数）

  ```python
  vectorstore = load_vector_store()
  if vectorstore is None:
      return None
  ```

####2.创建检索器

利用检索器进行（`知识库中向量`与`用户问题转化的向量`）相似度匹配

```python
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
```

####3.加载历史记录

- 构架历史记录函数（加载历史）

  ```python
  def get_session_history(session_id: str) -> FileChatMessageHistory:
      """根据 session_id 返回对应的文件历史记录对象"""
      file_path = os.path.join(CHAT_HISTORY_DIR, f"{session_id}.json")
      return FileChatMessageHistory(file_path)
  ```

- 包装基础链（包装历史）

  ```python
  def get_conversational_rag_chain():
      """返回包装了历史记忆功能的 RAG 链"""
      base_chain = create_rag_chain()  #返回基础链（见下面）
      if base_chain is None:
          return None

      chain_with_history = RunnableWithMessageHistory(
          runnable=base_chain,
          get_session_history=get_session_history,#工厂函数
          input_messages_key="question",       # 用户输入对应的 key
          history_messages_key="history",      # 提示词中历史记录的变量名
      )
      return chain_with_history
  ```

####4.构造LCEL链

- 提示词模版

  ```python
  system_prompt = """你是一个专业的知识问答助手。请严格基于以下【上下文】信息回答【问题】。
  如果上下文中没有相关信息，请直接说“我没有找到相关信息”，不要自己编造答案。
  如果问题与上下文无关，可以基于你的常识简单回应，但不要过度发挥。
  【上下文】：
  {context}"""
  #组装历史提示词模版
  prompt = ChatPromptTemplate.from_messages([
      ("system", system_prompt),
      MessagesPlaceholder(variable_name="history"),  # 历史对话占位符
      ("human", "{question}")
  ])
  ```


- 将检索的文档格式化为字符串

  ```python
  def format_docs(docs):
      return "\n\n".join(doc.page_content for doc in docs)
  ```

- 构建LCEL链

  ```python
  rag_chain = (
      {
                 #提取用户问题|检索知识库返回多个文档块|拼接成大字符串
          "context": (lambda x: x["question"]) | retriever | format_docs,
          "question": lambda x: x["question"],
          "history": lambda x: x["history"]
      }
      | prompt 
      | llm    
      | StrOutputParser()
  )
  ```

  > LCEL链的数据流向:
  >
  > ```text
  > 用户输入: {"question": "什么是Python装饰器？"}
  >           │
  >           ▼
  > ┌─────────────────────────────────────────────────────┐
  > │  并行执行三个分支                                      │
  > ├─────────────────────────────────────────────────────┤
  > │ 1. retriever.invoke("什么是Python装饰器？")           │
  > │     → 返回4个相关Document对象                          │
  > │     → format_docs() 将它们拼接为一个大字符串           │
  > │     → 赋值给变量 context                              │
  > │                                                       │
  > │ 2. RunnablePassthrough() 直接传递用户问题             │
  > │     → 赋值给变量 question                             │
  > │                                                       │
  > │ 3. RunnableWithMessageHistory 从 JSON 文件读取历史     │
  > │     → 返回 BaseMessage 列表                          │
  > │     → 赋值给变量 history                              │
  > └─────────────────────────────────────────────────────┘
  >           │
  >           ▼
  >     ChatPromptTemplate
  >     (填充 context, question, history)
  >           │
  >           ▼
  >     ChatTongyi (流式生成)
  >           │
  >           ▼
  >     StrOutputParser (提取纯文本)
  >           │
  >           ▼
  >     最终回答字符串
  > ```

### 3.1.4 前端渲染

#### 1.streamlit简介

[Streamlit中文开发手册](https://developer.baidu.com/article/details/3321118)

Streamlit 是一个开源的 Python 框架，让你可以用纯 Python 脚本快速构建和分享交互式 Web 应用

**设计思想：**

- 脚本化：Streamlit 应用本质上是一个从上到下执行的 Python 脚本。每当你在界面上交互（如点击按钮、移动滑块），整个脚本都会从头到尾重新执行一遍。
- 无状态：每次重跑，所有的变量都会重置，应用会“忘记”之前的状态，比如一个简单的计数器会归零。

**Streamlit 提供的内置功能：**

- 页面设置与布局

  ```python
  st.set_page_config(page_title="标题", page_icon="🤖", layout="wide")
  st.title("大标题")
  st.sidebar.header("侧边栏标题")
  st.divider()   # 分割线
  ```

  - `set_page_config` 必须在任何其他 Streamlit 命令之前调用
  - 侧边栏组件通过 `st.sidebar.xxx()` 调用，主区域用 `st.xxx()`

- 会话状态

  ```python
  if "session_id" not in st.session_state:
      st.session_state.session_id = str(uuid.uuid4())

  # 后续任何时候都可以读写
  st.session_state.messages.append({"role": "user", "content": prompt})
  ```

  > 如果不使用 `st.session_state`，每次交互时所有变量都会被重置为初始值。

- 聊天页面组件

  - **st.chat_message(role)**：创建一个聊天气泡容器，`role` 可以是 `"user"` 或 `"assistant"`。
  - **st.chat_input(placeholder)**：在页面底部显示一个固定的输入框，用于接收用户问题。
  - **st.markdown(content)**：在气泡内渲染 Markdown 格式的文本。

- 缓存装饰器

  用于缓存那些加载成本高、且不应被重复执行的操作

  ```python
  @st.cache_resource   #例如加载向量库、初始化嵌入模型
  def load_vector_store():
      return Chroma(...)
  ```

  被缓存的函数**只在第一次调用时执行**，后续调用直接从内存返回结果，即使脚本重新运行也不会重新加载


- 流式输出

  ```python
  message_placeholder = st.empty()   # 创建一个空占位符
  full_response = ""
  for chunk in chain.stream(...):
      full_response += chunk
      message_placeholder.markdown(full_response + "▌")  # 实时更新占位符内容
  message_placeholder.markdown(full_response)   # 最终显示完整答案
  ```

**streamlit执行流程：**

1. **用户打开页面** → 脚本从上到下执行一遍。
2. **用户触发交互**（输入文字、点击按钮等）→ 脚本**再次从上到下完整执行**。
3. 只有通过 `st.session_state` 存储的变量和 `@st.cache` 缓存的函数返回值才会被保留，其他局部变量都会重新初始化。

#### 2.搭建前端主体

- 页面设计

  ```python
  st.set_page_config(page_title="标题", page_icon="🤖", layout="wide")
  st.title("大标题")
  ...
  #侧边栏标题
  with st.sidebar:
      st.header("📁 知识库管理")
  ...
  #主区域  
  for message in st.session_state.messages:
      with st.chat_message(message["role"]):
          st.markdown(message["content"])

  ```

- 侧边栏（有上到下）

  1. 更新向量库状态
  2. 知识库构建引导
  3. 清空当前对话

- 主区域

  用户输入处理（调用前面5个步骤）

#### 3.数据渲染

侧边栏（略）

主区域的用户输入处理

1. 初始化会话状态

   ```python
   if "session_id" not in st.session_state:
       st.session_state.session_id = str(uuid.uuid4())  # 生成唯一会话ID
   if "messages" not in st.session_state:
       st.session_state.messages = []  # 用于前端展示的对话列表
   if "vector_store_ready" not in st.session_state:
       st.session_state.vector_store_ready = False
   ```

2. 将用户消息添加到展示列表

   ```python
   st.session_state.messages.append({"role": "user", "content": prompt})
   with st.chat_message("user"):
       st.markdown(prompt)
   ```

3. 获取带记忆的链

   ```python
   chain = get_conversational_rag_chain()
   if chain is None:
       st.error("无法初始化问答链，请检查向量库配置。")
       st.stop()
   ```

4. 调用链并生成回答（流式输出）

   ```python
   with st.chat_message("assistant"):
       message_placeholder = st.empty()
       full_response = ""

       # 准备 config（包含 session_id）
       config = {"configurable": {"session_id": st.session_state.session_id}}

       # 流式调用 LCEL 链
       try:
           for chunk in chain.stream(
               {"question": prompt},  # 注意 key 需与 input_messages_key 一致
               config=config
           ):
               full_response += chunk
               message_placeholder.markdown(full_response + "▌")
           message_placeholder.markdown(full_response)
       except Exception as e:
           full_response = f"出错了: {str(e)}"
           message_placeholder.error(full_response)
   ```

5. 将助手回答添加到展示列表

   ```python
    st.session_state.messages.append({"role": "assistant", "content": full_response})
   ```



## 3.2 Vue3 + FastAPI

- **优点**：前后端分离，前端自由度高，贴近真实项目。


###3.2.1 项目起步

- 项目结构：

  ```text
  rag_project/
  ├── backend/            
  ├── frontend/           
  ├── docker-compose.yml       # 一键启动所有服务
  ├── README.md                # 写给面试官看的项目说明
  └── .gitignore               # 全局忽略文件
  ```

####1.`docker-compose.yml` 文件

配置一个 PostgreSQL 16 数据库，设置好常用的环境变量（用户名、密码、数据库名），并完成 5432 的端口映射。  

1. 配置文件

2. 运行

   ```bash
   docker-compose up -d   #后台运行
   ```



####2.`backend`文件

1. 创建并启动虚拟环境

   ```bash
   cd backend
   python -m venv venv
   venv\Scripts\activate
   ```

2. 安装依赖

   ```bash
   pip install fastapi uvicorn pydantic
   ```

   记录依赖

   ```bash
   pip freeze > requirements.txt
   ```

3. 构建`main.py`

   ```python
   from fastapi import FastAPI
   from fastapi.middleware.cors import CORSMiddleware

   # 初始化 FastAPI 应用
   app = FastAPI(
       title="AI Study Copilot API",
       description="AI 辅助学习工作站后端接口",
       version="1.0.0"
   )

   # 配置 CORS (跨域资源共享)
   # 这非常重要，因为前端 (Vue) 和后端 (FastAPI) 本地开发时通常在不同的端口
   # 必须允许跨域，前端才能调得通后端的接口
   app.add_middleware(
       CORSMiddleware,
       allow_origins=["*"],  # 允许所有来源（开发环境下方便，生产环境需限制）
       allow_credentials=True,
       allow_methods=["*"],  # 允许所有 HTTP 方法 (GET, POST 等)
       allow_headers=["*"],  # 允许所有请求头
   )

   # 定义一个基础的 GET 路由，用于测试服务是否存活 (Health Check)
   @app.get("/")
   async def root():
       return {
           "status": "success",
           "message": "Welcome to AI Study Copilot API! 🚀",
           "docs_url": "/docs"  # 提示查看 API 文档的地址
       }
   ```

4. 启动后端

   ```bash
   uvicorn main:app --reload
   ```

   ​

####3.`frontend`文件

1. 创建项目

   ```bash
   cd ..
   npm create vite@latest
   ```

   ​

####4.`.gitignore`文件

1. 配置`gitginore`文件
2. ​














# 第四章 Agent

RAG与Agent的区别：

- RAG让模型“知道”得更多，通过检索外部知识库来回答问题
- Agent让模型“能做”得更多，它可以主动调用工具、规划步骤、执行操作

Agent的核心工作机制**ReAct**：

- “推理”与“行动”交替进行的循环。

  循环过程：

  用户输入 -> 推理（是否需要调度工具） -> 是：行动（选择工具 -> 执行工具）-> 推理

  ​								     -> 否：返回结果

工具（Tools）：

|   工具类型   |             作用             |              示例              |
| :----------: | :--------------------------: | :----------------------------: |
| **检索工具** | 连接向量数据库，进行语义搜索 |      RAG检索、知识库查询       |
| **API工具**  |   调用外部API获取实时数据    |  天气查询、股票行情、航班信息  |
| **计算工具** |      执行数学运算或代码      | 数学表达式求值、Python代码执行 |
| **存储工具** |       读写数据库或文件       |       SQL查询、文件操作        |



