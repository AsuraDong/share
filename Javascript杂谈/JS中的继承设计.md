> 众所周知，`javascript`的继承是通过原型链来实现的。经常看见下面这种写法：

```javascript
'use strict'
function FUN(name){
  this.name = name;
}

FUN.prototype.sayHello = function(){
  console.log('调用 sayHello 函数')
}

let fun = new FUN('godbmw')
fun.sayHello() 
// FUN('godbmw').sayHello()
// 报错：没有变量name
```

原因在于`this`的指向：**调用函数的那个对象**

所以，`FUN('godbmw').sayHello()`写法`this`指向全局，此时没有`name`属性。

## 构造函数
> 在`js`中，利用`new`生成实例对象。其后跟着的是构造函数。此时，`this`就代表新创建的实例对象。

### `new`缺点
> 用构造函数生成实例对象，有一个缺点，那就是无法共享属性和方法。

```javascript
'use strict'
function FUN(name){
  this.name = name;
}

FUN.prototype.sayHello = function(){
  console.log(this.name)
}

let fun1 = new FUN("one")
let fun2 = new FUN("two")

fun1.name = 'new name' // 更改fun1的name
fun1.sayHello() // 输出：new name
fun2.sayHello() // 输出：two
```

说明，实例对象都有自己的属性和方法的副本，互不影响。如果有数据需要共享，其实会浪费空间。

## `prototype`对象
> 利用`prototype`可以将需要共享的数据和对象放在一起。上面的代码改造如下。

```javascript
'use strict'
function FUN(){
}

FUN.prototype = {
  sayHello:function(){
    console.log('Name is ' + this.name)
  },
  name:"sayHello"
}

let fun1 = new FUN()
let fun2 = new FUN()

FUN.prototype.name = 'new name' 
fun1.sayHello() // 输出结果都是：
fun2.sayHello() // Name is new name
```

### 错误写法
- `FUN.name = 'new name'`：`FUN`是`function`，`FUN.prototype`才是`object`。如果想访问属性，必须利用`new`来实例化
- `fun1.name='new name'`：输出结果不一样。如果要一样，**需要在原型链上修改，而不是针对实例对象**。