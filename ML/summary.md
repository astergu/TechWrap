# Machine Learning

noise, variance and bias.

An ensemble is just a collection of predictors which come together (e.g. mean of all predictions) to give a final prediction. Ensembling techniques are further classified into *Bagging* and *Boosting*. 
- **Bagging**: Bagging is a simple ensembling technique in which we build many independent predictors/models/learners and combine them using some model averaging techniques ((e.g. weighted average, majority vote or normal average). Example of bagging ensemble is *Random Forest models*.
- **Boosting**: Boosting is an ensemble technique in which the predictors are not made independently, but sequentially. Gradient Boosting is an example of boosting algorithm.

# Classical Problems 典型问题

## 多标签分类问题 Multi-label classification

问题简介：[wiki](https://en.wikipedia.org/wiki/Multi-label_classification)

多标签分类问题是多分类问题的一般化问题，因为多分类问题一般是把实例分类到多个分类中的一个类别上，而多标签分类问题不限定实例的分类个数。

### 基本方法

方法基本上分为两种，一种是将问题转化为传统的分类问题，二是调整现有的算法来适应多标签的分类。

- **Baseline Approach** (*binary relevance* method)
    - 为每一个label单独训练一个二分类器(binary classifier)
- **Approaches without transformations**
    - **boosting**: AdaBoost
    - **k-nearest neighbors**: ML-kNN (extended from kNN classifier)
    - **Decision Tree**
    - **Neural Networks**

[sklearn support for Multiclass vs. Multilabel classification](http://scikit-learn.org/stable/modules/multiclass.html)

- **Multi-Label vs. Multi-Class**
    - Multi-class分类问题只会把实例分类到一个分类，而Multi-label分类问题会把实例分类到多个label。


- **One-Vs-The-Rest**策略，也就是**one-vs-all**，这种策略对每个类产生一个分类器。对每一个分类器，正例是当前类，负例是非当前类的所有其他类。

## Boosting Models

Boosting refers to this general problem of producing a very accurate prediction rule by combining rough and moderately inaccurate rules-of-thumb.

Gradient boosting involves three elements:
1. A loss function to be optimized.
2. A weak learner to make predictions.
3. An additive model to add weak learners to minimize the loss function.


### AdaBoost

The first boosting algorithm


XGBoost
