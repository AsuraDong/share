<!-- TOC -->

- [1. jQuery和DOM事件互相转换](#1-jquery和dom事件互相转换)
    - [1.1 jQuery对象转化成DOM对象](#11-jquery对象转化成dom对象)
    - [1.2 DOM对象转化成jQuery对象](#12-dom对象转化成jquery对象)
    - [1.3 jQuery对象检查](#13-jquery对象检查)
    - [1.4 特殊选择器this](#14-特殊选择器this)
- [2. jQuery选择器](#2-jquery选择器)
    - [2.1 层级选择器](#21-层级选择器)
    - [2.2 基本筛选选择器](#22-基本筛选选择器)
    - [2.3 内容和元素筛选选择器](#23-内容和元素筛选选择器)
    - [2.4 可见性筛选选择器](#24-可见性筛选选择器)
    - [2.5 属性筛选选择器](#25-属性筛选选择器)
    - [2.6 子元素筛选选择器](#26-子元素筛选选择器)
    - [2.7 表单元素选择器](#27-表单元素选择器)
    - [2.8 表单对象属性筛选选择器](#28-表单对象属性筛选选择器)
- [3. jQuery处理样式](#3-jquery处理样式)
    - [3.1 属性与样式之`.attr()`与`.removeAttr()`](#31-属性与样式之attr与removeattr)
    - [3.2 `html()`、`text()`和`val()`的用法](#32-htmltext和val的用法)
        - [3.2.1 `html()`](#321-html)
        - [3.2.2 `text()`](#322-text)
        - [3.2.3 表格样式`val()`](#323-表格样式val)
        - [3.2.4 `val()`用法](#324-val用法)
    - [3.2.5 三者差异](#325-三者差异)
    - [3.3 `Attribute`和`Property`区别](#33-attribute和property区别)
    - [3.4 增加和删除样式](#34-增加和删除样式)
        - [3.4.1 增加样式`addClass(className)`](#341-增加样式addclassclassname)
        - [3.4.2 删除样式`.removeClass( className)`](#342-删除样式removeclass-classname)
        - [3.4.3 切换样式 `.toggleClass()`](#343-切换样式-toggleclass)
    - [3.5 内联样式`css()`](#35-内联样式css)

<!-- /TOC -->
## 1. jQuery和DOM事件互相转换
### 1.1 jQuery对象转化成DOM对象

```javascript
var $div = $('div') //jQuery对象
var div = $div[0] //转化成DOM对象
div.style.color = 'red' //操作dom对象的属性
```
也可以通过jQuery自带的`get()`方法：
```javascript
var $div = $('div') //jQuery对象
var div = $div.get(0) //通过get方法，转化成DOM对象
div.style.color = 'red' //操作dom对象的属性
```

### 1.2 DOM对象转化成jQuery对象
> 如果传递给`$(DOM)`函数的参数是一个DOM对象，jQuery方法会把这个DOM对象给包装成一个新的jQuery对象
> 通过`$(dom)`方法将普通的dom对象加工成jQuery对象之后，我们就可以调用jQuery的方法了

```javascript
document.getElementsByTagName('div'); //dom对象
var $div = $(div); //jQuery对象
var $first = $div.first(); //找到第一个div元素
$first.css('color', 'red'); //给第一个元素设置颜色
```

### 1.3 jQuery对象检查
如右：`if(ele instanceof jQuery){ ... }`

### 1.4 特殊选择器this
> `this`，表示当前的上下文对象是一个html对象，可以调用html对象所拥有的属性和方法。
> `$(this)`,代表的上下文对象是一个jquery的上下文对象，可以调用jQuery的方法和属性值。

## 2. jQuery选择器
### 2.1 层级选择器
![](./image/jQuery样式处理/层级选择器.jpg)

**图中表格，`+`是相邻兄弟选择器，不是所有的紧接元素**

1. 层级选择器都有一个参考节点
2. 后代选择器包含子选择器的选择的内容
3. 一般兄弟选择器包含相邻兄弟选择的内容
4. 相邻兄弟选择器和一般兄弟选择器所选择到的元素，必须在同一个父元素下

### 2.2 基本筛选选择器
![](./image/jQuery样式处理/基本筛选选择器.jpg)

说明一下`$(not(selector))`的用法：
```javascript
//:not 选择所有元素去除不匹配给定的选择器的元素
//选中所有紧接着没有checked属性的input元素后的p元素，赋予颜色
$("input:not(:checked) + p").css("background-color", "#CD00CD");
```

### 2.3 内容和元素筛选选择器
![](./image/jQuery样式处理/内容和元素筛选选择器.jpg)

1. `:contains`与`:has`都有查找的意思，但是`contains`查找包含“指定文本”的元素，has查找包含“指定元素”的元素
2. 如果`:contains`匹配的文本包含在元素的子元素中，同样认为是符合条件的。

### 2.4 可见性筛选选择器
![](./image/jQuery样式处理/可见性筛选选择器.jpg)

>我们有几种方式可以隐藏一个元素：

    1. CSS display的值是none。
    2. type="hidden"的表单元素。
    3. 宽度和高度都显式设置为0。
    4. 一个祖先元素是隐藏的，该元素是不会在页面上显示
    5. CSS visibility的值是hidden
    6. CSS opacity的指是0

**元素的`visibility: hidden` 或 `opacity: 0`被认为是可见的，因为他们仍然占用空间布局。**

### 2.5 属性筛选选择器
![](./image/jQuery样式处理/属性筛选选择器.jpg)

### 2.6 子元素筛选选择器
![](./image/jQuery样式处理/子元素筛选选择器.jpg)

1. `:only-child`匹配某个元素是父元素中唯一的子元素，就是说当前子元素是父元素中唯一的元素，则匹配
2. jQuery实现`:nth-child(n)`是严格来自CSS规范，所以n值是“索引”，也就是说，从1开始计数，**`:nth-child(index)`从1开始的，而eq(index)是从0开始的**
3. `nth-child(n)` 与 `:nth-last-child(n)` 的区别前者是从前往后计算，后者从后往前计算


### 2.7 表单元素选择器
![](./image/jQuery样式处理/表单元素选择器.jpg)

> 除了input筛选选择器，几乎每个表单类别筛选器都对应一个input元素的type值。大部分表单类别筛选器可以使用属性筛选器替换。比如 $(':password') == $('[type=password]')

例如：`$(':input')`和`$(input:text)`

### 2.8 表单对象属性筛选选择器
![](./image/jQuery样式处理/表单对象属性筛选选择器.jpg)

1. 选择器适用于复选框和单选框，对于下拉框元素, 使用 `:selected` 选择器
2. 在某些浏览器中，选择器`:checked`可能会错误选取到`<option>`元素，所以保险起见换用选择器`input:checked`，确保只会选取`<input>`元素


## 3. jQuery处理样式

### 3.1 属性与样式之`.attr()`与`.removeAttr()`

> attr()有4个表达式

    1. attr(传入属性名)：获取属性的值
    2. attr(属性名, 属性值)：设置属性的值
    3. attr(属性名,函数值)：设置属性的函数值
    4. attr(attributes)：给指定元素设置多个属性值，即：{属性名一: “属性值一” , 属性名二: “属性值二” , … … }

> `removeAttr()`删除方法

    .removeAttr( attributeName ) : 为匹配的元素集合中的每个元素中移除一个属性（attribute）


**特别说明一下function的用法**

```javascript
// 设置所有img元素的title属性值：
// 1.如果该元素已经有了title属性，则不作改变
// 2.如果该元素之前没有title属性，则设置title属性等于它的alt属性
$("img").attr("title", function(index, attrValue){
    // 这里的this表示当前DOM元素
    return attrValue== undefined ? this.alt : attrValue;
});
```

### 3.2 `html()`、`text()`和`val()`的用法

#### 3.2.1 `html()`
> 这个操作是针对整个HTML内容（不仅仅只是文本内容）

1. `.html()` 不传入值，就是获取集合中第一个匹配元素的HTML内容
2. `.html( htmlString ) ` 设置每一个匹配元素的html内容
3. `.html( function(index, oldhtml) )` 用来返回设置HTML内容的一个函数

#### 3.2.2 `text()`
> .text()结果返回一个字符串，包含所有匹配元素的合并文本

1. `.text()` 得到匹配元素集合中每个元素的合并文本，包括他们的后代
2. `.text( textString )` 用于设置匹配元素内容的文本
3. `.text( function(index, text) )` 用来返回设置文本内容的一个函数


#### 3.2.3 表格样式`val()`
1. `.val()`无参数，获取匹配的元素集合中第一个元素的当前值
2. `.val( value )`，设置匹配的元素集合中每个元素的值
3. `.val( function )` ，一个用来返回设置值的函数

#### 3.2.4 `val()`用法
```html
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <title></title>
    <style>
    p {
        color: red;
        margin: 4px;
    }
    b {
        color: blue;
    }
    </style>
    <script src="https://www.imooc.com/static/lib/jquery/1.9.1/jquery.js"></script>
</head>
<body>
    <h3>.val()</h3>
    <select id="single">
        <option>慕课网</option><br/>
        <option selected="selected">博客园</option><br/>
    </select>
    <select id="multiple" multiple="multiple">
        <option selected="selected">imocc</option><br/>
        <option>慕课网</option><br/>
        <option selected="selected">博客园</option><br/>
    </select>
    <input type="text" value="click a button" id="temp"/>
    <p></p>
    <script type="text/javascript">
        //单个select，返回第一个
        alert( $("#single").val())
        $("p").text( $("#single").val() )
    </script>
    <script type="text/javascript">
        //多个select被选择，返回["imocc", "博客园"]
        $("p").text( $("#multiple").val()) 
    </script>
    <script type="text/javascript">
        //选择一个表单，修改value的值
        // $("input[type='text']").?('修改表的字段');
        $("input[type='text']").val("修改");
    </script>
</body>
</html>
```

### 3.2.5 三者差异
1. `val()`只能使用在表单元素上
2. `.val()`方法和`.html()`相同，如果其应用在多个元素上时，只能读取第一个表单元素的"value"值，但是`.text()`和他们不一样，如果`.text()`应用在多个元素上时，将会读取所有选中元素的文本内容。

### 3.3 `Attribute`和`Property`区别

dom中有个概念的区分：Attribute和Property翻译出来都是“属性”，《js高级程序设计》书中翻译为“特性”和“属性”。

简单理解，Attribute就是dom节点自带的属性
例如：html中常用的id、class、title、align等：
`<div id="immooc" title="慕课网"></div>`

而Property是这个DOM元素作为对象，其附加的内容，例如,tagName, nodeName, nodeType,, defaultChecked, 和 defaultSelected 使用.prop()方法进行取值或赋值等

**获取Attribute就需要用attr，获取Property就需要用prop**

### 3.4 增加和删除样式
#### 3.4.1 增加样式`addClass(className)`
> `.addClass()`方法不会替换一个样式类名。它只是简单的添加一个样式类名到元素上。例如原来是`class = "old"`，后来是`class="old new"`

1. `.addClass( className )` : 为每个匹配元素所要增加的一个或多个样式名
2. `.addClass( function(index, currentClass) )` : 这个函数返回一个或更多用空格隔开的要增加的样式名


#### 3.4.2 删除样式`.removeClass( className)`
1. `.removeClass( [className ] )`：每个匹配元素移除的一个或多个用空格隔开的样式名
2. `.removeClass( function(index, class) )` ： 一个函数，返回一个或多个将要被移除的样式名

一个实例：
```javascript
/.removeClass() 方法允许我们指定一个函数作为参数，返回将要被删除的样式
        $('.right > div:first').remove(function(index,className){
            
            //className = aa bb imoocClass
            //把div的className赋给下一个兄弟元素div上作为它的class
            $(this).next().addClass(className)

            //删除自己本身的imoocClass
            return 'imoocClass'
        })
```

#### 3.4.3 切换样式 `.toggleClass()`
> [详情请点击](https://www.imooc.com/code/8584)。

    1. .toggleClass( className )：在匹配的元素集合中的每个元素上用来切换的一个或多个（用空格隔开）样式类名
    2. .toggleClass( className, switch )：一个布尔值，用于判断样式是否应该被添加或移除
    3. .toggleClass( [switch ] )：一个用来判断样式类添加还是移除的 布尔值
    4. .toggleClass( function(index, class, switch) [, switch ] )：用来返回在匹配的元素集合中的每个元素上用来切换的样式类名的一个函数。接收元素的索引位置和元素旧的样式类作为参数

### 3.5 内联样式`css()`

**获取：**
1. `.css( propertyName ) `：获取匹配元素集合中的第一个元素的样式属性的计算值
2. `.css( propertyNames )`：传递一组数组，返回一个对象结果


**设置：**
1. `.css(propertyName, value )`：设置CSS
2. `.css( propertyName, function )`：可以传入一个回调函数，返回取到对应的值进行处理
.css( properties )：可以传一个对象，同时设置多个样式
