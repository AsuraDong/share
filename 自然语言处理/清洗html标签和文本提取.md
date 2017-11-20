## 一、工具准备
- python3.6
- 正则表达式(别的语言思路一样，容易借鉴)

***
## python正则表达式：flags的应用

#### 这里主要介绍一下`re.compile(pattern[, flags])`里面的flags用法

| 标识符 | 作用|
| - | -: |
|re.I|忽略大小写|
|re.L|表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境|
|re.M|多行模式|
|re.S|' . '并且包括换行符在内的任意字符（注意：' . '不包括换行符）|
|re.U| 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库|

#### 特别强调`re.I`和`re.S`的用法
1. 众所周知，html标签是**大小写不敏感的**，所以我们需要`re.I`
2. 其次html中`<style>..</style>`、`<sript>..</scipt>`等一些标签里面是包含换行符的。而我们为了保留原来文本的特点包括换行符，所以需要`re.S`。**让`.`可以匹配换行符**

***


## 二、清洗全角和半角字符
> 实现字符的清洗工作，否则，jieba词库会将全角数字全部分开。而且，清洗后的半角文本更适合观看

#### 小姿势
中文文字永远是全角，只有英文字母、数字键、符号键才有全角半角的概念,一个字母或数字占一个汉字的位置叫全角，占半个汉字的位置叫半角

#### 全角半角转换说明
1. 全角字符unicode编码从65281~65374 （十六进制 0xFF01 ~ 0xFF5E）
2. 半角字符unicode编码从33~126 （十六进制 0x21~ 0x7E）
3. 空格比较特殊，全角为 12288（0x3000），半角为 32（0x20）

#### 代码实现
```python
def Q2B(_char):#全角转半角
    if 65281<=ord(_char)<=65374:
        _char = chr(ord(_char)-65248)
    elif ord(_char)==12288:
        _char = chr(32)
    return _char

def isQ(Char):
    return True if (65281<=ord(Char)<=65374 or ord(Char)==12288) else False

def B2Q(_char):#半角转全角
    if 33<=ord(_char)<=126:
        _char = chr(ord(_char)+65248)
    elif ord(_char)==32:
        _char = chr(12288)
    return _char

def isB(Char):
    return True if (33<=ord(Char)<=126 or ord(Char)==32) else False
```

***

## 三、网页字符实体
> 标准的html代码中的文本内容是不会出现'<'/' '等这些字符的。现在很多工具都会将网页文本内容处理成标准形式再发布。我们这里讨论的就是标准的html代码及文本内容

