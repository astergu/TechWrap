## 数组 Array

### 元素之和

- **3Sum三数之和** [[geeks]](https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/) [[leet]](https://leetcode.com/problems/3sum/description/) 利用排序减少搜索范围 )
    - 题意：给定一个整数数组，寻找是否存在三个元素a,b,c，使得a,b,c相加之和等于某个给定值x？要求返回符合要求的a,b,c组合。
    - 分析：
        - **Extra memory**：最简单可以用一个map来记录已经遇到过的元素a及其index，再用两层loop来查看(x-b-c)是否在map中，如果有，则加入结果。时间复杂度O(N<sup>2</sup>)，空间复杂度O(N).
        - **Sorting**: 对数组进行排序，固定a的位置（从0到arr.size - 2），在循环内部，由后往前向内夹逼b和c。时间复杂度O(N^2)，空间复杂度O(1). [python](Array/3Sum.py)
        

## 字符串 String

- **Longest Palindromic Substring最长回文子串** [[leet]](https://leetcode.com/problems/longest-palindromic-substring/description/) [[geeks1]](https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/) [[geeks2]](https://www.geeksforgeeks.org/longest-palindromic-substring-set-2/)
    - 题意：在字符串s中找出最长的回文子串。
    - 分析：采用**动态规划**，最短回文子串为1。初始化一个二维bool数组dp为false，即记录的是s[i,j]是否是一个回文串。子结构为：1）dp[i][i]=true; 2）如果s[i]==s[j] and dp[i+1][j-1]=true or j - i < 2，那么dp[i][j]=true, 同时更新最长回文子串的起止位置。[python](String/LongestPalindromicSubstring.py)
    

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
