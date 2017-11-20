[toc]

**利用python3来实现TCP协议，和UDP类似。UDP应用于及时通信，而TCP协议用来传送文件、命令等操作，因为这些数据不允许丢失，否则会造成文件错误或命令混乱。下面代码就是模拟客户端通过命令行操作服务器。客户端输入命令，服务器执行并且返回结果。**

> TCP（Transmission Control Protocol 传输控制协议）:是一种面向连接的、可靠的、基于字节流的传输层通信协议，由IETF的RFC 793定义。

**TCP客户端**

```python
from socket import *

host  = '192.168.48.128'
port  = 13141
addr = (host,port)
bufsize=1024

tcpClient = socket(AF_INET,SOCK_STREAM) # 这里的参数和UDP不一样。
tcpClient.connect(addr) #由于tcp三次握手机制，需要先连接

while True:
    data  = input('>>> ').encode(encoding="utf-8")
    if not data:
        break
    # 数据收发和UDP基本一致
    tcpClient.send(data) 
    data = tcpClient.recv(bufsize).decode(encoding="utf-8") 
    print(data)

tcpClient.close()
```

**TCP客户端**

```python
from socket import *
from time import ctime
import os 

host = ''
port = 13140
bufsize = 1024
addr = (host,port)

tcpServer = socket(AF_INET,SOCK_STREAM)
tcpServer.bind(addr)
tcpServer.listen(5) #这里设置监听数为5(默认值),有点类似多线程。

while True:
    print('Waiting for connection...')
    tcpClient,addr = tcpServer.accept() #拿到5个中一个监听的tcp对象和地址
    print('[+]...connected from:',addr)

    while True:
        cmd = tcpClient.recv(bufsize).decode(encoding="utf-8") 
        print('   [-]cmd:',cmd)
        if not cmd:
            break
        ###这里在cmd中执行来自客户端的命令，并且将结果返回###
        cmd = os.popen(cmd) ###os.popen(cmd)对象是file对象子类，所以可以file的方法
        cmdResult = cmd.read()
        cmdStatus = cmd.close()
        #################################################
        data = cmdResult if (not cmdStatus) else "ERROR COMMAND"
        tcpClient.send(data.encode(encoding="utf-8"))

    tcpClient.close() #
    print(addr,'End')
tcpServer.close() #两次关闭，第一次是tcp对象，第二次是tcp服务器
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
