### 基础标签
| 标签 | 作用 |
| - | - |
| title | 文档标题 |
| base | `<base target="_blank"/>`超链接在新文档打开。`<base href="base_url"`规定页面中所有相对链接的基准 URL|
|link | 一般存放css|


### `<meta>`标签
> 通过标签的属性描述文档的属性和性质。

```html
<meta name="author" content="author的内容"/>
<meta name="generator" content="编辑软件"/>
<meta name="description" content="描述信息"/>
<meata name="keywords" content="关键词"/>
```

#### 页面刷新
- 10s刷新一次：
`<meta http-equiv="refresh" content="10"/>`
- 10s后刷新到指定网址：
`<meta http-equiv="refresh" content="10;url="http://www.baidu.com"/>`
- `javascript`刷新：
    ```javascript
    <script language="JavaScript">
    setTimeout(function(){location.reload()},1000); //指定1秒刷新一次
    </script>
    ```
