# Node.js前端知识体系

Node.js编写服务器端程序，主要作用：

1. 编写数据接口，此时Node.js作为**后端**运行。

2. Node.js是**前端工程化**的基础设施和构建平台

   ​

Node.js为什么能够运行JS代码？

- Node.js能够运行JS代码，是基于Chrome V8引擎进行封装
- 浏览器能够运行JS代码，是依靠内核中的V8引擎（这个V8引擎可以理解为C++编写的程序）
- 这两者都能独立运行JS代码，但有区别：
  1. 这两种环境都支持ECMAScript语法
  2. DOM、window、BOM、XMLHttpRequest等等只在浏览器存在
  3. fs、path、http只在Node.js环境存在

## 1 前端工程化

 **为什么Node.js成为前端工程化的基石？**

核心优势：

- **同一语言**：前后端都使用JavaScript，降低学习成本
- **npm生态**：全球最大的包管理系统，百万级工具包
- **跨平台**：Windows/macOS/Linux一致体验
- **高性能I/O**：适合构建工具链

**前端工程化**是一套系统化的方法论和工具链，旨在提高前端开发效率、保障代码质量、优化项目可维护性，并实现团队协作的标准化。

**Node.js中这些工具通常包括**：

| 角色           | 具体实现     | 工具示例                  |
| -------------- | ------------ | ------------------------- |
| **包管理器**   | 依赖管理     | npm、yarn、pnpm           |
| **构建工具**   | 代码转换打包 | Webpack、Vite、Rollup     |
| **开发服务器** | 本地开发环境 | webpack-dev-server、Vite  |
| **代码质量**   | 规范和检查   | ESLint、Prettier          |
| **测试框架**   | 自动化测试   | Jest、Mocha、Cypress      |
| **任务运行器** | 自动化脚本   | npm scripts、Gulp         |
| **脚手架**     | 项目生成     | Vue CLI、Create React App |

### 1.1 生态环境

**通俗说**：生态环境 = **核心工具 + 所有围绕它发展的配套设施+社区**

前端框架中有：Vue生态、React生态等

#### 1.1.1 生态环境的三大支柱

- **工具链（基础设施）**

  前端工具链包括：

  - 开发服务器：随时看到效果
  - 打包工具：把代码整理好
  - 代码检查：避免低级错误
  - 测试工具：确保质量


- **社区和文档（知识体系）**：用于学习交流


- **第三方库和插件（商业生态）**：应用于提供更多业务

#### 1.1.2 Node.js 生态环境

- **基础建设（市中心）**

  ```
  Node.js（核心）→ 提供：运行JavaScript的能力
  ```

- **周边配套设施（生态环境）**

  ```
  1. 包管理器：
     - npm：最大的超市（有30多万个包）
     - yarn：外资连锁超市
     - pnpm：高效仓储式超市

  2. 框架：
     - Express：简单直接
     - Koa：更现代化
     - NestJS：像开发区

  3. 数据库连接：
     - mongoose → 连接MongoDB
     - sequelize → 连接MySQL/PostgreSQL
     - redis → 连接Redis

  4. 工具链：
     - Webpack：地铁系统
     - Babel：语言翻译站
     - ESLint：交通规则检查站
     - Jest：质量检测中心
  ```

- **社区与服务（人和服务）**

  ```
  1. 开发者社区（市民）：
     - GitHub上的贡献者
     - Stack Overflow上的答疑者
     - 博客作者、教程制作者

  2. 公司支持（企业）：
     - Vercel、Netlify（提供部署服务）
     - AWS、阿里云（提供服务器）
     - 各种SaaS服务
  ```

#### 1.1.3 Vue 生态环境

- **核心设施（主园区）**

  ```
  Vue.js（核心）
  ```


