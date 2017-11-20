[toc]
> 声明一下，这篇文章，是在学习python的类的编写过程中，不断收集整理的个人笔记。配合着《python高级编程》和网上的文章，整理一下（有连接的我会给出连接）。并且保持持续更新。

## 1. [类的初始化](http://python.jobbole.com/86506/)

- 实例化级别：`__init__(self)`
- 类级别：`__new__(cls)`

> `__new__`方法主要是当你继承一些不可变的class时(比如int, str, tuple)， 提供给你一个自定义这些类的实例化过程的途径。

```python
class PositiveInteger(int):
    def __new__(cls, value):
        return super(PositiveInteger, cls).__new__(cls, abs(value))

i = PositiveInteger(-3)
print(i)
```

> 除此之外，因为是针对类级别的，所以可以用来实现别的，例如单例模式。

```python
class Singleton(object):
    def __new__(cls,*args,**kwgs):
        # 关键在于这，每一次实例化的时候，我们都只会返回这同一个instance对象
        if not hasattr(cls, 'instance'): # 针对类cls，是否拥有 instance对象
            cls.instance = super().__new__(cls)
        return cls.instance


obj1 = Singleton()
obj2 = Singleton()

obj1.attr1 = 'value1'
print(obj1.attr1, obj2.attr1)
print(obj1 is obj2)
```

## 2. `__getattr__`/`__setattr__`/`__delattr__`实例级别

以下是我觉得比较使用的，当然，深究，[可以看这篇](http://www.jb51.net/article/86749.htm)

```python
class Test():
    def __init__(self,name):
        self.name = name
    def __setattr__(self, key, value):
        print('__setattr__:', key, value)
    def __getattr__(self, item):
        print('__getattr__',item)
    def __delattr__(self, item):
        print('__delattr__',item)

test = Test('demo') # __setattr__
test.name # 调用__getattr__
del test.name # __delattr__
```

## 3. `__repr__(self)`和`__str__(self)`交互信息

推荐使用`__str__(self)`，因为这是针对用户交互。

```python
class Test():
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'My name is Test()'
test = Test('asuradong')        
print(test)
```

## 4. `__call__(self,*args,**kwargs)`类的自调用
可以使用`callable(obj)`来判断，到底有没有`__call__`

```python
class Test():
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'My name is Test()'
    def __call__(self, *args, **kwargs):
        print('Use : obj() to run myself')
test = Test('asuradong')
test() # 调用__call__
# 注意调用形式
print(callable(test))
```

## 5. [槽`__slots__`](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186739713011a09b63dcbd42cc87f907a778b3ac73000)



**要注意**:
1. `__slots__`定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
2. 除非在子类中也定义`__slots__`，这样，子类实例允许定义的属性就是自身的`__slots__`加上父类的`__slots__`。
3. 作用：限制实例的属性

```python
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
s.score = 99 # 绑定属性'score',会报错！！！
```

## 6. [神器：super()](http://python.jobbole.com/86787/)

### 6.1 简单来说
> 在类的继承中，如果重定义某个方法，该方法会覆盖父类的同名方法，但有时，我们希望能同时实现父类的功能，这时，我们就需要调用父类的方法了，可通过使用 super 来实现。

```python
class Animal(object):
    def __init__(self, name):
        self.name = name
    def greet(self):
        print ('Hello, I am %s.' % self.name)

class Dog(Animal):
    def greet(self):
        super().greet()   
        print ('WangWang...')

# 初始化实例
class Base(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
class A(Base):
    def __init__(self, a, b, c):
        super().__init__(a, b)  
        self.c = c
```

### 6.2 实现机制（真正的顺序）

**定义了下面的类继承关系：：：**

```
      Base
      /  \
     /    \
    A      B
     \    /
      \  /
       C
```

**代码实现如下：**
```python
class Base(object):
    def __init__(self):
        print ("enter Base")
        print ("leave Base")

class A(Base):
    def __init__(self):
        print ("enter A")
        super().__init__()
        print ("leave A")

class B(Base):
    def __init__(self):
        print ("enter B")
        super().__init__()
        print ("leave B")

class C(A, B):
    def __init__(self):
        print ("enter C")
        super().__init__()
        print ("leave C")

c = C()
print('真正的调用顺序：',C.mro())
```

**输出结果**
```
enter C
enter A
enter B
enter Base
leave Base
leave B
leave A
leave C
[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>]
```

> 事实上，对于你定义的每一个类，Python 会计算出一个方法解析顺序（Method Resolution Order, MRO）列表，它代表了类继承的顺序。运用的是`C3线性算法`。并且遵循下面原则。

    - 子类永远在父类前面
    - 如果有多个父类，会根据它们在列表中的顺序被检查
    - 如果对下一个类存在两个合法的选择，选择第一个父类





***

> 欢迎进一步交流本博文相关内容：<br>
GitHub地址 ：<https://github.com/AsuraDong/Blog><br>
CSDN地址 : <http://blog.csdn.net/asuradong><br>
简书地址：<http://www.jianshu.com/u/d1570f4a618a><br>
博客园地址 : <http://www.cnblogs.com/AsuraDong/>(不一定及时更新)<br>
也可以致信进行交流 : <xiaochiyijiu@163.com> <br>
欢迎关注个人微博：<http://weibo.com/AsuraDong><br>
**欢迎转载** , 但*请指明出处  :  )*

***
