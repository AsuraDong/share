<!-- TOC -->

- [1. 动画方法：`animate()`和停止方法：`stop()`](#1-动画方法animate和停止方法stop)
    - [1.1 `animate()`](#11-animate)
        - [注意事项：](#注意事项)
        - [属性设置方法](#属性设置方法)
        - [事件设置方法：duration](#事件设置方法duration)
        - [运动算法：easing](#运动算法easing)
        - [回调函数：complete](#回调函数complete)
        - [☆☆更高级的方法☆☆](#☆☆更高级的方法☆☆)
    - [1.2 停止函数`stop([],[])`](#12-停止函数stop)
- [2. 其他动画](#2-其他动画)
    - [2.1 隐藏和显示：`hide()`&&`show`&&`toggle()`](#21-隐藏和显示hideshowtoggle)
    - [2.2 用法类似的更多动画](#22-用法类似的更多动画)

<!-- /TOC -->

## 1. 动画方法：`animate()`和停止方法：`stop()`
### 1.1 `animate()`

#### 注意事项：
1. 特别注意所有用于动画的属性必须是数字的
1. CSS 样式使用 DOM 名称（比如 "fontSize"）来设置，而非 CSS 名称（比如 "font-size"）
1. background-color很明显不可以，因为参数是red或者GBG这样的值，除非用插件

#### 属性设置方法
1. 数值：
```javascript
$("...").animate({
    left: 50, 
    width: '50px'   
    opacity: 'show',  
    fontSize: "10em",
}, 500);
```
2. 每个属性能使用'show', 'hide', 和 'toggle'
```javascript
.animate({
    width: "toggle"
});
```
3. 如果提供一个以`+=`或`-=`开始的值，那么目标值就是以这个属性的当前值加上或者减去给定的数字来计算的
```javascript
.animate({ 
    left: '+=50px'
}, "slow");
```

#### 事件设置方法：duration
1. 单位：ms
1. 可以使用fast和slow，分别代表200ms和600ms

#### 运动算法：easing
1. 默认是swing
1. 其他请看文档

#### 回调函数：complete
1. 动画完成时执行的函数，这个可以保证当前动画确定完成后发会触发
```javascript
 $aaron.animate({
                fontSize: "5em"
            }, 2000, function() {
                alert("动画 fontSize执行完毕!");
            });
```

#### ☆☆更高级的方法☆☆
语法：`.animate( properties, options )`

其中，**options参数：**
1. duration - 设置动画执行的时间
2. easing - 规定要使用的 easing 函数，过渡使用哪种缓动函数
3. step：规定每个动画的每一步完成之后要执行的函数
4. progress：每一次动画调用的时候会执行这个回调，就是一个进度的概念
5. complete：动画完成回调

```javascript
$('#elem').animate({
    width: 'toggle',  
    height: 'toggle'
  }, {
    duration: 5000,
    specialEasing: {
      width: 'linear',
      height: 'easeOutBounce'
    },
    complete: function() {
      $(this).after('<div>Animation complete.</div>');
    },
    //每一个动画都会调用
    step: function(now, fx) {
        $aaron.text('高度的改变值:'+now)
    }
  });
```

### 1.2 停止函数`stop([],[])`
如下代码：
```javascript
$("#aaron").animate({
    height: 300
}, 5000)
$("#aaron").animate({
    width: 300
}, 5000)
$("#aaron").animate({
    opacity: 0.6
}, 2000)
```

1. stop()：只会停止第一个动画，第二个第三个继续
2. stop(true)：停止第一个、第二个和第三个动画
3. stop(true ture)：停止动画，直接跳到第一个动画的最终状态 

## 2. 其他动画
### 2.1 隐藏和显示：`hide()`&&`show`&&`toggle()`
`hide()`用法：
1. `$elem.hide()`
1. `$elem.hide(options)`
```javascript
$elem.hide({
    duration:3000,
    complete:func(){}
})
```
1. `$elem.hide(3000)`

show和toggle用法类似。

**注意事项：**
如果使用!important在你的样式中，比如display: none !important，如果你希望.show()方法正常工作，必须使用.css('display', 'block !important')重写样式

### 2.2 用法类似的更多动画
| 动画 | 操作 |
| - | - |
|下拉和上卷|slideDown&&slideUp&&slideToggle|
|淡出和淡入|fadeOut&&fadeIn&&fadeToggle|