- **周边游乐设施（生态）**

  ```
  1. 官方认证项目：
     - Vue Router
     - Vuex/Pinia
     - Vue DevTools

  2. 构建工具（乐园基础设施）：
     - Vite：高速游览车（极速启动）
     - Vue CLI：传统观光车（功能全面）
     - Nuxt.js：乐园度假套餐（一站式体验）

  3. UI组件库（餐饮和商店）：
     - Element Plus：中餐美食街
     - Ant Design Vue：亚洲风味区
     - Vuetify：西式餐饮区
     - Quasar：国际美食广场

  4. 插件系统（临时摊位和活动）：
     - vue-i18n：多语言翻译站
     - vue-test-utils：游乐设施安全检测
     - 各种社区插件：街头表演和临时活动
  ```

  ​

### 1.2 Vue 3 项目完整工程化配置

```
my-vue-project/
├── .github/                    # CI/CD配置
│   └── workflows/
├── .husky/                    # Git钩子
├── .vscode/                   # 编辑器配置
├── public/                    # 静态资源
├── src/
│   ├── api/                   # API接口
│   ├── assets/                # 资源文件
│   ├── components/            # 公共组件
│   ├── composables/           # 组合式函数
│   ├── layouts/               # 布局组件
│   ├── plugins/               # Vue插件
│   ├── router/                # 路由配置
│   ├── store/                 # 状态管理
│   ├── styles/                # 全局样式
│   ├── utils/                 # 工具函数
│   ├── views/                 # 页面组件
│   ├── App.vue
│   └── main.js
├── tests/
│   ├── e2e/                   # E2E测试
│   ├── unit/                  # 单元测试
│   └── __mocks__/            # Mock数据
├── .browserslistrc           # 浏览器兼容性
├── .editorconfig             # 编辑器配置
├── .eslintrc.js              # ESLint配置
├── .gitignore                # Git忽略
├── .npmrc                    # NPM配置
├── .prettierrc               # 代码格式化
├── babel.config.js           # Babel配置
├── commitlint.config.js      # 提交信息规范
├── cypress.config.js         # E2E测试配置
├── index.html                # HTML模板
├── jsconfig.json             # JS配置
├── package.json              # 项目配置
├── postcss.config.js         # PostCSS配置
├── README.md                 # 项目说明
├── vite.config.js            # Vite配置
└── vitest.config.js          # 测试配置
```



## 2 node.js常用模块

**前置知识**：

- 我们前面学习的JS代码，是可以在终端（CMD）通过`node 文件名.js`进行运行
- 模块：类似于插件，封装了方法、属性等

### 2.1 fs模块

- fs模块：封装了与本机系统进行交互的方法/属性

- 语法：

  ```js
  //加载fs模块对象
  const fs = require('fs') 

  //写入文件内容
  fs.writFile('文件','写入内容',err => {
      //写入后的回调函数
  })

  //读取文件内容
  fs.writFile('文件路径',(err,data) => {
      //读取后的回调函数
      //data是文件内容的Buffer的数据流
  })
  ```

### 2.2 path模块

- 目标：处理文件路径问题（在前置知识中介绍了通过终端执行JS文件，但会出现父子路径问题）

- 语法：

  ```javascript
  //加载path模块
  const path = require('path')

  //使用path.join方法，拼接路径
  path.join('路径1','路径2',……)
  ```

### 2.3 http模块

- 作用：创建Wed服务并**响应内容**给浏览器

- 语法：

  ```javascript
  //加载http服务，创建Wed服务对象
  const http = require('http')
  const server = http.createServer()

  //监听request请求事件，设置响应头和响应体
  server.on('request',(req,res) => {
      //设置请求头：内容类型，普通文本；编码格式为UTF-8
      res.setHeader('Coutent-Type','text/plain；charset=utf-8')
      res.end('你好，欢迎使用node.js创建的wed服务')
  })

  //配置端口号并启动Wed服务
  server.listen(3000,() => {
      console.log('Wed服务已经启动')
  })
  ```

### 2.4 模块导入、导出

|                  |          ECMAScript标准语法           |    CommonJS标准语法     |
| :--------------: | :-----------------------------------: | :---------------------: |
| **导入**（全局） |       export default { 变量名 }       |   module.exports = {}   |
|     （按需）     |       export const baseULR = ''       |                         |
| **导出**（全局） |   import 变量名 from '模块名/路径'    | require('模块名或路径') |
|     （按需）     | import { baseULR } from '模块名/路径' |                         |

