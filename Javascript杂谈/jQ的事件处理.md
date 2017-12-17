<!-- TOC -->

- [1. 事件绑定和卸载](#1-事件绑定和卸载)
    - [1.1 事件绑定:`on()`](#11-事件绑定on)
    - [1.2 事件卸载:`off()`](#12-事件卸载off)
- [2. 自定义事件](#2-自定义事件)
    - [2.1 `trigger()`](#21-trigger)
    - [2.2 `triggerHandler()`](#22-triggerhandler)
- [3. 鼠标事件](#3-鼠标事件)
    - [3.1 基础例子：`click()`和`dbclick()`](#31-基础例子click和dbclick)
    - [3.2 其他例子](#32-其他例子)
- [4. 键盘事件:`keydown()`&&`keyup()`](#4-键盘事件keydownkeyup)
- [5. 表单处理](#5-表单处理)
    - [5.1 焦点事件：`focus()`和`blur()`](#51-焦点事件focus和blur)
    - [5.2 表单改变事件:`change()`](#52-表单改变事件change)
    - [5.3 选中事件:`select()`](#53-选中事件select)
    - [5.4 提交事件:`submit()`](#54-提交事件submit)

<!-- /TOC -->
## 1. 事件绑定和卸载
### 1.1 事件绑定:`on()`
1. `$("#elem").on('click',function(){})`
1. 多事件绑定：
    ```javascript
    $("#elem").on({
        mouseover:function(){},  
        mouseout:function(){}
    });
    ```
1. 传递data给event
    ```javascript
    function greet( event ) {
    alert( "Hello " + event.data.name ); //Hello 慕课网
    }
    $( "button" ).on( "click", {
    name: "慕课网"
    }, greet );
    ```
### 1.2 事件卸载:`off()`
1. 删除一个事件：`$("elem").off("mousedown")`
1. 删除多个事件：`$("elem").off("mousedown mouseup")`
1. 删除所有事件：`$("elem").off()`

## 2. 自定义事件
> 是jq自定义的事件，在原生js中不存在的

### 2.1 `trigger()`
> 根据绑定到匹配元素的给定的事件类型执行所有的处理程序和行为

1. 可以自定义事件（下面为：Aaron事件）
    ```javascript
    $('#elem').on('Aaron', function(event,arg1,arg2) {
        alert("自触自定义时间")
    });

    $('#elem').trigger('Aaron',['参数1','参数2']);
    ```
2. 在处理参数的传递上更简单，如上所示
3. 简单点无参数，就是`selector.trigger("submit")`

### 2.2 `triggerHandler()`
1. 不会事件冒泡
1. 但还是推荐trigger，显式禁止事件冒泡

## 3. 鼠标事件
### 3.1 基础例子：`click()`和`dbclick()`

1. `$ele.click()`
    ```javascript
    <div id="test">点击触发<div>
    $("ele").click(function(){
        alert('触发指定事件')
    })
    $("#test").click(function(){
        $("ele").click()  //手动指定触发事件 
    });
    ```
2. `$ele.click(function(){ ... })`
3. `$ele.click( [eventData ], function(){ ... } )`
    ```javascript
    <div id="test">点击触发<div>
    $("#test").click(11111,function(e) {
        //this指向 div元素
        //e.data  => 11111 传递数据
    });
    ```
### 3.2 其他例子
| 事件 | 代码 |
| - | - |
|按下和抬起 | mousedown&&mouseup|
|鼠标移动 | mousemove |
| 进入和出去 | mouseover&&mouseout |
| （无冒泡）进入和出去 | mouseenter&&mouseleave |
| **封装在一起的进入和出去** | hover(handlerIn,handlerOut) |
| (会冒泡)元素内部获得焦点或失去焦点 | focusin&&focusout|

## 4. 键盘事件:`keydown()`&&`keyup()`

1. keydown是在键盘按下就会触发
2. keyup是在键盘松手就会触发
3. 理论上它可以绑定到任何元素，但keydown/keyup事件只是发送到具有焦点的元素上，**不同的浏览器中，可获得焦点的元素略有不同，但是表单元素总是能获取焦点，所以对于此事件类型表单元素是最合适的。**


## 5. 表单处理
### 5.1 焦点事件：`focus()`和`blur()`
和`focunin()`它们相比，避免了冒泡

### 5.2 表单改变事件:`change()`
> `<input>`元素，`<textarea>`和`<select>`元素的值都是可以发生改变的，开发者可以通过change事件去监听这些改变的动作

### 5.3 选中事件:`select()`
> select事件只能用于`<input>`元素与`<textarea>`元素

### 5.4 提交事件:`submit()`
具体能触发submit事件的行为：
1. `<input type="submit">`
2. `<input type="image">`
3. `<button type="submit">`
4. 当某些表单元素获取焦点时，敲击Enter（回车键）



