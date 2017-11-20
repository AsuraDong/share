[toc]

### 实例：计时器和计算器
```html
<!DOCTYPE>
<html>
    <head>
        <meta charset="utf-8"/>
        <title>计时器</title>
        <script type="text/javascript">
            // 计算器函数：count
            function count(){
                var value1 = document.getElementById("value1").value;
                var value2 = document.getElementById("value2").value;
                var op = document.getElementById("select").value;
                var result = "";
                switch (op){
                    case "+":
                    result = parseFloat(value1)+parseFloat(value2);
                    break;
                    case "-":
                    result = parseFloat(value1)-parseFloat(value2);
                    break;
                    case "*":
                    result = parseFloat(value1)+parseFloat(value2);
                    break;
                    default:
                    result = parseFloat(value1)/parseFloat(value2);
                }
                document.getElementById("result").value = result;
            }
            // 计时器函数：clock
            function clock() {
                let attime;
                let time = new Date();
                attime = time.getHours()+" : "+time.getMinutes()+" : "+time.getSeconds();
                document.getElementById("clock").value = attime;
            }
            
            window.onload = function(){
                setInterval(clock,1000);
            }

        </script>
    </head>
    <body>
        北京时间：<input type="text" id="clock" readonly>
        <br/>
        计算器：
        <input type="text" id="value1">
        <select id="select">
            <option value="+">+</option>
            <option value="-">-</option>
            <option value="/">/</option>
            <option value="*">*</option>
        </select>
        <input type="text"  id="value2">
        <input type="button" value=" = " 
        onclick="count()"/>
        <input type="text" id="result"/>
    </body>
</html>
```


### `onclick`鼠标点击事件
> onclick是鼠标单击事件，当在网页上单击鼠标时，就会发生该事件。同时onclick事件调用的程序块就会被执行，通常与按钮一起使用。

```html
<!DOCTYPE HTML>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>单击事件 </title>
<script type="text/javascript">
  function openwin(){
     window.open('http://www.imooc.com','_blank','height=600,width=400,top=100,toolbar=no,left=0,menubar=no,scrollbars=no,status=no');
     }
</script>
</head>
<body>
  <form>
    <input name="点击我" type="button" value="点击我"onclick="openwin()"/>
  </form>
</body>
</html>
```

### `onmouseover`鼠标经过事件
> 鼠标经过事件，当鼠标移到一个对象上时，该对象就触发onmouseover事件，并执行onmouseover事件调用的程序。

```html
<!DOCTYPE HTML>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title> 鼠标经过事件 </title>
<script type="text/javascript">
    function message(){
      confirm("请输入密码后，再单击确定!"); }
</script>
</head>
<body>
<form>
密码:<input name="password" type="password" onmouseover="message()">
<input name="确定" type="button" value="确定"/>
</form>
</body>
</html>
```

### `onmouseout`鼠标移开事件
> 鼠标移开事件，当移入该对象再移开当前对象时，执行onmouseout调用的程序。
```html
<!DOCTYPE HTML>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>鼠标移开事件 </title>
<script type="text/javascript">
  function message(){
    alert("不要移开，点击后进行慕课网!"); }
</script>
</head>
<body>
<form onmouseout="message()">
  <a href="http://www.imooc.com">点击我</a>
</form>
</body>
</html>
```

### `onfocus`聚焦事件
> 当网页中的对象获得聚点时，执行onfocus调用的程序就会被执行。

```html
<!DOCTYPE HTML>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title> 光标聚焦事件 </title>
  <script type="text/javascript">
    var tag = 1; // 防止不停的弹框！！！
    function message(){
        if (tag){
            alert("请选择，您现在的职业！");
            tag =0;
        }
	}
  </script>
</head>
<body>
请选择您的职业：<br>
  <form>
    <select name="career" onfocus="message()">  <!-- 注意位置 -->
      <option>学生</option> 
      <option>教师</option> 
      <option>工程师</option> 
      <option>演员</option> 
      <option>会计</option> 
    </select> 
  </form>
</body>
</html>
```

### `onblur`失去焦点事件
> onblur事件与onfocus是相对事件，当光标离开当前获得聚焦对象的时候，触发onblur事件，同时执行被调用的程序。
```html
<!DOCTYPE HTML>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title> 失焦事件 </title>
<script type="text/javascript">
  function message(){
    alert("请确定已输入密码后，在移开!"); }
</script>    
</head>
<body>
  <form>
   用户:<input name="username" type="text" value="请输入用户名！" onblur = "message()">
   密码:<input name="password" type="text" value="请输入密码！" >
  </form>
</body>
</html>
```


### `onselect`选中事件
> 选中事件，**当文本框或者文本域中的文字被选中时**，触发onselect事件，同时调用的程序就会被执行。

```html
<!DOCTYPE HTML>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title> 内容选中事件 </title>
<script type="text/javascript">
  function message(){
    alert("您触发了选中事件！"); }
</script>    
</head>
<body>
  <form>
  个人简介：<br>
   <textarea name="summary" cols="60" rows="5" onselect="message()">请写入个人简介，不少于200字！</textarea>
  </form>
</body>
</html>
```
### `onchange` 文本框改变事件
> 通过**改变文本框的内容来触发onchange事件**，同时执行被调用的程序。

```html
<!DOCTYPE HTML>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title> 文本框内容改变事件 </title>
<script type="text/javascript">
  function message(){
    alert("您改变了文本内容！"); }
</script>    
</head>
<body>
  <form>
  个人简介：<br>
   <textarea name="summary" cols="60" rows="5"onchange="message()">请写入个人简介，不少于200字！</textarea>
  </form>
</body>
</html>
```

### `onload`页面加载
> 事件会在页面加载完成后，立即发生，同时执行被调用的程序。

1. 加载页面时，触发onload事件，**事件写在`<body>`标签内**。
2. 可理解为打开一个新页面时

```html
<!DOCTYPE HTML>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title> 加载事件 </title>
<script type="text/javascript">
  function message(){
    alert("加载中，请稍等…"); }
</script>    
</head>
<body onload="message()">
  欢迎学习JavaScript。
</body>
</html>
```

### `onunload`事件
> 注意是如何调用的：`window.onunload = onunload_message;`

```html
<!DOCTYPE HTML>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title> 卸载事件 </title>
<script type="text/javascript">   
     window.onunload = onunload_message;  // 看看怎么调用  
     function onunload_message(){   
        alert("您确定离开该网页吗？");   
    }   
</script>   
</head>
<body>
  欢迎学习JavaScript。
</body>
</html>
```