## 3  包管理器

### 3.1 包的概念

- **概念**：将模块、代码、其他资料集合成的一个**文件夹**

- 包的分类：

  - 项目包：主要用于封装**项目与业务**逻辑
  - 软件包：封装**工具与方法**

- > 这两种包在其根目录下，必须有package.json文件，用于记录包的清单信息
  >
  > 引入包，引入的默认是main属性指定的模块文件（main.ts）
  >
  > 另外，
  >
  > - node_modules: 依赖存放目录
  > - package-lock.json: 锁定依赖版本（确保一致性）



### 3.2 npm软件包管理器

- npm是Node.js标准的软件包管理器
- npm仓库中拥有超3500000个软件包
- 从起初作为下载和管理Node.js包依赖的方式

使用：

1. 初始化清单工具

   ```bash
   npm init -y    #获得默认的package.json文件（-y  默认的）
   ```

2. 下载软件包

   ```bash
   npm i 软件包名称
   ```

3. 使用软件包

> 这一过程记录为：
>
> 1. `npm i 软件包`：从npm资源库下载
> 2. 把软件包放到`node_modules`文件夹中
> 3. `package.json` `package-lock.json`记录并固化版本（不会因版本迭代而改变）

#### 三大包管理器对比

| 特性             | npm              | Yarn          | pnpm          |
| ---------------- | ---------------- | ------------- | ------------- |
| **安装速度**     | 中等             | 快            | 极快          |
| **磁盘空间**     | 大               | 大            | 节省          |
| **node_modules** | 扁平化           | 扁平化        | 符号链接      |
| **确定性安装**   | 有(package-lock) | 有(yarn.lock) | 有(pnpm-lock) |
| **工作区**       | 支持             | 优秀支持      | 优秀支持      |
| **离线模式**     | 支持             | 支持          | 支持          |
| **安全审计**     | 内置             | 内置          | 内置          |
| **幽灵依赖**     | 存在             | 存在          | 避免          |

最佳实践建议

- **新项目**: 推荐 pnpm（性能好，节省空间）
- **企业级**: Yarn 2+（功能丰富，插件体系）
- **兼容性**: npm（官方标准，兼容性最好）

使用pnpm

```bash
# 安装pnpm
npm install -g pnpm

# 配置
pnpm config set store-dir ~/.pnpm-store  # 设置存储路径
pnpm config set auto-install-peers true  # 自动安装peer依赖
```

### 3.3 npm全局软件包

软件包的区别：

- 本地软件包：仅供**当前项目**使用，封装了属性和方法，存在于node_modules
- 全局软件包：可供**本机所有项目**使用，封装了命令和工具，存在于系统设置的位置

安装全局软件包：

- 例如，安装nodemon

  ```bash
  npm i nodemon -g     #（-g  全局）
  ```




### 3.4 短选项含义

由于每个命令行工具由不同作者或团队开发，各自定义自己的选项集，所以少数短选项因长期约定，而被广泛接受。

| 短选项 | 常见含义（示例）                           | 示例命令                                                     |
| ------ | ------------------------------------------ | ------------------------------------------------------------ |
| `-h`   | 帮助（help）                               | `pip -h`, `npm -h`, `git -h`                                 |
| `-v`   | 版本（version）或详细输出（verbose）       | `python -v`（verbose），`npm -v`（version），`git -v`（version） |
| `-q`   | 安静模式（quiet），减少输出                | `pip install -q`, `npm install -q`                           |
| `-f`   | 强制（force）                              | `rm -f`, `pip install -f`（但 `-f` 在 pip 中是 `--find-links`，非 force） |
| `-y`   | 对所有提示自动回答“是”（yes）              | `apt-get install -y`, `yum install -y`                       |
| `-g`   | 全局（global）                             | `npm install -g`, `pip` 没有 `-g`（用 `--user`）             |
| `-m`   | 消息（message）或模块（module）            | `git commit -m`, `python -m`                                 |
| `-r`   | 递归（recursive）或需求文件（requirement） | `cp -r`, `pip install -r requirements.txt`                   |
| `-U`   | 升级（upgrade）                            | `pip install -U`, `npm install -g npm@latest -U`（少见）     |
| `-s`   | 静默（silent）或符号链接（symbolic）       | `curl -s`, `ln -s`                                           |

