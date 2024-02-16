Facebook的工作方向

# Machine Learning in Facebook

Facebook使用的机器学习模型包括逻辑回归（Logistic Regression，LR）、支持向量机（Support Vector Machine，SVM）、梯度提升决策树（Gradient Boosted Decision
Tree，GBDT），以及深度神经网络（Deep Neural Network，DNN）。LR和SVM用于训练和预测的效率很高。GBDT使用额外的计算资源可以提高准确性。DNN是最具表现力的模型，有能力达到最高的准确性，但是它利用的资源最多（计算量至少超过像LR和SVM这样的线性模型一个数量级）。

在DNN中，主要使用的网络类型有三种：多层感知器（Multi-Layer Perceptrons，MLP）一般用于结构化的输入特征（如排序），卷积神经网络（Convolutional Neural Networks，CNN）作为空间处理器（如图像处理），以及循环神经网络（RNN、LSTM）主要用于序列处理器（如语言处理）。

![Facebook产品或服务使用的机器学习算法](https://s3.amazonaws.com/infoq.content.live.0/articles/applied-machine-learning-at-facebook/zh/resources/3541-1518027537279.png)

## Search
### Content Search

**Goal**

People use **content search** to find trillion pieces of shared content, such as posts, photos,
videos, and links. Thus they develop ML/ranking algorithms that are a three way optimization between
the query, searcher and context.

**Technologies**

Deep Learning, GBDT, Ranking, Recommendation Algorithms, NLP/Context Understanding

### Search System

**Goal**

It starts with Typeahead/Autocomplete, passes through NLP service for query understanding and query
rewriting (including spell correction), and ends with Whole Page Ranking to order and display the 
final results. Search System uses a wide variety of ranking algorithms, NLP, and entity linking to 
understand a searcher's intent and provide the most relevant results possible.

**Technologies**

Deep Learning, GBDT, Ranking, Recommendation Algorithms, NLP/Content Understanding


## Ads Core

### Business Integrity

**Goal**

Help make sure only high quality content created by advertisers, page owners,
merchants, etc. are delivered to the users in order to ensure a satisfactory
and sustainable experience. Ensure scalability of content review process and 
minimizes the amount of negative experiences within Ads, Pages, Marketplace, 
Groups, Messenger, etc., by automatically detecting policy violation and low 
quality content.

**Technologies**

Supervised and unsupervised ML, deep learning, content understanding and NLP, 
penalty/ranking features.

### Ads Ranking

**Goal**

Maximize the value of advertising delivered to advertisers and Facebook users, 
through building scalable and highly automated machine learning infrastructure.

**Technologies**

Deep learning, multi-task learning, Caffe 2.0, transfer learning, text/image understanding,
sparsity, recommender systems, user intent understanding, exploration and exploitation,
cold-start.
 

### Ads Targeting

**Goal**

Target exactly the users advertisers want.

**Technologies**

Deep learning, multi-task learning, Caffe 2.0, transfer learning, text/image understanding, 
sparsity, recommender systems, user intent understanding, exploration and exploitation,
cold-start.

## News Feed

### News Feed Ranking

**Goal**

Show people the stories that matter the most to them. Creates and sorts billions of stories 
every minute in realtime to create a personalized newspaper for each user.

**Technologies**

Deep learning, ranking, recommendation algorithms, NLP/Content understanding

# References
- Link: [Facebook的应用机器学习平台](http://www.infoq.com/cn/articles/applied-machine-learning-at-facebook?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=articles_link&utm_content=link_text) 