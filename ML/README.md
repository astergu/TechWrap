# 数学基础

向量内积的几何意义是两个向量之间的接近程度，内积越大，向量越接近，即夹角越小。

## 范数

## 随机梯度下降算法 Gradient Descent

## 评估方法

### 均方误差

均方误差是回归任务中最常用的性能度量，优化目标通常是使均方误差最小化。

(f(x<sub>i</sub>) - y<sub>i</sub>)<sup>2</sup>

均方误差有非常好的几何意义，它对赢了常用的欧几里得距离。基于均方误差最小化来进行模型求解的方法称为『最小二乘法(least square method)』。例如，在线性回归中，最小二乘法就是试图找到一条直线，使所有样本到直线上的欧式距离之和最小。

如果变量数多余样例数，X<sup>T</sup>X不满足满秩条件，此时可以解出多个w，它们都能使均方误差最小化，常见的做法是引入正则化（regularization）项。

# 工业界常见机器学习算法总结

机器学习通常需要习得的是*f(x)*，使得*f(x)*的值尽可能地逼近现实世界中存在的真值*y*。之所以说逼近，是因为真值不总能获得，所以才需要机器学习模型来做预测。

## 线性模型

### Linear Regression 线性回归

f(x) = w<sub>1</sub>x<sub>1</sub> + w<sub>2</sub>x<sub>2</sub> + ... + w<sub>d</sub>x<sub>d</sub> + b

一般用向量形式写成

f(x) = w<sup>T</sup> + b.

线性模型形式简单，易于建模。许多功能更为强大的非线性模型可再线性模型的基础上通过引入层级结构或高维映射而得。由于w直观表达了各属性再预测中的重要性，因此线性模型有很好的可解释性(comprehensibility)。

也可以令模型预测值逼近*y*的衍生物，假设示例所对应的输出标记是在指数尺度上变化，那么就可以将输出标记的对数作为线性模型标记的目标，即lny=w<sup>T</sup>x + b。这就是**对数线性回归(log-linear regression)**，它实际上是在试图让*e<sup>w<sup>T</sup>x + b</sup>*逼近*y*。虽然形式上仍是线性回归，但实质上已是再求取输入空间到输出空间的非线性函数映射。

### Logistic Regression 对数几率回归，也叫逻辑斯特回归

如果需要线性模型来做分类任务，那么只需找一个单调可微函数将分类任务的真实标记*y*与线性回归模型的预测值联系起来。也就是，我们需要将实值*z*转换为0/1值，最理想的是『单位跃阶函数』(unit-step function)，但是该函数不连续。可以用**对数几率函数(logistic function)**来替代：

*y = 1/(1 + e<sup>-z</sup>)*

虽然它的名字是回归，但实际确是一种分类学习方法。这种方法有很多优点，例如它是直接对分类可能性进行建模，无需事先假设数据分布，这样就避免了假设分布不准确所带来的问题；它不是仅预测出类别，而是可得到近似概率预测，这对许多需利用概率辅助决策的任务很有用。


### Maximum Entropy Model 最大熵模型

最大熵模型与逻辑斯特模型一样，都属于对数线性模型。

### Linear Discriminant Analysis (LDA) 线性判别分析

LDA用于二分类，它的思想非常朴素：给定训练样例集，设法将样例投影到一条直线上，使得同类样例的投影点尽可能接近、异类样例的投影点尽可能远离；在对新样本进行分类时，将其投影到同样的这条直线上，再根据投影点的位置来确定信仰本的类别。


## Clustering问题

## 半监督学习Semi-Supervised Learning


## Logistic Regression 逻辑回归

## Decision Tree 决策树

一般地，一棵决策树包含一个根节点、若干个内部节点和若干个叶节点；叶节点对应于决策结果，其他每个节点
对应于一个属性测试；每个节点包含的样本集合根据属性测试的结果被划分到子节点中；根节点包含样本全集。

给定一棵决策树，决策过程如下：
1. 从根节点开始
2. 观察根节点属性的值
3. 按照与观察值对应的路径往下走
4. 重复以上步骤，直至达到叶节点

构造决策树最常用的算法是ID3。




## Random Forest 随机森林

# Deep Learning 深度学习

The term "deep learning" was coined in 2006, and refers to machine learning algorithms that have *multiple non-linear layers* and can learn *feature hierarchies*.

Deep learning algorithms can be categorized by their architecture (feed-forward, feed-back, or bi-directional) and training protocols (purely supervised, hybrid, or unsupervised)


## Representation Learning

Representation learning attempts to automatically learn good features or representations.

Deep learning algorithms attempt to learn (multiple levels of) representation and an output.

