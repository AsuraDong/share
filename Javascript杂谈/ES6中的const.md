> `const`实际上保证的，并不是变量的值不得改动，而是变量指向的那个内存地址不得改动。

## 效果
- 对于简单类型的数据**（数值、字符串、布尔值）**，值就保存在变量指向的那个内存地址，因此**等同于常量**。
- 对于**复合类型的数据（主要是对象和数组）**，变量指向的内存地址，`const`只能保证这个**指针是固定的**，不能保证它指向的数据结构是不可变得

```javascript
'use strict'
const obj = {}
const arr = []
obj.prop = 123  // 不改动指针
arr.push('Hello')  // 只改变数据结构

try{
    obj = {} // obj重指向新对象
} catch (err) {
    console.log(err.message) // 失败
}

try{
    arr = []
} catch (err) {
    console.log(err.message) // 失败
}
```

## 彻底冻结
> 除了将对象本身冻结，**对象的属性也应该冻结**

### 关于`Object.freeze`
> 方法可以冻结一个对象。冻结对象是指那些不能添加新的属性，不能修改已有属性的值，不能删除已有属性，以及不能修改已有属性的可枚举性、可配置性、可写性的对象。

```javascript
'use strict'
const foo = {}
foo.prop = 1
foo.config = {
    prop:1
}

let freeze = (obj) => {
    Object.freeze(obj)
    Object.keys(obj).forEach( (key)=>{
        if(typeof obj[key] === 'object') {
            freeze(obj[key])
        }
    })
}

freeze(foo) // 完全冻结
try {
    foo.prop = 'test'
} catch (err) {
    console.log(err.message)
}
```