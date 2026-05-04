# JavaScript 知识体系

 JavaScript 知识体系由三大部分组成：

1. **ECMAScript（核心语法与语言基础）** - 这是房子的**地基和框架**。它规定了语言的基本语法、类型、语句、关键字、操作符、对象等。
2. **DOM（文档对象模型）** - 这是房子的**内部装修和交互界面**。它提供了与网页内容（HTML）交互的方法和接口，让你可以动态地修改页面结构、样式和内容。
3. **BOM（浏览器对象模型）** - 这是房子的**外部环境和设施**。它提供了与浏览器窗口交互的方法和接口，比如控制浏览器导航、操作历史记录、获取屏幕信息等。

预制模板（网站搜索）:swiper

## 1、 ECMAScript（语言核心）

这是 JavaScript 的“语言本身”，与任何宿主环境（如浏览器、Node.js）无关。它定义了以下核心概念：

- **语法基础**：变量声明（`var`, `let`, `const`）、数据类型（Number, String, Boolean, Null, Undefined, Symbol, BigInt）、操作符（`+`, `-`, `*`, `/`, `===`, `...`）、流程控制（`if...else`, `for`, `while`）。
- **函数**：函数定义与调用、参数、作用域、闭包。
- **对象**：对象字面量、属性、方法。
- **数组**：数组方法（`push`, `pop`, `map`, `filter`, `reduce`）。
- **原型与面向对象**：构造函数、原型链、ES6 的 `class` 语法。
- **异步编程**：回调函数、Promise、`async/await`。

### 1.1 语法基础

#### 1.1.1 变量声明

声明的这个变量可以更新；但声明的同一个变量只能被声明一次

可以同时声明多个变量（用逗号隔开）

```
let uname='pink',name='杜王'
```

`var`, `let`, `const`使用区别：

​	 const优先，且变量值（基本数据类型）不变；let变量值可以变；var老派（淘汰）

​	 因为const存放的是地址（放在栈内,不会因为值改变而改变），而值放在堆内。因此数组、对象优先用const		

​	声明（可以改变内容），简单数据类型优先用let声明

变量名不能用关键字，只能用下划线、字母（区分大小写）、数字、$组成，且数字不能打头。

**全局变量**：不加`var`, `let`, `const`直接声明一个变量

**声明常量**：常量名一般大写，但也可小写

```HTML
const PI = 3.14       // 必须进行赋值，但不能更改
```

#### 1.1.2  数据类型

数据类型：

1. string（字符串）：
   - 表示文本数据，可以使用单引号(' ')、双引号(" ")或反引号(``)括起来。
   - 例如：'hello'、"world"、`template string`。
2. number（数字）：
   - 表示整数或浮点数，还包括一些特殊值如Infinity、-Infinity和NaN（Not a Number）。
   - 例如：42、3.14、NaN、Infinity。
3. boolean（布尔值）：
   - 表示逻辑值，只有两个值：true和false。
   - 常用于条件判断。
4. null（空值）：
   - 表示一个空值或不存在的对象。
   - 注意：typeof null 返回的是"object"，这是历史遗留问题。
5. undefined（未定义）：
   - 表示变量已声明但未赋值时的默认值，或者函数没有返回值时默认返回undefined。
   - 例如：let a; 则a的值为undefined。
6. bigint（大整数）：
   - 用于表示任意精度的整数，通过在整数后面加n来创建。
   - 例如：1234567890123456789012345678901234567890n。
7. symbol（符号）：
   - ES6的新原始数据，JavaScript的第7种数据类型（类似于字符串），值是唯一的、不可变的；不能与其他数据进行运算；不能使用for循环遍历，通常用于对象属性的键，以避免属性名冲突。
   - 创建Symbol（两种）：let a = Symbol('内容') 或者 let b = Symbol.for('内容')
   - 例如：let sym = Symbol('description');
8. object（对象）：
   - 用于存储多个值作为属性和方法的集合。对象的值可以是任意数据类型。
   - 例如：{ name: 'John', age: 30 }。
   - 数组、函数、日期等都属于对象类型，但它们是对象的特殊形式。
   - 注意：函数（function）是对象的一种，但它除了有对象的特性外，还可以被调用。数组（array）也是对象，具有数字索引和length属性。

查询数据类型：typeof()

**类型转换**：JavaScript是弱数据类型，使用表单、portal获取的数据默认为字符串

```javascript
// 隐式转换
console.log(1 + 1)      //数字型
console.log('pink' + 1) //字符串型
console.log(+'123')   //数字型
console.log(11 - '11') 
// 显示转换
let str = '123'
console.log(Number(str))     //转换数字型
console.log(parseInt('12.1px'))//转换为整数，其他自动忽略
console.log(parseFloat('12.1px'))//转换为浮点数，其他自动忽略
```

#### 1.1.3 操作符

- 赋值运算符： **+=**（num=num+1）  **-=    *=    /=    %=**意思相同

-  一元运算符： **++**（num+=1）自增；**--**（num-=1）自减    **！**（非）

- 比较运算符：  **>  <  >=  <=  ==**（值相等）  **===**  (值和数据类型都相等)

