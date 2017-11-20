[toc]

### 表单元素 
|类型 | 描述|
| - | - |
|text|	定义常规文本输入。|
|radio|	定义单选按钮输入（选择多个选择之一）|
| checkbox | 复选框 |
|submit|	定义提交按钮（提交表单）|
| password | 密码输入 |

> `form`的属性：action（定义submit按钮的行为），method默认是GET（可以用POST）

一个例子：
```html
<html>
<body>

    <form action="/demo/demo_form.asp" method="GET"> 
    First name:<br>
    <input type="text" name="firstname">
    <br>
    Last name:<br>
    <input type="text" name="lastname">
    <br><br>
    
    <input type="radio" name="sex" value="female">Female
    <br>
    <input type="radio" name="sex" value="male">male
    <br>
    
    <input type="submit" value="提交按钮的值">
    </form>
    <p>请注意表单本身是不可见的。</p>
    
    <p>同时请注意文本字段的默认宽度是 20 个字符。</p>

</body>
</html>
```

#### 正确提交
1. 定义了action属性和method方法
2. 如果要正确提交，每个字段都必须设置一个name属性。最后相当于：`url?firstname=Mickey&lastname=Mouse`

```html
<html>
<body>
    <form action="/demo/demo_form.asp">
    First name:<br>
    <input type="text" name="firstname" value="Mickey">
    <br>
    Last name:<br>
    <input type="text" name="lastname" value="Mouse">
    <br><br>
    <input type="submit" value="Submit">
    </form> 
    <p>如果您点击提交，表单数据会被发送到名为 demo_form.asp 的页面。</p>
</body>
</html>
```

#### 组合表单数据
> 就是当下比较流行的嵌套的浏览框。结合`fieldset`和`legend`标签一起使用。

```html
<html>
<body>

<form>
<fieldset>
<legend>Outer</legend>

    <fieldset>
    <legend>Inner</legend>
    First name:<br>
    <input type="text" name="firstname" value="Mickey">
    <br>
    Last name:<br>
    <input type="text" name="lastname" value="Mouse">
    <br><br>
    <input type="submit" value="Submit">
    </fieldset>

</fieldset>
</form>

</body>
</html>
```

### HTML5表单元素

- 下拉框
    ```html
    <html>
    <body>
    
    <form action="/demo/demo_form.asp">
        <select name="cars">
        <option value="volvo">Volvo</option>
        <option value="saab">Saab</option>
        <option value="fiat">Fiat</option>
        <option value="audi">Audi</option>
        </select>
    <br><br>
    <input type="submit">
    </form>
    
    </body>
    </html>
    ```
    
- 多行文本
    ```html
    <html>
    <body>
    
    <textarea name="message" rows="10" cols="30">
    中间的是默认值
    </textarea>
    
    </body>
    </html>
    ```
    
- 点击按钮：不需要form的action属性
    ```html
    <button type="button" onclick="alert('Hello')">点击我</button>
    ```

- 预定义选项列表：不同于select，可以补全设置的选项，也可以自己输入不同选项。**input的list属性必须使用datalist的id值**。
    ```html
    <form action="/demo/demo_form.asp">
    
    <input list="browsers" name="browser">
    <datalist id="browsers">
      <option value="Internet Explorer">
      <option value="Firefox">
      <option value="Chrome">
      <option value="Opera">
      <option value="Safari">
    </datalist>
    <input type="submit">
    </form>
    ```


### HTML中INPUT

- [新增的一些input的type值](http://www.w3school.com.cn/html/html_form_input_types.asp)
    ```
    color
    date
    datetime
    datetime-local
    email
    month
    number
    file
    range
    search
    tel
    time
    url
    week
    ```
    
- 针对上面的输入限制

|属性|	描述|
|-|-|
|disabled|	规定输入字段应该被禁用。|
|max	|规定输入字段的最大值。|
|maxlength	|规定输入字段的最大字符数。|
|min	|规定输入字段的最小值。|
|pattern	|规定通过其检查输入值的正则表达式。|
|readonly|	规定输入字段为只读（无法修改）。|
|required	|规定输入字段是必需的（必需填写）。|
|size|	规定输入字段的宽度（以字符计）。|
|step|	规定输入字段的合法数字间隔。|
| value|	规定输入字段的默认值。|

- 更多属性
| 属性 | 作用 |
| - | - |
| readonly | 只读 |
| disabled | 不可点击和使用，**不可以提交** |
| autofocus | 自动获得焦点 |
| required | 必填字段 |
| multiple | 允许多个值，**用于email和file**|
| novalidate | 不对表单进行验证 |
| autocomplete | 自动填写值，设置为"on"或者"off" |