# 第一章 认识FastAPI

## 1 确认环境

1. 检查Python环境：FastAPI 依赖 Python 3.8 及更高版本

   ```bash
   python --version
   ```

2. 创建虚拟环境：避免依赖冲突

   ```python
   # 创建虚拟环境
   python -m venv venv

   # 激活虚拟环境（Windows）
   .venv\Scripts\Activate.ps1
   ```

3. 安装FastAPI

   ```python
   pip install fastapi          #只安装核心包
   pip install "fastapi[all]"   #安装所有可选依赖
   ```

4. 安装Uvicorn：FastAPI 是一个 ASGI 框架，需要一个 ASGI **服务器**来运行。最常用的是 Uvicorn

   ```bash
   pip install "uvicorn[standard]"
   ```

5. 创建项目并运行

   ```python
   from fastapi import FastAPI

   # 创建 FastAPI 应用实例
   app = FastAPI()

   # 定义根路径的 GET 路由
   @app.get("/")
   async def root():
       return {"message": "Hello World"}
   ```

   ```bash
   uvicorn main:app --reload #--reload热启动（自动更新）
   ```

   点击网址，跳转到API命令

   给网址添加`/docs`，查看文档

##2 核心语法

###2.1 路由

- 根路径路由：

  ```python
  from fastapi import FastAPI
  app = FastAPI()

  @app.get("/")    #使用装饰器创建一个处理根路径的路由
  def read_root(): #路由处理函数
      return {"Hello": "World"}
  ```

  FastAPI支持所有HTTP方法：

  | 装饰器          | HTTP 方法 | 常见用途      |
  | --------------- | --------- | ------------- |
  | `@app.get()`    | GET       | 获取/读取数据 |
  | `@app.post()`   | POST      | 创建新数据    |
  | `@app.put()`    | PUT       | 完整更新数据  |
  | `@app.patch()`  | PATCH     | 部分更新数据  |
  | `@app.delete()` | DELETE    | 删除数据      |

### 2.2 参数

#### 2.2.1 路径参数

```python
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

> `item_id: int`：
>
> `q: str = None`：可选参数（默认为None）
>
> 访问：`http://i27.0.0.1:8000/item/5?q=runoob`；返回：`"item_id": 5, "q": runoob`

路径参数_Path类型注解：

- 校验：

  ```python
  from fastapi import FastAPI, Path
  @app.get("/items/{item_id}")
  def read_item(item_id: int=Path(..., gt=0, lt=100, description="取值范围0-100")):
      return {"item_id": item_id, "q": q}
  ```


- Path参数：

  |       Path参数       |             说明              |
  | :------------------: | :---------------------------: |
  |         ...          |             必填              |
  |    gt/ge    lt/le    | 大于/大于等于   小于/小于等于 |
  |     description      |             描述              |
  | min_length/manlength |           长度限制            |

#### 2.2.2 查询参数

```python
@app.get("/items/")
def read_item(skip: int = 0,  limit: int = 10):
    return {"skip": skip, "limit": limit}
```

> 访问：`http://i27.0.0.1:8000/item/?skip=1&limit=5`；返回：`{"skip": 1, "limit": 5}`。
>
> 当然，直接访问`http://i27.0.0.1:8000/item/`；返回：`{"skip": 0, "limit": 10}`

查询参数_Query类型注解：

- 校验：

  ```python
  from fastapi import FastAPI, Query
  @app.get("/items/")
  def read_item(skip: int = Query(0, gt=0, lt=100, description="取值范围0-100")):
      return {"skip": skip, "limit": limit}
  ```

  > 用默认值替换`...`

  ​


#### 2.2.3 请求体参数

```python
from pydantic import BaseModel  #导入基类
from fastapi import FastAPI

app = FastAPI()
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")     #主要用于post请求
def create_item(item: Item):
    return item
```

> 访问：`http://127.0.0.1:8000/docs`，在Swagger UI中填写字段，点击Execute，返回结果

请求体参数_Field参数注解：

- 校验：

  ```python
  from pydantic import BaseModel, Field

  class Item(BaseModel):
      name: str = Field(default="张三", le=10)
      description: str = None

  @app.post("/items/")     #主要用于post请求
  def create_item(item: Item):
      return item
  ```

