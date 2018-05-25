"AV company" referring to autonomous driving companies.

## Jingchi
- Orienteering Game
    - Description: We are planning an orienteering game. The aim of this game is to arrive at the goal (G) from the start (S) with the shortest distance.
However, the players have to pass all the checkpoints (@) on the map.
In this problem, an orienteering map is to be given.
    - [http://www.cnblogs.com/crazyacking/p/4474932.html](http://www.cnblogs.com/crazyacking/p/4474932.html)
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
- 给定一个2D array，里面是像素值，还有两个阈值D和S。如果相邻像素值差别<=D，则在同一个object里面。如果一个object里面的元素个数<=S，则将这个object里面的像素值都设为0，否则把这个object里面所有像素值设为同一个ID，具体ID值随便，非负即可。
- 给一个API可以从一个stream读一定数量的字节到一个buffer，并且一个帧的末尾是0x00 0x00 0x01，写一个函数返回当前帧的末尾位置。
- 任务调度问题
- 二维平面一堆点，求最短线段的长度，必须N * logN。
- [MaxScoreCircle](MaxScoreCircle.py): 
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

### Business related
- Robotics planning question 
- How would you tackle this open-ended challenge for self-driving cars?
- Deep Learning