## Reading Materials
- [Deep Learning for Signal and Information Processing](http://cs.tju.edu.cn/web/docs/2013-Deep%20Learning%20for%20Signal%20and%20Information%20Processing.pdf), by Li Deng and Dong Yu (out of Microsoft).
- [Deep Learning Tutorial](http://www.cs.nyu.edu/~yann/talks/lecun-ranzato-icml2013.pdf), (2013 Presentation by Yann LeCun and Marc'Aurelio Ranzato)
- [How to Build and Run Your First Deep Learning Network](http://radar.oreilly.com/2014/07/how-to-build-and-run-your-first-deep-learning-network.html)



# Materials
## Open Courses
- **机器学习基石 Machine Learning Foundations by 林轩田**
[https://www.bilibili.com/video/av12463015/](https://www.bilibili.com/video/av12463015/)
    - *When do machines learn? 什么时候用机器学习？*
        - 存在一个pattern可以学习，并且可以衡量效果
        - 难以通过编码的方式人工定义问题和解决问题
        - 存在关于这个pattern可以利用的数据

- **机器学习技法  Machine Learning Techniques by 林轩田**

## Tech Books

- Understanding Machine Learning From Theory to Algorithms
- Machine Learning in Action
    - 

# Tricks

**训练集是真实样本总体的无偏采样**这个假设往往不成立，现有技术大体上有三类做法：第一类是直接对训练集里的反类样例进行『**欠采样**』(undersampling)，即去除一些反例使得正、反例数目接近，然后再进行学习；第二类是对训练集里的正类样例进行『**过采样**』(oversampling)，即增加一些正例使得正、反例数目接近，然后再进行学习；第三类则是直接基于原始训练集进行学习，但在用训练好的分类器进行预测时，进行『**阈值移动**』(threshold-moving)。

## 模型选择方法

### 正则化

结构风险最小化的实现，是在经验风险的基础上加一个正则化项（regularizer）或罚项（penalty term）。正则化项一般是模型复杂度的单调递增函数，模型越复杂，正则化值就越大。

### 交叉验证

随机地将数据集分为三个部分，分别为训练集（training set）、验证集（validation set）和测试集（test set）。训练集用来训练模型，验证集用于模型的选择，而测试集用于最终对学习方法的评估。在学习到的不同复杂度的模型中，选择对验证集有最小预测误差的模型。

但是，在许多实际应用中数据是不充足的，为了选择好的模型，可以采用交叉验证方法。交叉验证的基本想法是重复地使用数据；把给定的数据进行切分，将切分的数据集组合为训练集与测试集，在此基础上反复地进行训练、测试以及模型选择。

## 回归模型

回归学习最常用的损失函数是平方损失函数，在此情况下，回归问题可以由最小二乘法（least squares）求解。


# Questions and Answers

1. **为什么模型复杂度上升以后，训练误差会降低，但测试误差会提高？如何选择最优的模型？**

正则化和交叉验证有助于模型选择。

2. **生成式方法 vs. 判别式方法**

3. **范数如何使用？**

规则化函数有很多种选择，一般是模型复杂度的单调递增函数，模型越复杂，规则化值就越大。比如，规则化项可以是模型参数向量的范数，然而，不同的选择对参数*w*的约束不同，取得的效果也不同，但常见的范数有：零范数、一范数、二范数、迹范数、Frobenius范数和核范数等。

- **L<sub>0</sub>范数**：指向量中非0元素的个数。如果我们用L<sub>0</sub>范数来规则化一个参数矩阵*W*的话，就是希望参数*W*是稀疏的。
- **L<sub>1</sub>范数**：指向量中各个元素绝对值之和，也叫『稀疏规则算子』(Lasso Regularization)。但是，L<sub>1</sub>范数会使权值稀疏。**L<sub>1</sub>范数**是**L<sub>0</sub>范数**的最优凸近似，而且它比**L<sub>0</sub>范数**要容易优化求解。
- **L<sub>2</sub>范数**：称为『岭回归（Ridge Regression）』或者『权值衰减（weight decay）』。它的强大功效是改善机器学习里面一个非常重要的问题：过拟合。**L<sub>2</sub>范数**指的是向量各元素的平方和然后求平方根。我们让**L<sub>2</sub>范数**的规则项最小，可以使得*W*的每个元素都很小，都接近于0，越小的参数说明模型越简单，越简单的模型则越不容易产生过拟合现象。

采用稀疏规则化的一个关键原因在于它能实现特征的自动选择。一般来说，*x<sub>i</sub>*的大部分元素（也就是特征）都是和最终的输出*y<sub>i</sub>*没有关系或者不提供任何信息的，在最小化目标函数的时候考虑*x<sub>i</sub>*这些额外的特征，虽然可以获得最小的训练误差，但在预测新的样本时，这些没用的信息反而会被考虑，从而干扰了对正确*y<sub>i</sub>*的预测。稀疏规则化算子的引入就是为了完成特征自动选择，它会学习去掉这些没有信息的特征，也就是把这些特征对应的权重置为0。

另一个青睐于稀疏的理由是，模型更容易解释。


