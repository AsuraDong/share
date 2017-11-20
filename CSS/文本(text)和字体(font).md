[toc]

## 1. 文本

### 1.1 文本缩进:text-indent
> 可以设置为正值，**负值**，百分比和inherit。可以为所有的块级元素应用text-indent，但是行内元素不可以，**自动继承父元素的text-indent。**

设置负值的时候，为了避免溢出，可以**针对负缩进再设置一个外边距或一些内边距**：`p {text-indent: -5em; padding-left: 5em;}`

### 1.2 文本对其:text-align
> 值 left、right 和 center 会导致元素中的文本分别左对齐、右对齐和居中。注意`justify`的应用。

#### 1.2.1 文本两边对齐:justify

w3school上justify的解释如下：
> 在两端对齐文本中，文本行的左右两端都放在父元素的内边界上。然后，调整单词和字母间的间隔，使各行的长度恰好相等。您也许已经注意到了，两端对齐文本在打印领域很常见。

但是我在实现的时候，并没有显示出来效果，主要是因为：**text-align不会处理被打断的行和最后一行。如果你这里的文字只占了一行，所以也是最后一行了，所以text-align设置为justify不会产生任何效果。**


解决方法：
1. 将`text-align-last`设置成justify。但不一定所有的浏览器都支持。
    ```html
    <!DOCTYPE>
    <html>
    <head>
    <meta charset="utf-8"/>
    <style type="text/css">
    p.center {
      text-align:justify;
      text-align-last:justify;
    }
    </style>
    </head>
    
    <body>
    <p class="center">我是两端对齐文字端对齐文字</p>
    </body>
    
    </html>
    ```
2. 在文本最后添加一个宽度为100%的行内标签，来作为最后一行。
    ```html
    <!DOCTYPE>
    <html>
    <head>
    <meta charset="utf-8"/>
    <style type="text/css">
    p.center {
      text-align:justify;
    }
    p>span {
      display:inline-block;
      width:100%;
    }
    </style>
    </head>
    
    <body>
    <p class="center">我是两端对齐文字端对齐文字<span></span></p>
    </body>
    
    </html>
    ```

### 1.3 空白符处理:white-spacing
> 会影响到用户代理对源文档中的空格、换行和 tab 字符的处理。

|值	|空白符|	换行符	|自动换行|
| - | - | - | - |
|pre-line|	合并	|保留	|允许|
|normal|	合并|	忽略|	允许|
|nowrap|	合并|	忽略|	不允许||
|pre	|保留|	保留|	不允许|
|pre-wrap|	保留|	保留|	允许|

**注意自动换行，指的是是否根据元素width自动换行，如果是不允许，那么需要显式声明`<br>`标签**

### 1.4 特效:文本闪烁
> text-decoration有blink来设置文本闪烁，但是，实验并没有成功。这里还是**采用css3的动画效果来制作文本闪烁**。

```html
<!doctype>
<!-- 一断很酷炫的动态文字 -->
<html>
<head>
	<meta charset="utf-8"/>
	<title>文本闪烁</title>
	<style>
		.box{
			animation: change 1s ease-in infinite;
			font-size: 36px;
			color :#f00;
			font-weight:bold;
		}
		@keyframes change{
			0%{ text-shadow: 0 0 4px #f00}  
			50%{ text-shadow: 0 0 40px #f00}  
			100%{ text-shadow: 0 0 4px #f00}  
		}
	</style>
</head>
<body>
	<p class="box"> 一断闪烁文本</p>
</body>
</html>
```

### 1.5 更多
- 文本装饰：text-decoration
- 字符转换：text-transform
- 字间距和字母间距：word-spacing和letter-spacing
- 方向：direction。影响块级元素中文本的书写方向、表中列布局的方向、内容水平填充其元素框的方向、以及两端对齐元素中最后一行的位置。


## 2. 字体

| 标签 | 解释 |
| - | -|
| font-family | 字体 |
| font-style | 斜体：italic|
| font-weight | 字体粗细：bold(er)，light(er),inherit,100-900 |
| font-size | 字体大小 |