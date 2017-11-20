[toc]

> 在处理数据的时候，遇到了大量需要处理的时间序列。比如说：数据库读取的str和time的转化，还有time的差值计算。总结一下python的时间处理方面的内容。

## 一、字符串和时间序列的转化

- `time.strptime()`：字符串=>时间序列
- `time.strftime()`：时间序列=>字符串

```python
import time
start = "2017-01-01"
end = "2017-8-12"

startTime = time.strptime(start,"%Y-%m-%d")
endTime = time.strptime(end,"%Y-%m-%d") #第二个参数format指定格式

print(startTime);print(endTime)

_start = time.strftime('%Y%m%d-%H:%M:%S',startTime)
_end = time.strftime('%Y%m%d-%H:%M:%S',endTime) #参数位置刚好相反
print(_start)
print(_end)
```

## 二、时间戳

- `time.mktime(t)`:将t转化为时间戳
- `time.localtime(s)`：将时间戳转化为时间


```python
startStamp = time.mktime(startTime) #time => 时间戳
endStamp = time.mktime(endTime)
print(startStamp)
print(endStamp)

_startTime = time.localtime(startStamp) # 时间戳 => time 
print(_startTime)
```

## 三、日期运算
**注意：时间戳是从1970年开始，以秒数为单位，所以我们的计算可以根据秒数来实现**

例如，我这里计算 startTime 和 endTime之间相差的天数：
```python
print (int((endStamp-startStamp)/(24*60*60)))
```

## 四、格式汇总
```
%a 英文星期简写
%A 英文星期的完全
%b 英文月份的简写
%B 英文月份的完全
%c 显示本地日期时间
%d 日期，取1-31
%H 小时， 0-23
%I 小时， 0-12 
%m 月， 01 -12
%M 分钟，1-59
%j 年中当天的天数
%w 显示今天是星期几
%W 第几周
%x 当天日期
%X 本地的当天时间
%y 年份 00-99间
%Y 年份的完整拼写
```

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
