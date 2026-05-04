python

[简介 - Python教程 - 廖雪峰的官方网站](https://liaoxuefeng.com/books/python/introduction/index.html)

### python命令行参数

| 选项   | 描述                                                   |
| ------ | ------------------------------------------------------ |
| -d     | 在解析时显示调试信息                                   |
| -O     | 生成优化代码 ( .pyo 文件 )                             |
| -S     | 启动时不引入查找Python路径的位置                       |
| -V     | 输出Python版本号                                       |
| -X     | 从 1.6版本之后基于内建的异常（仅仅用于字符串）已过时。 |
| -c cmd | 执行 Python 脚本，并将运行结果作为 cmd 字符串。        |
| file   | 在给定的python文件执行python脚本。                     |

### 数据类型

Python有五个标准的数据类型：

- Numbers（数字）
- String（字符串）
- List（列表）
- Tuple（元组）
- Dictionary（字典）

### Python算术运算符

以下假设变量： **a=10，b=20**：

| 运算符 | 描述                                                | 实例                                               |
| ------ | --------------------------------------------------- | -------------------------------------------------- |
| +      | 加 - 两个对象相加                                   | a + b 输出结果 30                                  |
| -      | 减 - 得到负数或是一个数减去另一个数                 | a - b 输出结果 -10                                 |
| *      | 乘 - 两个数相乘或是返回一个被**重复**若干次的字符串 | a * b 输出结果 200                                 |
| /      | 除 - x除以y                                         | b / a 输出结果 2                                   |
| %      | 取模 - 返回除法的余数                               | b % a 输出结果 0                                   |
| **     | 幂 - 返回x的y次幂                                   | a**b 为10的20次方， 输出结果 100000000000000000000 |
| //     | 取整除 - 返回商的整数部分（**向下取整**）           | 9//2 = 4                                           |

###匿名函数

python 使用 lambda 来创建匿名函数。lambda函数只能写一行。

lambda函数只包含一个语句，如下：

```python
lambda [arg1 [,arg2,.....argn]]:expression
sum = lambda arg1, arg2: arg1 + arg2
# 调用sum函数
sum( 10, 20 )  #30
```

### python模块

- **import语句** 

  ```python
  import statistics  #模块名                                              
  print(statistics.madian([19,12,-12])
  ```

  也可以通过重命名：

  ```python
  import statisics as st
  st.madian[19,12,-12]
  ```

- **from...import...语句** 

  ```python
  #指定模块的哪个函数
  from statistics import madian,mean             print(meadian([19,12,-12]))     #可以同时引入多个模块，且后面不需要再加模块名               
  ```

- **from...import***

  ```python
  #指定模块的所有函数
  from statistics import*
  print(meadian([19,12,-12]))
  ```

  > 注意：`from a import*` ` from b import*`a,b内可能有相同的两个函数。因此一般采用第二种

​     

#  IO编程 

## 打开和关闭文件

- 读文件

  打开一个文件对象，使用Python内置的`open()`函数，传入文件名和标示符：

  ```python
  f = open("文件名" "标识符")
  f = open('/Users/michael/test.txt', 'r')
  ```

  | 模式 | 描述                                             |
  | :--: | ------------------------------------------------ |
  |  t   | 文本模式 (默认)。                                |
  |  x   | 写模式，新建一个文件，如果该文件已存在则会报错。 |
  |  +   | 打开一个文件进行更新(可读可写)。                 |
  | r/rb | 只读方式打开(文本)文件/（二进制）文件，如图片    |
  | w/wb | 打开一个文件写（文本）文件/（二进制）文件        |

  读取文件内容

  ```python
  f.read()  #read()方法可以一次读取文件的全部内容
  ```

  关闭文件

  ```python
  f.close()
  ```

  ​


- 写文件

  写文件和读文件是一样的，唯一区别是调用`open()`函数时，传入标识符`'w'`或者`'wb'`表示写文本文件或写二进制文件

  ```python
  f = open('/Users/michael/test.txt', 'w')
  f.write('Hello, world!')  #写入的内容
  f.close()
  ```

  频繁的打开和关闭太繁琐，可以使用with语句来自动调用close()方法

  ```python
  with open('/Users/michael/test.txt', 'r') as f:  #读文件
      print(f.read())

  with open('/Users/michael/test.txt', 'w') as f:   #写文件 w文本文件 wb二进制文件
      f.write("内容")
  ```

## 操作文件和目录

操作文件、目录，可以在命令行输入操作系统提供的各种命令来完成。比如`dir`、`cp`等命令，Python内置的os模块也可以直接调用操作系统提供的接口函数

```python
import os
os.name # 操作系统类型 
```

> 如果输出的是`posix`，说明系统是`Linux`、`Unix`或`macOS`，如果是`nt`，就是`Windows`系统。
>
> 因此，不同操作系统函数可能有不同

### 环境变量

Python 标准库的 `os` 模块提供了对环境变量的字典式访问

- 读取环境变量

  在操作系统中定义的环境变量，全部保存在`os.environ`这个变量中，可以直接查看：

  ```python
  os.environ
  ```

  > environ({'VERSIONER_PYTHON_PREFER_32_BIT': 'no', 'TERM_PROGRAM_VERSION': '326', 'LOGNAME': 'michael', 'USER': 'michael', 'PATH': '/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/mysql/bin', ...})

  获取某个环境变量的值

  ```python
  os.environ.get('PATH',"默认值")        #默认值（非必须），不存在返回默认值，没有返回None
  ```

  > `os.getenv()` 是 `os.environ.get()` 的一个别名，用法完全相同

- 从`.env`文件加载

  通常将敏感信息（如 API 密钥）写在项目根目录的 `.env` 文件中，并使用 `python-dotenv` 库自动加载到 `os.environ`

  1. 安装

     ```bash
     pip install python-dotenv
     ```

  2. 创建`.env`文件

     ```.env
     DASHSCOPE_API_KEY="sk-xxxxxxxxxxxx"
     OPENAI_API_KEY="sk-yyyyyyyyyyyy"
     DATABASE_URL="postgresql://user:pass@localhost/db"
     ```

  3. 加载

     ```python
     from dotenv import load_dotenv
     import os

     # 加载 .env 文件中的变量到系统环境变量
     load_dotenv()  # 默认查找当前目录下的 .env 文件（当然也可以在括号里指定路径）

     # 之后即可正常读取
     api_key = os.environ.get("DASHSCOPE_API_KEY")
     print(api_key)
     ```

     ​

### 操作文件和目录

#### 增、删、改、查

1. 查看当前目录路径

   ```python
   os.path.abspath('.')
   ```

   > '/Users/michael'

2. 创建一个新目录（在已有目录下，创建子目录）

   ```python
   os.path.join('/Users/michael', 'testdir')
   ```

   > '/Users/michael/testdir'

3. 创建一个新目录

   ```python
   os.mkdir('/Users/michael/testdir')
   ```

4. 删除一个目录

   ```python
   os.rmdir('/Users/michael/testdir')
   ```

#### 拼接/拆分路径

这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

```python
#拼接
os.path.join('/Users/michael', 'testdir')
#拆分
os.path.split('/Users/michael/testdir/file.txt') 
```

> 路径拆分为两部分，后一部分总是最后级别的目录或文件名：
>
> ('/Users/michael/testdir', 'file.txt')

`os.path.splitext()`直接得到文件扩展名：

```python
os.path.splitext('/path/to/file.txt')
```

> ('/path/to/file', '.txt')

#### os.walk()

通过在目录树中游走输出在目录中的文件名，向上或者向下

- 语法：

  ```python
  os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
  ```

  > 参数：
  >
  > - top：遍历的目录的地址，返回一个三元组（root,dirs,files）
  >   - root 所指的是当前正在遍历的这个文件夹的本身的地址
  >   - dirs是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
  >   - files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
  > - 其他：[Python os.walk() 方法 | 菜鸟教程](https://www.runoob.com/python/os-walk.html)

  ```python
  for root, _, files in os.walk(directory):
  ```

  ​

- ​


### 序列化

变量从内存中变成可存储或传输的过程称之为序列化

在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如JSON

- python转JSON（序列化）

  ```python
  import json
  d = dict(name='Bob', age=20, score=88)
  json.dumps(d)
  ```

  > '{"age": 20, "score": 88, "name": "Bob"}'

- JSON转python（反序列化）

  ```python
  json_str = '{"age": 20, "score": 88, "name": "Bob"}'
  json.loads(json_str)
  ```

  > {'age': 20, 'score': 88, 'name': 'Bob'}

# 面向对象编程

## 类和实例

类是一种**代码组织方式**，它允许我们把**数据**和**操作这些数据的方法**打包在一起。

以下的Dog就是一个类，每一个方法、数据定义就是一个这个Dog实例

- 创建类：

  ```python
  class Dog:
      pass   
  ```

- 创建实例：

  ```python
  my_dog = Dog()   # my_dog 是 Dog 类的一个实例
  ```


- 属性：存储数据

  使用 `__init__` 方法初始化属性

  ```python
  class Dog:
      def __init__(self, name, age):
          self.name = name   # self 指向当前实例
          self.age = age

  my_dog = Dog("旺财", 3)
  print(my_dog.name)   # 旺财
  print(my_dog.age)    # 3
  ```


- 方法：定义行为

  ```python
  class Dog:
      def __init__(self, name, age):
          self.name = name
          self.age = age

      def bark(self):
          print(f"{self.name} 汪汪叫！")

      def get_human_age(self):
          # 假设狗年龄乘以7得到人类年龄
          return self.age * 7

  my_dog = Dog("旺财", 3)
  my_dog.bark()                # 输出：旺财 汪汪叫！
  human_age = my_dog.get_human_age()
  print(human_age)             # 输出：21
  ```

  > 方法的第一个参数必须是 `self`


- 类变量 vs 实例变量

  - **实例变量**：属于每个实例自己，不同实例的值可以不同（如 `name`、`age`）。
  - **类变量**：属于类本身，所有实例共享同一个值。

  ```python
  class Dog:
      species = "Canis familiaris"   # 类变量

      def __init__(self, name, age):
          self.name = name            # 实例变量
          self.age = age

  dog1 = Dog("旺财", 3)
  dog2 = Dog("小黑", 4)

  print(dog1.species)   # Canis familiaris
  print(dog2.species)   # Canis familiaris

  # 修改类变量会影响所有实例
  Dog.species = "犬科"
  print(dog1.species)   # 犬科
  ```

  ​



