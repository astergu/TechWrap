"AV company" referring to autonomous driving companies.

# 自动驾驶中所用的状态

## 车辆定位信息

## 车辆状态信息

## 车辆动力学模型

Bicycle Model是汽车动力学模型的一种，此模型把汽车的两个前轮和两个后轮替换成一个前轮和一个后轮，用两个轮子的运动代替四个轮子的运动。汽车的状态会被描述成(x, y, \theta)，其中\theta代表汽车的朝向。另有一个\psi表示前轮的方向盘转角。

# 自动驾驶中所用到的算法

## 地图 Mapping

## 定位算法 Localization

## 规划算法 Motion Planning

    一般来说，自动驾驶的规划分为两个部分，一个是global planning（也就是routing），即根据高精地图和车的起止点信息规划出的路网级的规划路线，第二个是local planning，也就是道路级别的局部规划，即给定周围的环境信息（比如周围的障碍物信息，红绿灯信息等等）来进行路径和速度规划，目标是安全舒适的行驶。

### A*算法

A*搜索算法，俗称A星算法，作为启发式搜索算法中的一种。这是一种再图形平面上，有多个节点的路径，求出最低通过成本的算法。

A*算法最为核心的部分，就在于它的一个估值函数的设计上：*f(n) = g(n) + h(n)*.

其中*f(n)*是每个可能试探点的估值，它由两部分组成，*g(n)*表示从起始搜索点到当前点的代价（通常用某结点在搜索树中的深度来表示），*h(n)*表示启发式搜索中最为重要的一部分，即当前结点到目标结点的估值。

A*算法与广度、深度优先和Dijkstra 算法的联系就在于：当g(n)=0时，该算法类似于DFS，当h(n)=0时，该算法类似于BFS。且同时，如果h(n)为0，只需求出g(n)，即求出起点到任意顶点n的最短路径，则转化为单源最短路径问题，即Dijkstra算法。

### Incremental Search

常用两种方法：1) **Rapidly-exploring Random Trees (RRTs)**; 2) **Lattice Planners (LP)**.



## Jingchi
- Orienteering Game
    - Description: We are planning an orienteering game. The aim of this game is to arrive at the goal (G) from the start (S) with the shortest distance.
However, the players have to pass all the checkpoints (@) on the map.
In this problem, an orienteering map is to be given.
    - [http://www.cnblogs.com/crazyacking/p/4474932.html ](http://www.cnblogs.com/crazyacking/p/4474932.html)
    - **Calculate the minimum distance from the start to the goal with passing all the checkpoints.**
- Given a set of 2D points, **compute the convex hull**. (Convex hull is the smallest convex polygon containing
the points).   
    - **计算凸包**：在平面中给出N个点，找出一个由其中某些点作为顶点组成的凸多边形，恰好能围住所有的N个点。
    - Solutions:
        - Brute Force: 两点确定一条直线，如果剩余的其它点都在这条直线的同一侧，则这两个点是凸包上的点，否则就不是。
- Given some more points, find if they are inside the convex hull.
- Can you extend above problems to 3D points? 

## Drive.ai
- Probability. Bayes rule.
- Judge whether four points form a square.
- There is a huge binary file which has to be reversed. We can read/write using the following functions. The goal is to reverse the file without using any auxiliary file.
    - read(fileName, startIndex, buffer, bufferSize)
    - write(fileName, startIndex, buffer, bufferSize)
    - knowledge points: mutex, crash recovery
- Implement a connected component labeling algorithm on a 2D matrix.
- Given stride and kernel sizes for each layer of a neural network, compute the receptive field of a particular node in the network. 
- What is the difference between volatile and synchronized?
- Implement a scheduler.
- Radix sorting
- Identify objects in camera.
    - You're given a H-by-M matrix with each element the depth detected of part of an object. You're asked to identify objects in the matrix. If number of elements in smaller than S, it's ignored. If adjacent depth difference is bigger than D, it's considered to be different object.
- Implement malloc and free functions
- Get the sum of int array.
    - Follow up: 
        - integer overflow
        - distributed systems
- The data structure you like most, e.g.
    - hashmap
        - insert function of Cuckoo Hash
- Huffman Encoding
- Palindrome (DP)
- LRU Cache
- Merge two sorted array
- In Docker, building an image has dependencies. An image can only be built once its dependency is built (If the dependency is from outside, then the image can be built immediately). Sometimes, engineers make mistakes by forming a cycle dependency of local images. In this case, ignore the cycle and all the images depending on this cycle. Input is a vector of pair of images (image, its dependency). Output the order of images to be built in order.
- Math proof
    - 平面上六个点，任意三个点不共线（任意三点可以构成一个三角形）且任意两点距离唯一，求证一定存在两点，两点间线段既是一个三角形最大边又是另外一个三角形的最小边。
- 给定每秒帧数、每帧像素数量，每个像素大小，以及压缩率，计算一个给定大小的硬盘能够存多长的视频。无trick直接算。
- 给定一个2D array，里面是像素值，还有两个阈值D和S。如果相邻像素值差别小于等于D，则在同一个object里面。如果一个object里面的元素个数 小于等于S，则将这个object里面的像素值都设为0，否则把这个object里面所有像素值设为同一个ID，具体ID值随便，非负即可。
- 给一个API可以从一个stream读一定数量的字节到一个buffer，并且一个帧的末尾是0x00 0x00 0x01，写一个函数返回当前帧的末尾位置。
- 任务调度问题
- 二维平面一堆点，求最短线段的长度，必须N * logN。 [ShortestLineSegment.cpp](ShortestSegment.cpp)
- **MaxScoreCircle**: [python](MaxScoreCircle.py), [c++](MaxScoreCircle.cpp) 
    - 二维平面坐标系里一堆点，坐标点都是(X, Y)，X和Y都是整数，每个坐标点上携带一个double类型的score值，求从原点开始画一个圆，使得圆中的点的score之和最大。
- 给一个一维数组，比如，[1, 2, 3, 4, 5, 6, 7, 8]，然后两两求平均数，再把两两的差值记录在最后，得到[1.5, 3.5, 5.5., 7.5, -1, -1, -1, -1]。然后对前半部分进行相同的操作，后半数组保持不变，反复操作直到只有一个数了。

## Nuro
- How to check [two line segments intersect](../../Algorithms/Geometry/CheckTwoLineSegmentsIntersect.cpp) (2-Dimension)?
- How to tell [if a polygon is closed](../../Algorithms/Geometry/IsPolygonClosed.cpp)?
- Build a matrix class in C++
- Write a Lyapunov stability analysis for a first order diff eq. 
- Hashmap implementation ([C/C++](../../Algorithms/HashTable/HashTable.h))
- Write a function to get an angle between clock hands.
- [LC 778](../../Algorithms/Graph/SwimInRisingWater.cpp)
- Flip Image

## Didi Labs
- 给定由一组points<x, y>组成的线, 如何分割成相同长度的两条线段？

### Business related
- Robotics planning question 
- How would you tackle this open-ended challenge for self-driving cars?
- Deep Learning
