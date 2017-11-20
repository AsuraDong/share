[toc]

### 普通表格
> `tr`代表一行(row)，`td`代表一个数据,`caption`代表table标题

```html
<table border="1">
<caption>我的标题</caption>
<tr>
    <td>100</td>
    <td>200</td>
    <td>300</td>
</tr>
<tr>
    <td>100</td>
    <td>200</td>
    <td>300</td>
</tr>
</table>
```

```html
<table border="1">
<caption>我的标题</caption>
<tr>
    <td>100</td>
    <td>200</td>
    <td>300</td>
</tr>
<tr>
    <td>100</td>
    <td>200</td>
    <td>300</td>
</tr>
</table>
```

### 表头
> `th`标签代表加重表头

```html
<table>
<tr> 
    <th> 姓名 </th>
    <th> sex </th>
    <th> loc </th>
</tr>
<tr>
  <td>Bill Gates</td>
  <td>555 77 854</td>
  <td>555 77 855</td>
</tr>
</table>
```

```html
<table>
<tr>
  <th>姓名</th>
  <td>Bill Gates</td>
</tr>
<tr>
  <th>电话</th>
  <td>555 77 854</td>
</tr>
<tr>
  <th>电话</th>
  <td>555 77 855</td>
</tr>
</table>
```

### 跨行和跨列
> 在`th`和`td`级别中的属性，有跨列（`colspan`）和跨行（`rowspan`）

```html
<table>
<tr>
    <th>姓名</th>
    <th colspan="2">电话</th>
</tr>
<tr>
  <td>Bill Gates</td>
  <td>555 77 854</td>
  <td>555 77 855</td>
</tr>
</table>
```

```html
<table>
<tr>
    <th>姓名</th>
    <th>Bill</th>
</tr>
<tr>
    <th rowspan="2">电话</th>
    <td>555</td>
</tr>
<tr>
    <td>110</td>
</tr>
</table>
```

### 左右对齐
> 可以利用`align`属性来设置。


### HTML5方法
> 通过`table`的子标签、`tr`的父标签：`thead`、`tfoot`和`tbody`

```html
<html>
<head>
<style type="text/css">
thead {color:green}
tbody {color:blue;height:50px}
tfoot {color:red}
</style>
</head>
<body>

<table border="1">
  <thead>
    <tr>
      <th>Month</th>
      <th>Savings</th>
    </tr>
  </thead>

<tfoot>
    <tr>
      <td>Sum</td>
      <td>$180</td>
    </tr>
  </tfoot>
  <tbody>
    <tr>
      <td>January</td>
      <td>$100</td>
    </tr>
    <tr>
      <td>February</td>
      <td>$80</td>
    </tr>
  </tbody>
  
</table>

</body>
</html>
```