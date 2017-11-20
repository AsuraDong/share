[toc]

## 1. QQ登陆面板
> 为了简单，这里没有使用太多的图片和复杂的样式。全部的代码可以来我的[github来看看](https://github.com/AsuraDong/font-design/tree/master/1.7qq%E7%89%B9%E6%95%88%E5%92%8C%E6%8A%BD%E5%A5%96%E7%89%B9%E6%95%88)。

### 1.1 效果图和功能
功能： 
- 支持拖拽
- 可以切换登陆状态
- 能够退出

效果图：
![qq登陆面板.png](./image/js鼠标事件(QQ登陆面板)和键盘事件(抽奖系统)/qq登陆面板.png)

### 1.2 鼠标事件
- `mousemove`:鼠标指针在元素内部移动时候重复的触发。
- `mousedown`:当用户按下鼠标的任意按钮时，都会触发。
- `mouseup`:与`mousedown`相反，可用来取消`mousedown`。

### 1.3 日常贴代码
webqq.html
```html
<html>
    <head>
        <meta charset="utf-8"/>
        <title>网页QQ</title>
        <script type="text/javascript" src="drag.js"/></script>
        <link rel="stylesheet" type="text/css" href="sea.css">
    </head>
    <body>
        <div class="login-panel">
            <div style="position:relative;height=0px;">
                <div id="exit-login"></div>
            </div>
            <div class="panel-header">
                网页QQ登陆界面
            </div>
            <div class="panel-container">
                <div class="input">
                账号：<input type="text" name="id" placeholder="QQ账号或邮箱"/>
                </div>
                <div class="input">
                密码：<input type="password" name="pass" placeholder="登陆密码"/>
                </div>
            </div>
            <div class="panel-submit">
                <div class="login-submit">
                    <input type="submit" value="登陆">
                </div>
                <ul class="login-state">
                    <li class="show-state">我在线上</li>
                    <li class="hide-state">隐身</li>
                    <li class="hide-state">免打扰</li>
                    <li class="hide-state">目前忙碌</li>
                </ul>
            </div>
        </div>
    </body>
</html>
```

drag.js
```javascript
function fnDown(event){
    event = event || window.event;
    var my_drag = document.getElementsByClassName("login-panel")[0],
        offset_x = event.clientX-my_drag.offsetLeft,
        offset_y = event.clientY-my_drag.offsetTop;
    // 在对象移动的时候持续的触发
    document.onmousemove = function(event){
        event = event || window.event;
        // document.title = event.clientX+","+event.clientY;
        let left = event.clientX-offset_x,
            top = event.clientY-offset_y;
        let window_width = document.documentElement.clientWidth || document.body.clientWidth;
            window_height = document.documentElement.clientHeight|| document.body.clientHeight;
        let max_left = window_width - my_drag.offsetWidth,
            max_top = window_height - my_drag.offsetHeight;
        if(top<10){
            top = 10;
        } else if (top>=max_top-10 ){
            top = max_top-10;
        }
        if (left<10){
            left = 10;
        } else if(left>=max_left-10){
            left = max_left-10;
        }
        my_drag.style.left = left+"px";
        my_drag.style.top = top+"px";
    }
    document.onmouseup = function(){
        document.onmousemove = null;
        document.onmouseup = null;
    }
}

function loginFunc(){
    let panel_submit = document.getElementsByClassName("panel-submit")[0],
        li_arr = panel_submit.getElementsByTagName("li");
    if(this.className==="show-state"){
        for(let i=0;i<li_arr.length;++i){
            li_arr[i].className = "";
        }
    } else {
        for(let i=0;i<li_arr.length;++i){
            li_arr[i].className = "hide-state";
        }
        this.className="show-state";
    }

}

function drag(){
    let my_title = document.getElementsByClassName("panel-header")[0];
    my_title.onmousedown = fnDown; // 在鼠标按下时触发

    let panel_submit = document.getElementsByClassName("panel-submit")[0],
        li_arr = panel_submit.getElementsByTagName("li");
    
    for(let i=0;i<li_arr.length;++i){
        li_arr[i].onclick = loginFunc;
    }
    let exit_logo = document.getElementById("exit-login");
    exit_logo.onclick = function(){
        let  login_panel = document.getElementsByClassName("login-panel")[0];
        login_panel.style.display = "none";
    }
}

window.onload = drag;
```

sea.css
```css
*{
    margin:0;
    padding:0;
}

.login-panel{
    height: 150px;
    width:300px;
    position: absolute;
    left: 550px;
    top:200px;
    background: rgba(226, 239, 243, 0.89);
    border-top-left-radius: 20px;
    border-bottom-left-radius: 20px;
    border-bottom-right-radius: 20px;
}

#exit-login{
    position: absolute;
    top:-8px;
    right: -8px;
    cursor: pointer;
    background: url("./images/exit-login.png") no-repeat;
    height: 25px;
    width:25px;
}

.panel-header{
    font-weight: 400;
    line-height: 1.8em;
    margin:0 auto;
    height: 50px;
    line-height: 50px;
    text-align:center;
}

.panel-container{
    margin:0 auto;
}

    .panel-container .input{
        margin:0 auto;
        width:210px;
        font-weight: 800;
    }



.panel-submit .login-submit{
    margin:15px auto;
    width:50%;
    text-align: center;
    float: left;
}

.panel-submit .login-state{
    list-style-type: none;
    float: right;
    margin:16px auto;
    width:40%;
    font-size:13px;
    line-height: 1.2em;
}
.login-state li{
    text-align: center;
    padding:3px;
    width:70px;
    background: #ADCFF8
}

    .login-state li:hover{
        background: #81AFE7;
        cursor: pointer;
    }

    .login-state .hide-state{
        display: none;
        
    }
```


## 2. 抽奖系统

### 2.1 效果和功能
功能：
- 按下开始和结束按钮可以抽奖
- 按下回车可以开始/结束抽奖

效果图：
![抽奖特效.png](./image/js鼠标事件(QQ登陆面板)和键盘事件(抽奖系统)/抽奖特效.png)

### 2.2 键盘事件
![键盘事件.png](./image/js鼠标事件(QQ登陆面板)和键盘事件(抽奖系统)/键盘事件.png)

### 2.3 贴代码
index.html
```html
<!DOCTYPE>
<html>
    <head>
        <title>抽奖系统</title>
        <meta charset="utf-8"/>
        <link rel="stylesheet" type="text/css" href="sea.css">
        <script src="script.js"></script>
    </head>
    <body>
        <div id="prize">
            开始抽奖！
        </div>
        <div class="btns">
            <span id="start" style="margin-right:20px;">开 始</span>
            <span id="end">结 束</span>
        </div>
    </body>
</html>
```

script.js
```javascript
let prize_arr = ["iPhone-X","Ipad","谢谢参与","充气娃娃","谢谢参与","震动棒","QQ靓号","100元现金"],
    timer = null,
    flag = 0 // flag代表第几次敲击键盘
    ;

function startPrize(){
    let prize = document.getElementById("prize");
    /*
    每次添加定时器之前，一定要将之前的定时器关闭。否则，变化会过快。
    */
    clearInterval(timer); 
    // var self = this;
    timer = setInterval(function(){
        let index = Math.floor(Math.random()*prize_arr.length);
        prize.innerHTML = prize_arr[index];
    },50);
    // 这种方法错误。因为对于键盘事件，this指的是键盘，他没有background属性
    // self.style.background = "#999";
    // self.style.cursor = "auto";
    start.style.background = "#999";
    start.style.cursor = "auto";
}

function stopPrize(){
    clearInterval(timer);
    start.style.background = "#036";
    start.style.cursor = "pointer";
}

window.onload = function(){
    let start = document.getElementById("start"),
        end = document.getElementById("end");
    // start to play
   start.onclick = startPrize;
   // end 
   end.onclick = stopPrize;

    /*
    键盘事件：由于我们这里需要检测整个网页，所以绑定对象是document
    */
    document.onkeyup = function(event){
        event = event || window.event;
        // console.log(event.keyCode);
        // 使用这条语句来确定键对应的编码
        if(event.keyCode===13){
            if (flag===0){
                startPrize();
                flag = 1;
            } else {
                stopPrize();
                flag = 0;
            } 
        }
    }
}
```

sea.css
```css
*{
    margin: 0;
    padding: 0;
}

#prize{
    width:400px;
    height: 70px;
    line-height: 70px;
    margin:0 auto;
    padding:30px 0;
    text-align: center;
    font-weight: bold;
    font-size:25px;
    color: #ff0000;
}

.btns{
    width: 220px;
    height: 30px;
    margin:0 auto;
}

.btns span{
    display: block;
    float: left;
    width: 100px;
    height: 30px;
    line-height: 30px;
    text-align: center;
    color:#fff;
    background: #003366;
    font-size:14px;
    cursor: pointer;
}


```




