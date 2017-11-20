[TOC]

**关于分类文本，有三个问题**
1. 怎么识别出文本中用于明显分类的特征
2. 怎么构建自动分类文本的模型
3. 相关的语言知识

按照这个思路，博主进行了艰苦学习（手动捂脸。。）

---

## 一、监督式分类：建立在训练语料基础上的分类
> 训练过程中，特征提取器将输入转化为特征集，并且记录对应的正确分类。生成模型。预测过程中，未见过的输入被转换特征集，通过模型产生预测标签。

### 特征提取器和朴素贝叶斯分类器
> 特征提取器返回字典，这个字典被称为**特征集**。然后利用
nltk自带的朴素贝叶斯分类器 `NaiveBayesClassifier` 生成分类器。并且可以用`nltk.classify.accuracy(分类器,测试集)` 测试准确度。

```python
import nltk
from nltk.corpus import names
import random

def gender_features(word): #特征提取器
    return {'last_letter':word[-1]} #特征集就是最后一个字母

names = [(name,'male') for name in names.words('male.txt')]+[(name,'female') for name in names.words('female.txt')]
random.shuffle(names)#将序列打乱

features = [(gender_features(n),g) for (n,g) in names]#返回对应的特征和标签

train,test = features[500:],features[:500] #训练集和测试集
classifier = nltk.NaiveBayesClassifier.train(train) #生成分类器

print('Neo is a',classifier.classify(gender_features('Neo')))#分类

print(nltk.classify.accuracy(classifier,test)) #测试准确度

classifier.show_most_informative_features(5)#得到似然比，检测对于哪些特征有用
```

> 当然，当我们训练大的语料库的时候，链表会占用很大内存。这时候nltk提供了：`apply_features`，会生成链表，但是不会在内存中存储所有对象。

```python
from nltk.classify import apply_features
train_set = apply_features(gender_features,names[500:])
test_set = apply_features(gender_features,names[:500])
```

### 过拟合：当特征过多

当特征过多的时候（特征集的键值过多），会对一般化的新例子不起作用，称为**过拟合**。如果抉择特征集的大小，需要不停的测试，找到最吻合的特征集。

### 错误分析

**为了使特征提取器准确度更高，一般将源数据分为两大部分，三小部分：**
- 开发集：
	- 训练集：负责开发
	- 开发测试集：负责错误分析
- 测试集：负责最终评估

下面是查找报错信息的案例：
```python
import nltk
from nltk.corpus import names
import random

def gender_features(word): #特征提取器
    return {'last_letter':word[-1]} #特征集就是最后一个字母

names = [(name,'male') for name in names.words('male.txt')]+[(name,'female') for name in names.words('female.txt')]

train_names = names[1500:]
devtest_names = names[500:1500]
test_names = names[:500]

train_set = [(gender_features(n),g) for (n,g) in train_names]
devtest_set = [(gender_features(n),g) for (n,g) in devtest_names]
test_set = [(gender_features(n),g) for (n,g) in test_names]

classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier,devtest_set))
######################记录报错的案例###############################
errors = []
for (name,tag) in devtest_names:
    guess = classifier.classify(gender_features(name))
    if guess!=tag:
        errors.append((tag,guess,name))
##################################################################
```

我们发现准确度低，因为倒数第二个字母也很有关联。所以我们可以改进特征提取器：
```python
def gender_features(word): #特征提取器
    return {'last_letter':word[-1],'last__letter':word[-2]} #特征集就是最后一个字母和倒数第二个字母
```

**观察结果，发现，准确度提高了12%。重复这个过程，使得特征提取器更加完善。**

---

## 二、实例：文本分类和词性标注

### 文本分类
> 这里的分类标签选成词汇，通过对文本前N个词的观察，得到预测标签。

```python
import nltk
from nltk.corpus import movie_reviews

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.most_common(2) #前两千个最常出现的单词

def document_features(document):
    document_words = set(document)
    features = {}
    for (word,freq) in word_features:
        features['contains(%s)'%word] = (word in document_words) #参数文档中是否包含word：True/False
    return features

documents = [(list(movie_reviews.words(fileid)),category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

features = [(document_features(d),c)for (d,c) in documents]
train_set,test_set = features[100:],features[:100]

classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier,test_set))
```

###  词性标注：“决策树”分类器
> 这里的分类器是决策树分类器:`DecisionTreeClassifier`。可以通过`classifier.pseudocode(depth = ?)` 这查询深度为depth的树，并且打印出来。顺便表示，我再走下面的程序的时候，电脑炸了。建议在集群上运行。

