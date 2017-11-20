[toc]

> 这是**python3下**的MySQL基本操作。其他类型的数据库用法基本一样。就是库的名字不同。因为python官方很早之前就规定了数据库第三方库的借口，来避免API混乱的情况。

## 安装与准备
> 这是python3的库，所以windows下安装不会像python2那样各种奇葩VC错误。是比较方便的傻瓜安装。

- Windows平台下: `py -3 -m pip install PyMySQL`
- Linux：`python3 pip install PyMySQL`

当然，引入的时候：`import pymysql`

***

## 数据库连接对象connection
| Function | 描述 |
| - | - | 
| connection | 创建connection对象 | 
| cursor() | 使用该链接创建+返回游标 | 
|commit()|提交当前事务|
|rollback()|回滚当前十五|
|close()| 关闭连接|


介绍一下connection的参数
1. host mysql服务器地址
2. port 数字类型 端口
3. user 用户名
4. passwd 密码
5. db 数据库名称
6. charset 连接编码，**需要显式指明编码方式**


上一段代码示例：
```python
conn = pymysql.Connect(host='127.0.0.1',port=3306,user='root',passwd='dyx240030',db='imooc',charset='utf8')
cursor = conn.cursor()
print(conn)
print(cursor)
cursor.close()
conn.close()
```
    OUT:
    <pymysql.connections.Connection object at 0x00000051C15BFDA0>
    <pymysql.cursors.Cursor object at 0x00000051C15BFD68>
    
***

## 数据库游标对象cursor
| Function | 描述 |
| - | - | 
|execute(op[,args])|执行一个数据库查询和命令|
|fetchone()|取得结果集下一行|
|fetchmany(size)|取得结果集size行|
|fetchall()|取得结果集剩下所有行|
|rowcount  |最近一次execute返回数据的行数或影响行数|
|close()| 关闭cursor|

代码实现：
```python
conn = pymysql.Connect(host='127.0.0.1',port=3306,user='root',passwd='dyx240030',db='imooc',charset='utf8')
cursor = conn.cursor()
sql = "select * from user"
cursor.execute(sql)
print("cursor.excute:",cursor.rowcount)

rs = cursor.fetchone()
print("rs:",rs)

for each in cursor.fetchmany(2):
    print(each)
print()
for each in cursor.fetchall():
    print(each)
```
    OUT:
    cursor.excute: 4
    rs: ('1', 'name1')
    ('2', 'name2')
    ('3', 'name3')
    
    ('4', 'name4')
    
***

## 更新数据库insert/update/delete
> 不同于select操作，这三个操作修改了数据库内容，所以需要*commit()*，否则数据库没有做相应的更改，但是也不会报错。<br>

按照一般的思路，一般是以下套路：
1. 关闭自动commit:conn.autocommit(False)
2. 出现：conn.rowback()回滚
3. 未出现：conn.commit()

下面这段脚本，实现insert/update/delete操作。其实这种检错模式不对，这里只做简单raise，后面有更好的方法。
```python
conn = pymysql.Connect(host='127.0.0.1',port=3306,user='root',passwd='dyx240030',db='imooc',charset='utf8')
conn.autocommit(False)
cursor = conn.cursor()

sqlInsert = "insert into user(userid,username) values('6','name6')"
sqlUpdate = "update user set username='name41' where userd='4'"
sqlDelete = "delete from user where userid='1'"
try:
    cursor.execute(sqlInsert)
    print(cursor.rowcount)
    cursor.execute(sqlUpdate)
    print(cursor.rowcount)
    cursor.execute(sqlDelete)
    print(cursor.rowcount)
    
    conn.commit()
except Exception as e:
    print("Reason:",e)
    conn.rollback()
    
cursor.close()
cursor.close()
```
    [OUT]:
    1
    Reason: (1054, "Unknown column 'userd' in 'where clause'")
    

## 实例 银行转账
> 可以看一下类思想的SQL操作，其中之前提到过的高级报错模式用到了之前看似无用的`rowcount`函数，通过查看操作对于数据库的影响来检错。

```python
import os
import sys
import pymysql

class transferMoney(object):
    def __init__(self,conn):
        self.conn = conn
    def transfer(self,sourceID,targetID,money):
        #   其他函数中若是有错会抛出异常而被检测到。
        try:
            self.checkIdAvailable(sourceID)
            self.checkIdAvailable(targetID)
            self.ifEnoughMoney(sourceID,money)
            self.reduceMoney(sourceID,money)
            self.addMoney(targetID,money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e
    def checkIdAvailable(self,ID):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where id = %d" % ID #select语句判断可以用len(rs)
            cursor.execute(sql)
            rs=  cursor.fetchall()
            if len(rs) != 1:#   数据库类思想的报错模式，检查操作对数据库的影响条目。没有达到目标，抛出异常
                raise Exception("账号 %d 不存在"%ID)
        finally:
            cursor.close()
        
    def ifEnoughMoney(self,ID,money):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where id = %d and money>=%d" % (ID,money)
            cursor.execute(sql)
            rs=  cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账号 %d 不存在 %d Yuan"%(ID,money))
        finally:
            cursor.close()
    
    def reduceMoney(self,ID,money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money = money-%d where id=%d"%(money,ID)
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception("失败减钱")
        finally:
            cursor.close()
    
    def addMoney(self,ID,money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money = money+%d where id=%d"%(money,ID)
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception("失败加款")
        finally:
            cursor.close()
    

if __name__=="__main__":
    if len(sys.argv)>=2:
        sourceID = int(sys.argv[1])
        targetID = int(sys.argv[2])
        money = int(sys.argv[3])

        conn = pymysql.Connect(host='127.0.0.1',port=3306,user='root',passwd='dyx240030',db='imooc',charset='utf8')
        trMoney = transferMoney(conn)

        try:
            trMoney.transfer(sourceID,targetID,money)
        except  Exception as e:
            print("出现问题"+str(e))
        finally:
            conn.close()
```

***

## 我踩过的坑。。。(这里是Python3哦)

##### 'NoneType' object has no attribute 'encoding' ，之前指明的charset必须是"UTF8",不是"utf-8"/"UTF-8"

##### MySQL语句后面必须有';'，否则不会报错，也难以发现

##### 数据库insert/update/delete操作需要commit()

##### 在构造命令的时候，注意用 " 包裹起来，因为SQL语句字符串需要 ' 包裹。所以，" 比较简单的避免歧义。


##### <p style="color:red">数据库插入带有`'`的字符串的时候，请将其替换为`''`，再执行插入</p>
