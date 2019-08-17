# 1-50 Questions

1. **Two Sum** [[c++](1-50/1_TwoSum.cpp), [python](1-50/1_TwoSum.py)] :star: 
> Array
   - 问题描述：求数组中两数之和等于一个指定值的索引。
   - 方法：
     - Naive算法（Brute Force）:采用两层循环来为每个x寻找是否有对应的其他元素其加起来符合要求。时间复杂度为O(N<sup>2</sup>)，空间复杂度为O(1)；
     - Two-pass Hash table: 先遍历数组，把各个元素及其对应的index加入到dict，再遍历一次，对每个元素x去寻找对应的target - x是否在dict中。时间复杂度为O(N)，空间复杂度为O(N);
     - One-pass hash table: 采用HashTable记录数据和index，时间复杂度为O(N), 空间复杂度为O(N) [100%]
   - 拓展思考 
     - 如果有多个答案？
     - 如果元素可以被重复使用？
     - 如果是两个数以上的和呢？
   - Similar problems
2.  **Multiply Strings** [[c++](1-50/43_MultiplyStrings.cpp), [python](1-50/43_MultiplyStrings.py)]: 大数乘法
    -  问题描述：两个用字符串表示的字整数的乘积。
    -  方法
       -  把字符串当做整数，按位相乘再相加，时间复杂度为O(N*M)，N和M分别为两个字符串的长度。

3.  **PlusOne** [[c++](51-100/66_PlusOne.cpp), [python](51-100/66_PlusOne.py)] :star:
    - 问题描述： 加一
    - 方法
      - 遍历：重点需要考虑corner case，即增加以后多一位，也要避免首位为零的情况。[plusOne]，时间复杂度为O(N)。
      - 递归：[plusOne2]，时间复杂度为O(N)。

4.   **Single Number**

# 501-600 Questions

509. **Fibonacci Number**

# 801-900 Questions

832. **Fliping an Image**
     - 方法：

# 1001-1100 Questions

1086. **High Five** [python](1001-1000/1086_Hive_Five.py)  :star:
> Array
      
      - 方法：
          - 方法一：遍历。时间复杂度O(NKlogK)，K是student最多的科目数。
          - 方法二：排序，优先队列。



