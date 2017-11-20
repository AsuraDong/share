> 相信大多数人的工作平台都是再windows的环境下。例如我的工作本就是`Win 10`(因为很多要用到地方要用到office)。除此之外，在实验室我还有一台`Ubuntu16.04 LTS`的电脑。有时候需要远程连接实验室的ubuntu进行编码工作，就需要在windows上和linux上进行相应的配置。

1. windows平台：安装`VNC Viewer`。


![1.jpg.png](./image/Windows远程控制Linux/1.jpg.png)


2. Ubuntu平台；在搜索里面打开`桌面共享`。然后配置如下。（*注意，安全的`必须对本机每次访问进行确认`可以不勾选。因为你远程的时候，肯定不在电脑旁边呀。。。*）


![2.jpg.png](./image/Windows远程控制Linux/2.jpg.png)


3. Ubuntun平台，输入：` sudo apt-get install dconf-editor`。安装 dconf-editor工具，方便配置dconf。

4. 输入`dconf-editor`打开dconf。在`org->gnome->desktop->peripherals->remote-access`中取消`requre-encryption`。


![3.jpg.png](./image/Windows远程控制Linux/3.jpg.png)


5. Windows下，打开VncViewer，然后直接输入ip地址，连通后，输入密码。