- 逻辑运算符： **&&**（且） **||**（或）  **！**（非）

- **三元运算符**（条件？代码1：代码2）：console.log(3>5?3:5)            

  1. 条件正确执行代码1，反之执行代码2
  2. 三元语句一定会返回一个值

- **优先级**： () > 一元 > 算术运算符 >比较运算符 > 相等 > 逻辑运算符（先&&再||）

- **逻辑中断**：

  ```javascript
  //若&&两边都为真，则执行后者
  console.log(11&&22) 
  //若&&两边有一个假，则都不执行
  console.log(false&&22) 
  //若||其中一个为真，则就执行前者
  console.log(false||22) 
  //若||两边都为假，则执行后者
  console.log(null||0) 
  ```

  > 字符串中' '为false;数字中1为false;undefined为false;null为false;NeN为false   其余都为true

#### 1.1.4 流程控制

`if...else`：if(条件) { 

​			}else if(条件) {

​             		}else if(条件) {

​       			 }else { }     // 以上都不成立 

`switch`:    用于筛选需要**全等**的值，而非区间;当**分支较多**时用switch;分支较少时用if~else

```javascript
switch (month){     //执行小括号内与case的值全等（字符串、数字、null等）的语句，一般不用区间
    case 3||4||5:
        alert('春天')
        break  //退出switch；若是不加，他会在满足条件的case继续执行之后不满足的（穿透）
    case 6||7||8:
        alert('夏天')
        break  //退出switch
    case 9||10||11:
        alert('秋天')
        break  //退出switch
    case 1||2||12:
        alert('冬天')
        break  //退出switch
    default:
        alert('月份有误')
        break  //这里可加可不加，因为往下没有内容，漏不了
}
```

 `for`：遍历：for (let i in arr){ }         **注意**：*这里的 i是索引号*

​	     循环 ：for( let i =1;i<=3;i++){ }     **语法**：for(起始值；终止条件；变量变化量) {循环干什么}

 `while` 满足条件就循环，所以循环体内一定要写终止条件

```javascript
let num=1,sum=0
while (num<=100) {
    sum+=num
    num++
}
```

### 1.2 函数

函数，可以将一些代码进行抽取，达到复用的效果

#### 1.2.1 自定义函数

- **声明函数**：声明函数 函数名（参数）{函数内容}      function fn(shuzi) {}

- **参数**可有可无，也可有多个（**用逗号隔开**），声明函数是可以赋值（函数调用若不设参数,则作为默认值）

- **调用函数**：函数名（参数）；可以多次调用，每次调用都重新运行    

- 返回值（return）；pop()也可以返回值（当前数组长度）

- return后面代码不会被执行（*注意：不能换行*），立即结束当前函数；若没有返回值默认为undefined


#### 1.2.2 匿名函数

没有函数名    function(){}

匿名函数只能在函数声明之后用（具名函数可以先调用再声明）

匿名函数立即执行(写在前面，优先执行,且两两之间用分号隔开)

避免全局变量之间污染,也可命名函数:

```javascript
(function(x,y){console.log(x+y)})(2,3);
(function(x,y){console.log(x+y)}(2,3));//两种写法
```

#### 1.2.3 内置函数

JavaScript内部提供对象，包含各种属性和方法供调用 ，可以使用mdn网页查询各种内置对象 

Math(数学内置对象)：

Math.**PI**  //pi；Math.**ceil**(1.011) //向上取整（负数也是取大值）；Math.**floor**(-1.1) //向下取整（负数取小值）；Math.**round**(1.1)  //四舍五入（正数大于等于5取，负数大于5取）当然还有 **max；min；abs**（绝对值）；**pow**(4,2)（4的2次方）；**randonm() 随机数**（默认取[0,1)的随机数）

#### 1.2.4 参数   

1、动态参数:arguments（是一个伪数组，只存在于函数中）。用于不知传多少个参数，动态参数不存在于箭头函数中 。

2、剩余参数：...（是一个真数组）。用于获取多余的参数  

两者区别：

​        剩余参数可以传已知参数 + 未知参数。function fn(a,b,c,...arr) {}   console.log(arr)使用时不加...

​        另外注意，arr...也可以是数组展开符（arr = [1,2,3]  ...arr就能将括号展开

应用：Math.man(...arr)可以求该数组最大值（该函数不能直接求数组的）、合并数组（arr=[arr1,arr2]）

```javascript
//动态参数应用
function getSum() {    //这里不写形参
    let sum = 0
    for (let i=0; i<arguments.length; i++) {   //注意：这里是arguments的长度，而不是getSum的长度
        sum += arguments[i]
    }
    console.log(sum)
}
//getSum(2,1,3,……)   调用时随意写多少个参数
```

#### 1.2.5 闭包

闭包 = 内层函数 + 外层函数变量

作用：使外部可以访问函数内部的变量，同时实现数据私有（不会被改变，也不会被回收）

```javascript
//没有闭包
let i = 0
function fn() {
    i++
    console.log(`函数调用了${i}次`)
}
fn()       
```

这里，i作为一个全局变量，容易被篡改
改为闭包：

