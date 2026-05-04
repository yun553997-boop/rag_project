# 1 HTML

## 1.1 标签

### 1.1.1 文本标签

- `<h1>标题</h1>`
- `<p>段落</p>`
- `<em>着重文字</em>`
- `<b>粗体文字</b>`
- `<i>斜体字</i>`
- `<strong>加重语气</strong>`
- `<del>删除字</del>`
- `<u>加下划线</u>`


- `<hr>` 单标签，表示段落级元素之间的主题转换，一般显示为水平线。


- `<ul></ul>`  无序列表：可含有多个元素、无编号显示
- `<ol></ol>`  表示有序列表、通常是带编号列表
- `<li></li>`  写在ul和ol中，表示列表里的条目



### 1.1.2 图片

- `<img src="../tu-pian/a2.jpg" alt="课表正在加载中" title="课程">`

  `alt` :图像代替文本（图片没有路径时）

  `title：` 鼠标悬停在图片给予提示

- 路径：

  绝对路径：`src="D:\Wed-dev\html-课堂资料\assets\1573011521613.png"`

  相对路径：子级（/）、同级（./）、父级（../）

  > 注意：只有同级可以省略“./“

  网络路径：直接放网址



### 1.1.3 音频、视频

- ` <audio src="春泥.mp3" controls loop autoplay></audio>`

  `controls` :显示音频控制面板

  `loop` :循环播放

  `autoplay` :自动播放（浏览器一般是禁用的）

  > **注意**：在html中，如果属性名与属性完全相同，可以简写成一个单词

-  `<video src="朝花夕拾.mp4" controls loop autoplay></video>`



### 1.1.4 超文本链接

- `<a href="https://www.mi.com/shop" target="_blank">小米商城</a>`

  默认值：未被访问过显示为蓝色，反之为紫色；点击为红色，选中鼠标变小手；自带下划线

  `target` : 打开方式（当前页面/新建页面）

  `<a href=""><img src=""></a>` 其中的文本可以是字、词、画等

  `<a href="#">空连接</a>` 

  `text-decoration:none` :去下划线（underline:加下划线）

