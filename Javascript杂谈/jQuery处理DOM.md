<!-- TOC -->

- [1. 节点的创建](#1-节点的创建)
- [2. 节点的添加](#2-节点的添加)
    - [2.1 内部插入`append()`和`prepend()`](#21-内部插入append和prepend)
    - [2.2 外部插入`after()`和`before()`](#22-外部插入after和before)
- [3. 节点删除](#3-节点删除)
    - [3.1 删除子节点：`empty()`](#31-删除子节点empty)
    - [3.2 删除自身：`remove()`](#32-删除自身remove)
    - [3.3 保留内存的删除操作`detach()`](#33-保留内存的删除操作detach)
- [4. 节点的克隆和替换](#4-节点的克隆和替换)
    - [4.1 拷贝`clone()`或者`clone(true)`](#41-拷贝clone或者clonetrue)
    - [4.2 替换`replaceWith()`和`replaceAll()`](#42-替换replacewith和replaceall)
    - [4.3 增加和卸掉包裹:`wrap()`、`unwrap()`、`wrapAll()`](#43-增加和卸掉包裹wrapunwrapwrapall)
- [5. 节点遍历](#5-节点遍历)
    - [5.1 后代遍历 `find()`](#51-后代遍历-find)
    - [5.2 父类元素：`parent()`和祖先元素`parents()`](#52-父类元素parent和祖先元素parents)
    - [5.3 最近的元素:`closest(selector)`](#53-最近的元素closestselector)
    - [5.4 紧邻的同辈元素:`next(selector)`和`prev(selector)`](#54-紧邻的同辈元素nextselector和prevselector)
    - [5.5 所有同辈元素:`sublings([selector])`](#55-所有同辈元素sublingsselector)
- [6. 节点逻辑处理](#6-节点逻辑处理)
    - [6.1 添加元素：`add()`](#61-添加元素add)
    - [6.2 节点循环](#62-节点循环)

<!-- /TOC -->
## 1. 节点的创建
直接暴力：
```javascript
var $body = $('body');
    $body.on('click', function() {
        //通过jQuery生成div元素节点
        var div = $("<div class='right'><div class='aaron'>动态创建DIV元素节点</div></div>")
        $body.append(div)
    })
```

## 2. 节点的添加
### 2.1 内部插入`append()`和`prepend()`
> 还有个是：`appendTo()`，目标位置不一样。`prepend()`是加在内部的头部位置。

```javascript
$("#bt1").on('click', function() {
    		//.append(), 内容在方法的后面，
    		//参数是将要插入的内容。
    		$(".content").append('<div class="append">通过append方法添加的元素</div>')
    	});
$("#bt2").on('click', function() {
    		//.appendTo()刚好相反，内容在方法前面，
    		//无论是一个选择器表达式 或创建作为标记上的标记
    		//它都将被插入到目标容器的末尾。
    		$('<div class="appendTo">通过appendTo方法添加的元素</div>').appendTo($(".content"))
    	})
```

### 2.2 外部插入`after()`和`before()`
> `insertAfter()`和`insertBefore()`也是目标位置不一样

1. before与after都是用来对相对选中元素外部增加相邻的兄弟节点
2. 2个方法都是都可以接收HTML字符串，DOM 元素，元素数组，或者jQuery对象，用来插入到集合中每个匹配元素的前面或者后面
3. 2个方法都支持多个参数传递after(div1,div2,....)

```javascript
$("#bt1").on('click', function() {
        //在匹配test1元素集合中的每个元素前面插入p元素
        $(".test1").before('<p style="color:red">before,在匹配元素之前增加</p>', '<p style="color:red">多参数</p>')
    });
```

## 3. 节点删除
### 3.1 删除子节点：`empty()`
> 只是删除子节点，对自身不影响

### 3.2 删除自身：`remove()`
> 分为有参数(**参数选择**)和无参数用法
> 1. `$(".hello").remove()`
> 2. `$(".hello").filter(":contains('3')").remove()`:等效于：`$(".hello").remove(":contains('3')")`

### 3.3 保留内存的删除操作`detach()`

1. detach方法是JQuery特有的，所以它只能处理通过JQuery的方法绑定的事件或者数据
1. 只是显示效果删除，但是对象绑定的数据和事件还在，之后可以再拿回来。

```javascript
var p;
    $("#bt1").click(function() {
        if (!$("p").length) return; 
        p = $("p").detach()
    });

    $("#bt2").click(function() {
        $("body").append(p);
    });
```

## 4. 节点的克隆和替换
### 4.1 拷贝`clone()`或者`clone(true)`
1. 复制所有匹配的元素集合，包括所有匹配元素、匹配元素的下级元素、文字节点。
1. `clone(true)`也克隆结构、事件和数据
1. clone()方法是jQuery扩展的，只能处理通过jQuery绑定的事件与数据
1. **clone()方法是jQuery扩展的，只能处理通过jQuery绑定的事件与数据**

```javascript
//克隆节点
    	//克隆事件
	    $(".aaron2").on('click', function() {
            console.log(1)
	        $(".left").append( $(this).clone(true).css('color','blue') )
	    })
```

### 4.2 替换`replaceWith()`和`replaceAll()`
1. 源和目标的位置不一样
1. `.replaceWith()`与`.replaceAll()` 方法会删除与节点相关联的所有数据和事件处理程序
1. `.replaceWith( newContent )`：用提供的内容替换集合中所有匹配的元素并且返回被删除元素的集合

```javascript
$(".right > div:first p:eq(1)").replaceWith('<a style="color:red">replaceWith替换第二段的内容</a>')

$('<a style="color:red">replaceAll替换第六段的内容</a>').replaceAll('.right > div:last p:last');
```

### 4.3 增加和卸掉包裹:`wrap()`、`unwrap()`、`wrapAll()`

1. `wrap()`:在集合中匹配的每个元素周围包裹一个HTML结构
	```javascript
	$('p').wrap('<div></div>')

	$('p').wrap(function() {
		return '<div></div>';   //与第一种类似，只是写法不一样
	})
	```
1. `unwrap()`不接受参数：`$('p').unwrap();`
1. wrap是针对单个dom元素处理，如果要将集合中的元素用其他元素包裹起来，也就是给他们增加一个父元素(而不是每一个都增加一个父元素)
```javascript
$('p').wrapAll('<div></div>');


$('p').wrapAll(function() {
    return '<div><div/>'; 
}) // 这种方法和wrap等同
```

## 5. 节点遍历
### 5.1 后代遍历 `find()`
1. 必须有参数
1. 取回所有后代可以用`'*'`

```javascript
$("button:last").click(function() {
        //找到所有p元素，然后筛选出子元素是span标签的节点
        //改变其字体颜色
        var $spans = $('span');
        $("p").find($spans).css('color', 'red');
    });
```

### 5.2 父类元素：`parent()`和祖先元素`parents()`

1. `.parents()和.parent()`方法是相似的，但后者只是进行了一个单级的DOM树查找
2. `$( "html" ).parent()`方法返回一个包含document的集合，而$( "html" ).parents()返回一个空集合。

### 5.3 最近的元素:`closest(selector)`

> 从元素本身开始向上寻找第一个符合selector的元素，**返回的是包含零个或一个元素的jquery对象**。可以通过检查`length`属性来查看是否找到。

### 5.4 紧邻的同辈元素:`next(selector)`和`prev(selector)`

1. selector用法是针对`.next()`返回多个对象的情况。例如`$("li").next(":first")`，li标签肯定很多，所以next也很多，这里选取第一个。
1. `prev()`和`next()`用法类似

### 5.5 所有同辈元素:`sublings([selector])`

> 返回除了自己的所有同辈元素

## 6. 节点逻辑处理
### 6.1 添加元素：`add()`
> 用于向一个集合中添加元素，并且返回新的集合

实例：`$('li').add('<p>新的p元素</p>').appendTo($('.right'))`

### 6.2 节点循环
1. 利用传统的for和length循环
1. 无法使用for-in和for-of，因为不是迭代器。
1. **jq提供了`each()`**，利用回调函数使用

```javascript
$("li").each(function(index, element) {
     index 索引 0,1
     element是对应的li节点 li,li
     this 指向的是li
})
```