- Field参数：

  |      Field参数       |             说明              |
  | :------------------: | :---------------------------: |
  |         ...          |             必填              |
  |    gt/ge    lt/le    | 大于/大于等于   小于/小于等于 |
  |     description      |             描述              |
  | min_length/manlength |           长度限制            |
  |       default        |            默认值             |

###2.3 响应类型 - JSON格式

默认情况下，FastAPI会自动将返回的python对象（字典、列表、Pydantic模型），转换为JSON兼容格式，并包装为JSONResponse返回

- 常见响应类型：

  |     响应类型      |     用途     |               示例                |
  | :---------------: | :----------: | :-------------------------------: |
  |   JSONResponse    |   默认响应   |      return {"key": "value"}      |
  |   HTMLResponse    | 返回HTML内容 | return HTMLResponse(html_content) |
  |   FileResponse    | 返回文件下载 |     return FileResponse(path)     |
  | StreamingResponse |   流式响应   |        生成器函数返回数据         |
  | RedirectResponse  |    重定向    |   return RedlirectResponse(url)   |


- 指定响应类型：

  两种方式：

  - 装饰器中指定响应类：用于固定返回类型（HTML、txt等）
  - 返回响应对象：文件下载、图片、流式响应

####2.3.1 装饰器中指定响应类

- HTMLResponse

  ```python
  from fastapi import FastAPI
  from fastapi.responses import HTMLResponse
  app = FastAPI()

  @app.get("/html", response_class=HTMLResponse)
  def get_html():
      return "<h1>这是一级标题</h1>"
  ```

  > 访问：`http://127.0.0.1:8000/html`，可以看到解析后的HTML标签

- FileResponse

  ```python
  from fastapi import FastAPI
  from fastapi.responses import FileResponse
  app = FastAPI()

  @app.get("/file")
  def get_file():
      path = "./files/1.jpeg"
      return FileResponse(path)
  ```

  > 访问：`http://127.0.0.1:8000/file`，可以看到图片


- 自定义响应格式

  ```python
  from fastapi import FastAPI
  from pydantic import BaseModel
  app = FastAPI()

  class News(BaseModel):
      id: int
      title: str
      content: str

  @app.get("/news/{id}", response_model=News)
  def get_news(id: int):
      return {
  		'id': id,
  	    'title': f"这是第{id}本书",
  	    'content': "这是一本好书"
      }
  ```

  ​

###2.4 异常响应

在客户端引发错误（4xx），应使用fastapi.HTTPException来中断正常处理流程，并返回标准错误响应。

- 语法：

  ```python
  from fastapi import FastAPI, HTTPException
  app = FastAPI()

  @app.get("/news/{id}")
  def get_news(id: int):
      id_list = [1, 2, 3, 4, 5]
      if id not in id_list:
          return HTTPException(status_code=404, detail="当前id不存在")
      return {"id"： id}
  ```

  ​

###2.5 中间件

中间件是一种在每个请求进入FastAPI应用都会自动执行的函数。

他的请求到达实际路径之前运行，并且在响应返回给客户端之前再运行一遍

- 语法：

  ```python
  from fastapi import FastAPI, Request
  app = FastAPI()

  @app.middleware("http")
  async def process1(request: Request, call_next):
      print("中间件1，start")
      response = await call_nexe(request) 
      print（"中间件1，end"）
      return response
  ```

  注意：如果有多个中间件，从下往上执行，先进后出。例如，下面还有一个process1函数（中间件2）

  执行顺序：`中间件2，start` -> `中间件1，start` -> `中间件1，end` -> `中间件2，end`

  ​


### 2.6 依赖注入

使用依赖注入，减少代码重复，可以多次被使用

依赖项：重复函数组件

- 代码：

  ```python
  from fastapi import Depends, FastAPI
  app = FastAPI()

  # 1. 定义依赖函数
  def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
      return {"q": q, "skip": skip, "limit": limit}

  # 2. 在路由中使用依赖
  @app.get("/items/")
  async def read_items(commons: dict = Depends(common_parameters)): #Depends声明依赖
      # commons 接收依赖函数的返回值
      return commons
  ```













#第二章 使用Docker

## 1 Docker简介

每个服务独立容器化，每个运行环境就是一个容器，运行容器的计算机就是宿主机。

Docker容器与虚拟机的区别：

- Docker容器之间共用一个系统内核
- 每个虚拟机都包含一个操作系统完整内核

Docker的镜像与容器：

- 镜像是软件安装包
- 容器是软件应用