```python
from nltk.corpus import brown
import nltk

suffix_fdist = nltk.FreqDist()
for word in brown.words():
    word = word.lower()
    #suffix_fdist.inc(word[-1:]) python2
    suffix_fdist[word[-1:]] += 1 #python3
    suffix_fdist[word[-2:]] += 1
    suffix_fdist[word[-3:]] += 1

common_suffixes = suffix_fdist.most_common(100) #获得常见特征链表
#定义特征提取器：
def pos_features(word):
    features = {}
    for (suffix,times) in common_suffixes:
        features['endswith(%s)' % suffix] = word.lower().endswith(suffix)
    return features

tagged_words = brown.tagged_words(categories='news')
featuresets = [(pos_features(n),g)for (n,g) in tagged_words]
size = int(len(featuresets)*0.1)

train_set , test_set= featuresets[size:], featuresets[:size]
classifier = nltk.DecisionTreeClassifier.train(train_set) #“决策树分类器”
print(nltk.classify.accuracy(classifier,test_set))
```

***

## 三、更近一步的连续分类或贪婪序列分类：在朴素贝叶斯和“决策树”之后
> 这种分类模型是为了**获取相关分类之间的依赖关系**。为第一个输入找到最佳标签，然后再次基础上找到对应的下一个输入的最佳标签。不断重复，以至所有输入都被贴上标签。所以，我们需要提供一个参数history，用来扩展特征。<br>
*事实证明，我的电脑又炸了。*

利用**联合分类器**模型进行词性标注：

```python
import nltk
from nltk.corpus import brown
#带有历史的特征提取器
def pos_features(sentence,i,history):
    features = {'suffix(1)':sentence[i][-1:],\
               'suffix(2)':sentence[i][-2:],\
               'suffix(3)':sentence[i][-3:]}
    if i==0:#当它在分界线的时候，没有前置word 和 word-tag
        features['prev-word'] = '<START>'
        features['prev-tag'] = '<START>'
    else:#记录前面的history
        features['prev-word'] = sentence[i-1]
        features['prev-tag'] = history[i-1]
    return features

''' 
###########流程式###############
tagged_sents = brown.tagged_sents(categories="news")
size = int(len(tagged_sents)*0.1)
train_sents,test_sents = tagged_sents[size:],tagged_sents[:size]

train_set = []

for tagged_sent in train_sents:
    untagged_set = nltk.tag.untag(tagged_sent) 
    history = []
    for i,(word,tag) in enumerate(tagged_sent):
        featureset = pos_features(untagged_set,i,history)
        history.append(tag)
        train_set.append((featureset,tag))
    classifier = nltk.NaiveBayesClassifier.train(train_set)
'''
#########类思想重写##################

class ConsecutivePosTagger(nltk.TaggerI): #这里定义新的选择器类，继承nltk.TaggerI
    def __init__(self,train_sents):
        train_set = []
        for tagged_sent in train_sents:
            untagged_set = nltk.tag.untag(tagged_sent) #去标签化
            history = []
            for i,(word,tag) in enumerate(tagged_sent):
                featureset = pos_features(untagged_set,i,history)
                history.append(tag) #将tag添加进去
                train_set.append((featureset,tag)) #拿到了训练集
            self.classifier = nltk.NaiveBayesClassifier.train(train_set) #创建训练模型

    def tag(self,sentence): #必须定义tag方法
        history = []
        for i,word in enumerate(sentence):
            featureset = pos_features(sentence,i,history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence,history)
        
tagged_sents = brown.tagged_sents(categories="news")
size = int(len(tagged_sents)*0.1)
train_sents,test_sents = tagged_sents[size:],tagged_sents[:size]
#print(train_sents)
tagger = ConsecutivePosTagger(train_sents)
print(tagger.evaluate(test_sents))
```

***

## 四、评估

> 之前我们选择测试集和开发集，都是在一个原有集合下。这样，示例相似程度很大，不利于推广到其他数据集。而评估最简单的度量就是准确度，即：`accuracy()`函数。除了这个，精确度、召回率和F-度量值也确实影响了准确度。

**- 精确度：发现项目中多少是相关的。TP/(TP+FP)**
**- 召回率：表示相关项目发现了多少。TP(TP+FN)**
**- F-度量值：精确度和召回率的调和平均数。**
其中，T：true；P：Positive；F：false；N：negative。组合即可。例如TP：真阳性（正确识别为相关的），TN：真阴性（相关项目中错误识别为不想关的）

***

## 五、三种分类器的总结

之前我们发现。同样的特征集，朴素贝叶斯分类器就可以轻松跑完，但是决策树分类器不行。除了过拟合的因素外，还是因为树结构强迫特征按照特定的顺序检查，即便他是重复的，而在回溯的过程中，又有重复运算，导致时间和空间的双重浪费。<br>
朴素贝叶斯分类器允许所有恩正“并行”起作用，从计算每个标签的先验概率开始。并且建立朴素贝叶斯的时候采用了平滑技术（在给定的贝叶斯模型上）。<br>
最后的最大熵分类器，使用搜索技术找出一组能最大限度的提高分类器性能的参数。由于他会用迭代优化技术选择参数，花费时间很长。

***

## 六、后记
> 努力地看书了，然而还是没有看懂。感觉是因为相应的数学知识和算法知识没到位。以后积累充足会重看。<br>当然，对于现在用的层面来说，较深入的了解原理，基本可以解决大多数问题。但是要是做到算法优化，还是要自己去调参，或者改进算法。<br> **由于博主水平有限，希望各路大牛不li赐教。**
