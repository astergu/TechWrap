# 论文阅读清单

## 推荐系统

- **The Wisdom of The Few**
  - 目标
    - 为Netflix的用户做推荐: Predict a user's rating for a particular item
  - 背景
    - 现有方法：Nearest-neighbor collaborative filtering
        - 缺点：data sparsity (数据稀疏), noise (噪音)
    - 传统方法：Collaborative Filtering (协同过滤)
        - 缺点：新用户问题，如何定义用户间的相似度，数据中存在噪声，计算量大
        - 改进：传统的协同过滤基于显式的用户反馈（feedback）来预测，具有比较大的error。