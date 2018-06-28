Facebook面试准备的试题。
## ML Engineer Interview Process 机器学习工程师面试流程

- **Phone Screen Interview (45 min)**
    - 1~2 coding questions, about computer science foundamentals, including data structures, algorithms, etc.
- **Onsite Interview (4~5 hours), all on white board**
    - *2 coding interviews*: 2 coding questions per interview, each interview lasts 45 min. (4 coding questions in total)
    - *System Design Interview* (45min): mostly focus on building large-scale systems. Think through the design of a complex system, especially with regards to tradeoffs arounds consistency, availability, partition tolerance.
        - Example questions: 
            - Design a [**simplified version of Twitter**](design.md#task-2:-design-a-simplified-version-of-twitter)
            - Design a **key-value store**
            - Design [**Google Search**](design.md#task-4:-google-search是如何实现的)
            - Design a [**Facebook News Feed System**](design.md#task-5:-facebook-news-feed-design-信息流设计)
            - Architect a **world-wide video distribution system**
            - Build **Facebook chat**
            - Design a [**URL shortening service like bit.ly**](design.md#task-1:-design-a-url-shortening-service) 
            - Design a **client-server application which allows people to play chess with one another**
            - **How would you store the relations in a social network like Facebook and implement a feature where one user receives notifications when their friends like the same things as they do**
            - Design a [**Text Summarization system**](design.md#task-3:-text-summarization)
        - **Expectations**
            - Arrive at an answer in the face of unusual constraints
            - Visualize the entire problem and solution space
            - Make trade-offs like consistency, availability, partitioning, performance
            - Give ballpark numbers on QPS supported, number of machines needed using a modern computer
            - How much have you thought about Facebook and some of the unique problems we face
        - **A Good Design**
            - Clearly understand the problem
            - Propose a design for a system that breaks the problem down into components, that can be built independently, and you can drill into any piece of the design and talk about it in detail
            - Identify the bottlenecks as the system scales and understand the limitations in your design
            - Understand how to adapt the solution when requirements change
            - Draw diagrams that clearly describe the relationship between the different components in the system
            - Calculate (back-of-envelope) the physical resources necessary to make this system work
        - **How to study**
            - To practice, take any well-known app and imagine you work for a competitor. Your job is to figure out 1) where are the most important problems for their system and 2) what are the constraints for their system. Answering these questions will help you focus on the most important problems and not worry about solving problems that are not relevant.
            - For example, Google’s index building layer has many more components for document understanding. It would need components for extracting deep links, contact information, referrals (for page rank). On the other hand, Twitter’s index building should be simpler due to small size tweets and some rich media information for attached media. Twitter’s search is head heavy.  So a bulk of engineering efforts in designing their search should go to rapidly indexing new tweets and making them searchable.
            - Work out the above problems on a paper and just think about the ways to break them down.  It also helps to read up on common large scale systems, like watch the public videos about memcached and learn how search engines work.  But during the interview, don’t parrot back what you read; make sure your solution actually answers the question being asked.

    - *ML Practical Design interview* (45min): give a open design question, design a machine learning solution and explain why.
        - Example questions
            - Design a [**news feed ranking system**](newsfeed_ranking.md)
            - Design [**local search ranking system**](local_search_ranking.md)
            - Design [**ads targeting system**](ads_ranking.md)
            - How would you build, train, and deploy a system to detect if multimedia and/or ads contents being posted violate terms or contains offensive materials?
        - **Expections**
            - Visualize the entire problem and solution space
            - Feature engineering
            - Detect flaws in machine learning systems and suggest improvements
            - Design consistent evaluation and deployment techniques
            - Understand architecture requirements (storage, performance, etc) of your system
            - Model product requirements into your ML system
        - **A Good Design**
            - Problem formulation
                - Optimization function
                - Supervision signal
            - Feature engineering
                - Data source
                - Representation
            - Model architecture
            - Evaluation metrics
            - Deployment (A/B testing)
        - **How to study**
            - To practice, take any well-known app and pick a system that can benefit from machine learning. Consider that system is built using a handful of rules for a small set of people. Now, consider you want to deprecate those rules and want to take advantage of machine learning, so you can easily extend that functionality to millions of people.
            - Brush up basic ML theory and be comfortable with concepts like **overfitting** and **regularization**.
            - Practice ability to convert intuitive ideas to concrete features. For example: number of likes is a good idea but a better feature would use involves **normalization**, **smoothing** and **bucketing**.
            - **Think about the problem end to end. What will you do after you train the model and the model does not perform well? How do you go about debugging an ML model? How do you evaluate and continuously deploy an ML model?**
            - **Be ready to analyze your approach. Having a good toolset of several different algorithms and understanding the tradeoffs is helpful. For example, be able to example advantages of logistic regression compared to SVM.**
            - **Work out the above problems on a paper and just think about the ways to break them down. It also helps to read up on common large-scale ML systems.  Watch the public videos and learn how google search ranking works.**
    - *Career Development Interview (Behavioral)* (45min): hosted by one of the leadership engineers, consist of a combination of two aspects: a conversation and coding. 
    - *Lunch* (45min): NOT an interview. 

## Popular Questions
- [x] [Subarray Sum Equals K](../../Algorithms/Array/SubarraySumEqualsK.py)
    - 利用prefixSum，只遍历一次便可得到全部的subarray sum，另外利用额外的map来记录之前的结果，最终时间复杂度为O(N)，空间复杂度为O(N)。
- [x] [Minimum Window Substring](../../Algorithms/String/MinimumWindowSubstring.py)
- [x] [Subarray with Given Sum](../../Algorithms/Array/SubarrayWithGivenSum.py)
- [x] [Schedule Tasks](../../Algorithms/Array/TaskScheduler.cpp)


## Glassdoor Software Engineer Questions
- [x] [Write code to raise a number to a power.](RaiseNumberToPower.py)
- [x] Suppose you have a matrix of numbers. How can you easily compute the [sum of any rectangle](SumOfRectangle.py) (i.e. a range \[row_start, row_end, col_start, col_end\]) of these numbers? How would you code this? 
    - Analysis: frequent queries on a static matrix, use dynamic programming
    - wiki: [https://en.wikipedia.org/wiki/Summed_area_table](https://en.wikipedia.org/wiki/Summed_area_table)
- [] You have two lightbulbs and a 100-storey building. You want to find the floor at which the bulbs will break when dropped. Find the floor using the least number of drops.
    - same idea as Google egg-dropping problem.
    - **first intuition**: use binary search. Start with floor 50, if the lightbulb breaks, then starts from 1 to 49. But if the lightbulb does not break, then drop it from 75, if it breaks, then try from 51 to 74. However, if in the first case, floor 49 is the answer, then you need to try 50 times, which is not a good solution.
    - **dynamic programming**: f(n) = min(1 + max(i - 1, f(n-i)))
- [x] Implement a function [rotateArray(vector<int> arr, int r)](RotateArray.py) which rotates the array by r places. E.g. 1 2 3 4 5 on being rotated by 2 gives 4 5 1 2 3.
    - leetcode page: [Rotating array in place](https://articles.leetcode.com/rotating-array-in-place/) 
- [] 3Sum [15]
- [] Word Break I/II [139]
- [] Decode Ways [91]
- [] Minimum Size Subarray Sum [209]
    - Map store previous values (O(N))
    - 把第一题extend到2D。给一个matrix，all elements are positive，问有没有一个sub rectangle加起来和等于target，return true/false.
- Intersection of Two Arrays II [350]
- [] The Skyline Problem [218]
- [] First Bad Version [278]
    - Min Queue, 跟Min Stack类似，实现一个Queue，然后O(1)复杂度获得这个Queue里最小的元素。
- [] Integral Time Stamps
    - Interval[startTime, stopTime]，给这样的一串区间I1, I2, ...In，找出一个time stamp出现在interval的次数最多。startTime <= t <= stopTime代表这个数在区间里面出现过。
    - Example: [1, 3), [2, 7), [4, 8), [5, 9)。5和6各出现了三次，所以答案返回5，6。
- [] Shortest continuous substring with all characters in input
    - Minimum Window Substring [76]
- [] 合并邮件列表
    - Given 1 million email list: list1[a@a.com, b@b.com], list2[b@b.com, c@c.com]..., combine lists with identical emails, and output tuples: (list1, list2, list4).
- [] Word Search [79]
- [] Letter Combinations of a Phone Number [17]
- [] Implement strStr() [28]
- [] Random Pick Index [398]
- [] Sudoku Solver [37]
- [] 一个完全树。node有parent指针。每个node的值为0或1。每个parent的值为两个子node的 “and” 结果现在把一个leaf翻牌子（0变1或者1变0）. visit 1point3acres.com for more. 把树修正一遍。
- [] Number of Islands [200]
- [] Binary Search Tree Iterator [173]
- [] BST iterator
    - Iterator for a list of BSTs (heap contain each BST's iterator)
- [] Longest Consecutive Sequence [128]
- [] Generate Parentheses [22]
- [] Product of Array Except Self [238]
- [] Number of 1 Bits [191]
- [] 给2D平面上的N个点，求离原点最近的K个点。
- [] Combination Sum [39]
- [] Valid Palindrome [125]
- [] Shortest Palindrome [214]
- [] Validate Binary Search Tree [98]
- [] Longest Arithmetic Progression
- [] Regular Expression Matching [10]
- [] Add and Search Word [211]
- [] Copy List with Random Pointer [138]
- [] Simplify Path [71]
- [] Maximal Square
- [] Binary Tree Vertical Order Traversal [314]
- [] House Robber [198]
- [] Maximum Subarray [53]
- [] Maximum Product Subarray [152]
- [] Longest Valid Parentheses [32]
- [] Find the Celebrity [277]
- [] Merge Intervals [56]
    - Variant: 一串start time － end time，格式是Apr 2010 － Mar 2011这种，要求计算出这些时间的总跨度，重叠的跨度不重复计算。举例：["Apr 2010 - Dec 2010", "Aug 2010 - Dec 2010", "Jan 2011 - Mar 2011"]
- [] Insert Interval [57]
- [] Valid Number [65]
- [] Meeting Rooms II [253]
    - 求最多interval的时间点，返回任意一个就行。



## Geeks For Geeks Software Engineer Questions
- [x] [Rotate and Delete](../Array/RotateAndDelete.py): Given an array of numbers (e.g. integers), there are two kinds of operations: rotate (clock-wise) and delete. 
Rotate the array *n* times and then delete the *n*th last element. If the *n*th last element does not exist then
deletes the first element present in the array. Your task is to find out which is the last
element that you deletes from the array so that the array becomes empty after removing it.
    - source: [https://practice.geeksforgeeks.org/problems/rotate-and-delete/0] (https://practice.geeksforgeeks.org/problems/rotate-and-delete/0)     
     
## Data Scientist Questions
- [] You're about to get on a plane to Seattle. You want to know if you should bring an umbrella. You call 3 random friends of yours who live there and ask each independently if it's raining. Each of your friends has a 2/3 chance of telling you the truth and a 1/3 chance of messing with you by lying. All 3 friends tell you that 
"Yes" it is raining. What is the probability that it's actually raining in Seattle?
