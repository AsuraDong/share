[toc]

> **发布一个版本时，我们通常先在版本库中打一个标签（tag）**，这样，就唯一确定了打标签时刻的版本。将来无论什么时候，取某个标签的版本，就是把那个打标签的时刻的历史版本取出来。所以，标签也是版本库的一个快照。<br>
和commit相比，标签更容易记住和使用，而不是那一串hash值。标签的创建和删除很简单，直接记录一下命令吧

## 基本的创建和删除

查看标签：`git tag`查看所有标签。`git show tagname`查看对应的标签的详细内容

创建标签：`git tag  tagname` 默认是指向`HEAD`。可以通过`git log --pretty=oneline`查看commitID后，再`git tag tagname commitID`来对对应的commit打标签。

标签说明：`git tag -a tagname -m "一些说明"`。为每个标签增加说明。也可以简写成`git tag tagname -m "一些说明"`。


删除标签：`git tag -d tagname`。删除对应的标签。

## 远程推送

推送远程标签：`git push origin tagname`推送一个标签。`git push origin --tags`推送所有标签。

删除远程标签：
    1. 本地删除：`git tag -d tagname`
    2. 推送： `git push origin :refs/tags/<tagname>`。
