- [系统设计面试方法](#系统设计面试方法)
  - [面试流程](#面试流程)
    - [Step-by-Step Guide](#step-by-step-guide)
    - [思考方法\&找blog方法](#思考方法找blog方法)
  - [面试题类型](#面试题类型)
  - [资源](#资源)
    - [Educative.io系统设计课](#educativeio系统设计课)
    - [Design Data Intensive Applications](#design-data-intensive-applications)
    - [Engineer Blogs at Big Tech Companies](#engineer-blogs-at-big-tech-companies)
      - [Google](#google)
      - [Meta](#meta)
      - [LinkedIn](#linkedin)
      - [AWS](#aws)
      - [Netflix](#netflix)
      - [Airbnb](#airbnb)
      - [Uber](#uber)
      - [Twitter](#twitter)
      - [Pinterest](#pinterest)
      - [Datadog](#datadog)
    - [更多资源](#更多资源)
- [面经题](#面经题)
  - [General Questions](#general-questions)
  - [Meta](#meta-1)
  - [Amazon](#amazon)
  - [TikTok](#tiktok)
  - [Snowflake](#snowflake)
  - [LinkedIn](#linkedin-1)
  - [Databricks](#databricks)
  - [NewsBreak](#newsbreak)
  - [Oracle](#oracle)
  - [Cloudflare](#cloudflare)
  - [Nextdoor](#nextdoor)
  - [Wise](#wise)


# 系统设计面试方法

## 面试流程

### Step-by-Step Guide

- **Requirements Clarifcations**
  - Example: `Twitter-like service`
    - Will users of our service be able to post tweets and follow other people?
    - Should we also design and display the user's timeline?
    - Will tweets contain photos and videos?
    - Are we focuing on the backend only or are we developing the front-end too?
    - Will users be able to search tweets?
    - Do we need to display hot trending topics?
    - Will there by any push notification for new (or important) tweets?
- **System Interface Definition**
  - Define what APIs are expected from the system.
  - Example: `Twitter APIs`
    - postTweet(user_id, tweet_data, tweet_location, user_location, timestamp,...)
    - generateTimeline(user_id, current_time, user_location,...)
    - markTweetFavorite(user_id, tweet_id, timestamp,...)
- **Back-of-the-envelope Estimation**
  - Estimate the scale of the system we're going to design.
  - Example: `Twitter estimation`
      - What scale is expected from the system (e.g., number of new tweets, number of tweet views, number of timeline generations per sec., etc.)?
      - How much storage will we need? We will have different number if users can have photos and videos in their tweets.
      - What network bandwidth usage are we expecting? This will be crucial in deciding how we will manage traffic and balance load between servers.
- **Defining Data Model**
  - clarify how data will flow among different components of the system.
  - guide towards data partititioning and management.
  - Example: `Twitter Data Model`
    - **User**: UserId, Name, Email, DoB, CreationData, LastLogin, etc.
    - **Tweet**: TweetID, Content, TweetLocation, NumberOfLikes, Timestamp, etc.
    - **UserFollow**: UserID1, UserID2
    - **FavoriteTweets**: UserID, TweetID, TimeStamp
  - Which database system should we use?
- **High-level Design**
  - Draw a block diagram with 5-6 boxes representing the core components of our system. 
  - Example: `Twitter Design`
    - Need multiple application servers to serve all the read/write requests with load balancers in front of them for traffic distributions.
    - Need an efficient database that can store all the tweets and can support a huge number of reads.
    - Need a distributed file storage system for storing photos and videos.
- **Detailed Design**
  - Dig deeper into two or three componnents
  - Present different approaches, their pros and cons, and explain why we will prefer one approach on the other.
  - Example: `Twitter Design`
    - Since we will be storing a massive amount of data, how should we partition our data to distribute it to multiple databases? Should we try to store all the data of a user on the same database? What issue could it cause?
    - How will we handle hot users who tweet a lot or follow lots of people?
    - Since users' timeline will contain the most recent (and relevant) tweets, should we try to store our data in such a way that is optimized for scanning the latest tweets?
    - How much and at which layer should we introduce cache to speed things up?
    - What components need better load balancing?
- **Identifying and resolving bottlenecks**
  - Try to discuss as many bottlenecks as possible and different approaches to mitigate them.
  - Example: `Twitter bottlenecks`
    - Is there any single point of failure in our system? What are we doing to mitigate it?
    - Do we have enough replicas of the data so that if we lose a few servers we can still serve our users?
    - Similarly, do we have neough copies of different services running such that a few failures will not cause total system shutdown?
    - How are we monitoring the performance of our service? Do we get alerts whenever critical components fail or their performance degrades?

### 思考方法&找blog方法

1. 对每家onsite的公司，在地里翻完最近两年所有onsite面筋
2. aggregate所有design题目
3. 对每个题目找工业界实现的blog，阅读每个blog，选中最好的一到两个 
4. 读到烂熟，整理出我当面试官的话会问的所有问题不停考自己
5. 白板英文自行mock 3遍

## 面试题类型


## 资源

### Educative.io系统设计课
[https://www.educative.io/courses/grokking-modern-system-design-interview-for-engineers-managers](https://www.educative.io/courses/grokking-modern-system-design-interview-for-engineers-managers)

### Design Data Intensive Applications

- 第二部分请看3遍，可以解答40~50%你遇到的跟data有关的设计
- 有精力请看第三部分


### Engineer Blogs at Big Tech Companies

#### Google

> Official Blog: [https://blog.research.google/](https://blog.research.google/)

- **Google Research General**
  - [Google Research, 2022 & beyond: Language, vision and generative models](https://blog.research.google/2023/01/google-research-2022-beyond-language.html)
- **Youtube**
  - [Official Youtube Blog](https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/)
  - [Deep Neural Networks for YouTube Recommendations](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/45530.pdf)
  - [Recommending What Video to Watch Next: A Multitask Ranking System](https://daiwk.github.io/assets/youtube-multitask.pdf)
- **Question Answering**
  - [Exploring Transfer Learning with T5: the Text-To-Text Transfer Transformer](https://blog.research.google/2020/02/exploring-transfer-learning-with-t5.html)
- **Search**
  - [How Google Search Works](https://www.google.com/search/howsearchworks/)
    - Page Rank ([The algorithm that started Google](https://www.youtube.com/watch?v=qxEkY8OScYY))
- [TFX workshop by Robert Crowe](https://conferences.oreilly.com/artificial-intelligence/ai-ca-2019/cdn.oreillystatic.com/en/assets/1/event/298/TFX_%20Production%20ML%20pipelines%20with%20TensorFlow%20Presentation.pdf)
- [Google Cloud Platform Big Data and Machine Learning Fundamentals](https://www.coursera.org/learn/gcp-big-data-ml-fundamentals)

 
#### Meta

> Official Blog: [https://ai.meta.com/blog/](https://ai.meta.com/blog/)
> [Meta System Design Interview](https://igotanoffer.com/blogs/tech/meta-system-design-interview)

- **General**
  - [Machine Learning at Facebook Talk](https://www.youtube.com/watch?v=C4N1IZ1oZGw)
  - [Scaling AI Experiences at Facebook with PyTorch](https://www.youtube.com/watch?v=O8t9xbAajbY)
  - [Understanding text in images and videos](https://ai.facebook.com/blog/rosetta-understanding-text-in-images-and-videos-with-machine-learning/)
  - [Protecting people](https://ai.facebook.com/blog/advances-in-content-understanding-self-supervision-to-protect-people/) 
- **Ads**
  - [Practical Lessons from Predicting Clicks on Ads at Facebook](https://quinonero.net/Publications/predicting-clicks-facebook.pdf)
- **Newfeed Ranking**
  - [How Facebook News Feed Works](https://techcrunch.com/2016/09/06/ultimate-guide-to-the-news-feed/)
  - [How does Facebook’s advertising targeting algorithm work?](https://quantmar.com/99/How-does-facebooks-advertising-targeting-algorithm-work)
  - [ML and Auction Theory](https://www.youtube.com/watch?v=94s0yYECeR8)
  - [Serving Billions of Personalized News Feeds with AI - Meihong Wang](https://www.youtube.com/watch?v=wcVJZwO_py0&t=80s)
  - [Generating a Billion Personal News Feeds](https://www.youtube.com/watch?v=iXKR3HE-m8c&list=PLefpqz4O1tblTNAtKaSIOU8ecE6BATzdG&index=2)
  - [Instagram feed ranking](https://www.facebook.com/atscaleevents/videos/1856120757994353/?v=1856120757994353)
  - [How Instagram Feed Works](https://techcrunch.com/2018/06/01/how-instagram-feed-works/)
- [Photo Search](https://engineering.fb.com/ml-applications/under-the-hood-photo-search/)
- Social Graph Search
- **Recommendation**
  - [Instagram explore recommendation](https://about.instagram.com/blog/engineering/designing-a-constrained-exploration-system)
  - [Recommending items to more than a billion people](https://engineering.fb.com/core-data/recommending-items-to-more-than-a-billion-people/)
  - [Social recommendations](https://engineering.fb.com/android/made-in-ny-the-engineering-behind-social-recommendations/)
- [Live Videos](https://engineering.fb.com/ios/under-the-hood-broadcasting-live-video-to-millions/)
- [Large Scale Graph Partitioning](https://engineering.fb.com/core-data/large-scale-graph-partitioning-with-apache-giraph/)
- [TAO: Facebook’s Distributed Data Store for the Social Graph](https://www.youtube.com/watch?time_continue=66&v=sNIvHttFjdI&feature=emb_logo) ([Paper](https://www.usenix.org/system/files/conference/atc13/atc13-bronson.pdf))
- [NLP at Facebook](https://www.youtube.com/watch?v=ZcMvffdkSTE)

#### LinkedIn

> Official Blog: [https://www.linkedin.com/blog/member](https://www.linkedin.com/blog/member)

- [Learning to be Relevant](http://www.shivanirao.info/uploads/3/1/2/8/31287481/cikm-cameryready.v1.pdf)
- [Two tower models for retrieval](https://www.linkedin.com/pulse/personalized-recommendations-iv-two-tower-models-gaurav-chakravorty/)
- A closer look at the AI behind course recommendations on LinkedIn Learning: [Part 1](https://engineering.linkedin.com/blog/2020/course-recommendations-ai-part-one), [Part 2](https://engineering.linkedin.com/blog/2020/course-recommendations-ai-part-two)
- [Intro to AI at Linkedin](https://engineering.linkedin.com/blog/2018/10/an-introduction-to-ai-at-linkedin)
- [Building The LinkedIn Knowledge Graph](https://engineering.linkedin.com/blog/2016/10/building-the-linkedin-knowledge-graph)
- [The AI Behind LinkedIn Recruiter search and recommendation systems](https://engineering.linkedin.com/blog/2019/04/ai-behind-linkedin-recruiter-search-and-recommendation-systems)
- [Communities AI: Building communities around interests on LinkedIn](https://engineering.linkedin.com/blog/2019/06/building-communities-around-interests)
- [Linkedin's follow feed](https://engineering.linkedin.com/blog/2016/03/followfeed--linkedin-s-feed-made-faster-and-smarter)
- XNLT for A/B testing

#### AWS

> Official Blog: [https://aws.amazon.com/blogs](https://aws.amazon.com/blogs)

- [AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/)
- [Deploy a machine learning model with AWS Elastic Beanstalk](https://medium.com/swlh/deploy-a-machine-learning-model-with-aws-elasticbeanstalk-dfcc47b6043e)
- [Deploying Machine Learning Models as API using AWS](https://medium.com/towards-artificial-intelligence/deploying-machine-learning-models-as-api-using-aws-a25d05518084)
- [Serverless Machine Learning On AWS Lambda](https://medium.com/swlh/how-to-deploy-your-scikit-learn-model-to-aws-44aabb0efcb4)

#### Netflix
> Official Blog: [https://netflixtechblog.com/](https://netflixtechblog.com/)

- [Recommendation at Netflix](https://www.slideshare.net/moustaki/recommending-for-the-world)
- [Past, Present & Future of Recommender Systems: An Industry Perspective](https://www.slideshare.net/justinbasilico/past-present-future-of-recommender-systems-an-industry-perspective)
- [Deep learning for recommender systems](https://www.slideshare.net/moustaki/deep-learning-for-recommender-systems-86752234)
- [Reliable ML at Netflix](https://www.slideshare.net/justinbasilico/making-netflix-machine-learning-algorithms-reliable)
- [ML at Netflix (Spark and GraphX)](https://www.slideshare.net/SessionsEvents/ehtsham-elahi-senior-research-engineer-personalization-science-and-engineering-group-at-netflix-at-mlconf-sea-50115?next_slideshow=1)
- [Recent Trends in Personalization](https://www.slideshare.net/justinbasilico/recent-trends-in-personalization-a-netflix-perspective)
- [Artwork Personalization @ Netflix](https://www.slideshare.net/justinbasilico/artwork-personalization-at-netflix)
- [Evolution of Application Data Caching: From RAM to SSD](https://netflixtechblog.com/evolution-of-application-data-caching-from-ram-to-ssd-a33d6fa7a690)
- [Aplication Data Caching Using SSDs](https://netflixtechblog.com/application-data-caching-using-ssds-5bf25df851ef)
- [Caching for a Global Netflix](https://netflixtechblog.com/caching-for-a-global-netflix-7bcc457012f1)
- [Cache warming: Agility for a stateful service](https://netflixtechblog.com/cache-warming-agility-for-a-stateful-service-2d3b1da82642)
- [Caching at Netflix: The Hidden Microservice](https://www.youtube.com/watch?v=Rzdxgx3RC0Q)

#### Airbnb

> Official Blog: [https://medium.com/airbnb-engineering](https://medium.com/airbnb-engineering)

- [Categorizing Listing Photos at Airbnb](https://medium.com/airbnb-engineering/categorizing-listing-photos-at-airbnb-f9483f3ab7e3)
- [WIDeText: A Multimodal Deep Learning Framework](https://medium.com/airbnb-engineering/widetext-a-multimodal-deep-learning-framework-31ce2565880c)
- [Applying Deep Learning To Airbnb Search](https://dl.acm.org/doi/pdf/10.1145/3292500.3330658)
- [Avoiding Double Payments in a Distributed Payments System](https://medium.com/airbnb-engineering/avoiding-double-payments-in-a-distributed-payments-system-2981f6b070bb)


#### Uber

> Official Blog: [https://www.uber.com/en-US/blog/engineering/](https://www.uber.com/en-US/blog/engineering/)

- [Cherami: Scalable Task Queue](https://www.uber.com/blog/cherami-message-queue-system/)
- [DeepETA: How Uber Predicts Arrival Times Using Deep Learning](https://www.uber.com/blog/deepeta-how-uber-predicts-arrival-times/)

#### Twitter

- [Timelines at Scale](https://www.infoq.com/presentations/Twitter-Timeline-Scalability/)

#### Pinterest

- [Scaling Pinterest](https://www.infoq.com/presentations/pinterest/)

#### Datadog



### 更多资源

- [System Design Primer](https://github.com/donnemartin/system-design-primer)
- [Full Stack Deep Learning course](https://fall2019.fullstackdeeplearning.com/)
- [Production Level Deep Learning](https://github.com/alirezadir/Production-Level-Deep-Learning)
- [Machine Learning Systems Design](https://github.com/chiphuyen/machine-learning-systems-design)
- [Stanford course on ML system design](https://stanford-cs329s.github.io/) [[video]](https://www.youtube.com/watch?v=AZNTqytOhXk&t=12771s)
- Book: [Designing Machine Learning Systems: An Iterative Process for Production-Ready Applications](https://www.amazon.com/Designing-Machine-Learning-Systems-Production-Ready/dp/1098107969)
- [Building a reliable and scalable metrics aggregation and monitoring system](https://www.youtube.com/watch?v=UEJ6xq4frEw&t=667s)
- [RedisConf17: Geospatial Indexing](https://www.youtube.com/watch?v=cSFWlF96Sds)


# 面经题

## General Questions

- **Design a URL shortening service (TinyURL)**
 
## Meta

- 在线比赛系统
- **Ads aggregator**
- [[source]](https://leetcode.com/discuss/interview-question/1935481/meta-system-design-interview-question-e4e5) There's a very large website that we want to crawl. This site is organized like Wikipedia, with every page linking to multiple other pages. Please design a system that:
  - Downloads all pages from this website
  - Downloads each URL once
  - Minimizes the amount of traffic coming from any given node
- **Design messager/whatsapp**
- **Design instagram**
- Design a weapon ads sale enforce system (过滤卖武器的广告)
- Top K Songs
- **Design ticketmaster**
- Design a video watching system (Youtube)
  - Functional Requirement
    - switch video resolution
    - watch history
- Streaming Service

## Amazon

- Design a facebook messager/whatsapp
- 假设公司有很多可以监测天气的sensor分散在各地，设计一个app可以让也用户查看天气
- Design a URL shortener

## TikTok

- Design a distributed rate limiter
- Design ticketmaster
- Design a job scheduler
- 

## Snowflake

- **Design a file storage system**　(不能用现有的db，只能用OS file system的API，类似GFS)

## LinkedIn

- 设计LinkedIn主页
- 设计一个calender订会议室

## Databricks

- Design a distributed file system (建议把GFS/HDFS原文看，各种tradeoff)


## NewsBreak

1. 设计油管观看记录

## Oracle

- Design web crawler

## Cloudflare

- Distributed KV storage
  - 100 DBs globally put/get operation in 5mins，one write‍‌‍‍‌‍‍‌‍‍‌‌‌‌‍‌‍‍‌ server, others for read only

## Nextdoor

- nextdoor feeds with image, upvote a post, top k most voted post

## Wise

- 在主页上实时显示过去24小时汇款的总额度，总数必须转换成浏览者所在地区的货币为单位。
  - 这个总额必须准确，你如果使用了kafka或者其他eventual consistency的方法，他们会问你怎么handle 数据的完整性。