>   可以利用安装包安装无数个软件，还可以将安装包发送到其他宿主机，

镜像仓库用于存放镜像的地方，每个人都可以把镜像上传到仓库里，其他人就可以下载镜像。Docker的官方仓库就是Docker Hub



##2 使用Docker

###2.1 安装Docker

Docker是基于Linux的容器化部署技术，所以需要使用Linux系统，但Windows和Mac系统都虚拟了Linux子系统

1. 启动Linux子系统

2. 安装Docker

   - 在官网下载安装包（默认安装位置）
   - 使用命令行安装（可以指定安装位置）

3. 配置镜像源

   配置国内“镜像加速器”：Docker链接官方镜像仓库(Docker Hub)时，会因网络问题导致连接超时

   步骤：

   1. 打开 Docker Desktop 设置

   2. 进入 Docker Engine 配置页面

   3. 修改配置JSON文件

      ```json
      {
        "registry-mirrors": [ //添加镜像加速地址       
          "https://docker.1ms.run",   
          "https://docker-0.unsee.tech",
          "https://docker.m.daocloud.io"
        ],
        "features": {        //开启增强功能
          "buildkit": true
        }
      }
      ```

   ​

###2.2 使用容器

> 注意：使用Docker要一直保持打开状态

使用Docker可以使用可视化界面，也可以使用命令行

Docker常用的命令：

1. 获取镜像：用于从仓库下载镜像（拉取）

   ```bash
   docker pull ......
   ```

2. 使用镜像并创建运行容器

   ```bash
   docker run ......
   ```

   后面接名字或id等。每创建一个容器就会自动分配唯一id，若没有设置名字，系统会自动分配一个随机名字

   - -d：后台运行容器，例如 `docker run -d ubuntu`
   - nginx：镜像不存在，自动拉取，例如`docker run nginx`
   - -p：端口映射，因为Docker运行在容器，容器与宿主机隔离，宿主机无法访问容器网络，例如`docker run -p 80:80`，先外后里
   - -v：挂载卷，宿主机目录与容器目录隔离，删除容器时会删除所有，使用挂载卷就可以将目录保留在宿主机，即数据持久化。例如`docker run -v`

3. 查看正在运行容器

   ```python
   docker ps .....
   ```

   - -a：查看所有容器，例如`docker ps -a`

4. 对现有容器的开启与停止

   运行容器

   ```python
   docker start 名字/id
   ```

   停止运行容器

   ```python
   docker stop 名字/id
   ```



###2.3 使用镜像

1. 查看本地镜像

   ```bash
   docker images
   ```

   > 列出本地所有镜像列表

2. 查找镜像

   从Docker Hub网站来搜索镜像，Docker Hub网址为： **https://hub.docker.com/**

3. 删除镜像

   ```bash
   docker rmi 镜像名
   ```

4. 创建镜像

   除了拉取镜像，还可以自定义镜像， 使用Dockerfile指令创建一个新的镜像

   。。。

###2.4 容器连接

容器之间可以根据内部IP进行访问，但与宿主机是隔离的。要实现不同宿主机容器之间的通信，创建子网



###2.5 Docker Compose

将前端、后端、数据库分别打包成独立容器，但这样增加了使用成本（多次执行`docker run` ，配置各个网络），于是，产生了容器编排技术：Docker Compose

Docker Compose使用yml文件管理多个容器，即Docker Compose文件就是一个或多个Docker run命令，按照特定格式排列的文件

例如

- 传统写法：

  ```bash
  docker run -d `                       #-d：后台运行
    --name my-postgres-db `             #--name：命名
    -e POSTGRES_PASSWORD=yourpassword ` #-e:配置环境变量，用于定义用户名、密码、数据库名
    -e POSTGRES_USER=youruser `
    -e POSTGRES_DB=myragdb `
    -p 5432:5432 `      #-p 5432:5432：将容器的5432端口映射到Windows系统
    postgres:16
  ```

- Docker Compose写法：

  ```docker-compose.yml
  version: '3.8'

  services:
    postgres:
      image: postgres:16
      container_name: my-postgres-db
      environment:
        POSTGRES_PASSWORD: yourpassword
        POSTGRES_USER: youruser
        POSTGRES_DB: myragdb
      ports:
        - "5432:5432"
      # 建议添加数据卷持久化存储，但原命令未包含，故此处注释
      # volumes:
      #   - postgres_data:/var/lib/postgresql/data

  # volumes:
  #   postgres_data:
  ```

  - 启动文件命令：

    ```bash
    docker compose up -d
    ```

    > 会自动创建容器与子网

  - 查看全部容器

    ```bash
    docker ps -a
    ```

  - 停止并删除容器

    ```bash
    docker compose up -d
    ```

  - 停止容器

    ```bash
    docker composh start
    ```

    ​


