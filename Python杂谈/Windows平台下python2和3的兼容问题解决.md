[toc]

> 很多朋友都安装了python2和3，因为用些库例如scapy，不是scrapy，python3下面都是错，那么怎么让python2和3共存呢。

**像一般的程序员，达到如下效果**
- Windows平台下的兼容问题
- CMD可以分别进入python2和3的交互模式
- CMD可以正常使用pip对应的python2和3版本

**请按照步骤操作**
1. 确保把python2和3的路径添加到环境变量中
` C:\Python27\;C:\Python27\Scripts\;C:\Python36\Scripts\;C:\Python36\Scripts\ `
2. 将对应文件中的python.exe命名为python2.exe/python3.exe，将对应Scripts中的pip.exe命名为pip2/pip3.exe，这时候 *重启系统*
3. 打开命令行界面，输入python2/python3，成功进入！！！
4. 最后一步，查看pip
` pip `
` pip2 `
...
发先都不行，哎，被百度坑了
5. 重新装python2/3，python3可能卸载不了，先把他rapair之后再卸载。

**以上就是我被坑的过程，珍爱生命，远离百度**
**下面是正解**

- 安装完python2/3后，你会发现在Windows文件下多了一个* py.exe *的程序，这是官方正解。
- 以后命令行就可以按照下面命令操作了
` py -2 ` 进入python2的编辑界面
` py -3 `同理
` py -2 -m pip的各种命令 `python2运行pip
` py -3 -m pip的各种命令 `同理
` py -2 -m onefile.py `以python2运行onefile.py
` py -3 -m onefile.py ` 同理

**建议小伙伴多去[知乎](https://www.zhihu.com/question/21653286)看看，特记此坑，已警后人**
