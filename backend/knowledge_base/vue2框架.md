# vue2框架

[Vue.js中文网](https://vuejs.zcopy.site/)是一套用于构建用户界面的渐进式框架。

其他框架：[React](https://vuejs.zcopy.site/v2/guide/comparison#React)、[AngularJS (Angular 1)](https://vuejs.zcopy.site/v2/guide/comparison#AngularJS-Angular-1)

Vue版本: Vue2、Vue3(新版本)

Vue API风格：选项式API、组合式API

## 1 基础语法

### 1.1 创建vue

Vue.js 的核心是一个允许采用简洁的模板语法来声明式地将数据渲染进 DOM 的系统：

```html
<div id="app">
  	{{ message }}
</div>
<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
  	var app = new Vue({
    	el: '#app',
    	data: {
      		message: 'Hello Vue!'
    	}
  	})
</script>
```

data中的数据，是会被添加到实例中:
 1.访问数据，实例.属性名   
 2.修改数据，实例.属性名=新值  

### 1.2 插值表达式

插值表达式是Vue的一种模板语法，利用（单句）表达式进行插值，渲染到页面中

可以插入：

​	数字、字符串、join字符串

​	三元表达式

不能插入：

​	语句  如、if、for、var等等（且不能在标签属性中插入）

```html
<div id = 'app'>
    <h1>{{nickname + '你好'}}</h1>
    <span>我也{{friend.desc}}</span>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
    const app = new Vue ({
        el: '#app',
        data: {
            //响应式数据（数据变了，视图会自动更新）
            nickname:'tony',
            friend: {
                name: '张飞',
                desc: '爱发脾气'
            }
        }
    })
</script>
```

### 1.3 Vue指令

Vue指令:带有v-前缀的特殊属性

指令带有前缀 `v-`，以表示它们是 Vue 提供的特殊 attribute。

这些指令一般是表示给标签内部添加内容：

​	`v-html` 添加标签

​  	`v-show`、`v-if` 添加属性

#### 1.3.1 v-html

因为插值表达式无法解析标签 ，需要使用一个动态V属性

```html
<div id = 'app'>
    <div v-html="msg"></div>   
</div>
data: {
    msg: `<a href="http=://www.itheima.com">黑马</a> `
}
```

####  1.3.2 v-show&v-if

共同点：两个属性都是控制元素显示或隐藏 ，条件为真才渲染

不同点：`v-show`底层原理：**切换**CSS的display: none来控制隐藏

​               `v-if`底层原理：根据判断条件控制 **创建** 和 **移除**

```html
<div>
	<div v-show="flag" class="box">我是一个控制v-show的盒子</div> 
	<div v-if="flag" class="box">我是一个控制v-if的盒子</div>
</div>
<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
    const app = new Vue ({
        el: '#app',
        data: {
           flag:false  //使用布尔值来回切换
        }		
  	})
```

#### 1.3.3 v-else&v-else-if

```HTML
<div id="app">
    <p v-if="score >= 90">成绩评定A：奖励电脑一台</p>
    <p v-else-if="score >= 70">成绩评定B：奖励周末郊游</p>
    <p v-else-if="score >= 60">成绩评定C：奖励零食礼包</p>
    <p v-else>成绩评定D：惩罚一周不能玩手机</p>
</div>
```

#### 1.3.4 v-on 内联语句

v-on(绑定)：v-on: 等于 @

```HTML
<div id="app">
    <button @click="count--">-</button>
    <span>{{ count }}</span>
    <button v-on:click="count++">+</button>  <!-- 注册点击事件，内容为conut++ -->
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
  	const app = new Vue({
    	el: '#app',
    	data: {
      		count: 100
    	}
  	})
  </script>
```



#### 1.3.5 v-on-配置methods函数

`methods`提供方法（函数）

```HTML
<div id="app">
  <!-- 点击调用函数 -->
  <button @click="fn">切换显示隐藏</button>
  <h1 v-show="isShow">黑马程序员</h1>
</div>
<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
  const app4 = new Vue({
    el: '#app',
    data: {
      isShow: true
    },
    methods: {
      fn () {
        // 让提供的所有methods中的函数，this都指向当前实例(app)
      
        this.isShow = !this.isShow  //！this.isShow(取反，切换显隐)
      }
    }
  })
</script>
```



#### 1.3.6 v-on 传递参数

事件参数可以获取**event对象**和通过事件传递参函数

Vue中event和JS的event对象是一样的

```html
<button @click="fn">切换显示隐藏</button>
methods:{
    fn(e) {
        consloe.log(e)
    }
}
```

通过事件**传递参函数**

```vue
<template>
	<p @clike='getName(item)' v-for="(item index) of names" :key="index">{{ item }}</p>
</template>
<srcipt>
export default {
	data() {
		return{
			names: ['张三','李四','王二']
		}
	},
	methods:{
		getName(name) {
    		consloe.log(name)
		}
	}
}
</srcipt>
```

#### 1.3.7 v-bind动态设置

 动态设置：v-bind:属性名   等于   :属性名

1、通过切换属性达到动态：

​	设置单个动态属性：

​	`<img :src="imgUrl" :title="msg" alt="">`

​	设置多个动态属性：

​	`<img v-bind="对象名" alt="">`  将多个属性写在一个对象中

2、通过切换类名，来切换样式：

​	一个类名来回切换 

​	 `<div class="box" :class="{ pink: true, big: true }">黑马程序员</div>`

​	批量切换所有类名

​	`<div class="box" :class="['pink', 'big']">黑马程序员</div>`

​	另外，绑定class可以是数组与对象嵌套

​	`<div :class="[{ 'active':isActve }, errorClass]"></div>`    *注意：只能是数组嵌套对象*  

3、通过切换style,切换样式

​	 `<div class="box" :style="{ width: percent + '%' }">`

实例、导航栏切换：

```html
<div id="app">
  <ul>
    <!--                                                    设置点击切换高亮 -->
    <li v-for="(item, index) in list" :key="item.id" @click="activeIndex = index">
      <!--           0、1、2 = 2 第三项高亮 -->
      <a :class="{ active: index === activeIndex }" href="#">{{ item.name }}</a>
    </li>
  </ul>
</div>
<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      activeIndex: 2, // 设置初始默认谁高亮
      list: [
        { id: 1, name: '京东秒杀' },
        { id: 2, name: '每日特价' },
        { id: 3, name: '品类秒杀' }
      ]
    }
  })
</script>
```

#### 1.3.8 v-for

`v-for="(item, index) in list"`    

v-for="(标签需要渲染的内容，索引值)  in  数组（对象）"     需要那个写那个,注意两个不要写反。另外，如果是对象，还会有一个key

当然，也可以使用 `of` 代替 `in` ，这更接近于javaScript迭代语法

```html
<div id="app-4">
  <ol>
    <li v-for="todo in todos">
      {{ todo.text }}
    </li>
  </ol>
</div>

<script>
  var app4 = new Vue({
    el: '#app-4',
    data: {
      todos: [
        { text: '学习 JavaScript' },
        { text: '学习 Vue' },
        { text: '整个牛项目' }
      ]
    }
  })
</script>
```

#### 1.3.9 v-for-key

Vue默认按照“就地更新”策略：当数据顺序被改变时，Vue不会随之移动DOM元素顺序，而是重新更新顺序（也就是重新渲染），这样很消耗性能（浪费内存）

key作用：给元素添加唯一标识，以便跟踪每个节点。一般使用id作为key	

```html
<div id="app">
    <ul>
      <li v-for="(item, index) in booksList" :key="item.id">
        <span>{{ item.name }}</span>
        <span>{{ item.author }}</span>
        <!-- 注册点击事件 →  通过 id 进行删除数组中的 对应项 -->
        <button @click="del(item.id)">删除</button>
      </li>
    </ul>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        booksList: [
          { id: 1, name: '《红楼梦》', author: '曹雪芹' },
          { id: 2, name: '《西游记》', author: '吴承恩' },
          { id: 3, name: '《水浒传》', author: '施耐庵' },
          { id: 4, name: '《三国演义》', author: '罗贯中' }
        ]
      },
      methods: {
        del (id) {
          // 通过 id 进行删除数组中的 对应项 → filter(不会改变原数组)
          // filter: 根据条件，保留满足条件的对应项，得到一个新数组。
          // console.log(this.booksList.filter(item => item.id !== id))
          this.booksList = this.booksList.filter(item => item.id !== id)
        }
      }
    })
  </script>
```



#### 1.3.10 v-model

v-model 可以让数据和视图，形成双向数据绑定, 可以快速[**获取**]或[**设置**]表单元素的内容

​      (1) 数据变化，视图自动更新

​      (2) 视图变化，数据自动更新

基本用法：

```html
<div id="app">
    账户：<input type="text" v-model="username"> <br><br>
    密码：<input type="password" v-model="password"> <br><br
</div>
data: {
  	username: '',
  	password: ''
}   		
```

表单输入绑定：

​	`v-model` 指令在表单 `<input>`、`<textarea>` 及 `<select>` 元素上创建双向数据绑定，会根据控件类型自动	

​	选取正确的方法来更新元素

v-model修饰符：

​	`lazy` ：主要用表单焦点获取事件，使用`v-model.lazy`让焦点失去后再进行获取

​	`number` ：获取数字类型

​	`trim`：去掉前后空格



### 1.4 指令修饰符

在事件处理程序中调用 `event.preventDefault()` 或 `event.stopPropagation()` 是非常常见的需求。

Vue.js 为 `v-on` 提供了**事件修饰符**。之前提过，修饰符是由点开头的指令后缀来表示的。

在官网上查看

**事件修饰符**

​	@事件名.stop     →  阻止冒泡

​	@事件名.prevent  →  阻止默认行为

​	若没有阻止链接默认点击跳转，则 fn 与 跳转 会同时发生

- ```
  <a @click='fn'  href="http://www.baidu.com">阻止默认行为</a>
  methods: {
  	fn(e){}
  }
  ```

  1、可以通过调用 `event.preventDefault()` 阻止默认事件

1. ```
   <a @click='fn'  href="http://www.baidu.com">阻止默认行为</a>
   methods: {
   	fn(e){
   		e.preventDefault()
   	}
   }
   ```

   2、可以添加`prevent`事件修饰符

   ```
   <a @click.prevent='fn'  href="http://www.baidu.com">阻止默认行为</a>
   methods: {
   	fn(e){}
   }
   ```

**按键修饰符**

​	@keyup.enter  →  监听键盘回车事件

### 1.5 计算属性

​	模板内的表达式非常便利，但是设计它们的初衷是用于简单运算的。在模板中放入太多的逻辑会让模板过重且难以维护。所以，对于任何复杂逻辑，你都应当使用计算属性。

需要声明在computed中，最后用**return输出**，用于渲染

```javascript
const app = new Vue({
  el: '#app',
  data: {},
  methods: {},
  computed: {
    totalCount () {
      let total = this.list.reduce((sum, item) => sum + item.num, 0)
      return total
    }
  }
})
```

 `methods` 与`computed`两种方式的最终结果确实是完全相同的。

​	然而，不同的是**计算属性**是基于它们的响应式依赖进行**缓存的**。只要不变就不会重新执行。而methods每次调用都会重新执行。

 **简写**（只有getter） → 获取，没有配置设置的逻辑

```javascript
computed: {
	fullName () {
	    return this.firstName + this.lastName
	}
}
```

**完整写法**（带getter和setter） → 获取 + 设置

```javascript
computed: {
  fullName: {
    // (1) 当fullName计算属性，被获取求值时，执行get（有缓存，优先读缓存）
    //     会将返回值作为，求值的结果
    get () {
      return this.firstName + this.lastName
    },
    // (2) 当fullName计算属性，被修改赋值时，执行set（也就是get返回值变了）
    //     修改后的值，传递给set方法的形参
    set (value) {      
      this.firstName = value.slice(0, 1)     //截取0到1
      this.lastName = value.slice(1)         //从1往后取
    }
  }
}
```

- **get**：绝大多数情况下，我们只使用 `get` 来获取计算后的值。
- **set**：当你需要允许对计算属性进行赋值，并且这个赋值操作需要更新其依赖的源数据时使用。这种情况相对较少。

### 1.6 侦听器

虽然计算属性在大多数情况下更合适，但有时也需要一个自定义的侦听器。当需要在**数据变化**时执行异步或开销较大的操作时，这个方式是最有用的。

语法：

``````js
watch: {
	//当数据变化是函数自动执行
    函数名 ( newValue ) { }  // 函数名是data中需要侦听的数据；newValue新值, oldValue老值（一般不用）
}	
``````

完整写法：

```js
watch: {
  被监听数据: {
    deep: true, // 深度监视
    immediate: true, // 立刻执行，一进入页面handler就立刻执行一次（新值为现在值，旧值为nudefined）
    handler (newValue) {}
  }
}
```



### 1.7 模板引用

Vue的声明性渲染模型为编译者省去了大量DOM的直接操作：

​	内容改变：{{使用模板语法}}

​	属性改变：v-bind:指令

​	事件改变：v-on：绑定

`ref`属性可以直接操作DOM，但一般没有什么特别需求，一般不直接操作DOM，因为更麻烦

```vue
<div ref='conta' class='conta'>{{ obj }}</div>
<input type='text' ref='userName'></input>
methods:{
    getEleme(){
        this.$refs.conta.innterHtML = 'hahaha'
    }
}
```

### 1.8 组件生命周期

组件生命周期：从组件（创造--->卸载）的过程。在组件生命周期中有许多重要节点（钩子），在这些重要节点都有一个生命周期钩子的函数，这些函数到了各自的重要钩子就会**自动执行**。

四个阶段-八个钩子：

|      四个阶段   四个阶段      |         响应时机         |      八个钩子       |
| :---------------------------: | :----------------------: | :-----------------: |
|     创建阶段（准备数据）      |   响应式数据准备好之前   | beforeCreate () {}  |
|                               |   响应式数据准备好之后   |    created () {}    |
|     挂载阶段（渲染模板）      |        模板渲染前        |  beforeMount () {}  |
|                               |        模板渲染后        |    mounted () {}    |
| 更新阶段(修改数据 → 更新视图) | 数据修改了，视图还没更新 | beforeUpdate () {}  |
|                               |  数据修改了，视图更新了  |    updated () {}    |
|           卸载阶段            |          卸载前          | beforeDestroy () {} |
|                               |          卸载后          |   destroyed () {}   |

一般来说数据在结构渲染之后进行获取

## 2 自定义组件（可复用）

### 2.1 Vue文件基本组成

vue文件组成：

```vue
<template>
	<!-- 第三步：显示组件（唯一必须组件） -->
	<Myconponent></Myconponent>
</template>

<script>
//第一步：引入组件
import Myconponent from "./components/Myconponent.vue"
export default {
    //第二步注入组件
    components:{
        Myconponent
    }
}
</script>

<!-- scoped：将全局样式设置成本文件样式 -->
<style scoped>    
</style>
```

### 2.2 可复用组件组成

> components文件夹存放可复用Vue组件，这些可复用组件可以实现相应的功能
>
> Root.vue                           最大组件盒子             
>
> ​	Header.vue               顶上盒子
>
> ​	main.vue                   中部左盒子
>
> ​		Article.vue         中部左盒子中的小盒子
>
> ​	Aside.vue                  中部右盒子
>
> ​		Item.vue            中部右盒子中的小盒子
>



### 2.3 组件注册方式

​        上面这种可复用组件，就是局部组件：需要三步才能用。然而，全局组件可以直接在<template>中显示，且可以在任意组件中使用。

全局组件在main.js中注册

全局注册的缺点：

​	全局注册所有的组件即便不再使用了，它仍然会被包含在你最终的构建结果中。这造成了用户下载的 JavaScript 的无谓的增加。



## 3 组件间传递数据

除APP.vue文件外的其他子组件子组件间，也可以有父子际关系，例如：

Article.vue文件（子）：

```vue
<template>
	<div></div>
</template>

<script>
export default {
    data(){
        return{}
    }
}
</script>
```

main.vue 文件（父）：

```vue
<template>
	<Article></Article>
</template>

<script>
import Article from "./Article"    //跟引入APP.vue一样的方法
export default {
    components:{
        Article
    }
}
</script>
```

### 3.1 props（父传子）

props即可以传递动态数据、传递死数据，且可以传多条。但是切记props是只读的(只能读取，**不能修改**)

 例：将title与messge传给儿子

父：

```vue
<template>
	<Article title='我要给儿子的数据' :change="message"></Article>     //第一步：传入数据
</template>

<script>
data(){
  	return{messge:"我要传给儿子的动态数据"}  
}
</script>
```

子：

```vue
<template>
	<div>{{ title }}</div>                             
	<p>{{ message }}</p>
</template>

<script>
export default {
    data(){
        return{}
    },
    props:["title","message"]                          //第二步：接收数据
}
</script>
```

当然，props不仅可以传递简单类型，各种**复杂类型**都可以

```js
data(){
  	return{
  		messge:"我要传给儿子的动态数据",
  		messge1:['a','b','c'],
  		messge2:{a:1,b:2,c:3}
  	}  
}
```

### 3.2 props效验

1. props可以对父亲传来的数据进行效验，即满足要求的才传入(不满足要求也会传入，但会报警告)

   ```
   props:{
   	messge1:{type:Array},
   	messge:{type:[String,Number,Array]}   //满足一项即可
   }
   ```

2. 若父组件没有传递或子组件没有接受数据，我们可以设置**默认值**

   ```````
   props:{
   	messge1:{
   		type:Array,
   		default:"杜王"
   	}
   }
   ```````

   另外，数字与字符串可以直接default，但如果是**数组或对象**，则必须通过函数返回**默认值**

   ```
   props:{
   	messge1:{
   		type:Array,
   		default(){
               return ['空数组']
   		}
   	}
   }
   ```

3. 若父组件没有传递或子组件没有接受数据，我们可以通过设置`repuired`**报警告**

   ```
   props:{
   	messge1:{
   		type:Array,
   		default:"杜王",
   		repuired:true
   	}
   }
   ```

### 3.3 组件(自定义)事件（子传父）

将'someEvent'和this.msg传给父亲：

- Article.vue文件（子）：

  ```vue
  <template>
  	<button @click="clickEventHandle">点击传给父亲数据</button>  //第一步：绑定事件
  </template>

  <script>
  export default {
      data(){
          return{msg:'儿子的数据'}
      },
      methods:{
          clickEvenHandle(){                                   //第二步：给绑定的事件传入数据
              //自定义事件
              this.$emit('someEvent',this.msg)     
          }
      }  
  }
  </script>
  ```

- main.vue 文件（父）：

  当点击按钮的时候，事件回调内部调用$emit方法去触发自定义事件,第一个参数为触发事件类型，第二个、三个、N个参数即为传递给父组件的数据。

  ```vue
  <template>
  	<Article @someEvent="getHandle"></Article>             //第三步：给绑定的事件命名
  </template>

  <script>
  import Article from "./Article"    
  export default {
      components:{ Article },
      data(){
          message:''                                      //第五步：将获取到的数据进行重新命名
      }
      methods:{
          getHandle(data){                               //第四步：将传入的二三……数据传入事件参数
              this.message = data   //这里的data是this.msg,而'someEvent'也就是触发的这个事件
          }
      }
  }
  </script>
  ```

### 3.4 组件事件配合v-model

v-model指令可是收集表单数据(数据双向绑定)，除此之外它也可以实现父子组件数据同步。v-model实指利用props[modelValue]与自定义事件[update:modelValue]实现的。

在子组件中输入，在父组件中实时接收到子组件内容：

Article.vue文件（子）：

```vue
<template>
	<input type='text' v-model='search'>  
</template>

<script>
export default {
    data(){
        return{search:''}
    },
    methods:{
        watch:{
            search(newValue){
                this.$emit('someEvent',newValue)     
            }
        }                              
    }  
}
</script>
```

main.vue 文件（父）：

父组件接受内容格式基本不会有什么变化(和上面相同)

```vue
<template>
	<p>输入的内容是：{{ search }}</p>
	<Article @someEvent="getHandle"></Article>               
</template>

<script>
import Article from "./Article"    
export default {
    components:{ Article },
    data(){
        return{search:''}                                 
    }
    methods:{
        getHandle(data){                                
            this.search = data   
        }
    }
}
</script>
```

### 3.5 props传递函数-返回参数

通过**props**（父传子）传递函数，达到**子传父**

父：

```vue
<template>
	<Article :onEvent="dataFn"></Article> 
    <p> {{ message }} </p>
</template>

<script>
data(){
  	return{message:''}
},
methods:{                            //通过这里给message设置一个方法,利用函数传参达到子传父
	dataFn(data){
        this.message = data
  	}
}
</script>
```

子：

```vue
<template>                             
	<p>{{ onEvent('儿子数据') }}</p>
</template>

<script>
export default {
    data(){
        return{}
    },
    props:{onEvent:Function}    //接收这个数据，且为函数类型                     
}
</script>
```

### 3.6 依赖注入

使用 `props` 无法很好的扩展到更深层级的嵌套组件上。这也是依赖注入的用武之地，它用到了两个新的实例选项：`provide` 和 `inject`。

前辈组件：

```
data(){
    retrun{
        getMap:'前辈的数据'
    }
}
provide() {                      //给需要传递的数据放入provide中
  return {
    getMap: this.getMap
  }
}
```

在任何后代组件里，我们都可以使用 `inject` 选项来接收：

```
inject: ['getMap']               //直接接收即可，然后给data
data(){
    return {
    	message:this.getMap
    }
}
```

**注意**：依赖注入只能由前辈先后辈传递数据

因此如果该数据常被使用，可以直接在main.js中`app.provide()`



## 4 插槽（组件间传递模板）

插槽：默认插槽、具名插槽、作用域插槽可以实现父子组件通信。实现组件之间模块的传递

### 4.1 默认插槽

父组件向子组件传递了一个模板。注意：在**子组件**内部的模板中书写slot全局组件标签

父：

```vue
<template>
  	<Article>            //在标签内部写，而不再写为属性
  		<h3></h3>
  		<div></div>
  	</Article>  
</template>
```

子：

```vue
<template>
  	<div></div>
    <slot></slot>     //插槽出口(默认)，一般只有一个（要想有多个插槽，命名）
</template>
```

### 4.2 插槽作用域&默认内容

1. 作用域：

   插槽内容可以访问到父组件作用域，因为插槽内容本身是在父组件模板中定义的。但是子组件内部决定不了自身结构与外观(样式)

   意思就是：子组件不仅可以访问组件，也可以访问父组件属性、方法等

2. 默认内容：

   若插槽内没有内容，可以设置默认内容

   ```
   <slot><div>插槽默认内容</div></slot>
   ```

### 4.3 具名插槽

顾名思义，此插槽带有名字在组件内部留**多个**指定名字的插槽。

主要用于不想全部插入，而是**根据意愿插入**哪些

父：

```vue
<template>
  	<Article>
    	<template v-slot:a>
  			<h3></h3>
  		</template>
  		<template v-slot:b>
  			<div></div>
  		</template>
  	</Article>  
</template>
```

子：

```vue
<template>
  	<slot name='a'></slot> 
    <slot name='b'></slot>     
</template>
```

**注意**：需要注意`v-slot:`可以替换为`#`

### 4.4 插槽使用子组件数据

在插槽定义域中得知，插槽子组件不能使用子组件数据，例如：在某些场景下，插槽内容会同时需要子组件域和父组件域的数据，如何做呢？

先将子组件数据传入父组件，再一并将父组件与子组件数据通过插槽访问到

**1、默认插槽：**

父：

```vue
<template>
	<Article v-slot='slotProps'>                  //第二步：在子组件标签中使用v-slot接收数据
        <div>{{ search }}和{{ slotProps }}</div>   //第三步：将父子数据都渲染到子组件标签
    </Article>               
</template>

<script>
import Article from "./Article"    
export default {
    components:{ Article },
    data(){
        return{search:'父组件数据'}                                 
    }
}
</script>
```

子：

```vue
<template>
	<slot :msg='child'></slot>                   //第一步：在slot中将数据传递给父组件
</template>

<script>
export default {
    data(){
        return{child:"子元素数据"}
    }
}
</script>
```

这段代码含义是：父组件的`<div>`使用到`child:"子元素数据"`

**2、具名插槽**:

父：

```vue
<template>
	<Article> 
        <template #a='slotProps'>                       //注意这两行即可
        	<div>{{ search }}和{{ slotProps.msg }}</div>  
        </template>
    </Article>               
</template>
```

子：

```vue
<template>
	<slot name='a' :msg='child'></slot>                  //这里没什么变化，只是单纯的加了个名字
</template>
```

## 5 其他

### 5.1 动态组件

使用`component :is""`可以实现组件间来回切换

点击按钮实现组件来回切换

```vue
<template>
	<component :is="tabComponent"></component>
	<button @click="changeHandle">点击切换组件</button>
</template>
<script>
import ComponentA from "./ComponentA.vue"
import ComponentB from "./ComponentB.vue"    
export default {
    data(){
        return{tabComponent:ComponentA}
    },
    components:{
        ComponentA,
        ComponentB
    },
    methods:{
        changeHandle(){
            this.tabComponent = this.tabComponent == "ComponentA" ? "ComponentB" : "ComponentB"
        }
    }
}
</script>
```

另外，被切换的组件会被卸载，但可以通过`<keep-alive>`强制被切换的组件，仍保持存货状态

可以理解为放入了内存里

```
<keep-alive>
	<component :is="tabComponent"></component>
</keep-alive>
```

### 5.2 异步组件

可以实现页面用到哪个组件就加载哪个组件，Vue提供了`defineAsyncComponent`方法来实现异步

语法：

```
import { defineAsyncComponent } from 'vue'        //第一步：先引入
import ComponentA from "./ComponentA.vue"
const ComponentB = defineAsyncComponent(() =>     //第二步：对需要异步加载的组件进行处理
	import ("./ComponentB.vue")
)
```



1. ​

   ```vue
   父组件中：
         <Game v-slot="params">
         <!-- <Game v-slot:default="params"> -->
         <!-- <Game #default="params"> -->
           <ul>
             <li v-for="g in params.games" :key="g.id">{{ g.name }}</li>
           </ul>
         </Game>

   子组件中：
         <template>
           <div class="category">
             <h2>今日游戏榜单</h2>
             <slot :games="games" a="哈哈"></slot>
           </div>
         </template>

         <script setup lang="ts" name="Category">
           import {reactive} from 'vue'
           let games = reactive([
             {id:'asgdytsa01',name:'英雄联盟'},
             {id:'asgdytsa02',name:'王者荣耀'},
             {id:'asgdytsa03',name:'红色警戒'},
             {id:'asgdytsa04',name:'斗罗大陆'}
           ])
         </script>
   ```

