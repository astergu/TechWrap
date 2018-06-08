## Core Ideas

**interview-style coding questions**

**with pen and paper, or with a whiteboard**

**10-15 minutes to write out the solution**

**take into account the edge cases**

**see if you can improve**


## Mock System Design

### Search

- **Content Search (内容检索)**: 检索内容，包括posts，photos，videos and links. 采用deep learning, ranking，GBDT，Recommendation algorithms, NLP/内容理解

### Ads Core

- **Business Integrity (商务整合)**: 广告质量优化，选优，采用deep learning, content understanding NLP, penalty/ranking features.
- **Ads Ranking (广告排序)**: 采用deep learning, multi-task learning, Caffe 2.0, transfer learning, text/image understanding, sparsity, recommender systems, user intent understanding, exploration and exploitation, cold-start.
- **Ads Targeting (广告投放)**: 同上

### News Feed

- **News Feed Ranking (信息流资讯排序)**: 个性化特征，用户主题偏好，基于这些特征的内容推荐。采用Deep Learning, Ranking, Recommendation Algorithms, NLP/Content Understanding. 

### Applied Machine Learning

- **Speech Perception**: 视频理解，字幕生成，AR音频效果，音频交互。采用Deep Learning, signal processing, acoustic modeling, language modeling, speech recognition decoders, supervised/unsupervised training, Caffe2 and Torch.
- **Computer Vision**: 采用Deep Learning, Supervised, Semi-supervised and unsupervised learning, Caffe2, Torch, Compact Representations, Model Compression.
- **AR Tech**
- **Language and Translation Technology**
- **AML Personalization**

### Instagram


## 机器学习模型

Facebook使用的机器学习模型包括逻辑回归（Logistic Regression, LR）、支持向量机（Support Vector Machine, SVM）、梯度提升决策树（Gradient Boosted Decision Tree, GBDT），以及深度神经网络（Deep Neural Network, DNN）。LR和SVM用于训练和预测的效率很高，GBDT使用额外的计算资源可以提高准确性。DNN是最具表现力的模型，有能力达到最高的准确性，但是它利用的资源最多。

在DNN中，主要使用的网络类型有三种：多层感知器（Multi-Layer Perceptrons，MLP）一般用于结构化的输入特征（如排序），卷积神经网络（Convolutional Neural Networks，CNN）作为空间处理器（如图像处理），以及循环神经网络（RNN、LSTM）主要用于序列处理器（如语言处理）。

### FBLearner
FBLearner利用内部作业调度程序在GPU和CPU的共享池分配资源、安排工作。Facebook大多数的机器学习训练通过FBLearner平台完成。


### Caffe2

Caffe2是Facebook的内部训练和部署大规模机器学习模型的框架。Caffe2关注产品要求的几个关键的特征：性能、跨平台支持，以及基本的机器学习算法。Caffe2的设计使用的是模块化的方法，所有的后端实现（CPU，GPU，和加速器）共享一个统一的图表示。Caffe2，用于优化生产环境。


### Pytorch

PyTorch是Facebook人工智能研究所用的框架。它的前端注重灵活性、调试以及动态神经网络，能够快速进行实验。由于它依赖Python，所以它没有针对生产和移动部署而优化。当研究项目产生了有价值的结果时，模型需要转移到生产中。传统方法是通过在产品环境中用其他框架来重写训练流程来实现转移。最近Facebook开始搭建ONNX工具来简化这一转移过程。PyTorch，主要用于优化研究环境。


## 从数据到模型

对于Facebook的许多复杂机器学习应用，例如Ads和Feed Ranking，每一个训练任务需要处理的数据量超过上百的百万字节（terabytes）。此外，复杂的预处理操作用于确保数据的清理和规范化，以便高效传输和学习。这就对存储、网络和CPU提出了很高的资源要求。

Facebook采用将数据负载和训练负载分开的方法来解决这一问题。将不同的负载分配给不同的机器：数据处理机器“reader”从存储中读取数据，处理并压缩它们，随后传递给训练机器“trainer”，训练机器只需要快速高效地执行训练操作。

减少训练时间和加快模型交付需要分布式训练。分布式训练需要细致的网络拓扑和调度的协同设计，以有效地利用硬件达到良好的训练速度和质量。分布式训练中最常用的并行形式是数据并行，这就要求梯度下降在所有的节点上同步。

## Facebook推荐系统

Facebook团队之前已经在使用一个分布式迭代和图像处理平台——Apache Giraph。因其能够很好的支持大规模数据，Giraph就成为了Facebook推荐系统的基础平台。

在工作原理方面，Facebook推荐系统采用的是流行的协同过滤（Collaborative filtering，CF）技术。CF技术的基本思路就是根据相同人群所关注事物的评分来预测某个人对该事物的评分或喜爱程度。从数学角度而言，该问题就是根据用户-物品的评分矩阵中已知的值来预测未知的值。其求解过程通常采用矩阵分解（Matrix Factorization, MF）方法。MF方法把用户评分矩阵表达为用户矩阵和物品的乘积，用这些矩阵相乘的结果R’来拟合原来的评分矩阵R，使得二者尽量接近。如果把R和R’之间的距离作为优化目标,那么矩阵分解就变成了求最小值问题。

对大规模数据而言，求解过程将会十分耗时。为了降低时间和空间复杂度，一些从随机特征向量开始的迭代式算法被提出。这些迭代式算法渐渐收敛，可以在合理的时间内找到一个最优解。**随机梯度下降（Stochastic Gradient Descent, SGD）算法**就是其中之一，其已经成功的用于多个问题的求解。SGD基本思路是以随机方式遍历训练集中的数据，并给出每个已知评分的预测评分值。用户和物品特征向量的调整就沿着评分误差越来越小的方向迭代进行，直到误差到达设计要求。因此，SGD方法可以不需要遍历所有的样本即可完成特征向量的求解。**交替最小二乘法（Alternating Least Square, ALS）**是另外一个迭代算法。其基本思路为交替固定用户特征向量和物品特征向量的值，不断的寻找局部最优解直到满足求解条件。
