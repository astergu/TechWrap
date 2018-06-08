## 数组 Array

## 最小问题 Min

- **Coin Change** [[leet]](https://leetcode.com/problems/coin-change/description/) **动态规划**
    - 题意：给定一组硬币可能的取值，比如[1, 2, 5], 和需要拿出的总共的钱，求最少需要的硬币数量。如果不存在，返回-1.
    - 分析：直观反应是贪心算法，先尽可能拿最大面值的硬币，直到不能拿了再取次大的硬币，实际上行不通，因为原本有答案的可能会没有答案。因此这题应该采用**动态规划**，从0到需要达到的总钱数，子结构为dp[i] = min(dp[i-coins[j]) + 1, dp[i])，两层循环，内层是coins的枚举。[python](DynamicProgramming/CoinChange.py)

## 排列问题 Permutation

- **Next Permutation** [[leet]](https://leetcode.com/problems/next-permutation/description/)
    - 题意：找出当前数字排列的下一个字典序比它大的数字，原地排列。
    - 分析：借助举例来让问题更清晰，比如123->132, 213->231, 321->123，首先需要找到需要开始变化的位置，观察一下，123从倒数第二位开始变化，321从第一位开始变化，规律是从后往前找出第一个符合数字增序的索引i，比如123就是2, 213就是2，321就是0。接下去要做的是，从后往前，把第一个大于i-1的数字位的数字和i-1位进行交换. [python](String/NextPermutation.py) 

### 元素之和

- **3Sum三数之和** [[geeks]](https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/) [[leet]](https://leetcode.com/problems/3sum/description/) ** 利用排序减少搜索范围**
    - 题意：给定一个整数数组，寻找是否存在三个元素a,b,c，使得a,b,c相加之和等于某个给定值x？要求返回符合要求的a,b,c组合。
    - 分析：
        - **Extra memory**：最简单可以用一个map来记录已经遇到过的元素a及其index，再用两层loop来查看(x-b-c)是否在map中，如果有，则加入结果。时间复杂度O(N<sup>2</sup>)，空间复杂度O(N).
        - **Sorting**: 对数组进行排序，固定a的位置（从0到arr.size - 2），在循环内部，由后往前向内夹逼b和c。时间复杂度O(N^2)，空间复杂度O(1). [python](Array/3Sum.py)
        

## 字符串 String

- **Longest Palindromic Substring最长回文子串** [[leet]](https://leetcode.com/problems/longest-palindromic-substring/description/) [[geeks1]](https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/) [[geeks2]](https://www.geeksforgeeks.org/longest-palindromic-substring-set-2/)
    - 题意：在字符串s中找出最长的回文子串。
    - 分析：采用**动态规划**，最短回文子串为1。初始化一个二维bool数组dp为false，即记录的是s[i,j]是否是一个回文串。子结构为：1）dp[i][i]=true; 2）如果s[i]==s[j] and dp[i+1][j-1]=true or j - i小于2，那么dp[i][j]=true, 同时更新最长回文子串的起止位置。[python](String/LongestPalindromicSubstring.py)
    
## 链表 Linked List

- **Add Two Numbers** [[leet]](https://leetcode.com/problems/add-two-numbers/description/)
    - 题意：两个非负整数是用两个链表来表示的，数据是reverse order存储的，每个节点包含一个数字，把这两个数相加并且以链表返回。
    - 分析：实现问题，用一个carry记录进位. [python](LinkedList/AddTwoNumbers.py)

## Searching and Sorting 搜索和排序 

### Linear Search 线性搜索

定义：给定一组数，在数组中搜索元素x。时间复杂度O(n)，现实生活中很少用，因为哺乳Binary Search或哈希表高效。

### Binary Search 二分查找



## 预计算

- [Subarray Sum Equals K](Array/SubarraySumEqualsK.py)
    - 题目：找出一个数组中的连续元素之和等于K的子数组的个数。

## DFS/BFS

- **Number of Islands**: [Python](Graph/NumberOfIslands.py), [C++](Graph/NumberOfIslands.cpp)

# Backtracking 回溯算法
- [Permutations in a given string](String/PermutationsOfAGivenString.py)
- [Permutations of an array](Array/Permutations.py)
- [Permutations of an array with duplicates](Array/PermutationsII.py)

# Sliding Windows 滑动窗口算法

# Dynamic Programming 动态规划算法
- [Longest Palindrome Substring](String/LongestPalindromeSubstring.py)