```javascript
function count() {
    let i = 0
    function fn() {
        i++
        console.log(`函数调用了${i}次`)
    }
    return fn    //关键步骤
}
count()
```

原理：利用垃圾回收机制（局部变量在不用时会被立即回收，全局变量不会）；闭包使局部变量不会被回收（即，内存泄漏）

#### 1.2.6 箭头函数

作用：用于代替部分匿名函数

function () {} 等同于() => {}  

当只有一个形参时，可以省略小括号；函数体只有一行代码时，可以省略大括号，且如果有return，也可以省略

**注意**：箭头函数可以返回一个对象(因为大括号冲突，用小括号)    即   (uname) => ({ name: uname})

​	    箭头函数this  指向上一层作用域的this的指向(因为箭头函数没有this)

### 1.3 数组

在JavaScript 中的数组，数据类型和长度都没有限制。

**1、声明**：

​	字面量声明： let arr = ['李白', '杜甫', 11]； 

​	使用new Array声明数组： let b = new Array(1,2,3,9)

**2、增加**：

​	增(**更新**)：对应索引值有值就更新；无值则增加                        arr[2] = '杜王'

​	**向后增加**(追加在最后,可以是多个，并返回新数组长度)            arr.push('deeppink','red')

​	**向前增加**（在前面加，可以是多个，并返回新数组长度）        arr.unshift('张良','韩信')

**3、删除:**

​	删除最后一项(只能删除一项)                                                        arr.pop()

​	删除第一项（只能删除一项）                                                      arr.shift()

​        删除指定元素（起始位置(索引)，删除几个元素（默认删除到最后））      arr.splice(0,1)

#### 1.3.1 数组解构

数组解构：将数组单元值批量赋值

应用：

```
1、快速赋值：const arr = [a,b,c] = [1,2,3]

2、交换变量：let a = 1

	        let b = 2;       //注意：要加分号

            [b,a] = [a,b] 
3、多维数组的解构：const arr = [1,2,[3,4]]得到3：

				const [a,b,[c,d]] = [1,2,[3,4]]  console.log(c)   //传统方法：   arr[2][0]
```

**注意：**加分号的情况：

​        1、立即执行的函数: (function() {})();

​        2、使用数组的时候（以数组开头语句），否则会与上一句自动连接（加在上句末或这句前都可以），所以若			没有上一句，也可以不加

#### 1.3.2 数组方法

数组方法在mdn网站中查找[Array.prototype.find() - JavaScript | MDN](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/find)

1. **map**方法：

​        数组1.map(function(item,index) {}) ,其中，item表示数组1的元素（遍历）；index表示该元素的索引号

​        map方法是一种映射方法，会返回一个数组（forEach只遍历，不返回） 

2. **forEach**类似于一个加强版的for，主要遍历数组 

​        数组.forEach(function(当前数组元素，当前数组索引号)｛｝) 　当前元素必须写，索引号可以不写

3. **join()**方法：

​        数组2.Join()  ,括号内用什么隔开，字符串之间就用什么隔开（若为''则不隔开）

​        用于将数组中所有元素**转换为一个字符串** 

4. **reduce**:

   返回累计处理的结果，用于**数组求和**

   ```javascript
   const arr = [1,2,3]
   		//数组1.reduce(function(上次值, 当前值){}, 始值)      当然也可以没有初始值（少遍历一遍）
   const total = arr.reduce((prev,current) => prev + current, 10)    
   	    //这里的当前值就是数组中要求和的值（例如数组中有对象：current => current.属性）
   ```

5. **find:**

​        用于**数组查找**（返回数组中满足提供的测试函数的 第一个 元素的值，否则返回undefined）

​        find(callbackFn, thisArg)           

### 1.4 对象

对象：javascript中的数据类型(一共五种数据类型)：无序数据类型（数组有序）

对象声明：**let a = null**   //相当于let a = {}

遍历对象：   for (let k in odj) {}  其中k是属性名（但，都是**字符串型**）

**访问**属性：

​	静态属性：对象名.属性名

​	动态属性：对象名.['属性名']

**增、改**属性：

​        对象名.属性名=属性

 **删除**属性：

​        delete 对象名.属性名

#### 1.4.1 对象解构

语法：const {a,b,c} = {a:'1',b:'2',c:3}                  **注意**：*变量名必须与属性名一样，否则该变量的值就为undefined*

 解构的变量名可以改名：

​        const {a,b,c:d} = {a:'1',b:'2',c:3}    //注意：新名在后

多级对象解构：

1. ```HTML
   const {name,family:{mother,father,sister}} = {name = '佩奇',
                                                     family:{
                                                       mother:'猪妈妈',
                 //注意：上面有个family:                father:'猪爸爸',
                                                       sister:'乔治'}
                                                     } 
   应用:
   	 只拿到family: const { famliy } = arr（这个对象名）   
        将family当作参数传给函数： function fn({ famliy }) {}  
        为防止命名混淆，需将famliy改为myFamliy: function fn({ famliy：myFamliy }) {} 
   ```



### 1.5 原型与面向对象

#### 1.5.1 构造函数