# 第三章 数据库

市面上有关系型数据库、其他统称为非关系型数据库。

- 关系型数据库：用二维表来存储数据，并且表格之间能按规则联系。主流关系型数据库（见下）都遵循 **SQL 标准**

  常用数据库：

  - **MySQL**：开源、免费，互联网公司最爱，比如Facebook、淘宝早期都用它。
  - **PostgreSQL**：功能更丰富、标准，被称为“最先进的开源数据库”。
  - **Oracle**：功能极其强大，但非常昂贵，银行、政府等大型机构常用。
  - **SQL Server**：微软出品，和Windows生态系统结合得很好。
  - **SQLite**：轻量级，嵌入式设备常用，你的手机里很可能就有它。

- 非关系型数据库：放弃严格的**表结构**、**多表关联**和 **ACID 事务**中的某些要求，换取了**超高的读写性能**、**极致的水平扩展能力**以及对**非结构化数据**（如图片、JSON文档）的灵活存储。

  常用的数据库：

  |      类型      |                           核心特点                           |     代表产品      |                         典型应用场景                         |
  | :------------: | :----------------------------------------------------------: | :---------------: | :----------------------------------------------------------: |
  |  **键值存储**  | 就像一个大字典，通过一个唯一的“键”快速获取对应的“值”。简单、极快。 | Redis, Memcached  |        缓存（比如网页会话、热点数据）、队列、计数器。        |
  | **文档数据库** | 存储的是文档（通常是JSON格式），结构灵活，可以嵌套。每个文档的字段可以不同，很像“表结构自由的关系型数据库”。 | MongoDB, CouchDB  | 内容管理系统、用户资料、日志分析，适合数据模型经常变化的场景。 |
  | **列族数据库** | 以“列族”为单位存储，而不是按行。非常适合处理海量数据中少数几列的查询。 | Cassandra, HBase  |           大数据分析、物联网时序数据、分布式存储。           |
  |  **图数据库**  | 专门用于存储和查询**关系**。把数据抽象成“节点”（人、地点）和“边”（认识、属于）。 | Neo4j, JanusGraph | 社交网络（推荐好友）、反欺诈分析（识别资金流转路径）、知识图谱。 |

实际中，大厂经常**混合使用**两者（比如用 MySQL 存核心订单，用 Redis 存购物车缓存，用 MongoDB 存商品评价）。

## 1 关系型数据库简介

核心结构：表、列（相同列类型相同）、行（一行代表一个完整信息）

实现关系：两表之间使用共同列，例如：

- `学生表`：存储`学号`（主键）、`姓名`、`班级编号`（外键）
- `班级表`：存储`班级编号`（主键）、`班级名称`、`教室`、`班主任`



#第四章 使用ORM

ORM（对象关系映射），仅使用对象和类的方式来操作数据库，而不是直接写 SQL 语句（将python语句转化为转化为SQL语句）。

python支持的ORM框架：

1. SQLAlchemy：生态最全，能处理中大型项目
2. Tortoise ORM：异步优先（处理高并发）
3. Peewee：轻量级

## 1 SQLAlchemy基本使用

步骤：

### 1.1 安装ORM：

```bash
pip install sqlalchemy[asyncio] asyncpg  #数据库+连接MySQL的异步驱动
```

### 1.2 构建数据库

> 数据库的简介：
>
> | 数据库         | 上手难度 | 适合场景                                   | 安装方式              |
> | -------------- | -------- | ------------------------------------------ | --------------------- |
> | **SQLite**     | 极简单   | 本地开发、原型验证、单机小工具             | Python 内置，无需安装 |
> | **PostgreSQL** | 中等     | 生产环境、需要向量检索（pgvector）、高并发 | 独立安装或 Docker     |
> | **MySQL**      | 中等     | 常见 Web 应用、熟悉 LAMP 栈                | 独立安装或 Docker     |

安装PostgreSQL（直接安装&使用Docker）

1. 启动Docker

