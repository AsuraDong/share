[toc]

> 记录一下Python**函数式编程**，**高级的几个BIF**，**高级官方库**方面的用法和心得。

# 函数式编程
> 函数式编程是使用一系列函数去解决问题，按照一般编程思维，面对问题时我们的思考方式是“怎么干”，而函数函数式编程的思考方式是我要“干什么”。很多好用的函数很大程度节约了编程成本。

## 函数参数问题

总结来说就三种基本的情况：
- `fun(a,b)`
- `fun(a,*b)`：b是可迭代对象
- `fun(a,**b)`：b是带有检索的迭代对象，在函数体内部解析的时候类似字典

其他的情况基本是上面的改动，注意`fun(*a,**b)`这种形式是任意参数。

```python
ls = [i for i in range(10)]
def fun1(a,*b):
    for i in b:
        print(a,i)
fun1(1,*ls)

def fun2(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
fun2('AsuraDong',12,参数="random")
```

## 匿名函数：lambda

1. 没有return返回值，返回值就是表达式的值
2. 函数没有名字，不必担心函数名冲突
3. 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数

```python
fun = lambda x:x+1
print(fun(5)) #6

fun2 = lambda x,y:x*y
print(fun2(5,2)) #10
```

## 装饰器：@
> 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

### 没有参数的装饰器

```python
# 定义一个装饰器
def log(func):
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')
    
now()
```

注意装饰器的内部逻辑关系（调用顺序）：**log()->return wrapper -> wrapper() -> return func() -> now()**

### 含参数的装饰器

```python

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log("可爱的参数")
def now():
    print('2015-3-25')
    
```

### 进一步完善：保留函数的内置方法__name__不改变

如果调用`now.__name__`，得到的结果是`wrapper`而不是我们希望的`now`（本来函数的名字）。显然这与我们的初衷相背离。这是需要在`wrapper`前面加上functools库里的`@functools.wraps(func)`。

```python
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):            
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log("可爱的参数")
def now():
    print('2015-3-25')
    
print(now.__name__)
```

### 装饰器用途

**除了之前讲的可以让代码更容易理解之外（但是确实不好写），还有什么作用？本来我也觉得没啥用。。。直到后来接触NLTK，里面有一个`@memorize`装饰器，在递归的时候可以自动保留每次的结果，避免了手动去完善代码（可以去翻之前的博客）。所以用处还是很大的。**


***

> 欢迎进一步交流本博文相关内容：<br>
GitHub地址 ：<https://github.com/AsuraDong/Blog><br>
CSDN地址 : <http://blog.csdn.net/asuradong><br>
简书地址：<http://www.jianshu.com/u/d1570f4a618a><br>
博客园地址 : <http://www.cnblogs.com/AsuraDong/>(不一定及时更新)<br>
也可以致信进行交流 : <xiaochiyijiu@163.com> <br>
欢迎关注个人微博：<http://weibo.com/AsuraDong><br>
**欢迎转载** , 但*请指明出处 &nbsp;:&nbsp;&nbsp;)*

***

# BIF：内建的函数(built-in functions)

## zip：将两个迭代对象合成一个迭代对象

注意：**多余的没有匹配的迭代元素会被自动舍弃**

```python
a = [1,2,3]
b = 'avsss'
for i in zip(a,b):
    print(i)
for i,j in zip(a,b):
    print('Index:',i,"; Item:",j)
```

## enumerate：返回的是迭代对象，由位置+元素构成

```python
for i,j in enumerate(b):
    print("Index:",i,":Item:",j)
```

## filter：过滤函数

**两个参数，第一个是函数，第二个是一个可迭代对象。返回的值是一个可迭代对象，其中的每个元素是参数中迭代对象的每个元素在参数中的函数返回值为True的元素。（有点乱，看代码）**

```python
list(filter(lambda m:m%2==0,range(1,6)))
```

结果是[2,4]

## map：映射函数

用法和filter类似，区别如下：
- 参数里面的函数作用是对迭代对象每个元素操作
- 返回的被操作过的迭代对象

```python
list(map(lambda m:m**2,range(1,6)))
```
结果是[1, 4, 9, 16, 25]

## reduce
- 在functools库里
- func接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

```python
#一道经典的1+2+..+100的例题
from functools import reduce

add = lambda x,y : x+y

ls = [i for i in range(1,101)]
print(reduce(add,ls))
```

# sorted：排序函数

> 非常重要，主要是在对**参数的调整**上做工作，甚至可以实现对**类对象**的排序。

## 基本排序和倒序

默认的排序是从小到大，如果需要从大到小，那么应该修改`reverse`参数为`True`。

```python
print(sorted([-1,0,-100],reverse = True))
print(sorted([-1,0,-100]))
```

## key参数

key参数来指定一个函数，此函数将在每个元素比较前被调用。

```python
sorted([-1,0,-100],key = abs,reverse = True)#对绝对值的大小进行排序

student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]
print(sorted(student_tuples, key=lambda student: student[2])) #按数字排序

```

