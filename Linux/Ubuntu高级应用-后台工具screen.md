[toc]

> 之前在putty之类的远程命令行操作服务器的时候，遇到关闭软件，对应的操作就会关闭。很多时候，就是开着电脑，然后挂在那里，虽然不用电脑跑，但是也耗电。。。主要是putty这些软件有时候会伴随黑屏崩掉。那天突然发现`screen`这款linux的后台神器，网上的教程乱七八糟（比较高级的linux用法），这里介绍常用的用法。

### 安装：`sudo apt-get install screen`

### 常用参数
- 查看screen的线程： `screen -ls`。查看用screen创建或在运行的线程
- 创建线程：`screen -S 线程名称`。**创建并且进入**了那个线程
- 线程切换：`screen -r 线程名称/id`。可以通过`screen -ls`查看一下（以防忘记）,再切换
- 删除：`kill -9 id`。用的是linux下的`kill`命令。
- 清理线程列表：`screen -wipe`。删除后的线程用`screen -ls`查看会提示`???`。这时候清除一下，list就干净了。

### 常用快捷键
`CTRL+A+D`。返回主线程。就是你想启动一个脚本，然后`screen -S scanner1`进入了scanner1里面，启动了程序。这时候，要回到原来的控制界面，需要快捷键。然后在原来的控制界面中又可以干别的事情了。

### **[更多内容](http://www.cnblogs.com/mchina/archive/2013/01/30/2880680.html)**

#### 语法

`screen [-AmRvx -ls -wipe][-d <作业名称>][-h <行数>][-r <作业名称>][-s ][-S <作业名称>]`

#### 参数说明

-A 　将所有的视窗都调整为目前终端机的大小。

-d <作业名称> 　将指定的screen作业离线。

-h <行数> 　指定视窗的缓冲区行数。

-m 　即使目前已在作业中的screen作业，仍强制建立新的screen作业。

-r <作业名称> 　恢复离线的screen作业。

-R 　先试图恢复离线的作业。若找不到离线的作业，即建立新的screen作业。

-s 　指定建立新视窗时，所要执行的shell。

-S <作业名称> 　指定screen作业的名称。

-v 　显示版本信息。

-x 　恢复之前离线的screen作业。

-ls或--list 　显示目前所有的screen作业。

-wipe 　检查目前所有的screen作业，并删除已经无法使用的screen作业。

#### 常用screen参数

screen -S yourname -> 新建一个叫yourname的session

screen -ls -> 列出当前所有的session

screen -r yourname -> 回到yourname这个session

screen -d yourname -> 远程detach某个session

screen -d -r yourname -> 结束当前session并回到yourname这个session

在每个screen session 下，所有命令都以 ctrl+a(C-a) 开始。

C-a ? -> 显示所有键绑定信息

C-a c -> 创建一个新的运行shell的窗口并切换到该窗口

C-a n -> Next，切换到下一个 window 

C-a p -> Previous，切换到前一个 window 

C-a 0..9 -> 切换到第 0..9 个 window

Ctrl+a [Space] -> 由视窗0循序切换到视窗9

C-a C-a -> 在两个最近使用的 window 间切换 

C-a x -> 锁住当前的 window，需用用户密码解锁

C-a d -> detach，暂时离开当前session，将目前的 screen session (可能含有多个 windows) 丢到后台执行，并会回到还没进 screen 时的状态，此时在 screen session 里，每个 window 内运行的 process (无论是前台/后台)都在继续执行，即使 logout 也不影响。 

C-a z -> 把当前session放到后台执行，用 shell 的 fg 命令则可回去。

C-a w -> 显示所有窗口列表

C-a t -> Time，显示当前时间，和系统的 load 

C-a k -> kill window，强行关闭当前的 window

C-a [ -> 进入 copy mode，在 copy mode 下可以回滚、搜索、复制就像用使用 vi 一样

    C-b Backward，PageUp 

    C-f Forward，PageDown 

    H(大写) High，将光标移至左上角 

    L Low，将光标移至左下角 

    0 移到行首 

    $ 行末 

    w forward one word，以字为单位往前移 

    b backward one word，以字为单位往后移 

    Space 第一次按为标记区起点，第二次按为终点 

    Esc 结束 copy mode 

C-a ] -> Paste，把刚刚在 copy mode 选定的内容贴上


***

> 欢迎进一步交流本博文相关内容：<br/>
GitHub地址 ：<https://github.com/AsuraDong/Blog><br/>
CSDN地址 : <http://blog.csdn.net/asuradong><br/>
简书地址：<http://www.jianshu.com/u/d1570f4a618a><br/>
博客园地址 : <http://www.cnblogs.com/AsuraDong/>(不一定及时更新)<br/>
也可以致信进行交流 : <xiaochiyijiu@163.com> <br/>
欢迎关注个人微博：<http://weibo.com/AsuraDong><br/>
**欢迎转载** , 但*请指明出处 &nbsp;:&nbsp;&nbsp;)*

***
