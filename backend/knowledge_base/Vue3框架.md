#   Vue3框架

- 2020年9月18日，`Vue.js`发布版`3.0`版本，代号：`One Piece`（n
- 官方发版地址：[Release v3.0.0 One Piece · vuejs/core](https://github.com/vuejs/core/releases/tag/v3.0.0)
- 性能的提升
  - 打包大小减少`41%`。
  - 初次渲染快`55%`, 更新渲染快`133%`。
  - 内存减少`54%`。


- 1.2.【 源码的升级】

  ​	使用     `Proxy`代替`defineProperty`实现响应式。

  ​	重写虚拟     `DOM`的实现和`Tree-Shaking`。

- `Vue3`可以更好的支持`TypeScript`。

## 1 Vue3创建

### 1.1 基于vue-cli创建

利用wedpack创建脚手架

点击查看[官方文档](https://cli.vuejs.org/zh/guide/creating-a-project.html#vue-create)

> 备注：目前`vue-cli`已处于维护模式，官方推荐基于 `Vite` 创建项目。

```powershell
## 查看@vue/cli版本，确保@vue/cli版本在4.5.0以上
vue --version

## 安装或者升级你的@vue/cli 
npm install -g @vue/cli

## 执行创建命令
vue create vue_test

##  随后选择3.x
##  Choose a version of Vue.js that you want to start the project with (Use arrow keys)
##  > 3.x
##    2.x

## 启动
cd vue_test
npm run serve
```

### 1.2 基于vite创建(推荐)

`vite` 是新一代前端构建工具，官网地址：[https://vitejs.cn](https://vitejs.cn/)

`vite`能实现**极速的启动**服务。

- 具体操作如下（点击查看[官方文档](https://cn.vuejs.org/guide/quick-start.html#creating-a-vue-application)）

```bash
## 创建命令
npm create vue@latest
```

总结：

- `Vite` 项目中，`index.html` 是项目的入口文件，在项目最外层。
- 加载`index.html`后，`Vite` 解析 `<script type="module" src="xxx">` 指向的`JavaScript`。
- `Vue3`**中是通过 **`createApp` 函数创建一个应用实例。

### 1.3 vue项目文件

node-modoules               项目依赖模块

public                                 静态资源目录

​	index.html                 项目主HTML文件，Vue应用的挂载点

​	favion.ico                   网站图标

src                                       源代码目录

​	apis                             API接口

​	assets                         静态资源（图片、字体图标、全局样式表）

​	components              可复用Vue组件

​	composables             公共组件函数

​	layouts                       布局组件

​	plugins                       插件

​	router                         路由

​	store                           Vuex状态管理

​	styles                          全局样式

​	utils                            工具函数

​	views                          页面组件

​	APP.vue                      根组件

​	main.js                       应用入口文件（创建Vue实例，引入全局插件、挂载根组件到DOM）

.gitignore                            Git忽略

package.json                     项目配置和依赖

babel.config.js                   Babel配置（Babel转译配置，预设插件配置）

vite.config.js                       Vue配置文件（这里是vite配置）

tsconfig.json                      TypeScript配置



### 1.4 Vue框架运行原理

1、应用实例（实例对象）：

​	每个Vue应用都是通过`createAPP`创建一个新应用实例

```javascript
import { createAPP } from 'vue'      //创建应用（造花盆）
//在Vue项目中，有且仅有一个Vue实例对象
const app = createAPP({
   //根组件选项 
})
```

2、根组件：APP

```javascript
import { createAPP } from 'vue'
import APP from './APP.vue'     //引入根组件（花的根）

const app = createAPP(APP)
```

3、挂载应用

实例对象必须再调用了`mount()`方法才能渲染出来

```javascript
import { createAPP } from 'vue'
import APP from './APP.vue'     //引入根组件

const app = createAPP(APP)

app.mount('#app')              //挂载到index.html中的<div id='app'></div>（将花插入花盆）
```

可以直接被浏览器执行的文件：

​	1、HTML

​	2、CSS

​	3、JavaScript

​	4、图片

4、使用构建工具（wedpack、vite等）实现打包、发布等操作。vue文件的代码最终都会被编译成main.js文件，所以在index.html还会引入main.js

```html
<div id='app'></div>                              <!-- 花盆摆放的位置 -->
<script tpye="module" src="/src/main.js"></script>
```

## 2 Vue3语法

### 2.1 两种API

- `Vue2`的`API`设计是`Options`（配置）风格的。
- `Vue3`的`API`设计是`Composition`（组合）风格的。

1. Options API 的弊端

   `Options`类型的 `API`，数据、方法、计算属性等，是**分散**在：`data`、`methods`、`computed`中的，若想新增或者修改一个需求，就需要分别修改：`data`、`methods`、`computed`，不便于维护和复用。

2. Composition API 的优势

   可以用函数的方式，更加优雅的组织代码，让相关功能的代码更加有序的**组织在一起**。

### 2.2 setup 概述

`setup`是`Vue3`中一个新的配置项，值是一个函数，它是 `Composition API` **“表演的舞台**_**”**_，组件中所用到的：数据、方法、计算属性、监视......等等，均配置在`setup`中。

#### 2.2.1setup的基本使用

1、特点如下：

- `setup`函数返回的对象中的内容，可直接在模板中使用。

- `setup`中访问`this`是`undefined`。

- `setup`函数会在`beforeCreate`之前调用，它是“领先”所有**钩子**执行的。

  ```vue
  <script lang="ts">
    export default {
      name:'Person',
      setup(){
        // 数据，原来写在data中（注意：此时的name、age、tel数据都不是响应式数据）
        let name = '张三'
        let age = 18
        let tel = '13888888888'

        // 方法，原来写在methods中
        function changeName(){}
        function changeAge(){}
        function showTel(){}

        // 返回一个对象，对象中的内容，模板中可以直接使用
        return {name,age,tel,changeName,changeAge,showTel}
      }
    }
  </script>
  ```

2、setup 的返回值：

- 若返回一个**对象**：则对象中的：属性、方法等，在模板中均可以直接使用**（重点关注）。**

- 若返回一个**函数**：则可以自定义渲染内容，代码如下：

  ```js
  setup(){
    return ()=> '你好啊！'
  }
  ```

3、setup 与 Options API 的关系：

- `Vue2` 的配置（`data`、`methos`......）中**可以访问到** `setup`中的属性、方法。
- 但在`setup`中**不能访问到**`Vue2`的配置（`data`、`methos`......）。
- 如果与`Vue2`冲突，则`setup`优先。

#### 2.2.2 **setup 语法糖**

1. `setup`函数有一个语法糖，这个语法糖，可以让我们把`setup`**独立**出去，代码如下：

- ```vue
  <script lang="ts">
    export default {
      name:'Person',
    }
  </script>

  <!-- 下面的写法是setup语法糖 -->
  <script setup lang="ts">
    let name = '张三'
    let age = 18
    let tel = '13888888888'

    function changName(){}
    function changAge(){}
    function showTel(){}
  </script>
  ```


2. **扩展**：上述代码，还需要编写一个不写`setup`的`script`标签，去指定组件名字，比较麻烦，我们可以借助`vite`中的插件简化
   第一步：`npm i vite-plugin-vue-setup-extend -D`

   第二步：在`vite.config.ts`引入

- ```jsx
  import { defineConfig } from 'vite'
  import VueSetupExtend from 'vite-plugin-vue-setup-extend'

  export default defineConfig({
    plugins: [ VueSetupExtend() ]
  })
  ```


​      第三步：`<script setup lang="ts" name="Person">`直接在标签上写名字，就不需要单独写一个`<script>`

​      标签写名字

### 2.3 响应式数据

#### 2.3.1 ref创建基本类型的响应式数据

在Vue2中data的数据直接就是响应式，但setup不是，所以需要使用ref创建

- **返回值：**一个`RefImpl`的实例对象，简称`ref对象`或`ref`，`ref`对象的`value`**属性是响应式的**。
- **注意点：**
  - `JS`中操作数据需要：`xxx.value`，渲染时不需要`.value`，直接使用即可。
  - 对于`let name = ref('张三')`来说，`name`不是响应式的，`name.value`是响应式的。

```vue
</template>
    //模板中不需要加value 
</template>
<script setup lang="ts" name="Person">
  import {ref} from 'vue'                           //第一步：引入ref
  
  let name = ref('张三')                            //第二步：包裹数据
  let age = ref(18)
  let tel = '13888888888'

                             //在下面操作时，都需要：数据.value，否则在下面就不是响应式数据
  function changeName(){
    name.value = '李四'
    console.log(name.value)
  }
  function showTel(){
    alert(tel)
  }
</script>
```

#### 2.3.2 reactive创建对象响应式数据

- **作用：**定义一个**响应式对象**（基本类型不要用它，要用`ref`，否则报错）
- **语法：**`let 响应式对象= reactive(源对象)`。
- **返回值：**一个`Proxy`的实例对象，简称：响应式对象。
- 注意点：`reactive`定义的响应式数据是“深层次”的。

```vue
<template>
    //模板中不需要加value 
</template>

<script lang="ts" setup name="Person">
import { reactive } from 'vue'                            //第一步：调用reactive

// 数据
let car = reactive({ brand: '奔驰', price: 100 })         //第二步：在对象/数组包裹
let games = reactive([
  { id: 'ahsgdyfa01', name: '英雄联盟' },
  { id: 'ahsgdyfa02', name: '王者荣耀' },
  { id: 'ahsgdyfa03', name: '原神' }
])

function changeCarPrice() {
  car.price += 10
}
function changeFirstGame() {
  games[0].name = '流星蝴蝶剑'                              //下面操作，不需要额外加什么
}
</script>
```

#### 2.3.3 ref 创建对象响应式数据

- 其实`ref`接收的数据可以是：**基本类型**、**对象类型**。
- 若`ref`接收的是对象类型，内部其实也是调用了`reactive`函数。

```vue
<script lang="ts" setup name="Person">
import { ref } from 'vue'

let car = ref({ brand: '奔驰', price: 100 })    //用法与基本类型响应式一样
let games = ref([
  { id: 'ahsgdyfa01', name: '英雄联盟' },
  { id: 'ahsgdyfa02', name: '王者荣耀' },
  { id: 'ahsgdyfa03', name: '原神' }
])

function changeCarPrice() {
  car.value.price += 10                     
}
function changeFirstGame() {
  games.value[0].name = '流星蝴蝶剑'      //注意：索引号位置
}
</script>
```

#### 2.3.4 ref 对比 reactive

宏观角度看：

> 1. `ref`用来定义：**基本类型数据**、**对象类型数据**；
> 2. `reactive`用来定义：**对象类型数据**。

- 区别：

> 1. `ref`创建的变量必须使用`.value`（可以使用`volar`插件自动添加`.value`）。
>
>    <img src="D:/Wed-dev/%E8%B5%84%E6%96%99/images/%E8%87%AA%E5%8A%A8%E8%A1%A5%E5%85%85value.png" alt="自动补充value" style="zoom:50%;border-radius:20px" /> 
>
> 2. `reactive`重新分配一个新对象，会**失去**响应式（可以使用`Object.assign`去整体替换）。

- 使用原则：

> 1. 若需要一个基本类型的响应式数据，必须使用`ref`。
> 2. 若需要一个响应式对象，层级不深，`ref`、`reactive`都可以。
> 3. 若需要一个响应式对象，且层级较深，推荐使用`reactive`。

#### 2.3.5 toRefs 与 toRef

- 作用：将一个响应式对象中的每一个属性，转换为`ref`对象。
- 备注：`toRefs`与`toRef`功能一致，但`toRefs`可以批量转换。
- 语法如下：

```vue
<template>
 	//模板中不需要加value 
</template>

<script lang="ts" setup name="Person">
  import {ref,reactive,toRefs,toRef} from 'vue'

  // 数据
  let person = reactive({name:'张三', age:18, gender:'男'})
	
  // 通过toRefs将person对象中的n个属性批量取出，且依然保持响应式的能力
  let {name,gender} =  toRefs(person)
	
  // 通过toRef将person对象中的gender属性取出，且依然保持响应式的能力
  let age = toRef(person,'age')

  // 方法
  function changeName(){
    name.value += '~'
  }
  function changeAge(){
    age.value += 1
  }
  function changeGender(){
    gender.value = '女'
  }
</script>
```

### 2.4 computed计算属性

作用：根据已有数据计算出新数据（和`Vue2`中的`computed`作用一致）。

```vue
<script setup lang="ts" name="App">
  import {ref,computed} from 'vue'         //第一步：引入computed

  let firstName = ref('zhang')
  let lastName = ref('san')

  // 计算属性——既读取又修改
  let fullName = computed({              //第二步：对数据进行计算
    // 读取
    get(){
      return firstName.value + '-' + lastName.value
    },
    // 修改
    set(val){
      firstName.value = val.split('-')[0]
      lastName.value = val.split('-')[1]
    }
  })

  function changeFullName(){               //上述都不要，返回这个
    fullName.value = 'li-si'
  } 
</script>
```

### 2.5 watch

- 作用：监视数据的变化（和`Vue2`中的`watch`作用一致）
- 特点：`Vue3`中的`watch`**只能**监视以下四种数据：

> 1. `ref`定义的数据。
> 2. `reactive`定义的数据。
> 3. 函数返回一个值（`getter`函数）。
> 4. 一个包含上述内容的数组。

我们在`Vue3`中使用`watch`的时候，通常会遇到以下几种情况：

#### * 情况一

监视`ref`定义的【**基本类型**】数据：直接写数据名即可，监视的是其`value`值的改变。

```vue
<script lang="ts" setup name="Person">
  import {ref,watch} from 'vue'
    
  let sum = ref(0)
  function changeSum(){
    sum.value += 1
  }
  // 监视，情况一：监视【ref】定义的【基本类型】数据
  const stopWatch = watch(sum,(newValue,oldValue)=>{      //注意：被监视的数据没有.value
    if(newValue >= 10){
      stopWatch()           //解除监视
    }
  })
</script>
```

#### * 情况二

监视`ref`定义的【**对象类型**】数据：直接写数据名，监视的是对象的【地址值】，若想监视对象内部的数据，要手动开启深度监视。

> 注意：
>
> - 若修改的是`ref`定义的对象中的属性，`newValue` 和 `oldValue` 都是新值，因为它们是同一个对象。
> - 若修改整个`ref`定义的对象，`newValue` 是新值， `oldValue` 是旧值，因为不是同一个对象了。

```vue
<script lang="ts" setup name="Person">
  import {ref,watch} from 'vue'
  
  let person = ref({
    name:'张三',
    age:18
  })
  /* 
    监视的是对象的地址值，若想监视对象内部属性的变化，需要手动开启深度监视
    watch的第一个参数是：被监视的数据
    watch的第二个参数是：监视的回调
    watch的第三个参数是：配置对象（deep、immediate等等.....） 
  */
  watch(person,(newValue,oldValue)=>{
    console.log('person变化了',newValue,oldValue)
  },{deep:true})
  
</script>
```

配置对象：

​	deep：深度监视

​	immediate：在侦听器创建时立即出发回调，响应式数据变化之后继续执行回调

#### *  情况三

监视`reactive`定义的【对象类型】数据，且默认开启了**深度监视**。

```vue
<script lang="ts" setup name="Person">
  import {reactive,watch} from 'vue'
  
  let person = reactive({
    name:'张三',
    age:18
  })
  
  // 监视，情况三：监视【reactive】定义的【对象类型】数据，且默认是开启深度监视的
  watch(person,(newValue,oldValue)=>{
    console.log('person变化了',newValue,oldValue)
  })
</script>
```

#### * 情况四

监视`ref`或`reactive`定义的【对象类型】数据中的**某个属性**，注意点如下：

1. 若该属性值**不是**【对象类型】，需要写成函数形式。
2. 若该属性值是**依然**是【对象类型】，可直接编，也可写成函数，建议写成函数。

结论：监视的要是对象里的属性，那么最好写函数式，注意点：若是对象监视的是地址值，需要关注对象内部，需要手动开启深度监视。

```vue
<script lang="ts" setup name="Person">
	//情况四：监视响应式对象中的某个属性，且该属性是对象类型的，可以直接写，也能写函数，更推荐写函数
	
	watch(()=>person.name,(newValue,oldValue)=>{
	  console.log('person.car变化了',newValue,oldValue)
	},{deep:true})
</script>
```

#### * 情况五

监视上述的多个数据

```vue
<script lang="ts" setup name="Person">
  //情况五：监视上述的多个数据
    
  watch([()=>person.name,person.car],(newValue,oldValue)=>{    //name、car可写函数、写可直接写
    console.log('person.car变化了',newValue,oldValue)
  },{deep:true})
</script>
```

### 2.6 watchEffect

- 官网：立即运行一个函数，同时响应式地追踪其依赖，并在依赖更改时重新执行该函数。

- `watch`对比`watchEffect`

  > 1. 都能监听响应式数据的变化，不同的是监听数据变化的方式不同
  > 2. `watch`：要明确指出监视的数据
  > 3. `watchEffect`：不用明确指出监视的数据（函数中用到哪些属性，那就监视哪些属性）。

- 示例代码：

  ```vue
  <script lang="ts" setup name="Person">
    import {ref,watch,watchEffect} from 'vue'
   
    let temp = ref(0)
    let height = ref(0)

    // 用watch实现，需要明确的指出要监视：temp、height
    watch([temp,height],(value)=>{})

    // 用watchEffect实现，不用指名点姓
    const stopWtach = watchEffect(()=>{})
  </script>
  ```

### 2.7 标签的 ref 属性

作用：用于注册模板引用。

> - 用在普通`DOM`标签上，获取的是`DOM`节点。
> - 用在组件标签上，获取的是组件实例对象。

1. 用在普通`DOM`标签上：

   ```vue
   <template>
       <h1 ref="title1">尚硅谷</h1>
       <input type="text" ref="inpt">   //第一步：添加ref属性
   </template>

   // 通过id获取元素
   const t1 = document.getElementById('title1')    //相当于ID属性    
   ```


2. 用在组件标签上：

   父组件：

   ```vue
   <template>
     <Person ref="ren"/>
   </template>
   <script lang="ts" setup name="App">
     import Person from './components/Person.vue'
     import {ref} from 'vue'

     let ren = ref()
     function test(){
       console.log(ren.value.name)
       console.log(ren.value.age)
     }
   </script>
   ```

   子组件：

   子组件Person.vue中要使用defineExpose暴露内容 

   ```vue
   <script lang="ts" setup name="Person">
     import {ref,defineExpose} from 'vue'
   	
     let name = ref('张三')
     let age = ref(18)
    
     // 使用defineExpose将组件中的数据交给外部
     defineExpose({name,age})
   </script>
   ```

### 2.8 props

> ```js
> // 定义一个接口，限制每个Person对象的格式
> export interface PersonInter {
>  id:string,
>  name:string,
>     age:number
>    }
>    
> // 定义一个自定义类型Persons
> export type Persons = Array<PersonInter>
> ```
>
> `App.vue`中代码：
>
> ```vue
> <template>
> 	<Person :list="persons"/>
> </template>
>   
> <script lang="ts" setup name="App">
> import Person from './components/Person.vue'
> import {reactive} from 'vue'
> import {type Persons} from './types'
>   
> let persons = reactive<Persons>([
>   {id:'e98219e12',name:'张三',age:18},
>   {id:'e98219e13',name:'李四',age:19},
>   {id:'e98219e14',name:'王五',age:20}
> ])
> </script>
>   
> ```
>
> `Person.vue`中代码：
>
> ```vue
> <template>
> <div class="person">
>  <ul>
>      <li v-for="item in list" :key="item.id">
>         {{item.name}}--{{item.age}}
>       </li>
>     </ul>
>    </div>
>    </template>
>   
> <script lang="ts" setup name="Person">
> import {defineProps} from 'vue'
> import {type PersonInter} from '@/types'
>   
>   // 第一种写法：仅接收
> // const props = defineProps(['list'])
>   
>   // 第二种写法：接收+限制类型
> // defineProps<{list:Persons}>()
>   
>   // 第三种写法：接收+限制类型+指定默认值+限制必要性
> let props = withDefaults(defineProps<{list?:Persons}>(),{
>      list:()=>[{id:'asdasg01',name:'小猪佩奇',age:18}]
>   })
>    console.log(props)
>   </script>
> ```

### 2.9 生命周期

- `Vue2`的生命周期

  > 创建阶段：`beforeCreate`、`created`
  >
  > 挂载阶段：`beforeMount`、`mounted`
  >
  > 更新阶段：`beforeUpdate`、`updated`
  >
  > 销毁阶段：`beforeDestroy`、`destroyed`

- `Vue3`的生命周期

  > 创建阶段：`setup`
  >
  > 挂载阶段：`onBeforeMount`、`onMounted`
  >
  > 更新阶段：`onBeforeUpdate`、`onUpdated`
  >
  > 卸载阶段：`onBeforeUnmount`、`onUnmounted`

- 常用的钩子：`onMounted`(挂载完毕)、`onUpdated`(更新完毕)、`onBeforeUnmount`(卸载之前)

### 2.10 自定义hook

- 什么是`hook`？—— 本质是一个函数，把`setup`函数中使用的**组合式API**进行了封装，类似于`vue2.x`中的`mixin`。
- 自定义`hook`的优势：复用代码, 让`setup`中的逻辑更清楚易懂。

主要是基于业务逻辑的函数拆分：

1. 业务a、业务b……模板：

   `useXXX.js`

   ```js
   import {ref,onMounted} from 'vue'

   //需要向外暴露
   export default function(){
     //数据
     //方法
     //计算属性
     //钩子函数
       
     return {数据1，数据2，方法1，计算属性1……}
   }		
   ```


2. 在组件中组合使用：

   ```vue
   <template>
     。。。   //3. 使用数据
   </template>

   <script setup lang="ts">
     //1. 先引入封装好的两个hooks
     import useSum from './hooks/useSum'      
     import useDog from './hooks/useDog'
     //2. 通过解构里面的数据（不仅是数据，方法、计算属性……）
     let {sum,increment,decrement} = useSum() 
     let {dogList,getDog} = useDog()
   </script>
   ```

   > 业务模块不仅可以在组件中使用，也可以在其他文件中使用，其调用方法都是这个样子


## 3 路由

1. 安装router

   ```bash
   npm install vue-router
   ```


2. 新建文件夹views(页面组件)、键入一级路由所指向的页面

### 3.1 路由的基本配置

- 路由配置文件代码如下：

  ```js
  import {createRouter,createWebHistory} from 'vue-router'  //第一步：引入路由
  import Home from '@/pages/Home.vue'                       //第三步：引入各组件
  import News from '@/pages/News.vue'

  const router = createRouter({                             //第二步：创建路由器
  	history:createWebHistory(),
  	routes:[               //路由：[{path:路径,component:组件名},{...},...]                
  		{
  			path:'/home',
  			component:Home
  		},
  		{
  			path:'/about',
  			component:About
  		}
  	]
  })
  export default router                                      //第四步：（统一）暴露路由
  ```


- `main.ts`代码如下：

  ```js
  import router from './router/index'                        //第五步：引入路由并挂载
  app.use(router)                  //使用路由
  ```


- `App.vue`代码如下

  ```vue
  <template>
    <div class="app">
      <h2 class="title">Vue路由测试</h2>
      <!-- 导航区 -->
      <div class="navigate">                  
        <RouterLink to="/home" active-class="active">首页</RouterLink>
        <RouterLink to="/news" active-class="active">新闻</RouterLink>
      </div>
      <!-- 展示区 -->
      <div class="main-content">
        <RouterView></RouterView>                      //第七步：在展示的位置写入占位标签
      </div>
    </div>
  </template>

  <script lang="ts" setup name="App">
    import {RouterLink,RouterView} from 'vue-router'      //第六步：在展示的文件中引入RouterLink
  </script>
  ```

**路由组件**与普通组件：

​	需要有路由的组件就叫路由组件，普通组件没有路由

**注意：**

> 1. 路由组件通常存放在`pages` 或 `views`文件夹，一般组件通常存放在`components`文件夹。
> 2. 通过点击导航，视觉效果上“消失” 了的路由组件，默认是被**卸载**掉的，需要的时候再去**挂载**。

### 3.2 路由器工作模式

1. `history`模式

   > 优点：`URL`更加美观，不带有`#`，更接近传统的网站`URL`。
   >
   > 缺点：后期项目上线，需要服务端配合处理路径问题，否则刷新会有`404`错误。
   >
   > ```js
   > const router = createRouter({
   >   	history:createWebHistory(), //history模式
   > })
   > ```

2. `hash`模式

   > 优点：兼容性更好，因为不需要服务器端处理路径。
   >
   > 缺点：`URL`带有`#`不太美观，且在`SEO`优化方面相对较差。
   >
   > ```js
   > const router = createRouter({
   >   	history:createWebHashHistory(), //hash模式
   > })
   > ```

### 3.3 to的两种写法

```vue
<!-- 第一种：to的字符串写法 -->
<router-link active-class="active" to="/home">主页</router-link>

<!-- 第二种：to的对象写法 -->
<router-link active-class="active" :to="{path:'/home'}">Home</router-link>
```

### 3.4 命名路由

作用：可以简化路由跳转及传参

给路由规则**命名**：

```js
routes:[
  {
    name:'zhuye',
    path:'/home',
    component:Home
  }
]
```

跳转路由：

```vue
<!--简化前：需要写完整的路径（to的字符串写法） -->
<router-link to="/news/detail">跳转</router-link>

<!--简化后：直接通过名字跳转（to的对象写法配合name属性） -->
<router-link :to="{name:'guanyu'}">跳转</router-link>
```

### 3.5 嵌套路由

1. 编写`News`的子路由：`Detail.vue`

2. 配置路由规则，使用`children`配置项：

   ```ts
   routes:[
   	{
   		name:'xinwen',
   		path:'/news',
   		component:News,
   		children:[                    //children追加路由
   			{
   				name:'xiang',
   				path:'detail',       //子集路由不需要加斜杠
   				component:Detail
   			}
   		]
   	}
   ```

3. 跳转路由（记得要加完整路径）：

   ```vue
   <router-link to="/news/detail">xxxx</router-link>
   <!-- 或 -->
   <router-link :to="{path:'/news/detail'}">xxxx</router-link>
   ```


### 3.6 Vue 路由组件引入方式

这两种引入方式可以混合使用，也可以嵌套

#### 3.6.1 **同步引入（直接导入）**

```javascript
component: Home
```

**工作原理：**

- 在应用初始化时**立即加载**组件
- 组件代码会打包到主 JavaScript 文件中
- 页面首次加载时就包含该组件的所有代码

#### 3.6.1 **异步引入（懒加载）**

```javascript
component: () => import('@/views/login/index.vue')
```

**工作原理：**

- 在访问该路由时**动态加载**组件
- 组件代码会被分割成独立的 chunk 文件
- 按需加载，减少初始包体积

### 3.7 路由传参

二级路由跳转后，呈现页面结构相同，只是让值不一样，就可以通过传递参数改变值

#### 3.7.1 query参数

1. （一级路由）传递参数

   a、跳转并携带query参数（to的字符串写法)

   ```vue
   <router-link :to="`/news/detail?id=${news.id}&title=${news.title}&conten=${news.conten}`">
   	点击跳转
   </router-link>
   ```

   b、跳转并携带query参数（to的对象写法）

   ```vue
   <RouterLink
     :to="{
       path:'/news/detail',
       query:{                      //利用query传参
         id:news.id,
         title:news.title,
         content:news.content
       }
     }"
   >
   	点击跳转
   </RouterLink>
   ```

2. （在二级路由组件中）接收参数：

   ```js
   import {useRoute} from 'vue-router'
   const route = useRoute()
   const {query} = route
   ```

   结束后就可以直接在这个组件中使用

   ```vue
   <ul class="news-list">
   	<li>编号：{{ query.id }}<li>
   	<li>标题：{{ query.title }}<li>
   	<li>内容：{{ query.content }}<li>
   <ul>
   ```

#### 3.7.2 params参数

1. 传递参数

   a、跳转并携带params参数（to的字符串写法）

   ```vue
   <RouterLink :to="`/news/detail/${news.id}/${news.title}/${news.conten}`">					{{news.title}}
   </RouterLink>
   ```

   b、跳转并携带params参数（to的对象写法）

   ```vue
   <RouterLink 
     :to="{
       name:'xiang',                 //要用name跳转
       params:{
         id:news.id,
         title:news.title,
         content:news.title
       }
     }"
   >
     {{news.title}}
   </RouterLink>
   ```

2. 接收参数：

   ```js
   import {useRoute} from 'vue-router'
   const route = useRoute()
   // 打印params参数
   console.log(route.params)
   ```

> 备注1：传递`params`参数时，若使用`to`的对象写法，必须使用`name`配置项，不能用`path`。
>
> **备注2**：传递`params`参数时，需要提前在规则中**占位**（在创建路由文件中的上面名字的路由path后）。

#### 3.7.3 路由的props配置

有三种写法

作用：让路由组件更方便的收到参数（可以将路由参数作为`props`传给组件）

```js
{
	name:'xiang',
	path:'detail/:id/:title/:content',
	component:Detail,

  // 1、props的对象写法，作用：把对象中的每一组key-value作为props传给Detail组件
  // props:{a:1,b:2,c:3}, 

  // 2、props的布尔值写法，作用：把收到了每一组  params  参数，作为props传给Detail组件
  // props:true
  
  // 3、props的函数写法，作用：把返回的对象中每一组key-value作为props传给Detail组件
  //props(route){
  //  return route.query
  //}
}
```

### 3.8 replace属性

1. 作用：控制路由跳转时操作浏览器**历史记录**的模式。

2. 浏览器的历史记录有两种写入方式：分别为```push```和```replace```：

   - ```push```是追加历史记录（默认值）。
   - `replace`是替换当前记录（就是当他点击跳转了就不能返回上一个记录）。

3. 开启`replace`模式：

   ```vue
   <RouterLink replace .......>News</RouterLink>     //导航区
   ```

### 3.9 编程式导航

编程式导航：与**声明式导航**（使用`<router-link>`标签）相对应，脱离`<RouterLink>`实现导航，因为<RouterLink>在HTML中解析出来就是<a>，意味着只能当作链接才能被跳转。

路由组件的两个重要的属性：`$route`和`$router`变成了两个`hooks`

1. `$router `和`$route `的区别

   `$router`

   - **路由器实例**：包含了整个路由系统的导航方法和配置信息
   - **全局唯一**：整个应用只有一个`$router`实例
   - **用于导航操作**：提供跳转、前进、后退等方法

   `$route`

   - **当前路由对象**：包含当前激活路由的信息
   - **响应式**：路由变化时会自动更新
   - **只读属性**：用于获取当前路由的参数、查询参数、路径等信息

2. 模板中的 $ 符号含义:

   > 在 Vue 2 中，$router 自动注入到组件实例
   >
   > 在组合式 API 中，需要显式引入

   ```html
   <!-- 在模板中，$router 是组件实例的属性 -->
   <li><a href="javascript:;" @click="$router.push('/login')">请先登录</a></li>

   <!-- 如果没有 $，Vue 会在当前组件的数据和方法中查找 -->
   <li><a href="javascript:;" @click="router.push('/login')">请先登录</a></li>
   <!-- 这会报错，因为组件中没有定义 router 数据或方法 -->
   ```

#### 3.9.1核心方法

1. push() - 导航到新页面

   ```js
   // 字符串路径
   this.$router.push('/home')

   // 对象形式
   this.$router.push({ path: '/home' })

   // 命名路由
   this.$router.push({ name: 'user', params: { id: 123 } })

   // 带查询参数
   this.$router.push({ path: '/search', query: { keyword: 'vue' } })

   // 组合使用
   this.$router.push({
     name: 'user',
     params: { id: 123 },
     query: { tab: 'profile' }
   })
   ```

2. replace() - 替换当前页面

   ```js
   // 不会在历史记录中添加新记录
   this.$router.replace('/home')
   this.$router.replace({ path: '/home' })
   ```


3. go() - 在历史记录中前进/后退

   ```js
   // 前进一条记录
   this.$router.go(1)

   // 后退一条记录
   this.$router.go(-1)

   // 后退到首页（假设当前在第三页）
   this.$router.go(-2)
   ```

4. back() - 后退

   ```js
   this.$router.back()
   ```

5. forward() - 前进

   ```javascript
   this.$router.forward()
   ```


#### 3.9.2 实际应用

1. 基本导航控制

   ```javascript
   export default {
     methods: {
       // 跳转到用户详情页
       goToUserDetail(userId) {
         this.$router.push({
           name: 'userDetail',
           params: { id: userId }
         })
       },
       
       // 搜索功能
       search(keyword) {
         this.$router.push({
           path: '/search',
           query: { q: keyword }
         })
       },
       
       // 替换当前页面（用于登录后跳转）
       redirectToDashboard() {
         this.$router.replace('/dashboard')
       },
       
       // 返回上一页
       goBack() {
         this.$router.go(-1)
       }
     }
   ```


2. 路由传参和接收

   ```javascript
   // 发送参数
   this.$router.push({
     name: 'article',
     params: { 
       id: articleId,
       category: 'tech'
     },
     query: {
       from: 'homepage',
       timestamp: Date.now()
     }
   })

   // 接收参数
   export default {
     mounted() {
       // 获取 params 参数
       const articleId = this.$route.params.id
       const category = this.$route.params.category
       
       // 获取 query 参数
       const from = this.$route.query.from
       const timestamp = this.$route.query.timestamp
       
       this.loadArticle(articleId)
     }
   }
   ```

3. 导航守卫中的编程式导航

   ```javascript
   // 路由配置中
   const router = new VueRouter({
     routes: [{
       path: '/admin',
       component: Admin,
       beforeEnter: (to, from, next) => {
         if (!isAuthenticated()) {
           // 未认证时重定向到登录页
           next('/login')
         } else {
           next()
         }
       }
     }]
   })
   ```

#### 3.9.3 最佳实践和注意事项

1. 参数处理

   ```javascript
   // 推荐：使用命名路由和 params
   this.$router.push({ 
     name: 'product', 
     params: { id: productId } 
   })

   // 注意：使用 path 时 params 会被忽略
   this.$router.push({ 
     path: '/product/123', 
     params: { id: 456 } // 这个 params 会被忽略
   })
   ```


2. 错误处理

   ```javascript
   // 添加错误处理
   this.$router.push('/some-path').catch(err => {
     // 处理导航错误
     if (err.name !== 'NavigationDuplicated') {
       console.error('导航失败:', err)
     }
   })
   ```


3. 条件导航

   ```javascript
   // 根据条件决定是否导航
   navigateIfAllowed() {
     if (this.hasPermission) {
       this.$router.push('/target-page')
     } else {
       this.showPermissionDeniedMessage()
     }
   }
   ```


4. 组合使用

   ```javascript
   // 复杂的导航逻辑
   handleFormSubmit() {
     this.submitForm().then(() => {
       // 提交成功后替换当前页面
       this.$router.replace({
         name: 'success',
         query: { 
           submitted: 'true',
           timestamp: new Date().getTime()
         }
       })
     }).catch(error => {
       // 失败时停留在当前页面
       console.error('提交失败:', error)
     })
   }
   ```

### 3.10 重定向

1. 作用：将特定的路径（404），重新定向到已有路由。

2. 具体编码：

   ```js
   {
       path:'/XXX',
       redirect:'/about'                //将原来的content变为redirect
   }
   ```

## 4 pinia

**pinia官网:https://pinia.web3doc.top/**

pinia也是集中式管理状态容器（**全局使用**）,类似于Vue2的vuex。但是核心概念没有mutation、modules,使用方式参照官网

**在storts文件创建pinia：**

1. 新建index.js大仓库、modules文件夹内若干小仓库（user.js，counter.js）
2. 在main.js中引入
3. 在index.js中创建大仓库：


4. 创建小仓库：

   ```ts
   import { defineStore } from 'pinia'       //定义小仓库

   export const useUserStore = defineStore('仓库名',() => {
       存储内容  
       return {对存储内容进行输出}
   }）                
   //注意：小仓库的内容在大仓库一并暴露    
   ```


5. 在组件中引入使用：

   ```ts
   import { useUserStore from } '@/storts'

   const userStore = useUserStore()            //获取仓库存储内容

    ……useUserStort.Token……                    //使用（进行更新修改等等）
   ```

### 4.1 搭建 pinia 环境

第一步：`npm install pinia`

第二步：操作`src/main.ts`

```ts
/* 引入createPinia，用于创建pinia */
import { createPinia } from 'pinia'

/* 创建pinia */
const pinia = createPinia()       //此处的pinia可替换为state

/* 使用插件 */{}
app.use(pinia)              //或者可以直接暴露仓库：export default pinia   
```

此时开发者工具中已经有了`pinia`选项

### 4.2 存储+读取数据

`Store`文件是一个保存：**状态**、**业务逻辑** 的实体，每个组件都可以**读取**、**写入**它。

#### 4.2.1 选项式API格式

1. 它有三个概念：`state`、`getter`、`action`，相当于组件中的： `data`、 `computed` 和 `methods`。

2. 具体编码：`src/store/talk.ts`

   ```js
   import {defineStore} from 'pinia'                      //第一步： 引入defineStore用于创建store

   export const useTalkStore = defineStore('仓库名',{     // 第二步：定义并暴露一个store
     // 动作（存储方法，用于相应组件的动作(数据变化））                
     actions:{},
     // 状态（真正存储数据的地方）
     state(){
       return {
         talkList:[
           {id:'yuysada01',content:'你今天有点怪，哪里怪？怪好看的！'},
        	...
         ]
       }
     },
     // 计算
     getters:{}
   })
   ```
   > 注意：这里的仓库名，是本仓库的唯一标识

#### 4.2.2 组合式API格式

1. ```js
   import {defineStore} from 'pinia'

   export const useTalkStore = defineStore('talk',()=>{
     ...
     //里面直接写就是了，不必定义上面三个
     return {talkList,getATalk}                          //区别只是在这里：这需要retrn,上边不需要
   })
   ```

#### 4.2.3 组件中读取数据

2. ```vue
   <template>
     <li v-for="talk in talkStore.talkList" :key="talk.id"> {{ talk.content }}</li>
   </template>                                            //第四步：使用数据

   <script setup lang="ts" name="Count">
     import axios from 'axios'
     // 引入对应的useXxxxxStore	
     import {useTalkStore} from '@/store/talkList'        //第三步：引入仓库的数据talkList
     // 调用useXxxxxStore得到对应的store
     const talkStore = useTalkStore()
   </script>
   ```

### 4.3 修改数据(三种方式)

1. 第一种修改方式，直接在**组件中**修改

   ```ts
   talkStore.talkList:nsh.hovor[0].id = "yuysada11"
   ```

2. 第二种修改方式：**组件中**批量修改（使用$patch）

   ```ts
   talkStore.$patch({
     sum:999,
     school:'atguigu'
   })
   ```

3. 第三种修改方式：借助`action`(**动作**)修改（`action`中可以编写一些业务逻辑）

   ```js
   import { defineStore } from 'pinia'

   export const useCountStore = defineStore('count', {
     actions: {
       //加
       increment(value:number) {                 //第二步：接受这个n(数字型)
         if (this.sum < 10) {
           this.sum += value
         }
       },
       //减
       decrement(value:number){
         if(this.sum > 1){
           this.sum -= value
         }
       }
     }
   })
   ```

4. 组件中调用`action`即可

   ```js
   // 使用countStore
   const countStore = useCountStore()

   // 调用对应action（要先引入axios,当然上边已经引入了）                    第一步
   countStore.incrementOdd(n.value)   //increment是配置文件中的方法；传入一个n
   ```

### 4.4 storeToRefs

- 借助`storeToRefs`将`store`中的数据转为**`ref`对象**，方便在模板中使用。
- 注意：`pinia`提供的`storeToRefs`**只会**将数据做转换，而`Vue`的`toRefs`会转换`store`中数据。

```vue
<script setup lang="ts" name="Count">
  import { useCountStore } from '@/store/count'
  /* 引入storeToRefs */
  import { storeToRefs } from 'pinia'

	/* 得到countStore */
  const countStore = useCountStore()
  /* 使用storeToRefs转换countStore，随后解构 */
  const {sum} = storeToRefs(countStore)
</script>
```

### 4.5 $subscribe

通过 store 的 `$subscribe()` 方法侦听 `state` 及其变化

```ts
talkStore.$subscribe((mutate,state)=>{   //mutate：本次修改的信息；state：数据
  console.log('LoveTalk',mutate,state)
  localStorage.setItem('talk',JSON.stringify(talkList.value))
})
```

## 5. 组件通信

**`Vue3`组件通信和`Vue2`的区别：**

- 移出事件总线，使用`mitt`代替。


- `vuex`换成了`pinia`。
- 把`.sync`优化到了`v-model`里面了。
- 把`$listeners`所有的东西，合并到`$attrs`中了。
- `$children`被砍掉了。

**常见搭配形式：**

### 5.1 props

概述：`props`是使用频率最高的一种通信方式，常用与 ：**父 ↔ 子**。

- 若 **父传子**：属性值是**非函数**。
- 若 **子传父**：属性值是**函数**。

父组件：

```vue
<template>
  <div class="father">
	<h4>我的车：{{ car }}</h4>
	<h4>儿子给的玩具：{{ toy }}</h4>
	<Child :car="car" :getToy="getToy"/>
  </div>
</template>

<script setup lang="ts" name="Father">
	import Child from './Child.vue'
	import { ref } from "vue";
    
	const car = ref('奔驰')
	const toy = ref()
	function getToy(value:string){
		toy.value = value
	}
</script>
```

子组件

```vue
<template>
  <div class="child">
	<h4>我的玩具：{{ toy }}</h4>
	<h4>父给我的车：{{ car }}</h4>
	<button @click="getToy(toy)">玩具给父亲</button>
  </div>
</template>

<script setup lang="ts" name="Child">
	import { ref } from "vue";
	const toy = ref('奥特曼')
	
	defineProps(['car','getToy'])             //注意：在setup语法糖中是defineProps（编译器宏）
</script>
```

**注意：**不能直接对传入的数据进行修改

### 5.2 自定义事件

1. 概述：自定义事件常用于：**子 => 父。**
2. 注意区分好：原生事件、自定义事件。

- 原生事件：
  - 事件名是特定的（`click`、`mosueenter`等等）	
  - 事件对象`$event`: 是包含事件相关信息的对象（`pageX`、`pageY`、`target`、`keyCode`）

- 自定义事件：
  - 事件名是任意名称
  - 事件对象`$event`: 是调用`emit`时所提供的数据，可以是任意类型！！！

  `$emit` 是 Vue 组件实例的方法，用于触发自定义事件。

  `emit` 是 `<script setup>` 中通过 `defineEmits` 定义的函数，用于触发事件。

  `defineEmits` 用于在 `<script setup>` 中声明组件可以触发哪些自定义事件。

  `$event` 在模板中代表事件对象，对于自定义事件，它就是 `$emit` 的第二个参数。


- 子

  ```
  <button @click="toy">测试</button>
  const emit = defineEmits(['toy'])
  const toy = () => {
      emit(chengaToy,数据)             //注意：setup没有this,所以不能通过this.$emit传参
  }
  ```

- 父

  ```
  <SonCom @chengaToy="chengaFu"></SonCom>
  const chengaFu = (newToy) => {
      Toy.value = newToy
  }
  ```

  > ​	defineEmits方法是vue3提供的方法,不需要引入直接使用。defineEmits方法执行，传递一个数组，数组元素即为将来组件需要触发的自定义事件类型，此方执行会返回一个$emit方法用于触发自定义事件。
  >
  > ​	当事件触发的时候，事件回调内部调用$emit方法去触发自定义事件,第一个参数为触发事件类型，第二个、三个、N个参数即为传递给父组件的数据。

### 5.3 mitt

概述：与消息订阅与发布（`pubsub`）功能类似，可以实现**任意**组件间通信。

> 全局事件总线可以实现任意组件通信，在vue2中可以根据VM与VC关系推出全局事件总线。
>
> 但是在vue3中没有Vue构造函数，也就没有Vue.prototype.以及组合式API写法没有this，
>
> 那么在Vue3想实现全局事件的总线功能就有点不现实啦，如果想在Vue3中使用全局事件总线功能，使用插件mitt实现。

官网地址:https://www.npmjs.com/package/mitt

安装`mitt`

```shell
npm i mitt
```

新建文件：`src\utils\emitter.ts`

```javascript
// 引入mitt 
import mitt from "mitt";

// 创建emitter
const emitter = mitt()

/*
  // 绑定事件
  emitter.on('abc',(value)=>{
    console.log('abc事件被触发',value)
  })
  emitter.on('xyz',(value)=>{
    console.log('xyz事件被触发',value)
  })
 
  setInterval(() => {
    // 触发事件
    emitter.emit('abc',666)
    emitter.emit('xyz',777)
  }, 1000);

  setTimeout(() => {
    // 清理事件
    emitter.all.clear()
  }, 3000); 
*/

// 创建并暴露mitt
export default emitter
```

接收数据的组件中：绑定事件、同时在销毁前解绑事件：

```typescript
import emitter from "@/utils/emitter";
import { onUnmounted } from "vue";

// 绑定事件
emitter.on('send-toy',(value)=>{
  console.log('send-toy事件被触发',value)
})

onUnmounted(()=>{
  // 解绑事件
  emitter.off('send-toy')
})
```

【第三步】：提供数据的组件，在合适的时候触发事件（main.js）

```javascript
import emitter from "@/utils/emitter";

function sendToy(){
  // 触发事件
  emitter.emit('send-toy',toy.value)
}
```

**注意这个重要的内置关系，总线依赖着这个内置关系**

### 5.4 v-model

1. 概述：实现 **父↔子** 之间相互通信。

   `AtguiguInput`组件中：

   ```vue
   <template>
     <div class="box">
       <!--将接收的value值赋给input元素的value属性，目的是：为了呈现数据 -->
   	<!--给input元素绑定原生input事件，触发input事件时，进而触发update:model-value事件-->
       <input 
          type="text" 
          :value="modelValue" 
          @input="emit('update:model-value',$event.target.value)"
       >
     </div>
   </template>

   <script setup lang="ts" name="AtguiguInput">
     // 接收props
     defineProps(['modelValue'])
     // 声明事件
     const emit = defineEmits(['update:model-value'])
   </script>
   ```

2. 也可以更换`value`，例如改成`abc`

   ```vue
   <!-- 也可以更换（名字）value，例如改成abc-->
   <AtguiguInput v-model:abc="userName"/>

   <!-- 上面代码的本质如下 -->
   <AtguiguInput :abc="userName" @update:abc="userName = $event"/>
   ```

   `AtguiguInput`组件中：

   ```vue
   <template>
     <div class="box">
       <input 
          type="text" 
          :value="abc" 
          @input="emit('update:abc',$event.target.value)"
       >
     </div>
   </template>

   <script setup lang="ts" name="AtguiguInput">
     // 接收props
     defineProps(['abc'])
     // 声明事件
     const emit = defineEmits(['update:abc'])
   </script>
   ```

3. 如果`value`可以更换，那么就可以在组件标签上多次使用`v-model`

   ```vue
   <AtguiguInput v-model:abc="userName" v-model:xyz="password"/>
   ```

### 5.5 $attrs

1. 概述：`$attrs`用于实现**当前组件的父组件**，向**当前组件的子组件**通信（**祖→孙**）。

2. 具体说明：`$attrs`是一个对象，包含所有父组件传入的标签属性。

   > 注意：`$attrs`会自动排除`props`中声明的属性(可以认为声明过的 `props` 被子组件自己“消费”了)

父组件：

```vue
<template>
  <div class="father">
    <h3>父组件</h3>
		<Child :a="a" :b="b" :c="c" :d="d" v-bind="{x:100,y:200}" :updateA="updateA"/>
  </div>
</template>

<script setup lang="ts" name="Father">
	import Child from './Child.vue'
	import { ref } from "vue";
	let a = ref(1)
	let b = ref(2)
	let c = ref(3)
	let d = ref(4)

	function updateA(value){
		a.value = value
	}
</script>
```

子组件：

```vue
<template>
	<div class="child">
		<h3>子组件</h3>
		<GrandChild v-bind="$attrs"/>
	</div>
</template>

<script setup lang="ts" name="Child">
	import GrandChild from './GrandChild.vue'
</script>
```

孙组件：

```vue
<template>
	<div class="grand-child">
		<h3>孙组件</h3>
		<h4>a：{{ a }}</h4>
		<h4>b：{{ b }}</h4>
		<h4>c：{{ c }}</h4>
		<h4>d：{{ d }}</h4>
		<h4>x：{{ x }}</h4>
		<h4>y：{{ y }}</h4>
		<button @click="updateA(666)">点我更新A</button>
	</div>
</template>

<script setup lang="ts" name="GrandChild">
	defineProps(['a','b','c','d','x','y','updateA'])
</script>
```

### 5.6  `$refs` 、 ` $parent`

1. 概述：

   - `$refs`用于 ：**父→子。**
   - `$parent`用于：**子→父。**

2. 原理如下：

   | 属性      | 说明                                                     |
   | --------- | -------------------------------------------------------- |
   | `$refs`   | 值为对象，包含所有被`ref`属性标识的`DOM`元素或组件实例。 |
   | `$parent` | 值为对象，当前组件的父组件实例对象。                     |

### 5.7 provide、inject

1. 概述：实现**祖孙组件**直接通信

2. 具体使用：

   - 在祖先组件中通过`provide`配置向后代组件提供数据
   - 在后代组件中通过`inject`配置来声明接收数据

3. 具体编码：

   【第一步】父组件中，使用`provide`提供数据

   ```vue
   <template>
     <div class="father">
       <h3>父组件</h3>
       <h4>资产：{{ money }}</h4>
       <h4>汽车：{{ car }}</h4>
       <button @click="money += 1">资产+1</button>
       <button @click="car.price += 1">汽车价格+1</button>
       <Child/>
     </div>
   </template>

   <script setup lang="ts" name="Father">
     import Child from './Child.vue'
     import { ref,reactive,provide } from "vue";
     // 数据
     let money = ref(100)
     let car = reactive({
       brand:'奔驰',
       price:100
     })
     // 用于更新money的方法
     function updateMoney(value:number){
       money.value += value
     }
     // 提供数据
     provide('moneyContext',{money,updateMoney})
     provide('car',car)
   </script>
   ```

   > 注意：子组件中不用编写任何东西，是不受到任何打扰的

   【第二步】孙组件中使用`inject`配置项接受数据。

   ```vue
   <template>
     <div class="grand-child">
       <h3>我是孙组件</h3>
       <h4>资产：{{ money }}</h4>
       <h4>汽车：{{ car }}</h4>
       <button @click="updateMoney(6)">点我</button>
     </div>
   </template>

   <script setup lang="ts" name="GrandChild">
     import { inject } from 'vue';
     // 注入数据
    let {money,updateMoney} = inject('moneyContext',{money:0,updateMoney:(x:number)=>{}})
     let car = inject('car')
   </script>
   ```

### 5.9 slot

用法与Vue2基本一致

#### 5.9.1 默认插槽

```vue
父组件中：
		<template>
    	    <Category>
    	      ...
    	    </Category>
		</template>
子组件中：
        <template>
    		<slot></slot>
        </template>
```

#### 5.9.2 具名插槽

```vue
父组件中：
		<template>
    	    <Category>
    	      <template v-slot:s1>
    	        ...
    	      </template>
    	      <template #s2>
    	        ...
    	      </template>
    	    </Category>
		<template>
子组件中：
        <template>
          <slot name="s1"></slot>
          <slot name="s2"></slot>
        </template>
```

#### 5.9.3 作用域插槽

1. 理解：<span style="color:red">数据在组件的自身，但根据数据生成的结构需要组件的使用者来决定。</span>（新闻数据在`News`组件中，但使用数据所遍历出来的结构由`App`组件决定）

2. 具体编码：

   1. 具体编码：

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

   # 

## 6 其它 API

### 6.1 shallowRef 与 shallowReactive 

1. `shallowRef`

   作用：创建一个响应式数据，但只对顶层属性进行响应式处理。

   用法：

   ```js
   let myVar = shallowRef(initialValue);
   ```

   特点：只跟踪引用值的变化，不关心值内部的属性变化。

2. `shallowReactive`

   作用：创建一个浅层响应式对象，只会使对象的最顶层属性变成响应式的，对象内部的嵌套属性则不会变成响应式的

   用法：

   ```js
   const myObj = shallowReactive({ ... });
   ```

   特点：对象的顶层属性是响应式的，但嵌套对象的属性不是。

**总结**

> 通过使用 [`shallowRef()`](https://cn.vuejs.org/api/reactivity-advanced.html#shallowref) 和 [`shallowReactive()`](https://cn.vuejs.org/api/reactivity-advanced.html#shallowreactive) 来绕开深度响应。浅层式 `API` 创建的状态只在其顶层是响应式的，对所有深层的对象不会做任何处理，避免了对每一个内部属性做响应式所带来的性能成本，这使得属性的访问变得更快，可提升性能。



### 6.1 readonly 与 shallowReadonly

1. **`readonly`**

- 作用：用于创建一个对象的深只读副本。

- 用法：

- ```js
  const original = reactive({ ... });
  const readOnlyCopy = readonly(original);
  ```

- 特点：

- - 对象的所有嵌套属性都将变为只读。
  - 任何尝试修改这个对象的操作都会被阻止（在开发模式下，还会在控制台中发出警告）。

- 应用场景：

- - 创建不可变的状态快照。
  - 保护全局状态或配置不被修改。

2. **`shallowReadonly`**

- 作用：与 `readonly` 类似，但只作用于对象的顶层属性。

- 用法：

- ```js
  const original = reactive({ ... });
  const shallowReadOnlyCopy = shallowReadonly(original);
  ```

- 特点：

- - 只将对象的顶层属性设置为只读，对象内部的嵌套属性仍然是可变的。
  - 适用于只需保护对象顶层属性的场景。

### 6.3 toRaw 与 markRaw

1. `toRaw`

- 作用：用于获取一个响应式对象的原始对象， `toRaw` 返回的对象不再是响应式的，不会触发视图更新。

  > 官网描述：这是一个可以用于临时读取而不引起代理访问/跟踪开销，或是写入而不触发更改的特殊方法。不建议保存对原始对象的持久引用，请谨慎使用。

  > 何时使用？ —— 在需要将响应式对象传递给非 `Vue` 的库或外部系统时，使用 `toRaw` 可以确保它们收到的是普通对象

- 具体编码：

  ```js
  import { reactive,toRaw,markRaw,isReactive } from "vue";

  /* toRaw */
  // 响应式对象
  let person = reactive({name:'tony',age:18})
  // 原始对象
  let rawPerson = toRaw(person)
  ```


  /* markRaw */
  let citysd = markRaw([
    {id:'asdda01',name:'北京'},
    {id:'asdda02',name:'上海'},
    {id:'asdda03',name:'天津'},
    {id:'asdda04',name:'重庆'}
  ])
  // 根据原始对象citys去创建响应式对象citys2 —— 创建失败，因为citys被markRaw标记了
  let citys2 = reactive(citys)
  console.log(isReactive(person))
  console.log(isReactive(rawPerson))
  console.log(isReactive(citys))
  console.log(isReactive(citys2))
  ```

2. `markRaw`

- 作用：标记一个对象，使其**永远不会**变成响应式的。

  > 例如使用`mockjs`时，为了防止误把`mockjs`变为响应式对象，可以使用 `markRaw` 去标记`mockjs`

- 编码：

  ```js
  /* markRaw */
  let citys = markRaw([
    {id:'asdda01',name:'北京'},
    {id:'asdda02',name:'上海'},
    {id:'asdda03',name:'天津'},
    {id:'asdda04',name:'重庆'}
  ])
  // 根据原始对象citys去创建响应式对象citys2 —— 创建失败，因为citys被markRaw标记了
  let citys2 = reactive(citys)
  ```

### 6.4 customRef

作用：创建一个自定义的`ref`，并对其依赖项跟踪和更新触发进行逻辑控制。

实现防抖效果（`useSumRef.ts`）：

```typescript
import {customRef } from "vue";

export default function(initValue:string,delay:number){
  let msg = customRef((track,trigger)=>{
    let timer:number
    return {
      get(){
        track() // 告诉Vue数据msg很重要，要对msg持续关注，一旦变化就更新
        return initValue
      },
      set(value){
        clearTimeout(timer)
        timer = setTimeout(() => {
          initValue = value
          trigger() //通知Vue数据msg变化了
        }, delay);
      }
    }
  }) 
  return {msg}
}
```

组件中使用：





## 7 Vue3新组件

### 7.1 Teleport

- 什么是Teleport？—— Teleport 是一种能够将我们的**组件html结构**移动到指定位置的技术。

```html
<teleport to='body' >
    <div class="modal" v-show="isShow">
      <h2>我是一个弹窗</h2>
      <p>我是弹窗中的一些内容</p>
      <button @click="isShow = false">关闭弹窗</button>
    </div>
</teleport>
```

### 7.2 Suspense

- 等待异步组件时渲染一些额外内容，让应用有更好的用户体验 
- 使用步骤： 
  - 异步引入组件
  - 使用`Suspense`包裹组件，并配置好`default` 与 `fallback`

```tsx
import { defineAsyncComponent,Suspense } from "vue";
const Child = defineAsyncComponent(()=>import('./Child.vue'))
```

```vue
<template>
    <div class="app">
        <h3>我是App组件</h3>
        <Suspense>
          <template v-slot:default>
            <Child/>
          </template>
          <template v-slot:fallback>
            <h3>加载中.......</h3>
          </template>
        </Suspense>
    </div>
</template>
```



### 7.3 全局API转移到应用对象

- `app.component`
- `app.config`
- `app.directive`
- `app.mount`
- `app.unmount`
- `app.use`

### 7.4 其他

- 过渡类名 `v-enter` 修改为 `v-enter-from`、过渡类名 `v-leave` 修改为 `v-leave-from`。


- `keyCode` 作为 `v-on` 修饰符的支持。

- `v-model` 指令在组件上的使用已经被重新设计，替换掉了 `v-bind.sync。`

- `v-if` 和 `v-for` 在同一个元素身上使用时的优先级发生了变化。

- 移除了`$on`、`$off` 和 `$once` 实例方法。

- 移除了过滤器 `filter`。

- 移除了`$children` 实例 `propert`。

  ......