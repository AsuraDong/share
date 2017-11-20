[toc]

**利用python中的socket模块中的来实现UDP协议，这里写一个简单的服务器和客户端。为了说明网络编程中UDP的应用，这里就不写图形化了，在两台电脑上分别打开UDP的客户端和服务端就可以了。**

> UDP:用户数据报协议，是一个面向无连接的协议。采用该协议不需要两个应用程序先建立连接。UDP协议不提供差错恢复，不能提供数据重传，因此该协议传输数据安全性差。

**客户端**

python3只能收发二进制数据，需要显式转码

```python
from socket import *

host  = '192.168.48.128' # 这是客户端的电脑的ip
port = 13141 #接口选择大于10000的，避免冲突
bufsize = 1024  #定义缓冲大小

addr = (host,port) # 元祖形式
udpClient = socket(AF_INET,SOCK_DGRAM) #创建客户端

while True:
    data = input('>>> ')
    if not data:
        break
    data = data.encode(encoding="utf-8") 
    udpClient.sendto(data,addr) # 发送数据
    data,addr = udpClient.recvfrom(bufsize) #接收数据和返回地址
    print(data.decode(encoding="utf-8"),'from',addr)

udpClient.close()
```

**服务器**

同样需要显式转码

```python
from socket import *
from time import ctime

host = '' #监听所有的ip
port = 13141 #接口必须一致
bufsize = 1024
addr = (host,port) 

udpServer = socket(AF_INET,SOCK_DGRAM)
udpServer.bind(addr) #开始监听

while True:
    print('Waiting for connection...')
    data,addr = udpServer.recvfrom(bufsize)  #接收数据和返回地址
    #处理数据
    data  = data.decode(encoding='utf-8').upper()
    data = "at %s :%s"%(ctime(),data)
    udpServer.sendto(data.encode(encoding='utf-8'),addr)
    #发送数据
    print('...recevied from and return to :',addr)

udpServer.close()
```

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
