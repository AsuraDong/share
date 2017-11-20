[TOC]
> 自然语言处理中算法设计有两大部分：分而治之 和 转化 思想。一个是将大问题简化为小问题，另一个是将问题抽象化，向向已知转化。前者的例子：归并排序；后者的例子：判断相邻元素是否相同（与排序）。<br>
这次总结的**自然语言中常用的一些基本算法**，算是入个门了。

***

## 递归
> 使用递归速度上会受影响，但是便于理解算法深层嵌套对象。而一些函数式编程语言会将尾递归优化为迭代。

#### 如果要计算n个词有多少种组合方式？按照阶乘定义：n! = n\*(n-1)\*...\*1
```python
def func(wordlist):
    length = len(wordlist)
    if length==1:
        return 1
    else: 
        return func(wordlist[1:])*length
```

#### 如果要寻找word下位词的大小，并且将他们加和。
```python
from nltk.corpus import wordnet as wn

def func(s):#s是WordNet里面的对象
    return 1+sum(func(child) for child in s.hyponyms())

dog = wn.synset('dog.n.01')
print(func(dog))
```

#### 构建一个字母查找树
> 建立一个嵌套的字典结构，每一级的嵌套包含既定前缀的所有单词。而子查找树含有所有可能的后续词。

```python
def WordTree(trie,key,value):
    if key:
        first , rest = key[0],key[1:]
        if first not in trie:
            trie[first] = {}
        WordTree(trie[first],rest,value)
    else:
        trie['value'] = value

WordDict = {}
WordTree(WordDict,'cat','cat')
WordTree(WordDict,'dog','dog')
print(WordDict)
```

***

## 贪婪算法：不确定边界自然语言的分割问题(退火算法的非确定性搜索)
>  爬山法是完完全全的贪心法，每次都鼠目寸光的选择一个当前最优解，因此只能搜索到局部的最优值。模拟退火其实也是一种贪心算法，但是它的搜索过程引入了随机因素。模拟退火算法以一定的概率来接受一个比当前解要差的解，因此有可能会跳出这个局部的最优解，达到全局的最优解。

```python
import nltk
from random import randint

#text = 'doyou'
#segs = '01000'

def segment(text,segs):#根据segs，返回切割好的词链表
    words = []
    last = 0
    for i in range(len(segs)):
        if segs[i]=='1':#每当遇见1,说明是词分界
            words.append(text[last:i+1])
            last = i+1
    words.append(text[last:])
    return words 

def evaluate(text,segs): #计算这种词分界的得分。作为分词质量，得分值越小越好(分的越细和更准确之间的平衡)
    words = segment(text,segs)
    text_size = len(words)
    lexicon_size = len(' '.join(list(set(words))))
    return text_size + lexicon_size

###################################以下是退火算法的非确定性搜索############################################

def filp(segs,pos):#在pos位置扰动
    return segs[:pos]+str(1-int(segs[pos]))+segs[pos+1:]

def filp_n(segs,n):#扰动n次
    for i in range(n):
        segs = filp(segs,randint(0,len(segs)-1))#随机位置扰动
    return segs

def anneal(text,segs,iterations,cooling_rate):
    temperature = float(len(segs))
    while temperature>=0.5:
        best_segs,best = segs,evaluate(text,segs)
        for i in range(iterations):#扰动次数
            guess = filp_n(segs,int(round(temperature)))
            score = evaluate(text,guess)
            if score<best:
                best ,best_segs = score,guess
        score,segs = best,best_segs
        temperature = temperature/cooling_rate #扰动边界，进行降温
        print( evaluate(text,segs),segment(text,segs))
    print()
    return segs
text = 'doyouseethekittyseethedoggydoyoulikethekittylikethedoggy'
seg =  '0000000000000001000000000010000000000000000100000000000'
anneal(text,seg,5000,1.2)
```

***

## 动态规划
> 它在自然语言中运用非常广泛。首先他需要一张表，用来将每一次的子结果存放在查找表之中。避免了重复计算子问题！！！

这里我们讨论一个梵文组合旋律的问题。短音节：S，一个长度；长音节：L，两个长度。所以构建长度为2的方式：{SS,L}。

#### 首先用递归的方式编写一下找到任意音节的函数
```python
def func1(n):
    if n==0:
        return [""]
    elif n==1:
        return ["S"]
    else:
        s = ["S" + item for item in func1(n-1)]
        l = ["L" + item for item in func1(n-2)]
        return s+l
print(func1(4))
```

