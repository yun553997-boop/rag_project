# AJAX

官网：[https://axios-http.com/zh/docs/intro](https://axios-http.com/zh/docs/intro)

AJAX是异步的JavaScript和XML,实现客户端与服务器的通信

**核心思想**：在不需要重新加载整个网页的情况下，能够与服务器交换数据并更新部分网页内容。

**工作原理**：

```
ECMAScript (创建请求) 
    ↓
BOM (XMLHttpRequest/Fetch API 发送请求)
    ↓
服务器处理请求并返回数据
    ↓
ECMAScript (处理响应数据)
    ↓
DOM (用数据更新页面内容)
```

## 1 前置知识

### 1.1 URL

- **概念**：统一资源定位器，简称网址，用于访问服务器里的资源

- **结构**：

  url: "`http`:// `hmajax.itheime.net`:`80` `/api/province`"

  ​           协议                   域名                端口号       资源路径

  - 常见协议：`http`、`https`、`ftp`、`mailto`、`file` 等
  - 域名：资源所在服务器的域名或 IP 地址。示例：`www.example.com`
  - 资源路径一般还包括：`协议://主机名:端口号/路径?查询参数#片段标识`

- **端口号**：

  - 作用：通过不同的端口号区分服务器上不同的服务（因为一台服务器可以提供多种服务）

  - 默认端口号：

    | 端口号    | 服务/协议 | 说明               |
    | --------- | --------- | ------------------ |
    | **80**    | HTTP      | Web 服务的标准端口 |
    | **443**   | HTTPS     | 安全 Web 服务端口  |
    | **21**    | FTP       | 文件传输协议       |
    | **22**    | SSH       | 安全 shell 连接    |
    | **25**    | SMTP      | 邮件发送           |
    | **53**    | DNS       | 域名解析           |
    | **3306**  | MySQL     | 数据库服务         |
    | **27017** | MongoDB   | NoSQL 数据库       |



## 1 axios

### 1.1 axios的基本使用

1. 安装axios

   ```bash
   npm install axios
   ```


2. axios方法的基本语法

   ```javascript
   axios({
       url: "http://hmajax.itheime.net/api/province",
       //指定请求方法
       method: 'post',        
       //提交数据（data）
       data: {
           username: '杜王',
           possword: '12345'
       }    
   }).then(result => {
       console.log('成功访问到网址')
   }).chtch(error => {
       console.log('出错了')
       })
   })
   ```

​       **注意：**若请求方法是get，method：'get'这行可以省略

3. 常见的请求方式

   > 1. GET 请求：用于获取数据
   > 2. POST 请求：用于提交数据
   > 3. PUT 请求：用于更新整个资源
   > 4. PATCH 请求：用于部分更新资源
   > 5. DELETE 请求：用于删除资源

### 1.2 请求方式别名

为了方便起见，已经为所有支持的请求方法提供了别名。

> axios.request(config)
>
> axios.get(url[, config])
>
> axios.delete(url[, config])
>
> axios.head(url[, config])
>
> axios.post(url[, data[, config]])
>
> ......
>

在使用别名方法时， `url`、`method`、`data` 这些属性都不必在配置中指定。

```javascript
axios.post(
    'http://localhost:3000/comments', 
    {
        "参数1": "喜大普奔",
        "参数2": 2
    }
).then(response => {
    console.log(response);
})
```

### 1.3 axios实例

作用：用于封装api（因为通常只有一个基地址）

语法：`axios.create([config])`

1. 封装

   ```javascript
   const httpInstance = axios.create({
     // 设置所有请求的基础路径
     baseURL: 'https://api.myapp.com/api/v1',
     // 请求超时时间（单位：毫秒）
     timeout: 5000, 
     //请求头配置
     headers: {...}
     //拦截器
     ...
     
      export default httpInstance
   });
   ```

2. 简单调用

   例如`httpInstance.get()` 、 `httpInstance.post()` ...

   ```js
   // 实际请求的URL会是：https://api.myapp.com/api/v1/users
   httpInstance.get('/users')
   // 如果请求完整URL，会忽略baseURL，不会使用baseURL
   httpInstance.get('https://other-api.com/data');
   ```

   当然，axios的请求也是promise对象，后面可以跟 catch 、then等等

   ```javascript
   httpInstance.get('/users')
     .then(response => {
       console.log('成功获取数据');
     })
     .catch(error => {
       if (axios.isCancel(error)) {
         console.log('请求被取消');
       } else if (error.code === 'ECONNABORTED') {
         console.log('请求超时，请检查网络或稍后重试');
       } else {
         console.log('其他错误:', error.message);
       }
     });
   ```

3. 实战调用

   注意：`async...await axios`axios在后边

   ```javascript
   const getSubCategoryAPI = (data) => {
     return httpInstance({
       url:'/category/goods/temporary',
       method:'POST',
       data
     })
   }

   const getGoodList = async() => {
     const res = await getSubCategoryAPI(reqDate.value)
     goodList.value = res.result.items
   }
   onMounted(() => getGoodList())
   ```

### 1.4 传参方法

1. URL 参数（适用于 GET 请求）

   ```javascript
   // 方法1：直接在 URL 中传递
   axios.get('/api/users?page=1&limit=10');

   // 方法2：使用 params 对象
   axios.get('/api/users', {
     params: {
       page: 1,
       limit: 10,
       search: 'john'
     }
   });

   // 方法3：使用 URLSearchParams
   const params = new URLSearchParams({
     page: 1,
     limit: 10
   });
   axios.get(`/api/users?${params}`);
   ```

2. 请求体参数（适用于 POST、PUT、PATCH）

   ```javascript
   // 传递 JSON 数据（默认）
   axios.post('/api/users', {   //也就是我们前面所说的取别名
     name: 'John',
     age: 30,
     hobbies: ['reading', 'coding']
   });

   // 传递表单数据
   const formData = new FormData();
   formData.append('name', 'John');
   formData.append('avatar', fileInput.files[0]);

   axios.post('/api/users', formData, {
     headers: {
       'Content-Type': 'multipart/form-data'
     }
   });

   // 传递 URL 编码数据
   const urlEncodedData = new URLSearchParams();
   urlEncodedData.append('name', 'John');
   urlEncodedData.append('age', '30');

   axios.post('/api/users', urlEncodedData, {
     headers: {
       'Content-Type': 'application/x-www-form-urlencoded'
     }
   });
   ```

### 1.5 axios默认配置

您可以指定默认配置，它将作用于每个请求。

通过创建实例配置默认值，在创建后进行修改：

1. 创建实例时配置默认值

   ```javascript
   const duanzi = axios.create({
       baseURL: 'https://api.apiopen.top',   //地址是某个接口地址
       timeout: 2000
   });
   ```

2. 创建实例后修改默认值

   ```javascript
   axios.defaults.method = 'GET';                    //设置默认的请求类型为 GET
   axios.defaults.baseURL = 'http://localhost:3000'; //设置基础 URL
   axios.defaults.params = {id:100};
   axios.defaults.timeout = 3000;                    //修改请求等待时间
   ```

### 1.6 拦截器

在请求或响应被 then 或 catch 处理前拦截它们。

```javascript
// 设置请求拦截器  config 配置对象
axios.interceptors.request.use(function (config) {
    // 在发送请求之前做些什么
    console.log('请求拦截器 成功 - 1号');
    config.params = {a:100}; //修改 config 中的参数

    return config;
}, function (error) {
    // 对请求错误做些什么
    console.log('请求拦截器 失败 - 1号');
    return Promise.reject(error);
});


// 设置响应拦截器
axios.interceptors.response.use(function (response) {
    // 2xx 范围内的状态码都会触发该函数。
    // 对响应数据做点什么
    console.log('响应拦截器 成功 1号');
    return response.data;
}, function (error) {
    // 超出 2xx 范围的状态码都会触发该函数。
    // 对响应错误做点什么
    console.log('响应拦截器 失败 1号')
    return Promise.reject(error);
});



//发送请求
axios({
    method: 'GET',
    url: 'http://localhost:3000/posts'
}).then(response => {
    console.log('自定义回调处理成功的结果');
    console.log(response);
});
```

移除拦截器

```
const myInterceptor = axios.interceptors.request.use(function () {/*...*/});
axios.interceptors.request.eject(myInterceptor);
```

### 1.7 取消请求

```javascript
//发送请求
btns[0].onclick = function(){
    //检测上一次的请求是否已经完成
    if(cancel !== null){
        //取消上一次的请求
        cancel();
    }
    axios({
        method: 'GET',
        url: 'http://localhost:3000/posts',
        //1. 添加配置对象的属性
        cancelToken: new axios.CancelToken(function(c){
            //3. 将 c 的值赋值给 cancel
            cancel = c;
        })
    }).then(response => {
        console.log(response);
        //将 cancel 的值初始化
        cancel = null;
    })
}
//绑定第二个事件取消请求
btns[1].onclick = function(){
    cancel();
}
```



## 2 HTTP协议---请求报文、响应报文

- **请求报文**由：

  请求行、请求头、空行、请求体组成。在网页面板中查看

- **响应报文**结构也由这4部分组成：

  响应行（协议、响应状态码、状态信息）、请求头、空行、请求体（返回的资源）

- HTTP响应码：

  一般来说由1开头表示信息，由2开头表示成功，由3开头表示重定向消息，由4开头表示客户端错误，由5开头表示服务端错误

  | *状态码* |        *含义*         |                       *说明*                        |
  | :------: | :-------------------: | :-------------------------------------------------: |
  |   200    |          OK           |                      请求成功                       |
  |   201    |        CREATED        |                      创建成功                       |
  |   204    |        DELETED        |                      删除成功                       |
  |   400    |      BAD REQUEST      |        请求的地址不存在或者包含不支持的参数         |
  |   401    |     UNAUTHORIZED      |                       未授权                        |
  |   403    |       FORBIDDEN       |                     被禁止访问                      |
  |   404    |       NOT FOUND       |                  请求的资源不存在                   |
  |   422    |  Unprocesable entity  | [POST/PUT/PATCH] 当创建一个对象时，发生一个验证错误 |
  |   500    | INTERNAL SERVER ERROR |                 内部（服务端）错误                  |
  |          |                       |                                                     |


- 接口文档：用来描述接口的文章（一般是由后端写）






## 3 XMLHttpRequest

- axios内部采用XMLHttpRequest与服务器进行交互

- XMLHttpRequest在一些简单请求中被使用，比如一些静态页面


### 3.1 XMLHttpRequest基本使用

```javascript
// 创建XHR对象
const xhr = new XMLHttpRequest();

// 配置请求
xhr.open('GET', 'https://api.example.com/data', true);

// 处理响应
xhr.onload = function() {
    if (xhr.status === 200) {
        console.log(xhr.responseText);  //response接受响应结果
    }
};

// 发送请求
xhr.send();
```

response接受响应结果，但会以JSON字符串返回，所以进行转回：`JSON.parse(xhr.response)`

#### 3.1.1 查询参数

在地址后面查询

```
xhr.open('GET', 'https://api.example.com/data?data=四川省')
```



#### 3.1.2  数据提交

在axios中提交数据直接写在data后面

```javascript
// 创建XHR对象
const xhr = new XMLHttpRequest();

// 配置请求
xhr.open('GET', 'https://api.example.com/data');
xhr.addEventListener('loadend', () => {
    consloe.log(xhr.response)
})

// 设置请求头（告诉服务器我传递的内容数据类型是JSON字符串）
xhr.setRequesHeader('Content-Type', 'application/json')
//准备数据并转成字符串
const user = { username: '杜王', password: '5432121'}
const userStr = JSON.stringify(user)

// 发送请求体数据
xhr.send(userStr);
```

