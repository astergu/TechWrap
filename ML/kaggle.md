Kaggle competitions

# Keyword Extraction

## Problem Formulation

训练数据主要分为4个部分，Id, Question Name, Question Body, Tags。

## Feature Engineering

首先需要把输入中的Question Name和Question Body转化为输入特征。简单来说，可以用sklearn的**TfidfVectorizer**和**CountVectorizer**来提取文本特征。

[如何使用scikit-learn进行文本数据的特征抽取](http://www.infoq.com/cn/articles/prepare-text-data-machine-learning-scikit-learn)

### 词袋模型

词袋模型假设我们不考虑文本中词与词之间的上下文关系仅仅只考虑所有词的权重。而权重与词在文本中出现的频率有关。词袋模型首先会进行分词，在分词之后，通过统计每个词在文本中出现的次数，就可以得到该文本基于词的特征，如果将各个文本样本的这些词与对应的词频放在一起，就是向量化。向量化完毕后一般也会使用TF-IDF进行特征的权重修正，再将特征进行标准化。再进行特征工程。

词袋模型的三部曲：分词(tokenizing)，统计修订词特征值(counting)与标准化(normalization)。词袋模型有很大的局限性，因为它仅仅考虑了词频，没有考虑上下文的关系，因此会丢失一部分文本的语义。

#### 词频向量化

CountVectorizer类会将文本中的词语转换为词频矩阵，例如矩阵中包含一个元素a<sub>ij</sub>，它表示j词在i类文本下的词频。它通过 fit_transform 函数计算各个词语出现的次数，通过get_feature_names()可获取词袋中所有文本的关键字，通过 toarray()可看到词频矩阵的结果。


```python
from sklearn.feature_extraction.text import CountVectorizer
# 文本文档列表
text = ["The quick brown fox jumped over the lazy dog."]
# 构造变换函数
vectorizer = CountVectorizer()
# 词条化以及建立词汇表
vectorizer.fit(text)
# 总结
print(vectorizer.vocabulary_)
# 编码文档
vector = vectorizer.transform(text)
```

#### TF-IDF处理

统计单词出现次数是一个很好的切入点，但也是很基础的特征。简单的次数统计的一个问题在于，有写单词，例如"the"会出现很多次，它们的统计数量对于编码向量没有太大意义。

一个替代方法是统计单词权重，目前最流行的方法是TF-IDF。这是一个缩写词，代表“词频-逆文档频率”（Term Frequency–Inverse Document Frequency），代表一个词对于一个文档的重要程度。

**词频（Term Frequency）**：指的是某一个给定的词语在一篇文档中出现的次数。
**逆文档频率（Inverse Document Frequency）**：单词在文档中出现的频率越高，IDF值越低。

```python
from sklearn.feature_extraction.text import TfidfVectorizer
# 文本文档列表
text = ["The quick brown fox jumped over the lazy dog.",
"The dog.",
"The fox"]
# 创建变换函数
vectorizer = TfidfVectorizer()
# 词条化以及创建词汇表
vectorizer.fit(text)
# 总结
print(vectorizer.vocabulary_)
print(vectorizer.idf_)
# 编码文档
vector = vectorizer.transform([text[0]])
```

#### 哈希量化文本

单词频率和权重是很有用的，但是当词汇表变得很大时，以上两种方法就会出现局限性。反过来，浙江需要巨大的向量来编码文档，并对内存要求很高，而且会减慢算法的速度。

一种很好的方法是使用单向哈希方法来将单词转化成整数。好处是该方法不需要词汇表，可以选择任意长的固定长度向量。缺点是哈希量化是单向的，因此无法将编码转换回单词（对与许多有监督的学习任务来说或许并不重要）。

HashingVectorizer类实现了这一方法，所以可以使用它对单词进行连续哈希量化，然后按需求词条化和编码文档。

## Model Selection
