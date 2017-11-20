### 1. 查看是否安装和安装
1. 输入：`git`即可。
2. 如果没有安装，使用`sudo apt install git`。

### 2. 配置git
1. 配置用户名字：`git config --global user.name xxx`
2. 配置用户邮箱：`git config --global user.email email`

*以上两种方法是全局配置，即所有的git仓库都是相同的name和email。如果只想在当前仓库配置，去掉`--global`即可。*

### 3. 生成公钥
1. 生成：`ssh-keygen -C yourOwnEmail -t rsa`
    - -C 是备注，一般使用邮箱 
    - -t 公钥格式

2. 查找：进入用户目录下的`.ssh`文件，找到`id_rsa.pub`，打开即可，然后复制到git服务器上：`gedit ~/.ssh/id_rsa.pub`

### 4. 克隆仓库应该注意
应当克隆ssh地址。在windows下，没有关系。但是在linux下，如果克隆的时网址，那么每次push都要输入密码。