**[html字符实体查询地址](http://www.w3school.com.cn/tags/html_ref_entities.html)**<br>
*为了方便讨论，我们这里取了几个常用的作为示范，并且构造以下dict*
```python
html_char = {}
html_char['"'] = html_char['"']='"'
html_char['''] = html_char['''] = "'"
html_char['&'] = html_char['&'] = '&'
html_char['<'] = html_char['<'] = '<'
html_char['>'] = html_char['>'] = '>'
html_char[' '] = html_char[' ']= ' '
```

***

## 四、Code实现
> 难点重点就在这里，做了很多准备工作，幸好python比较方便，其他语言的玩家可以借鉴一下思路

#### 正则Code实现去标签[^1]
```python
    ...
    #CDATA 部分由 "<![CDATA[" 开始，由 "]]>" 结束：
    cdata_rule = re.compile(r'<![CDATA[.*]]>',re.I | re.S)

    #去除脚本（随时会出现）
    script_rule = re.compile(r'<script.*?</script>',re.I | re.S)

    #取出<head>..</head>和中间的内容，style也在里面，不需要再写了
    head_rule = re.compile(r'<head.*?/head>',re.I | re.S)

    #为了以防一些文本不是全部截取html代码，还是写一下以防万一
    style_rule = re.compile(r'<style.*?/style>',re.I | re.S)

    #处理注释
    comment_rule = re.compile(r'<!.*?>',re.I | re.S)
    
    #处理换行
    br_rule = re.compile(r'<br\s*?/{0,1}>',re.I)

    #html标签
    html_rule = re.compile(r'<.*?/{0,1}>',re.I)
    ...
```

[^1]:代码备注以标明作用

#### 正则Code实现去字符实体
```python
    ...
    global html_char
    letter_char = re.compile(r'&[a-z]+;',re.I)
    for char in letter_char.findall(raw):
        raw = re.sub(char,html_char[char],raw)

    number_char = re.compile(r'&#\d+;',re.I)
    for char in number_char.findall(raw):
        raw = re.sub(char,html_char[char],raw)
    ...
```

#### 全部代码（含测试文本）
```python
"""
清洗网页标签
全角和半角的转换
"""

#encoding:utf-8
import re

# 网页中的字符实体
# 需要更多的补充
html_char = {}
html_char['&quot;'] = html_char['&#34;']='"'
html_char['&apos;'] = html_char['&#39;'] = "'"
html_char['&amp;'] = html_char['&#38;'] = '&'
html_char['&lt;'] = html_char['&#60;'] = '<'
html_char['&gt;'] = html_char['&#62;'] = '>'
html_char['&nbsp;'] = html_char['&#160;']= ' '

def Q2B(_char):
    """
    全角字符转半角字符
    :param _char: 待转换字符
    :return: 转化后的字符
    """
    if 65281<=ord(_char)<=65374:
        _char = chr(ord(_char)-65248)
    elif ord(_char)==12288:
        _char = chr(32)
    return _char

def isQ(Char):
    """
    判断是否是全角字符
    :param Char: 待判断字符
    :return: bool值
    """
    return True if (65281<=ord(Char)<=65374 or ord(Char)==12288) else False

def B2Q(_char):
    """
    半角字符转全角字符
    :param _char: 待转换字符
    :return: 转化后的字符
    """
    if 33<=ord(_char)<=126:
        _char = chr(ord(_char)+65248)
    elif ord(_char)==32:
        _char = chr(12288)
    return _char

# 类似 isQ(Char)
def isB(Char):
    return True if (33<=ord(Char)<=126 or ord(Char)==32) else False


def cleanHtml(html_str,special_char=None,to_char=None):
    """
    清洗html标签
    :param html_str: html文本
    :param special_char: 自定义的需要处理的特殊字符列表（迭代器类型）
    :param to_char: special_char的转化目标
    :return: html中的正文部分
    """

    # 如果有需要处理的额外字符
    if special_char:
        special_rule = re.compile('|'.join(set(special_char))) # '|'在正则表达式中代表'或'。所有的特殊字符都要替换
        if not to_char:
            to_char = ''

    #CDATA 部分由 "<![CDATA[" 开始，由 "]]>" 结束：
    cdata_rule = re.compile(r'<![CDATA[.*]]>',re.I | re.S)

    #去除脚本（随时会出现）
    script_rule = re.compile(r'<script.*?</script>',re.I | re.S)

    #取出<head>..</head>和中间的内容，style也在里面，不需要再写了
    head_rule = re.compile(r'<head.*?/head>',re.I | re.S)

    #为了以防一些文本不是全部截取html代码，还是写一下以防万一
    style_rule = re.compile(r'<style.*?/style>',re.I | re.S)

    #处理注释
    comment_rule = re.compile(r'<!.*?>',re.I | re.S)
    
    #处理换行
    br_rule = re.compile(r'<br\s*?/{0,1}>',re.I)

    #html标签
    html_rule = re.compile(r'<.*?/{0,1}>',re.I)

    if special_char:
        raw = special_rule.sub(to_char,html_str)
    else:
        raw = html_str

    raw = cdata_rule.sub('',raw)
    raw = script_rule.sub('',raw)
    raw = head_rule.sub('',raw)
    raw = style_rule.sub('',raw)
    raw = comment_rule.sub('',raw)
    raw = br_rule.sub('\n',raw)
    raw = html_rule.sub('',raw)

    global html_char
    letter_char = re.compile(r'(&[a-z]+;)|(&#\d+;)',re.I)
    for _,__ in letter_char.findall(raw): # _，__分别对应两种形式的字符实体
        if _ not in html_char.keys() and __ not in html_char.keys(): # 针对字符实体不在html_char的情况
            continue
        if _ in html_char.keys():
            raw = re.sub(_,html_char[_],raw)
        else:
            raw = re.sub(__, html_char[__], raw)

    raw_list = list(raw)
    for i in range(len(raw_list)):
        if isQ(raw_list[i]):
            raw_list[i] = Q2B(raw_list[i])
    raw = ''.join(raw_list)
    
    return raw

# 测试函数
def test():
    # 下面是一段html的测试代码
    test_html = """
        
    <div id="sidebar">

    <div id="tools">
    <h5 id="tools_example"><a href="/example/xmle_examples.asp">&nbsp;XML 实例,特殊字符：１５（处理之后应该没有了）</a></h5>
    <h5 id="tools_quiz"><a href="/xml/xml_quiz.asp">&#60;XML 测验&gt;</a></h5>
    <h3>&#39;ｖｅｖｅｖ&#39;</h3>
    </div>

    <div id="ad">
    <script type="text/javascript"><!--
    google_ad_client = "ca-pub-3381531532877742";
    /* sidebar-160x600 */
    google_ad_slot = "3772569310";
    google_ad_width = 160;
    google_ad_height = 600;
    //-->
    </script>
    <script type="text/javascript"
    src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
    </script>
    </div>

    </div>
    """

    print(cleanHtml(test_html,'】１５'))

if __name__=='__main__':
    test()
```

***

## 四、进一步

#### 其他脚本引用
**在python的其他程序中，可以直接`from clean_html import clean_html`进行方便的调用(假设这个脚本名字为clean_html.py)**

#### 完善
1. 补充字符实体(可以用爬虫爬下来，有空弄一下)
2. html标签可能因为前端框架不同而有所差异（虽然不大）。但是都有规律，如`<Vue>..</Vue>`等，有规律，正则表达式就容易构建了