2. 创建数据库容器

   ```powershell
   docker run -d `                       #-d：后台运行
     --name my-postgres-db `             #--name：命名
     -e POSTGRES_PASSWORD=yourpassword ` #-e:配置环境变量，用于定义用户名、密码、数据库名
     -e POSTGRES_USER=youruser `
     -e POSTGRES_DB=myragdb `
     -p 5432:5432 `      #-p 5432:5432：将容器的5432端口映射到Windows系统
     postgres:16
   ```

3. 在项目中连接数据库

   ```python
   # 使用 Docker 安装的连接字符串
   #数据库驱动+数据库引擎://用户名:密码@主机:端口/数据库名
   DATABASE_URL = "postgresql+asyncpg://youruser:yourpassword@localhost:5432/myragdb"
   ```

   ​

### 1.3 建表

####1.3.1 基本流程

步骤：创建数据库异步引擎 -> 定义模型类 -> 启动应用时建表

核心概念：

- **Engine (引擎)**: 数据库的核心接口，即连接池管理者，因为建立连接很耗时，所以保持一个池子复用。

  应用启动创建一次；全局共享

- **Base (基类)**: 所有模型类的基类。当你定义模型时，需要继承它。

- **Session (会话)**: 与数据库交互的“工作区”，所有数据的增删改查操作都在这里进行。

- **Model (模型)**: 一个 Python 类，代表数据库中的一张表。类的属性对应表的字段。

1. 创建异步引擎

   ```python
   from sqlalchemy.ext.asyncio import create_async_engine
   # 数据库驱动+数据库引擎://用户名:密码@主机:端口/数据库名
   DATABASE_URL = "postgresql+asyncpg://youruser:yourpassword@localhost:5432/myragdb"

   engine = create_async_engine(
       DATABASE_URL,       #数据库地址
       echo=True,          #开发时打印SQL
       pool_size=10,       #常驻5个连接
       max_overflow=20,    #高峰最多创建10个连接
   )
   ```

2. 定义模型、基类

   ```python
   from sqlalchemy.orm import DeclarativeBase

   #定义基类
   class Base(DeclarativeBase):
       create_time: Mapped[datetime] = mapped_column(
           DateTime,
           server_default=func.now(),      # 插入时数据库自动设置
           comment="创建时间",
       )
       update_time: Mapped[datetime] = mapped_column(
           DateTime(timezone=True),
           server_default=func.now(),
           onupdate=func.now(),            # 更新时自动更新
           comment="更新时间",
       )
   ```

   `Base` 是所有模型类的父类，它维护了模型的元数据（MetaData），用于管理表结构信息。

   ```python
   from sqlalchemy.orm import Mapped, mapped_column

   #定义第一个模型（一个类就是一个表，类的实例 = 一行数据）
   class User(Base):
       __tablename__ = "users"    #指定数据库表名

       id: Mapped[int] = mapped_column(primary_key=True, comment="用户ID")#必填整数字段
       name: Mapped[str] = mapped_column(index=True, comment="用户名")
       email: Mapped[str] = mapped_column(index=True, unique=True, comment="用户邮箱")
       password: Mapped[str] = mapped_column(comment="用户密码")
   ```
   > 当我们操作User对象是，会自动翻译成users表的SQL

   - `Mapped[int]` → 必填整数字段
   - `Mapped[Optional[str]]` → 可为空的字符串
   - `Mapped[List["Conversation"]]` → 一对多关系


3. 启动时建表

   定义好模型后，使用 `Base.metadata.create_all()` 自动创建所有表

   ```python
   #建表：定义函数建表 -> FastAPI 应用启动时调用
   async def create_tables():
       # 获取异步引擎，创建事务 - 建表
       async with engine.begin() as conn:
           await conn.run_sync(Base.metadata.create_all)
   ```
   > - 这个方法只会创建不存在的表，不会覆盖已有数据，非常安全
   > - 从 Engine 借出的一个具体连接，`with` 确保连接用完自动关闭


#### 1.3.2 关系映射

用于解决：

- 一个用户有多个对话
- 一个对话有多条消息