目的：利用构造函数**创建对象**（创建一个对象壳子，可以进行多次赋值）

语法：

```javascript
function Goods(name,price,count) {    //构造函数名的首字母一般大写（一种共识）
    this.name = name        
    this.price= price 
    this.count = count
    //this指向空对象（这个空对象实际就是实例对象（mi、oppo）），相当于往空对象中赋值
}
const mi = new Goods('小米',1999,20)
const oppo = new Goods('OPPO',2399,30) 
//构造出的对象是一个壳子，可以另外赋值
```

在构造函数中，创建的多个对象是不同对象，它们之间彼此独立，互不影响

#### 1.5.2 时间对象

|                     实例                     | 获取的是什么 |
| :------------------------------------------: | :----------: |
|           const date = new Date()            | 获取当前时间 |
| const date1 = new Date('2003-10-2 08:30:00') | 获取指定时间 |

获取时间的**年  月  日  星期  时  分  秒**：

|        方法        | 获取的是什么 |
| :----------------: | :----------: |
| date.getFullYear() |      年      |
|  date.getMonth()   |      月      |
|   date.getDate()   |      日      |
|   date.getDay()    |     星期     |
|  date.getHours()   |      时      |
| date.getMinutes()  |      分      |
| date.getSeconds()) |      秒      |

date.toLocaleDateString()   //将**日期**部分转换为本地化的字符串表示。例如2023/12/25

**时间戳**：

​	获取时间数（从1970-01-01 00：00：00到现在的毫秒数），一般用于倒计时的操作

​	三种获得时间戳的方式:

​	第一种需要实例化，另外两种不需要；第三种只能得到当前时间戳，前两种可以指定时间

```js
// 1. getTime()
const date = new Date()
console.log(date.getTime())
// 2. +new Date()
console.log(+new Date())
// 3. Date.now()
console.log(Date.now());    
```

#### 1.5.3 实例成员&静态成员

实例成员 = 实例属性 + 实例方法

​	只要是被new过的构造函数，就是实例成员。

​	在实例成员中，对其中一个更改，另个不受影响（可以理解为每new来的对象是一个独立的对象），这个对				     象名就是new它的名字   

静态成员 = 静态属性 + 静态方法。

​	在构造函数中，没被实例化的构造函数属性，就是静态成员

​	1、静态成员只能构造函数来访问 

​	2、静态方法中的this指向构造函数

​	例如Date.new()、Math.PI、Math.random()都是静态方法

#### 1.5.4 内置构造函数

内置构造函数：

​        引用类型：Object、Array、RegExp、Date等等

​        包装类型：String、Number、Boolean等等 

**Object静态方法** ：

```js
const a = { uname: 'pink', age: 18}
const b = {}
	Object.keys(a),         //获得所有键
	Object.values(a),       //获得所有值
	Object.assign(b,a)      //将a拷贝给b （给对象添加属性）
```

**Array:**

用于创建数组，但一般都使用字面量创建数组（直接创建）

#### 1.5.5 编程思想

​        面向过程：按照分析好的步骤，然后一步一步解决问题。性能更高、适合跟硬件联系紧密的东西（单片机就  	是面向过程）前端也用的会更多

 	面向对象：按照功能划分工作。具有灵活性、代码可复用、容易维护和开发。后端会用的更多（Java面向对象）。JS中面向对象需要借助构造函数来实现，但是构造函数会存在浪费内存的问题（不同的new用地址区分）

#### 1.5.6原型对象

原型可以解决构造函数浪费内存的问题

原型：

​     构造函数都有**protoype**属性，指向另一个对象，这就是原型对象

​     构造函数的公共方法可以写进这个对象，可以共享，从而节约内存

```javascript
//公共属性封装到构造函数
function Sear (uname, age) {
     this.uname = uname
     this.age = age
}
//公共方法封装到原型对象
Sear.prototype.sing = function () {
     console.log('唱歌')
}
const lab = new Sear('刘德华','55')
const zxy = new Sear('张学友','57')
console.log(lab.sing === zxy.sing)   //这两个是相同，从而节约了内存
```

**constructer**属性指向原构造函数

​        构造函数.prototype --- > 原型

​        构造函数 < --- 原型.constructer

### 1.6 异步编程

**为什么需要异步？**
	JavaScript 是单线程的，为了避免阻塞主线程（导致页面卡顿），异步操作让程序在等待耗时操作（网络请求、文件读写等）时能够继续执行其他任务。

在JavaScript中，两种实现异步方法：回调函数、Promise

#### 1.6.1 JS执行机制

​        1、从上到下运行

​        2、单线程（同一时间只能做一件事） 

为解决单线程的弊端（要等定时函数之类的运行完才运行下一步），利用多核CPU的计算能力，可以使JavaScript脚本创建多个线程。于是，JS出现同步和异步 

​     **同步**：按顺序一步一步执行

​     **异步**：可以同时执行多项（在等待定时函数的同时运行其他） 

JS执行顺序：

​        1、执行栈中同步任务，可以理解“栈”为单行道

​        2、异步任务放入队列中，可以理解为前两步在分类（不耗时任务执行，耗时任务丢一边）

