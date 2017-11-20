> 对于远程github的项目，分支是个很重要的概念。例如，常用的拉取分支的命令有`pull`和`fetch`，甚至是`git checkout -b 本地分支名x origin/远程分支名x`。那他们又有什么区别呢？为了减少水的内容，本文直截了当地进行记录了。

### 1. 下载特定分支

- 在团队协作中，如果只想下载一个分支，而不是主分支，可以这样：`git clone -b <branchname> gitsite`。例如：`git clone -b Dev https://github.com/AsuraDong/Machine-Learning.git`


### 2. 查看特定分支
- 默认查看本地分支：`git branch`
- 查看远程分支:`git branch -r`。远程分支的模式都是`origin/name`
- 查看所有分支：`git branch -a`

### 3. 不推荐的一种（不安全）

`git checkout -b 本地分支名x origin/远程分支名x`：抓取远程分支x，并创建本地分支x,然后`merge`后，进入本地分支x


### 4. `pull`命令

- `git pull <远程主机名> <远程分支名>`：取回远程分支，并与当前分支合并。例如：`git pull origin Dev`
- `git pull <远程主机名> <远程分支名>:<本地分支名>`：取回远程分支，并与指定分支合并。例如：`git pull origin Dev:Dev`

### 5.最安全的`fecth`命令

- `git fetch`：取回远程的所有分支
- `git fetch <远程主机名> <分支名>`：取回远程的对应分支

### 6. 删除远程分支

- `git push origin --delete remote_branch`