1. 一对多（多对一）模型

   ```python
   from sqlalchemy.orm import Mapped, mapped_column, relationship
   class User(Base):
       __tablename__ = "users"
       # 一对一
       id: Mapped[int] = mapped_column(primary_key=True)
       # 一对多（一个用户有多条消息）
       conversations: Mapped[List["Conversation"]] = relationship(
           back_populates="user",  #指向模型反相关联属性名（用户）
       )

   class Conversation(Base):
       __tablename__ = "conversations"
       id: Mapped[int] = mapped_column(primary_key=True)
       
       # 外键：指向 users 表
       user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
       
       # 反向关系：从对话找到用户
       user: Mapped["User"] = relationship(back_populates="conversations")
   ```
   ​

2. 多对多



### 1.4 建立会话

Session是ORM的工作空间，所有对对象的修改，都先在Session里暂存，最后统一提交到数据库，

- 异步Session

  ```python
  from sqlalchemy.ext.asyncio import asyuc_sessionmaker

  #创建会话工厂函数
  AsyncSessionLocal = asyuc_sessionmaker(
      bind=engine,           #绑定引擎
      class_=AsynsSession,   #指定会话类
      autocommit=False,      # 不自动提交
      autoflush=False,       # 不自动刷新
      expire_on_commit=False # 提交后不过期对象（不会重新查询数据库）
  )
  ```

  > `sessionmaker` 是一个工厂函数，调用它就能生成新的 Session 对象

## 2 对数据库增删改查

使用 Python 对象进行数据库的（异步）增删改查

1. 创建会话工厂函数

   ```python
   AsyncSessionLocal = asyuc_sessionmaker(
   	bind=engine,           #绑定引擎
       class_=AsynsSession,   #指定会话类
       expire_on_commit=False # 提交后不过期对象（不会重新查询数据库）
   )
   ```

2. 定义依赖项

   ```python
   async def get_database():
       async with AsyncSessionLocal() as session:
            await session.commit()  #提交事务（关键）
   ```

3. 引用依赖项

   ```python
   @app.get("/book/books")       
   async def get_book_list(db: AsyncSession = Depends(get_database)):
       pass   #增删改查业务
   ```

###2.1 新增数据

核心步骤：定义ORM对象  -> 添加对象到事务 ->  提交到数据库

代码：

- ```python
  class BookBase(BaseModel):
      id: int
      bookname: str
      author: str
      price: float
      publisher: str

  @app.pust("/book/add_books")       
  async def add_book_list(book: BookBase, db: AsyncSession = Depends(get_database)):
      book_obj = Book(**book.__dict__)   #定义ORM对象
      db.add(book_obj)  #新增
      await db.commit()  #提交事务
      return book
  ```

  > 定义ORM对象：用户输入`book` -> 通过`__dict__`转为字典 -> 通过`**`展开，拿到所有键值对 -> 通过`Book`转为ORM对象



###2.2 查询数据

#### 2.2.1 获取所有数据

```python
@app.get("/book/books")       
async def get_book_list(db: AsyncSession = Depends(get_database)):
    stmt = select(Book)     #查询
    reslut = await db.execute(stmt)
    book = result.scalars().all()  # 提取所有 User 实例
    return book
```

- `execute(stmt)` 返回一个 `Result` 对象
- `scalars()` 返回一个可迭代的 `ScalarResult`，提取每一行的第一个字段（这里是 `User` 对象）
- `.all()` 将所有结果收集为 Python `list`

#### 2.2.2 获取单条数据

- 方法一：使用select（）

  ```python
  #其它代码同上	
      book = result.scalars().first()  # 返回第一条或None
  ```

- 方法二：db.get(模型类，主键值)

  ```python
  async def get_book_list(db: AsyncSession = Depends(get_database)):
      book = await db.get(Book, 5)  # 提取所有Book的第五条
      return book
  ```



####2.2.3 条件过滤

- 比较判断：

  ```python
  @app.get("/book/{book_id}")       
  async def get_book_list(db: AsyncSession = Depends(get_database)):
      stmt = select(Book).where(Book.id == book_id)    #查询
      reslut = await db.execute(stmt)
      book = result.scalars().first()  # 提取满足条件的第一个实例
      return book
  ```

  > `result.scalars().first()` 可以改成`result.scalars_one_or_none()`，满足条件返回第一个，不满足条件返回null

- 模糊判断（like）：

  ```python
  #其他不变
      stmt = select(Book).where(Book.author.like("李%"))  ##查询姓李的作者（author）
      
  ```