​        3、一旦栈中的任务执行完毕，系统会依次读取队列的异步任务（谁先完成，先运行谁）

​        （反复在“栈”和“队列”两头执行任务，保证这条单行道一直在运行任务。直至执行完毕）

#### 1.6.2 环境对象

环境对象指的是函数执行时的上下文环境，主要体现为 `this` 关键字的值。每个函数都有this(环境对象)，`this` 的值不是在函数定义时确定的，而是在**函数被调用时**动态绑定的。

**this指向**：

​	普通函数：全局对象（windon）

​	方法调用：所属对象（谁调用就指向谁）

​	构造函数：新创建的对象实例

​	箭头函数：继承外层作用域的 this

​	回调函数：指向windon

**控制 this方向 的方法**：

​	`call()` / `apply()`：立即调用并指定 this  

​		1、fn.call(this指向谁，参数) 

​		2、fn.apply(this指向谁，数组参数)   这两种都是调用函数

​	`bind()`：创建新函数并永久绑定 this

​		3、bind(this指向谁)。常用于定时函数中,且不会调用函数

​	箭头函数：自动绑定定义时的 this

```javascript
const btn = document.querySelector("button")
btn.addEventListener('click', function() {
	this.disabled = true    //禁用开;this指向btn
	setTimeout(function() {
		this.disabled = false
	}.bind(this),2000)      //将第二个this改变为第一个'this'
})
```



#### 1.6.3 回调函数

回调函数：函数以参数方式调用，如事件监听回调、定时器回调、自定义回调

```js
 function fu() {
     console.log('我是回调函数')
 }
 setInterval(fn,1000)   //注意回调函数调用只写函数名
```

 **回调地狱**：   

```javascript
//回调地狱的演示：
setTimeout(() => {
    console.log(111)
    setTimeout(() => {
        console.log(222)
        setTimeout(() => {
            setTimeout(() => {
                console.log(333)
            }, 1000)
        }, 1000)
    }, 1000)
},1000)
```

#### 1.6.4 迭代器&生成器        

**迭代器**

是一个对象，它提供一个 `next()` 方法，每次调用返回一个包含 `value` 和 `done` 属性的对象。

需要自定义遍历数据的时候，就要想到迭代器：`for (let v of arr) {}`

```javascript
const dmwc = ['严嵩','徐阶','高拱','张居正'];
for (let i of dmwc) {console.log(i)}   
// 工作原理：
//1、创建一个指针对象（指向当前数据结构的起始位置）
let iterator = dmwc[Symbol.iterator]()
//2、第一次调用对象的next方法，指向自动指向数据结构的第一个成员
console.log(iterator.next());                 //严嵩
//3、不断调用next方法，指针一直往后移，直到最后一个成员
console.log(iterator.next());                 //徐阶
console.log(iterator.next());                 //高拱
console.log(iterator.next());                 //张居正
console.log(iterator.next());                 //undefined
```

**生成器**

是一种特殊函数，用来进行异步编程；因为之前处理异步操作都是纯回调函数，容易造成回调地狱

生成器函数使用 `function*` 声明，使用 `yield` 暂停执行。

```javascript
function* simpleGenerator() {
  	console.log('开始执行');
  	yield '第一个值';
  	console.log('继续执行');
  	yield '第二个值';
  	console.log('即将结束');
  	return '结束值';
}

// 使用生成器
const gen = simpleGenerator();

console.log(gen.next());     //每执行一次，就执行yield之上的代码，并返回一个对象
// 开始执行
// { value: '第一个值', done: false }
```

next()中可以进行传参，传入的参数将作为上一句yield之前的语句，也就是说，这个参数将替换上一个yield返回值

```javascript
function* twoWayGenerator() {
  const name = yield '请输入你的名字：';
  const age = yield `你好 ${name}，请输入你的年龄：`;
  return `${name}，你今年 ${age} 岁`;
}

const gen = twoWayGenerator();

console.log(gen.next().value);    // "请输入你的名字："
console.log(gen.next('张三').value); // "你好 张三，请输入你的年龄："
console.log(gen.next(25).value);  // "张三，你今年 25 岁"
```

#### 1.6.5 promise

Promise是JavaScript中用于处理异步操作的对象（这个对象不受外界影响），它代表一个异步操作的最终完成（或失败）及其结果值

 Promise有三种状态：

​        pending（待定）：    初始状态

​        fulfilled（已兑现）：操作成功完成

​        rejected（已拒绝）： 操作失败

**基本语法**：

```javascript
// 1、创建Promise
const promise = new Promise((resolve, reject) => {     //注意：这两个参数也是方法（调用在下面）
// 2、异步操作
    setTimeout(() => {
        const success = true; // 模拟操作是否成功
        
        if (success) {
            resolve("操作成功！"); // 状态变为fulfilled  //成功的方法
        } else {
            reject("操作失败！"); // 状态变为rejected    //失败的方法
        }
    }, 1000);
});
// 3、使用Promise
promise
.then(result => {                //promise.then是promise对象的一个属性
    console.log(result); // 操作成功时执行
})
.catch(error => {
    console.error(error); // 操作失败时执行
})
.finally(() => {
    console.log("操作完成"); // 无论成功失败都会执行
});
```