#### 使用动态规划来实现找到任意音节的函数
> 之前递归十分占用时间，如果是40个音节，我们需要重复计算632445986次。如果使用动态规划，我们可以把结果存到一个表中，需要时候调用，而不是很坑爹重复计算。

```python
def func2(n):#采用自下而上的动态规划
    lookup = [[""],["S"]]
    for i in range(n-1):
        s = ["S"+ item for item in lookup[i+1]]
        l = ["L" + item for item in lookup[i]]
        lookup.append(s+l)
    return lookup
print(func2(4)[4])
print(func2(4))
```
```python
def func3(n,lookup={0:[""],1:["S"]}):#采用自上而下的动态规划
    if n not in lookup:
        s = ["S" + item for item in func3(n-1)]
        l = ["L" + item for item in func3(n-2)]
        lookup[n] = s+l
    return lookup[n]#必须返回lookup[n].否则递归的时候会出错
print(func3(4))
```
**对于以上两种方法，自下而上的方法在某些时候会浪费资源，因为，子问题不一定是解决主问题的必要条件。**

#### NLTK自带装饰符:默记
> 装饰器`@memoize` 会存储每次函数调用时的结果及参数，那么之后的在调用，就不用重复计算。而我们可以只把精力放在上层逻辑，而不是更关注性能和时间（被解决了）

```python
from nltk import memoize
@memoize
def func4(n):
    if n==0:
        return [""]
    elif n==1:
        return ["S"]
    else:
        s = ["S" + item for item in func4(n-1)]
        l = ["L" + item for item in func4(n-2)]
        return s+l
print(func4(4))
```

***

## 其他的应用
> 这里主要介绍一下除了上述两种主要算法外，一些小的使用技巧和相关基础概念。

#### 词汇多样性
> 词汇多样性主要取决于：平均词长（字母个数/每个单词）、平均句长（单词个数/每个句子）和文本中没歌词出现的次数。

```python
from nltk.corpus import gutenberg
for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
    print(int(num_chars/num_words),int(num_words/num_sents),int(num_words/num_vocab),'from',fileid)
```

#### 文体差异性
> 文体差异性可以体现在很多方面：动词、情态动词、名词等等。这里我们以情态动词为例，来分析常见情态动词的在不同文本的差别。

```python
from nltk.corpus import brown
from nltk import FreqDist,ConditionalFreqDist
cfd = ConditionalFreqDist(( genere,word) for genere in brown.categories() for word in brown.words(categories=genere))
genres=['news','religion','hobbies']
models = ['can','could','will','may','might','must']
cfd.tabulate(conditions = genres,samples=models)
```

#### 随机语句生成
> 从《创世纪》中得到所有的双连词，根据概率分布，来判断哪些词最有可能跟在给定词后面。

```python
import nltk
def create_sentence(cfd,word,num=15):
    for i in range(num):
        print(word,end=" ")
        word = cfd[word].max()#查找word最有可能的后缀
text= nltk.corpus.genesis.words("english-kjv.txt")
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)

print(create_sentence(cfd,'living'))
```

#### 词谜问题解决
> 单词长度>=3,并且一定有r,且只能出现'egivrvonl'中的字母。

```python
puzzle_word = nltk.FreqDist('egivrvonl')
base_word = 'r'
wordlist = nltk.corpus.words.words()
result = [w for w in wordlist if len(w)>=3 and base_word in w and nltk.FreqDist(w)<=puzzle_word]
#通过FreqDist比较法（比较键对应的value），来完成字母只出现一次的要求！！！
print(result)
```

***


## 时间和空间权衡:全文检索系统
> 除了研究算法，分析内部实现外。**构造辅助数据结构**，可以显著加快程序执行。

```python
import nltk
def raw(file):
    contents = open(file).read()
    return str(contents)

def snippet(doc,term):#查找doc中term的定位
    text = ' '*30+raw(doc)+' '*30
    pos = text.index(term)
    return text[pos-30:pos+30]

files = nltk.corpus.movie_reviews.abspaths()
idx = nltk.Index((w,f) for f in files for w in raw(f).split())
#注意nltk.Index格式

query = 'tem'
while query!='quit' and query:
    query = input('>>> input the word:')
    if query in idx:
        for doc in idx[query]:
            print(snippet(doc,query))
    else:
        print('Not found')
```