按照这个思路，可以实现对类的排序。当然这是根据类中的某一类元素来进行的。

```python
class Student:
        def __init__(self, name, grade, age):
                self.name = name
                self.grade = grade
                self.age = age
        def __repr__(self):
                return repr((self.name, self.grade, self.age))
            
student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
]

sorted(student_objects, key=lambda student: student.age) 
```

## 多级排序
如果你想根据类里面的多个元素或者迭代对象中的多个元素来排序，那么就需要`operator`库里面的两个函数。应该注意的是它们的参数对应的是名字还是位置。并且排序为了避免二义性，都是先以第一个参数为基础依次进行排序。

```python
from operator import itemgetter,attrgetter
class Student:
        def __init__(self, name, grade, age):
                self.name = name
                self.grade = grade
                self.age = age
        def __repr__(self):
                return repr((self.name, self.grade, self.age))
            
student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
]
student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]
print(sorted(student_objects, key=attrgetter('name','age'))) 
print(sorted(student_tuples, key=itemgetter(1,2)))
```

# 高级官方库

## itertools

> itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算

### itertools.count(start=0,step=1)

默认是从0开始，间隔为1。

```python
import itertools
natuals = itertools.count(0)
for i in natuals:
    print (i)
```

这段代码会一直打印下去，直到遇到终止。

### itertools.cycle(iterator)

将iterator中的元素无限循环下去。

```python
cc = itertools.cycle('456')
for c in cc:
	print(c)
```

### itertools.repeat(obj[,最大重复次数])

将obj默认无限重复。

```python
np = itertools.repeat('1A.', 3)
for i in np:
	print(i)
```

### itertools.chain(a,b,..,n,...)

将迭代器abc串联起来，形成一个新的迭代器。

```python
a = [1,2]
b =[3,4]
for i in itertools.chain(a,b):
	print(i)

c = {"fef":1}
for i in itertools.chain(a,b,c):
	print(i)
```


### itertools.groupby(iterator)

将iterator中相邻的重复元素挑出来。所以，如果想对一个迭代对象查找不重复的元素，可以县排序，再调用这个方法。

```python
for i in itertools.groupby('ABCA'):
	print(i)
```

### itertools.takewhile(func,iterator)

无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列

```python
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x :x<=10,natuals)
print(list(ns))
```

### 组合生成器

迭代器         	|	参数                      |  结果
-|-|-
|product()       		|p, q, ... [repeat=1]        |cartesian product, equivalent to a nested for-loop
|permutations()      |p[, r]                      |r-length tuples, all possible orderings, no repeated elements
combinations()  |	p, r      |                  r-length tuples, in sorted order, no repeated elements 
combinations_with_replacement() |p, r     |   r-length tuples, in sorted order, with repeated elements
product('ABCD', repeat=2)     |         |     AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
permutations('ABCD', 2)          |         |  AB AC AD BA BC BD CA CB CD DA DB DC
combinations('ABCD', 2)            |       |  AB AC AD BC BD CD
combinations_with_replacement('ABCD', 2)  | |  AA AB AC AD BB BC BD CC CD DD

## collections

> 里面收集了很多常用的数据结构，例如计数器、队列、顺序字典等等。而这些很多继承于基本的数据结构，所以可以调用对应的BIF。

### Counter：计数器

用法如下：

```python
from collections import *
c  = Counter()
for ch in 'this is a string':
	c[ch]+=1 #自动生成对应的键和值，值默认为0.每次出现则加1

print(c)
```

结果是：Counter({'i': 3, 's': 3, ' ': 3, 't': 2, 'h': 1, 'a': 1, 'r': 1, 'n': 1, 'g': 1})

### deque：队列

高效实现插入和删除操作的双向列表，适合用于队列和栈。如果数据量大而插入删除操作又多，可以使用deque。并且他继承了list的方法。

多出的两种常用方法：
1. appendleft(obj):Add an element to the left side of the deque.
2. popleft():Remove and return the rightmost element.

### namedtuple

> namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。

我们知道tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成：`p = (1,2) `。但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。定义一个class又小题大做了，这时，namedtuple就派上了用场：

```python
>>> from collections import namedtuple
>>> Point = namedtuple('Point', ['x', 'y'])
>>> p = Point(1, 2)
>>> p.x
1
>>> p.y
2
>>> isinstance(p, Point)
True
>>> isinstance(p, tuple)
True
```

### defaultdict：key不存在时的dict

```python
from collections import defaultdict
dd = defaultdict(lambda: 'N/A') #默认值是调用函数返回的，而函数在创建defaultdict对象时传入
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['不存在的'])
```

### OrderedDict：留有顺序的字典

顺序是添加键值对的顺序，这样，在迭代的时候可以保持顺序。并且可以实现先入先出等类似的字典对象。

```python
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d) # dict的Key是无序的

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od) # OrderedDict的Key是有序的

```