**then方法**：

then方法的返回结果是Promise对象属性值，属性值状态由回调函数执行结果决定

​	1、这个属性值为非promise属性

 	2、这个属性值为promise属性

​	3、抛出错误


```javascript
const result = fn(1000).then(value => {
    console.log(value)
    //1、这个属性值为非promise属性
    //return 123
    //2、这个属性值为promise属性
    return new Promise((resolve,reject) => resolve('ok'))
    //3、抛出错误
    //throw new Error
},reason => {
    console.warn(reason)
}).then(value => {           //then后面还可以跟then（then的链式调用）,利用this链式调用避免回调地狱
    
},reason => {

})
```

#### 1.6.6 async&await	

**async函数**的返回值为promise对象，这个对象结果由async执行返回值决定:

 基本语法：

```js
 async function fn() {
     return  
 }
```

  return后面啥也加，返回Promise成功
             如果加了值，且不是promise对象，则返回Promise成功
             如果加了值，且是promise对象，则由这个Promise状态决定
  例如，return new Promise((resolve,reject) => resolve('成功的数据')) 
                                         //这里成功，则fn()成功；失败，则fn()失败  

**await表达式**：

​        1、必须写在async函数中，且一般只有一个await

​        2、await**右侧**表达式一般为promise对象

​            返回值promise成功值

​            promise失败则抛出异常，需要通过try…cstch捕获处理

```javascript
const Tuo = new Promise((resovle,reject) => {
    reject('失败了')
})
async function fn() {
    try {                           //因为这里执行的是失败，所以抛出错误
        await Tuo 
    } catch(e) {
        console.log(e)
    }  
}
```



## 2. DOM（文档对象模型）

DOM 将 HTML 文档表示为一个树形结构，允许程序和脚本动态访问和更新文档的内容、结构和样式。

**主要学习内容：**

- **选择元素**：`document.getElementById`, `document.querySelector`, `document.querySelectorAll` 等。
- **操作元素**：
  - **内容**：`innerHTML`, `textContent`, `innerText`。
  - **属性**：`getAttribute`, `setAttribute`。
  - **样式**：`element.style.color = 'red';`, `classList.add/remove/toggle`。
- **遍历节点**：`parentNode`, `childNodes`, `firstChild`, `nextSibling` 等。
- **创建、添加和删除节点**：`document.createElement`, `appendChild`, `removeChild`。
- **事件处理**：`addEventListener`, 事件对象、事件冒泡与捕获、事件委托。


### 2.1 选择元素

`document.getElementById（）`   选择Id

 `document.querySelector（）`    获取到该选择器的第一个元素

`document.querySelectorAll（）`  ...All('ul li')   //选择所有的li，若没有All则选择的是第一个li

```javascript
const n = document.documentElement.scrollTop   //获取HTML标签（整个网页）
```



### 2.2 操作元素

#### 2.2.1 操作内容

更新标签内容：

​	box.innerText（）      不解析标签（内容的标签）

​	box.innerHTML（）   解析标签

​	*注意：里面什么都不加，就是获取内容*

#### 2.2.2 操作属性/样式

操作**单个属性/样式**：

​	1、标准属性： 如，img.title = '照片'

​	2、style样式：如，box.style.marginTop = '10px'      *注意： 不是 margin-top（CSS属性名要用**驼峰命名**）*

​	3、通用属性：

```javascript
	// 设置属性
	box.setAttribute('data-id', '123');
	box.setAttribute('title', '提示信息');
	// 获取属性		
	const id = box.getAttribute('data-id');
	const title = box.getAttribute('title');
```

​	4、自定义属性：

```javascript
	<div data-id="'1" data-user-name="杜王"></div>
	
	document.querySelector('div').dataset.id   //获取自定义的属性
	document.querySelector('div').dataset.userName   //获取自定义的属性      
```

操作类名修改**多个样式/属性**：

​        1、直接修改类名：box.className = 'xiugai'    //box ===> xiugai   *注意clssName会覆盖之前的类名*

​	2、通过classList修改（不会覆盖之前类名）:

​        	box.classList.add(actre)          //添加类

​        	box.classList.remove(fghjhk)    //删除类

​        	box.classList.toggle(tyui)        //更新类（如果有就切换，没有就添加）

#### 2.2.3 遍历节点

目的：减少document.querySelector('.x')的使用

**父节点**：

​	`parentNode`    box.parentNode返回box的父节点

​        	当然，在同一句中也可以跟多个parentNode（表示爷爷或更高的祖先）

**子节点：**

 	`childNodes`  : 获得**所有**子节点（包括文本节点（空格、换行）、注释节点）

​	`firstChild` ：仅获得**所有**子元素节点，并返回一个伪数组

**兄弟节点：**

​	`previousElementSibling`：上一个**兄弟节点**（元素）

​	`nextElementSibling`：下一个**兄弟节点**（元素）。一般用于获取<li>

**增加节点：**

​	`createElement` : 创建标签

