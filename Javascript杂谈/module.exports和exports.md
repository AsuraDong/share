## 推荐写法
> 具体解释可以往后看。

```javascript
'use strict'

let app = { // 注册全局对象
    ...
}

... // 封装工具箱

exports = module.exports = app // 导出工具箱
```

## 原理
1. 每一个`node.js`执行文件，都自动创建一个`module`对象，同时，`module`对象会创建一个叫`exports`的属性，初始化的值是 `{}`。即：` module.exports = {}`
2. `exports`是引用 `module.exports`的值
3. 模块导出的时候，真正导出的执行是`module.exports`，而不是`exports`

#### 1与2的demo

`foo.js`

```javascript
'use strict'
module.exports.sayHello = function(){
    console.log(this.name)
}
exports.name = 'foo.js' // exports引用module.exports的值
```

`test.js`

```javascript
'use strict'

let foo = require('./foo')
foo.sayHello()
```

#### 3的demo
> 为了验证真正导出的是`module.exports`而不是`exports`，我们对`foo.js`修改如下：

```javascript
'use strict'

module.exports = {
    sayHello:function(){
        console.log(this.name)
    },
    name:'module.exports'
}

exports.sayHello = function(){
    console.log('exports')
}
```

`test.js`的输出就是：`module.exports`。

因为`module.exports`的引用改变（`js`中对象的赋值都是引用），断开了和`exports`的连接，而真正导出的只是`module.exports`。