- 样式:

  访问前样式: a:link{ color:#00cc00 }

  访问后样式: a:visited{}

  鼠标悬停:  a:hover{}

  点击时: a:active{}



## 1.2 三个表

### 1.2.1 列表

- 无序列表：

  ```html
  <ul>
      注意：
      <li>ul标签只能包裹li标签</li>
      <li>li标签里面可以包裹任何内容</li>
      <li>li标签独占一行</li>
  </ul>
  ```

- 有序列表：

  ```html
  <ol>
      <li>ol标签自动添加数字编号</li>
      <li>li标签里面可以包裹任何内容</li>
      <li>li标签里面可以包裹任何内容</li>
  </ol>
  ```

- 定义列表：

  ```html
  <dl>
      <dt>dt是标题</dt>
      <dd>dd是表述</dd>
      <dd>dl标签只能包含dt和dd</dd>
      <dd>dt和dd里可以包含任何内容</dd>
  </dl>
  ```



### 1.2.2 表格

> table:表格,默认没有边框线，border添加一像素边框线
>
> tr行:有几行就写几行tr标签
>
> th**表头**单元格：默认加粗
>
> td**内容**单元格

```html
<table border="1px">
    <tr>
        <th>姓名</th>
        <th>语文</th>
        <th>数学</th>
        <th>总分</th>
    </tr>
    <tr>
        <td>张三</td>
        <td>99</td>
        <!--跨行合并单元格rowspan='合并几个单元格'{保留最左上单元格，删除其他}-->
        <td rowspan="2">100</td>
        <td>199</td>
    </tr>
    <tr>
        <td>李四</td>
        <td>98</td>
        <!--<td>100</td> 合并后需删除合并之前的另一个单元格-->
        <td>198</td>
    </tr>
    <tr>
        <td>总结</td>
        <!--跨列合并单元格colspan='合并几个单元格'{保留最左上单元格，删除其他}-->
        <td colspan="3">全市第一</td>
        <!--<td>全市第一</td>-->
        <!--<td>全市第一</td>-->
    </tr>
    <!--注意不能跨结构合并单元格、表格靠内容撑开-->
```



### 1.2.3 表单

使用`<form>`封装

1. `<input>`

   文本框：<input type="text">单行文本，输入什么就显示什么

   密码框：<input type="password">单行文本，输入显示点

   单选框：<input type="radio">

   多选框：<input type="checkbox">

   上传文件：<input type="file">

   > placeholder提示文字
   >


# 2 CSS

## 2.1 选择器

### 2.1.1 类选择器

> 一个类选择器可以供多个标签使用
>
> 一个标签可以多个类名，类名之间用空格隔开



### 2.1.2 复合类选择器

1. 后代选择器：

   ```css
   div span{
     color:#0000ff
   }
   ```

   > 此处是选择的div的后代（不管span是div的儿子、孙子……）

2. 子代选择器：

   ```css
   div > span{
       color:#00ff00
   }
   ```

   > 只选择儿子

3. 并集选择器：

   ```css
   div, p, span{
       color:#ff0000
   }
   ```

   > 三个标签都拥有这个属性

4. 交集选择器：

   ```css
   p .box{
       color:#ccaa00
   }
   ```

   > 同时拥有p标签box类名的语句

### 2.1.3 伪类选择器

伪类标签多用于超链接，但其他任何标签也都可以用，例如设置鼠标悬停状态，只需在标签后加上hover

1. 子元素选择器

   ```css
   .container:hover .child {
     display: block;
   }
   ```


2. 相邻兄弟选择器

   ```css
   h1:hover + p {
     font-weight: bold;
   }
   ```


3. 通用兄弟选择器 

   ```css
   h2:hover ~ p {
     color: blue;
   }
   ```

   > :link(访问前),:visited(访问后),:hover(鼠标悬停),:active(点击时)

### 2.1.4 结构伪类选择器

first-child（选择第一个）

last-child（选择最后一个）

nth-child(……)（括号内可以为数字、公式、奇数（odd）、偶数（even））

```css
li:nth-child(2n){
    background-color: #091;
}
```

### 2.1.5 伪元素选择器

创建虚拟元素（伪元素），用来摆放装饰性的内容

1. 在div里面最前面添加一个元素，必须要有content

   ```css
   div::before{
       content:"老鼠";

       width: 100px;
       height: 100px;
   }
   ```

2. 在div里面最后面添加一个元素，必须要有content

   ```css
   div::after{
       content:"大米";

       width: 100px;
       height: 100px
   }
   ```


## 2.2 盒子样式属性

### 2.2.1 背景属性

- 背景色

  ```css
  background-color: #0ff;
  ```

- 背景图

  背景图默认平铺（即图片大小不变，只通过裁剪，复制来适应背景大小）

  ```css
  background-image: url(../tu-pian/a1.jpg);
  ```

  1. 平铺方式：

     > repeat（平铺）,no-repeat（不平铺）,repeat-x（水平平铺）,repeat-y（垂直平铺）

     ```css
     background-repeat:no-repeat;
     ```

  2. 背景图位置

     > 可以用位置的英文单词，也可用数字（正右、下；负左、上），也可两种混用；若只有一个有值，则另一个默认

     ```css
     background-position: 0 150px;
     background-position: center top;
     ```

  3. 背景图放缩（大小）

     > 百分比：100%为contain
     > 关键字：(cover等比例完全覆盖背景区(注意不要移动图片位置)，图片会被裁减；contain等比例放缩将图片完全装入背景区

     ```css
     background-size:cover;
     ```


- **复合写法**

  > 背景色 背景图 平铺方式 图片位置/图片放缩

  ```css
  background: #071 url("../tu-pian/a1.jpg") no-repeat center bottom/cover;
  ```

### 2.2.2 显示模块转换

- 显示模块转换：block(转为块级)、inline-block(转为行内块)、inline(转为行内)

  ```css
  display: block;
  ```

###  2.2.3 盒子溢出

- 盒子溢出

  > scroll（溢出滚动，无论是否溢出都显示滚动条）
  >
  > auto（溢出滚动，溢出才显示滚动条）

  ```css
  overflow: hidden（溢出的隐藏）
  ```

### 2.2.4 盒子其他属性

- 外边距

  ```css
  margin: 0;
  ```

- 边框

  ```css
  /**边框粗细、边框样式（实线、虚线、双线等）、颜色**/
  border: 1px solid red;
  ```

- 盒子尺寸

  ```css
  width: 60%;
  height: 500px;
  ```

- 内边距

  ```css
  padding: 0;
  ```

  > 单位可以是px、%、位置（如auto）


- 角的形状

  > 只写一个值：统一设置四个角；两个值：左上和右下、右上和左下；四个值左上、右上、右下、左下
  >
  >  若盒子/图片为正方形，将值设置为50%就会变为圆形（小于50%趋近于方）；若盒子/图片为长方形，将值设置为短边的一半就会变为椭圆形

  ```css
  border-radius: 10px 20px;
  ```

- 盒子阴影

  > X轴偏移量 Y轴偏移量 模糊半径 扩散半径 颜色 内外阴影（默认外阴影，inset设为内阴影）

  ```css
  box-shadow: 5px 2px 10px 1px rgba(0,0,0,0.5);
  ```

## 2.3 布局

### 2.3.1 浮动

float:left、right(左对齐、右对齐)

```css
/*清除浮动-1（哪里需要清除浮动，就跟在哪个标签类名后）*/
.clearfix::after{
    clear: both;
}
/*清除浮动-2（哪里需要清除浮动，就写在哪个标签下的子标签）*/
.clearfix{
    clear: both;
}
```

### 2.3.2 Flex布局

- 基本使用

  > 弹性盒子（默认主轴在水平方向）：会自动挤压（当弹性容器不足以容纳弹性盒子，盒子会挤压至容纳），若没有宽度，宽度靠内容撑开

  ```html
  <style>
      .box{
      	display: flex;/*设置弹性盒子(可以同行，div不可以)*/
      }
      .box div{
          width: 200px;/*若没有设置盒子大小，则会填满弹性容器*/
          height: 100px;
          background-color: #c98010;
      }
  </style>

  <div class="box">
      <div></div>
      <div></div>
      <div></div>
  </div>
  ```

- 其他属性

  - 自动换行（宽度不足，自动换行）

    ```css
    flex-wrap: wrap
    ```

  - 修改主轴方向

    ```css
    flex-direction: column;  /*将主轴改为垂直方向*/
    ```

  - 主轴对齐方式

    ```css
    justify-content: space-around;            
    ```

    > flex-start(弹性盒子从起点开始排列)
    > flex-end(弹性盒子从终点开始排列)
    > center(弹性盒子沿主轴居中)
    > space-around(弹性盒子沿主轴均匀排列，空白间距均分在盒子两侧)
    > space-between(弹性盒子沿主轴均匀排列，空白间距均分在盒子之间)
    > space-evenly(弹性盒子沿主轴均匀排列，盒子与容器之间间距相等)

  - 侧轴对齐方式

    ```css
    align-items: center;
    ```

    > flex-start(弹性盒子从起点开始排列)
    > flex-end(弹性盒子从终点开始排列)
    > 注意：当盒子没有高，则默认将盒子拉升至容器高度

    在换行之后的侧轴排列方式align-content,属性值与没换行的主轴排列相同

- 弹性伸缩比

  > 控制弹性盒子的主轴方向的尺寸（属性值为整数，表示占用容器剩余尺寸的分数）

  ```css
  .box div:nth-child(1){
      width: 200px;
  }
  .box div:nth-child(2) {
      flex: 1;    若只设置第二个盒子，且分数为1，则占用剩余全部
  }
  .box div:nth-child(3) {*/
      flex: 2;    设置了第二、三个，则第三个盒子占用剩余的2/3
  ```

## 2.4 定位

- **相对定位**

  特点：a将转移位置（但原来位置不会被其他占用，会被空着），转移后的元素会覆盖在其他标签上面，且转移后的a的显示类型不变

  ```html
  <style>
      .xd {
      	position: relative;/*相对定位*/
      	right: 300px;
      }
  </style>

  <div class="xd"></div>
  ```

- **绝对定位**

  特点：脱标不占位，且显示模式会转化为行内块元素

  用法：父级（就近的祖先），设置为相对定位，子集（已设置为绝对定位的子集）就会悬浮

  ```html
  <style>
      .fuji{
      	position: relative;  /*相对定位*/
  	}
  	.fuji a {
  	    position: absolute; /*绝对定位*/
  	    top:0;
  	    right: 0;
  	}
  </style>
  <div class="fuji">
      <div class="ziji"><img src="../tu-pian/a2.jpg" alt=""></div>
  </div>
  ```

- **居中定位**

  ```html
  <style>
      .jz{
          position: relative;  /*相对定位*/
      }
      .jz .b{
          position: absolute;  /*绝对定位*/
          left: 50%;
          top: 50%;
          margin-left: -150px;
          margin-top: -84px;
          /*transform: translate(-50%,-50%);*/
      }
  </style>
  <div class="jz">
      <img src="../tu-pian/王者登录.webp" alt="" class="b">
  </div>
  ```

- 固定定位

  脱标、不占位，参照物：浏览器窗口，显示模块：具备行内块特点

  ```html
  <style>
      .gd {
      	position: fixed;    
      	top: 0;
      	width: 500px;
  	}
  </style>

  <div class="gd">
      <img src=''>
  </div>
  ```


## 2.5 堆叠顺序

- 同属绝对定位情况下，标签定位堆叠顺序

  > 谁越大谁在上（比较的是同级,父级在下，子级在上），默认后来者居上,默认为auto，可以为负

  **注意**：只对设置了position有效

  ```css
  z-index: 1;  
  ```

## 2.6 垂直对齐

本属性解决的是图片与文字并排时，垂直对齐方式

- 图片是行内块元素，低对齐方式按照基线对齐，与同等大小的背景框下有条缝

  ```css
  vertical-align: middle;
  /*属性值：top、bottom*/       
  ```

  > 此属性可解决；转块级元素也可解决

## 2.7 过渡效果

- 过渡效果

  > 属性值：过度属性 花费时间
  >
  > 过度属性可以是具体的CSS属性，也可以是all(过度两个阶段之间的所有属性)

  ```css
  transition: all 0.5s;
  ```

## 2.8 透明、鼠标

- 透明

  ```css
  /*设置这个元素(包括背景和内容)的透明度，属性值：0-1（0：完全看不见）*/
  opacity: 0.3;
  /*只能设置背景透明度*/
  color: rgba(0,0,0,0.5);
  ```


- 鼠标

  > 属性值：
  >
  > - pointer:小手效果，提示用户可以点击
  > - text:工字形，提示用户可以选择文字
  > - move十字光标：提示用户可以移动
  > - default：箭头

  ```css
  cursor: pointer;
  ```

  ​







​





​

​

​

​