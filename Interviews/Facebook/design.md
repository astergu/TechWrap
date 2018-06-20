# Google Search是如何实现的

## 搜索词解析

利用语言模型把搜索关键词分解为可以在索引中查询(lookup)的词。


# Facebook News Feed Design 信息流设计

## Requirements Gathering

- **目标平台**：手机，网络，电脑桌面
- **需要什么特征？**
    - CRUD posts
    - Commenting on posts
    - Sharing posts
    - Trending posts
    - Tag People
    - Hashtags
- **什么是一个news feed post?**
    - 作者、内容、媒体、Tags、Hashtags、评论、回复、操作（CRUD, 评论/回复）
- **什么是一个news feed?**
    - Sequence of posts
    - Query pattern: query for a user's ranked news feed
    - Operations:
        - Append: fetch more posts.
        - Delete: I don't want to see this.
- **度量标准**
    - User retention
    - Ads revenue
    - Fast loading time
    - Bandwidth
    - Server costs

## Data Modelling 数据模型

- **使用什么样的数据库?**
    - 数据是结构化的
- **设计必要的数据表，及其关系**
    - `users`, `posts`, `likes`, `follows`, `comments`