相比而言，长选项在各包管理工具中就表现基本一致，因为GNU 项目制定了详细的命令行接口建议，推荐使用双连字符加描述性单词，并且鼓励常见的选项名（如 `--help`、`--version`、`--verbose`）。



## 4 构建工具

- 在前端编写html、css、js等等这些代码时，不能放心使用模块化规范，即，使用模块化规范浏览器会面临模块过多，需要加载的文件过多。
- 于是迫切需要一款工具对代码进行打包，将多模块打包成一个文件。这样既解决兼容性问题，也解决了模块过多的问题。
- 构建工具就应运而生，它可以将使用ESM规范编写代码转换为旧的JS代码
- 市场上一般使用webpack、vite这两种构建工具

### 4.1 webpack-模块打包器的先驱

官网：[webpack | webpack中文文档 | webpack中文网](https://www.webpackjs.com/)

**核心理念：**

Webpack是一个**静态模块打包器**，它将所有资源（JS、CSS、图片等）视为模块，通过依赖关系构建依赖图，最终打包成浏览器可识别的静态文件。

#### 4.1.1 基本配置

- ` webpack.config.js `

  ```javascript
  module.exports = {
    entry: './src/index.js',      // 入口文件（这里是相对路径）
    output: {                     // 输出配置（即出口，包含打包结果的位置和名称）
      path: path.resolve(__dirname, 'dist'),//位置（这里是绝对路径）
      filename: 'bundle.js'                 //名称
    },
    module: {                     // 模块处理规则(打包js、CSS)
      rules: [                       
        {
          test: /\.js$/,
          use: 'babel-loader'     // 使用loader处理JS
        },
        {
          test: /\.css$/,
          use: ['style-loader', 'css-loader'] // 处理CSS
        }
      ]
    },
    plugins: [                    // 插件：执行更广泛的任务（打包优化、资源管理等）
      new HtmlWebpackPlugin({
        template: './src/index.html'   //自动生成HTML文件
      })
    ],
    mode: 'production'            // 模式：development开发模式/production生产模式
  };
  ```

- > - 以上配置都是最基本配置，如果要完成打包，还需在规则中进行配置（例如lcss、scss、图片等等）
  > - 具体如何配置，参考官网[Loaders | webpack 中文文档 | webpack中文文档 | webpack中文网](https://www.webpackjs.com/loaders/)Loaders内容

#### 4.1.2 搭载开发环境

- 作用：启动Web服务，自动检测代码变化，**热更新**到网页

- 步骤

  1. 下载webpack-dev-server软件包到当前项目

     ```bash
     npm i webpack-dev-server --save-dev
     ```

  2. 设置模式为开发模式，并配置自定义命令

     ```javascript
     module.exports = {
     	mode: 'development'    //设置模式：开发模式
     }
     ```

     ```json
     { //package.json
         "scripts":{
             "dev":"webpack serve --open"   //自定义：自动启动浏览器
         }
     }
     ```

  3. 启动项目，测试热更新效果

     ```bash
     npm run dev
     ```

     > 启动后，自动打开浏览器， webpack-dev-server借助http模块创建8080端口默认Web服务

#### 4.1.3 打包模式

- 打包模式：告知Webpack使用相应模式的内置优化

- 分类：

  |   模式名称   |  模式名字   |               特点               | 使用场景 |
  | :----------: | :---------: | :------------------------------: | :------: |
  | **开发模式** | development | 调试代码，实施加载，模块热替换等 | 本地上线 |
  | **生产模式** | production  |   压缩代码，资源优化，更轻量级   | 打包上线 |


- 设置：

  - 方式1：在webpack.config.js配置文件设置model选项

    ```javascript
    module.exports = {
    	mode: 'development'    //设置模式：开发模式
    }
    ```

  - 方式2：在package.json命令行设置mode参数

    ```json
    { 
        "scripts":{
            "build": "webpack --mode=production",
            "dev":"webpack serve --mode=development"   //自定义：设置为开发模式
        }
    }
    ```

    > 注意：如果同时用两种方法设置，方法2的优先级更高

#### 4.1.4 前端-注入环境变量

环境变量允许在编译时将你代码中的**变量替换为其他值**或表达式。这在需要**根据**开发**模式**与生产模式进行不同的操作时，执行不同的配置。

例，

- 需求：在前端项目中，开发模式下打印语句失效，生产模式下打印语句失效

- 问题：cross-env设置在node.js环境生效，前端代码无法访问process.env.NODE_ENV

- 解决：使用Webpack内置的DefinePlugin插件

  ```js
  //入口文件或其他文件
  if (process.env.NODE_ENV === 'production') {
      console.log = function() {}
  }
  console.log('...')
  ```

  ```javascript
  module.exports = {
   ...
    module: { },                  // 模块处理规则(打包js、CSS)
    plugins: [                    // 插件：执行更广泛的任务（打包优化、资源管理等）
      new Webpack.DefinePlugin({
        ...
        'process.env.NODE_ENV': JSON.stringify(process.env.NODE_ENV),
      })
    ],
    mode: 'production'            // 模式：development开发模式/production生产模式
  };
  ```

#### 4.1.5 修改别名

- 作用：使用import引入路径时，使其更简单更安全

- 语法：

  ```javascript
  module.exports = {
    resolve: {
      alias: {
        '@': path.resqlve(__dirname, 'scr'))
      },
    },
  }
  ```

#### 4.1.6 小结

- 工作流程：

  ```text
              [入口文件] --> [解析模块依赖]--> [构建依赖图] 
                                                  |
                                                  |
                                                  V
         [生成打包文件] <-- [应用插件优化]<-- [使用Loader转换]
  ```


- Webpack的优势：

- 1. "生态丰富": "超过2000个官方和社区loader/plugin",
  2. "高度可配置": "几乎可以处理任何构建需求",
  3. "代码分割": "支持动态import()，实现按需加载",
  4. "长期稳定": "经过多年生产环境验证",
  5. "渐进式迁移": "支持旧项目逐步升级"

- **典型Webpack项目结构**

  ```
  my-webpack-app/
  ├── src/
  │   ├── index.js              # 入口文件
  │   ├── styles/
  │   │   └── main.scss
  │   ├── components/
  │   │   └── App.jsx
  │   └── utils/
  ├── public/
  │   └── index.html
  ├── webpack.config.js         # Webpack配置
  ├── webpack.dev.js           # 开发配置
  ├── webpack.prod.js          # 生产配置
  └── package.json
  ```

- Webpack的痛点：

  1. **冷启动慢**：项目越大，启动时间越长
  2. **热更新慢**：修改文件后，HMR需要重新构建
  3. **配置复杂**：学习曲线陡峭
  4. **开发体验**：随着项目增长而下降

### 4.2 vite-下一代前端构建工具

**核心理念**

Vite（法语意为"快速"）利用**原生ES模块**和现代浏览器特性，提供极速的开发体验。

官网：[开始 | Vite 官方中文文档](https://vitejs.cn/vite3-cn/guide/)

- Vite的工作原理：按需编译
- 传统打包：先打包所有模块，再启动服务器
- Vite：启动服务器，按需编译请求的模块

#### 4.2.1 基本配置

- `vite.config.js` 简洁的配置

  ```ts
  import { defineConfig } from 'vite'
  import vue from '@vitejs/plugin-vue'

  export default defineConfig({
    plugins: [vue()], 
    server: {            //本地开发   
      port: 3000,   //端口
      open: true    //自启动
    },
    build: {            //配置（线上构建）
      rollupOptions: {      //打包
        output: {
          // 分包策略
          manualChunks: {
            'vendor': ['vue', 'vue-router'],  //vue,vue-router打包到vuedor
            'utils': ['lodash', 'axios']      //lodash,axios打包到utils
          }
        }
      }
    }
  })
  ```

- 入口文件（index.html）

  ```javascript
  // 浏览器直接请求ES模块
  <script type="module" src="/src/main.js"></script>

  //使用原生ESM导入
  import { createApp } from 'vue'  // 直接从node_modules导入
  import App from './App.vue'

  createApp(App).mount('#app')
  ```

#### 4.2.2 搭载vite

- 步骤

  1. 创建Vite项目

     ```bash
     npm create vite@latest #my-vue-app -- --template vue  
                           #使用什么框架（vue、react、vanilla(原生JS)）
     ```

  2. 构建产物预览

     ```json
     { //package.json
         "scripts": {
             "dev": "vite",
             "build":"vite build",      //打包命令
             "preview": "vite preview", //自定义：自动启动浏览器 （预览，即还没有打包）
         },
     }
     ```

  3. 启动项目，测试热更新效果

     ```bash
     npm run dev   #首次启动时，将CommonJS模块转换为ESM
     ```

#### 4.2.3 插件化开发

- 插件化微内核思想：vue、react等通过插件的方式，进入vite体系，即最小化核心系统（vite）和一系列插件，构成微内核思想

- 基本使用步骤：

  1. 安装插件库并初始化项目

     ```json
     { //package.json
     	"scripts": {},
     	"dependencies": {
     		"vue": "^3.5.22",
          }
     }
     ```

     ```ts
     //main.ts
     import App from './App.vue'
     import { createApp } from 'vue'
     const app = createApp(App)
     app.mount('#app')
     ```

     ```html
     <body>
         <div id="app"></div>
         <script type="module" src="/src/main.ts"></script>
     </body>       //注意：type="module"是ESM规范化，因为浏览器不认识imoprt/export
     ```

  2. 安装插件

     ```json
     "dependencies": {           //这里以axios和element-plus为例
         "axios": "^1.13.2",
         "element-plus": "^2.11.7",
     }
     ```

  3. 导入插件（vite.config）

     ```ts
     export default defineConfig({
       plugins: [
         vue(),
       ]
     })  
     ```



#### 4.2.4 自定义插件

- 插件本质就是函数

  ```ts
  export default defineConfig({
    plugins: [
      vue(),
      //利用钩子函数
      Components({
        resolvers: [ElementPlusResolver({importStyle: "sass"})],  
      })
    ],
  ```


#### 4.2.5 小结

- **vite优势：**

  1. 闪电般的启动速度


  1. 快速的热更新

     > "基于ESM": "只更新修改的模块，不刷新页面",
     >
     > "精确更新": "CSS更新不刷新组件状态",
     >
     > "即时反馈": "修改后立即看到变化"


  1. 开箱即用的体验

     ```bash
     # 无需复杂配置，立即开始开发
     cd my-vue-app
     npm install
     npm run dev  # 瞬间启动！
     ```


- **Vite项目结构**

  ```
  my-vite-app/
  ├── src/
  │   ├── main.js              # 入口文件（使用ESM）
  │   ├── App.vue              # Vue单文件组件
  │   ├── components/
  │   │   └── HelloWorld.vue
  │   ├── styles/
  │   │   └── main.css
  │   └── assets/
  ├── index.html              # 入口HTML（直接引用main.js）
  ├── vite.config.js          # Vite配置（可选）
  ├── package.json
  └── public/
  ```

### 4.3 Vite vs Webpack 详细对比

| 特性           | Webpack                | Vite               |
| -------------- | ---------------------- | ------------------ |
| **启动速度**   | 慢（随项目增大而变慢） | 极快（毫秒级）     |
| **HMR速度**    | 较慢（需要重新构建）   | 极快（按需更新）   |
| **配置复杂度** | 高（需要大量配置）     | 低（开箱即用）     |
| **构建原理**   | 打包所有资源           | 按需编译 + 原生ESM |
| **生产构建**   | 自带优化               | 基于Rollup         |
| **生态**       | 极其丰富               | 快速增长           |
| **学习曲线**   | 陡峭                   | 平缓               |
| **适用场景**   | 大型复杂项目           | 现代前端项目       |