​	`appendChild ` : 向后追加标签      如、 ul.appendChild(li)         //追加在ul标签中的**最后**一个位置

​        `insertBefore`  ：任意位置追加标签；语法：父元素.insertBefore(要插入的元素，在那个元素前面)

​		如、ul.insertBefore(li,ul.children[0])  //追加在ul标签某个（第一个）子元素的前面

**克隆节点：**

​	`cloneNode(true)`

```
 ul.appendChild(ul.children[0].cloneNode(true))    //克隆并追加
```

**删除节点：**

​	`removeChlid`  语法：父元素.removeChlid(要删除的子元素)



### 2.3 事件处理

#### 2.3.1 事件监听

事件监听：检测是否有事件发生，一旦发生，立即调用一个函数做出响应

语法：

​	开启事件监听：触发对象.addEventListener('触发操作'， 触发后执行的函数)

​	移除事件监听：button  .`removeEventListener` ('click', handleClick); 

​	*注意：匿名函数不能被解绑，要想移除事件就命名*

触发操作：

​	鼠标触发：click(鼠标点击)、mouseenter(鼠标经过)、mouseleave(鼠标离开)

​	表单获得光标（用于搜索框点击后）：focus(获得焦点)、blur(失去焦点)  

​	键盘触发（用于文本发布）：keydown(键盘按下触发)、keyup(键盘抬起触发）  

​	表单输入触发（用于用户随输入的内容变化而触发）：input(用户输入触发)

​	窗口触发：需要在windon运行

​		load（加载）：等待页面所有资源加载完毕后，执行function()

​		scroll（滚动）：

​		resize （尺寸）：检测盒子宽度，好像是用于响应式

```javascript
//加载事件
window.addEventListener('load', function() {})  //等待页面所有资源加载完毕后，执行function()
img.addEventListener('load', function() {})     //等待图片所有资源加载完毕后，执行function()
                        //DOMContentLoaded需要在dom中运行
document.addEventListener('DOMContentLoaded', function() {})//等待HTML元素加载完毕后，执行（无需等待css,js）


//滚动事件
div.addEventListener('scroll', function() {
    console.log(div.scrollTop)             //scrollTop被卷起的内容的高度(上)
})                                         //scrollLeft左侧被卷起的宽度（左）
```

#### 2.3.2 事件流

事件流：事件完整执行流动路径 

**捕获**：从大到小；

**冒泡**：从小到大 

捕获 例:事件监听(同名事件)若存在祖先关系(触发对象(相同)存在祖先关系),优先从祖先开始执行 

冒泡 例:当一个事件被触发,会依次向上调用所有父级的同名事件 

**阻止冒泡：** `e.stopPropagation()`

```javascript
const son = document.querySelector('.son')
son.addEventListener('click', function(e) {
    alert('我是儿子')
    // 阻止流动(冒泡)
    e.stopPropagation()  
})
```

**事件委托：** 利用冒泡,委托给父级

```javascript
const ul = document.querySelector('ul')
ul.addEventListener('click', function(e) {    //只要点击了ul及以下就触发
  	console.log(e)
    console.log(e.target)   //e.target表示ul的所有子元素，也就是我们点击的对象
    					  //当然，当我们点击其他地方，就不是li,而是ul,因此我们可以通过判断对象名，进行下一步
    if (e.target.tagName === 'LI')  {   
    //ul下只有li执行   e.tagget指向单个li，而this指向ul(所有li,也包括其他)
        e.target.style.color = 'red'  //单个li
    }                      
})
```



#### 2.3.3组织元素默认行为

```javascript
 const form = document.querySelector('form')
 form.addEventListener('submit', function(e) {   //subit提交事件
     //阻止默认行为（阻止提交）
     e.preventDefault()   //pr……lt阻止链接跳转
 })
```




## 3. BOM（浏览器对象模型）

BOM 提供了独立于网页内容而与浏览器窗口进行交互的对象。

**主要学习内容：**

- **window 对象**：它是 BOM 的核心，代表浏览器窗口。全局变量和函数都是 `window` 对象的属性和方法。
- **navigator**：提供关于浏览器的信息（名称、版本、用户代理等）。
- **location**：提供当前窗口的 URL 信息，并可以用于页面重定向 (`location.href`, `location.reload`)。
- **history**：提供与浏览器历史记录交互的接口 (`history.back()`, `history.go()`)。
- **screen**：提供用户屏幕的信息（宽度、高度、色彩深度）。
- **定时器**：`setTimeout` 和 `setInterval`。

### 3.1 navigator&history

`navigator.userAgent`:检测浏览器信息。常用于检测用于设备（PC端、苹果端、安卓端等）

​	一般都有专业一段代码（VC即可），用于检测在该设备上是否呈现

`histroy`  用于管理历史记录 

 	histroy.back:  后退

 	histroy.forward:  前进

 	histroy.go(参数):参数为1：前进一个界面；-1：后退一个界面 

### 3.2 location对象

location.href = 'http://www.baidu.com'  location.href常用于跳转 

location.search:获取地址中携带的参数('?'后面的内容)

location.hash(哈希):获取地址中的哈希值。用于在导航条不变，下面的大盒子变

```html
<a href="#/shouye">首页</a>   <!-- 哈希地址 -->
<a href="#/chuangzuo">创作</a>
<a href="#/wode">我的</a>
```

location.reload():刷新页面（相当于F5键）

​        location.reload(true)强制刷新

### 3.3 本地存储

本地存储：在同一浏览器中，可以永久保留（本质是存在浏览器中），存入的类型会转为**字符串型**

1. 简单类型存储：

2. - 存入本地：  localStorage.setItem('键','值')
   - 从本地获取：localStorage.getItem('键')
   - 从本地删除：localStorage.removeItem('键')    当然，也可以手动删除（在浏览器中的检查）

3. 复杂类型（如字典）的存储：

   1. 必须先将复杂类型转换为**JSON**字符串：`localStorage.setItem('键',JSON.stringfy(键))`。否则，

   ​       在本地中就是一串乱码

   ​   2. 在本地中查看值：为JSON对象（属性和值都有双引号） 

   3. 从本地获取：`JSON.parse(localStorage.getItem('键'))`。将JSON字符串转换为字典

### 3.4 定时函数

1. **间歇函数**：`setInterval`一直运行,除非手动清除; 会返回数字（定义它的变量会变）

	       	语法：setInterval(function() {}，间隔时间) 

​        关闭间歇函数：`clearInterval`

​	       语法：clearInterval(定时器的变量名)

​	       **注意**：*重新开启就重新调用，但变量名(返回 ID)会变*

2. **延时函数**: `setTimeout`只运行一次 

​        语法：setTimeout(funlction() {},间隔时间)

### 3.5深浅拷贝

#### 3.5.1 浅拷贝

原理：拷贝地址（复杂类型拷贝地址、简单类型直接拷贝内容）

​            因此对只有一层简单类型的复杂类型可以使用（直接复制地址，会影响原复杂类型的属性）

哪些是浅拷贝，列如（两种）：

```javascript
//1、进行展开，再装入
const abj = {a = 1, b = 2}
const abg = {}
const abg = { ...abj }     //不能直接赋值（赋值的话，就是直接复制地址，会影响abj）

//2、内置构造函数方法
Object.assign(abg,abj )
```

####  3.5.2 深拷贝

原理：拷贝对象

可以通过三种方式实现深拷贝：递归、lodash/cloneDeep、JSON.stringfy()

1、递归

```javascript
const obj = {lq: '篮球',zq: '足球', ppq: '乒乓球',yy: ['蛙泳','蝶泳']}
const o = {}
function deepCopy(newObj, oldObj) {        
    for (let i in oldObj) {
        if (oldObj instanceof Array) {      //判断oldObj属性值中是否有数组
            newObj[i] = []                  //在新对象中创建一个空数组
            deepCopy(newObj[1],oldObj[i])   //重新执行
        // } else if (oldObj instanceof Object){    //判断oldObj属性值中是否有对象
        //     newObj[i] = {}                  //在新对象中创建一个空对象
        //     deepCopy(newObj[1],oldObj[i]) //重新执行
        } else {                          //否则
            newObj[i] = oldObj[i]         //直接直接添加进新对象中
        }
    }
}
deepCopy(o, obj)
        console.log(o)
```

2、深拷贝-lodash

​	一种封装好的深拷贝方法，引入库即可使用

3、JSON.stringfy()

​	原理：先转换为字符串，在转回来

- ```
  const oo = JSON.parse(JSON.stringify(obj))
  ```


### 3.6 异常处理

异常处理是指预估代码执行过程中可能发生的错误，然后最大程度地避免错误的发生导致整个程序无法继续运行。

1. **throw抛异常**
   - throw抛出异常信息，程序**终止**执行
   - `throw new Error("这是什么错误")` 用来提示错误
2. **try/catch捕获错误**

- ```js
  //可能发生错误的代码
  try{
  	
  //拦截错误，提示浏览器提供的错误信息，但不终止运行
  }catch(err){
      throw new Error("这是什么错误")  //终止（一般都用这句）
  }
  //无论正确与否都执行
  finally{
      
  }
  ```

3. **debugger**


1. - 需要打断点的代码处写入，用于找BUG。写入之后，我们打开开发者工具，就自动跳转到这行代码处

### 3.7 节流与防抖

1. 防抖：单位时间内，频繁触发事件，只执行最后一次

- 用途：搜索框输入时，只需用户最后一次输入完，再发送请求

- 语法：_.debounce(需要防抖的函数, 时间)



- ```javascript
  const box = document.querySelector('.box')
  let i = 0
  function mouseMove() {
      box.innerHTML = i++
      //box.addEventListener('mousemove', mouseMove)  //鼠标滑动1像素，盒子数字加1
      //利用lodash库防抖
      //语法：_.debounce(需要防抖的函数, 时间)
      box.addEventListener('mousemove', _.debounce(mouseMove, 1000))  //每隔1秒钟发动一次（鼠标滑动1像素，盒子数字加1）
  }
  ```


2. 节流：在单位之间内不管事件触发了多少次，只执行一次（相当于冷却时间）


