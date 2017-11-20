[toc]

[TOC]

## 创建仓库
创建新文件夹：`mkdir learngit`

进入：`cd learngit`

**`ls`发现没有任何东西：`git init` 将这个文件夹设置为git文件夹。目录下面会出现.git 的隐藏文件**

---

## 创建文件/文件夹
当移入/创建新的文件和文件夹时，需要`git add file`

然后，`git commit -m 说明`将文件提交到当前分支。执行命令前后的区别，可以通过`git status`来查看。

---

## 修改文件/文件夹

当修改文件内容的时候，调用`git status`会发现modified:，说明没有提交到当前分支。

此时，可以`git diff 修改的文件名`，来查看文件哪里进行了修改。

当然，最后还是需要先`git add file`,再`git commit -m 说明`一下。

查看`git status`的结果的最后应该是：`working directory clean`


---

## 回到修改前的版本

`git log`:可以查看最近到最远的提交日志。如果嫌输出信息太多，看得眼花缭乱的，可以试试加上--pretty=oneline参数,使用`git log --pretty=oneline`

> 需要友情提示的是，你看到的一大串类似3628164...882e1e0的是commit id（版本号），和SVN不一样，Git的commit id不是1，2，3……递增的数字，而是一个SHA1计算出来的一个非常大的数字，用十六进制表示，而且你看到的commit id和我的肯定不一样，以你自己的为准。为什么commit id需要用这么一大串数字表示呢？因为Git是分布式的版本控制系统，后面我们还要研究多人在同一个版本库里工作，如果大家都用1，2，3……作为版本号，那肯定就冲突了。

`git reset --hard 一段commit_id的缩写`：重回对应的版本，不需要全部的commit_id,只要前几位可以区分就行。嫌麻烦的话，可以`git reset --hard HEAD~num`，例如 `git reset --hard HEAD~100`回退到前100个版本。

---

## 撤销修改

`git checkout -- file`:如果只是想在没有`commit`提交之前撤销修改，这条命名会让文件撤销修改。<br>
注意，必须有 \-\- ，否则就是切换分支了。

---

## 删除文件

如果手动删除了文件/命令行`rm file`删除了文件
1. 如果想彻底删除：`git rm file`，然后再`git commit -m "..."` 提交到版本库
2. 不小心删错了：`git checkout -- file` 恢复即可。

---

## 工作区、暂存区、版本区

[请访问廖大大的博客](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013745374151782eb658c5a5ca454eaa451661275886c6000)


***

> 欢迎进一步交流本博文相关内容：<br>
博客园地址 : <http://www.cnblogs.com/AsuraDong/><br>
CSDN地址 : <http://blog.csdn.net/asuradong><br>
也可以致信进行交流 : <xiaochiyijiu@163.com> <br>
**欢迎转载** , 但*请指明出处 &nbsp;:&nbsp;&nbsp;)*

***
