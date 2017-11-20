Git安装后，对于中文信息默认使用8位编码，所以看到的是如图的乱码：


![1.png](./image/Git中文乱码解决/1.png)


这是因为：**`core.quotepath`默认为`true`，对0x80以上的字符进行quote**

所以通过：**`git config --global core.quotepath false`**将其设置为`false`即可。


![2.png](./image/Git中文乱码解决/2.png)