- 与或非、包含判断

  ```python
  #其他不变
  	#查询姓李的作者（author）且 价格（price）大于100
      stmt = select(Book).where(Book.author.like("李%"))&(Book.price>100) 
      #查询姓李的作者（author）或 价格（price）大于100
      stmt = select(Book).where(Book.author.like("李%"))|(Book.price>100) 
      #数据库id列表 在 我的id列表
      my_id = [12, 34, 48, 21, 62]
      stmt = select(Book).where(Book.id.in_(my_id))
  ```

  ​

####2.2.4 聚合查询

聚合计算：func.方法（模型类.属性）

方法：

- count：统计行数量
- avg：平均值
- max/min：最大值/最小值
- sum：求和

代码：

- ```python
  #其他不变
      stmt = select(func.avg(Book.price)) #查询平均价格  
      ...
  ```



#### 2.2.5 分页查询

目的：自定义查询第几页的数据

分页查询：select.offset.limit()

- offset：跳过的记录数
- limit：返回的记录数
- offset数 = （当前页码 - 1）*每页数量limit

代码：

- ```python
  @app.get("/book/books")       
  async def get_book_list(
      page: int = 1,    #当前页码数
      page_size: int = 3, #每页数量
      db: AsyncSession = Depends(get_database)
  ):
      skip = (page-1)*page_size    
      stmt = select(Book).offset(skip).limit(page_size)     
      reslut = await db.execute(stmt)
      book = result.scalars().all()  
      return book
  ```

  ​

###2.3 更新数据

方式一：先查询再修改

方式二：批量更新（不加载对象，效率更高）

####2.3.1  先查询再修改

核心步骤：查询get -> 属性重新赋值 -> commit提交到数据库

代码：

- ```python
  #更新类型
  class BookBase(BaseModel):
      id: int
      bookname: str
      author: str
      price: float
      publisher: str
  #查询
  @app.put("/book/updata/{book_id}")       
  async def updata_book(
      book_id: int, 
      data: BookBase, 
      db: AsyncSession = Depends(get_database)
  ):
      book = await db.get(Book, book_id)
      if book is None:
          raise HTTPException(
          	status_code=404,
              delail='查无此书'
          )
      #重新赋值
      book.bookname = data.bookname
      book.author = data.author
      book.price = data.price
      book.publisher = data.publisher
      await db.commit()
      return book
  ```

  ​

###2.4 删除数据

方法一：先查询，再删除

方法二：批量删除

####2.4.1 先查询再删除

核心步骤：查询get -> delete删除 -> commit提交到数据库

代码：

- ```python
  #查询
  @app.delete("/book/delete——book/{book_id}")       
  async def updata_book(book_id: int,  db: AsyncSession = Depends(get_database)):
      book = await db.get(Book, book_id)
      if book is None:
          raise HTTPException(
          	status_code=404,
              delail='查无此书'
          )
      await db.delete(book)
      await db.commit()
      return {"msg": "删除成功"}
  ```

  ​

##3 数据库迁移

在生产项目中，数据库结构会不断变化。Alembic 是 SQLAlchemy 官方推荐的迁移工具，可以**版本化管理数据库**。

使用步骤：

1. 安装与初始化

   ```bash
   pip install alembic
   alembic init alembic  #初始化Alembic环境
   ```

   执行后，根目录会多一个alembic文件夹（存放迁移脚本文件）和alembic.ini文件（配置文件）

2. 配置 Alembic 连接你的数据库

   > 异步 PostgreSQL，需要同时配置 Alembic 以同步方式连接（Alembic 本身不支持异步操作，但可以通过异步引擎的 `sync_engine` 桥接）

   1. 修改alembic.ini

      ```ini
      # 假设你的数据库信息为：用户名 youruser，密码 yourpassword，主机 localhost，端口 5432，数据库 myragdb
      sqlalchemy.url = postgresql+psycopg2://youruser:yourpassword@localhost:5432/myragdb
      ```

   2. 修改alembic/env.py

      ```python
      from app.database import Base   # 导入你的声明式基类
      from app import models            # 确保所有模型都被导入，这样 Base.metadata 才能包含所有表

      target_metadata = Base.metadata
      ```

      ​

3. 产生迁移文件

   ```bash
   alembic revision --autogenerate -m "init database"
   ```

   > - `--autogenerate`：让 Alembic 比较你定义的模型（`target_metadata`）和当前数据库的实际状态，自动生成升级/降级代码。
   > - `-m "init database"`：给这次迁移一个描述性的消息。

