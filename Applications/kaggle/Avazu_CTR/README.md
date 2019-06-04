# Avazu Click-Through Rate Prediction

## 简介

在CTR预估任务里，一般优化的是：
- expected value，也就是一个广告的点击概率乘以该广告的价值，这是基于CPC（Cost-per-click）的广告计算基础。
- 单纯优化点击。



## 数据分析

```python
import pandas as pd

df = pd.read_csv('train.csv')
print(df['click'].mean())
print(df.groupby(by='device_type').agg({'click':'mean'}))
```
训练数据一共有40428967条记录，**click**列代表了用户是否点击了该条广告。**mean**可以取得平均点击率，由此我们得到**0.16980562476404604**，这个可以作为点击率预估得**baseline**。同时，根据**device_type**分类得到的点击率如下：
| device_type      | click |
| ----------- | ----------- |
| 0      | 0.210731       |
| 1   | 0.169176        |
| 2   | 0.064516        |
| 4   | 0.095444        |
| 5   | 0.093842        |

## 方法

### 方法一：Logistic Regression

[https://turi.com/learn/gallery/notebooks/click_through_rate_prediction_intro.html](https://turi.com/learn/gallery/notebooks/click_through_rate_prediction_intro.html)

### 方法二：


## 链接

- 《机器学习》，周志华。
- 